import requests
from bs4 import BeautifulSoup
import time
import sqlite3

# Başlangıç sayfası numarası
BASLANGIC_SAYFA = 3

def create_database():
    """Veritabanını ve tabloyu oluşturur"""
    conn = sqlite3.connect('isimler.db')
    cursor = conn.cursor()
    
    # İsimler tablosunu oluştur
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS isimler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT UNIQUE,
        ebced_degeri INTEGER,
        arapca_yazilis TEXT,
        kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    return conn

def get_and_process_page(page_number, conn):
    """Belirtilen sayfa numarasındaki tüm isimleri işler"""
    base_url = "https://ebced.mollacami.com/isimler-s{}.html"
    url = base_url.format(page_number)
    print(f"\n{'='*50}")
    print(f"SAYFA {page_number} İŞLENİYOR")
    print(f"URL: {url}")
    print(f"{'='*50}\n")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # ul class="alt" içindeki tüm linkleri bul
        links_container = soup.find('ul', class_='alt')
        if not links_container:
            print(f"Sayfa {page_number} de link bulunamadı.")
            return False
            
        name_links = links_container.find_all('a')
        if not name_links:
            print(f"Sayfa {page_number} de isim linki bulunamadı.")
            return False
        
        print(f"Bu sayfada {len(name_links)} isim bulundu.")
        print("-" * 50)
        
        # Sayfadaki her ismi işle
        for i, link in enumerate(name_links, 1):
            name = link.text.strip()
            href = link['href']
            print(f"\nİşleniyor {i}/{len(name_links)}: {name}")
            
            details = get_name_details(href)
            print(details)
            if details:
                save_to_database(conn, name, details)
            time.sleep(0.5)  # Siteye fazla yük bindirmemek için bekle
        
        print(f"\n{'*'*50}")
        print(f"SAYFA {page_number} TAMAMLANDI!")
        print(f"Toplam {len(name_links)} isim işlendi.")
        print(f"{'*'*50}\n")
        return True
        
    except Exception as e:
        print(f"Sayfa {page_number} işlenirken hata oluştu: {e}")
        return False

def get_name_details(url):
    max_retries = 3
    retry_delay = 5  # saniye
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)  # 30 saniyelik timeout
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Ebced değerini bul - paragraflar içinde ara
                ebced_degeri = None
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    if 'ebced değeri' in p.text.lower():
                        try:
                            ebced_degeri = int(p.text.split(':')[1].strip())
                        except:
                            continue
                
                # Arapça yazılışı bul - osmani class'ına sahip p etiketinde
                arapca_p = soup.find('p', class_='osmani')
                arapca_yazilis = None
                if arapca_p:
                    try:
                        arapca_yazilis = arapca_p.text.split('::')[1].strip()
                    except:
                        pass
                
                return {
                    'ebced_degeri': ebced_degeri,
                    'arapca_yazilis': arapca_yazilis
                }
            else:
                print(f"HTTP Hata Kodu: {response.status_code}")
                
        except requests.Timeout:
            print(f"Zaman aşımı hatası (Deneme {attempt + 1}/{max_retries})")
        except requests.RequestException as e:
            print(f"Bağlantı hatası: {e} (Deneme {attempt + 1}/{max_retries})")
        
        if attempt < max_retries - 1:  # Son deneme değilse bekle
            print(f"{retry_delay} saniye bekleniyor...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Her denemede bekleme süresini iki katına çıkar
    
    print("Maksimum deneme sayısına ulaşıldı, isim atlanıyor.")
    return None

def save_to_database(conn, name, data):
    if not data:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT OR REPLACE INTO isimler (isim, ebced_degeri, arapca_yazilis)
        VALUES (?, ?, ?)
        ''', (name, data['ebced_degeri'], data['arapca_yazilis']))
        
        conn.commit()
        print(f"✓ {name} veritabanına kaydedildi")
    except Exception as e:
        print(f"Veritabanına kayıt sırasında hata: {e}")

def manuel_isim_ekle():
    """Kullanıcıdan manuel olarak isim bilgilerini alıp veritabanına kaydeder"""
    conn = create_database()
    print("\nManuel İsim Ekleme (Çıkmak için 'q' yazın)")
    print("Format: isim, arapça_yazılış, ebced_değeri")
    print("Örnek: Ahmed, احمد, 53")
    
    while True:
        try:
            user_input = input("\nLütfen isim bilgilerini girin: ").strip()
            
            if user_input.lower() == 'q':
                break
                
            # Virgülle ayrılmış değerleri al
            parts = [part.strip() for part in user_input.split(',')]
            
            if len(parts) != 3:
                print("Hata: Lütfen tüm bilgileri virgülle ayırarak girin!")
                continue
                
            isim, arapca, ebced = parts
            
            try:
                ebced = int(ebced)
            except ValueError:
                print("Hata: Ebced değeri sayı olmalıdır!")
                continue
                
            # Veritabanına kaydet
            cursor = conn.cursor()
            cursor.execute('''
            INSERT OR REPLACE INTO isimler (isim, ebced_degeri, arapca_yazilis)
            VALUES (?, ?, ?)
            ''', (isim, ebced, arapca))
            
            conn.commit()
            print(f"✓ {isim} başarıyla veritabanına eklendi!")
            
        except Exception as e:
            print(f"Hata oluştu: {e}")
            
    conn.close()
    print("\nManuel isim ekleme işlemi tamamlandı.")

def main():
    while True:
        print("\n1. Web'den isim verilerini çek")
        print("2. Manuel isim ekle")
        print("3. Çıkış")
        
        secim = input("\nLütfen bir işlem seçin (1-3): ")
        
        if secim == "1":
            # Veritabanını oluştur
            conn = create_database()
            print("Veritabanı oluşturuldu/bağlantı kuruldu.")
            
            current_page = BASLANGIC_SAYFA
            while True:
                success = get_and_process_page(current_page, conn)
                if not success:
                    print("\nTüm sayfalar tamamlandı veya bir hata oluştu.")
                    break
                current_page += 1
                time.sleep(1)  # Sayfalar arası bekleme
            
            conn.close()
            print(f"\nİşlem tamamlandı. Son işlenen sayfa: {current_page-1}")
            
        elif secim == "2":
            manuel_isim_ekle()
            
        elif secim == "3":
            print("\nProgram sonlandırılıyor...")
            break
            
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")

"""
    # tekrar veri tabanını oluşturmak için main kodunu buna oluştur.
    # Veritabanını oluştur
    conn = create_database()
    print("Veritabanı oluşturuldu/bağlantı kuruldu.")
    
    current_page = BASLANGIC_SAYFA
    while True:
        success = get_and_process_page(current_page, conn)
        if not success:
            print("\nTüm sayfalar tamamlandı veya bir hata oluştu.")
            break
        current_page += 1
        time.sleep(1)  # Sayfalar arası bekleme
    
    conn.close()
    print(f"\nİşlem tamamlandı. Son işlenen sayfa: {current_page-1}")
"""

if __name__ == "__main__":
    main()

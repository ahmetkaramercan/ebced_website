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
        VALUES (LOWER(?), ?, ?)
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
            
            # İsim kontrolü yap
            existing_name = check_name_exists(conn, isim)
            if existing_name:
                print(f"\nBu isim zaten veritabanında mevcut:")
                print(f"İsim: {existing_name['isim']}")
                print(f"Ebced Değeri: {existing_name['ebced_degeri']}")
                print(f"Arapça Yazılış: {existing_name['arapca_yazilis']}")
                
                update_choice = input("\nBu kaydı güncellemek ister misiniz? (E/H): ").strip().lower()
                if update_choice != 'e':
                    print("İşlem iptal edildi.")
                    continue
            
            try:
                ebced = int(ebced)
            except ValueError:
                print("Hata: Ebced değeri sayı olmalıdır!")
                continue
                
            # Veritabanına kaydet
            cursor = conn.cursor()
            cursor.execute('''
            INSERT OR REPLACE INTO isimler (isim, ebced_degeri, arapca_yazilis)
            VALUES (LOWER(?), ?, ?)
            ''', (isim, ebced, arapca))
            
            conn.commit()
            if existing_name:
                print(f"✓ {isim} başarıyla güncellendi!")
            else:
                print(f"✓ {isim} başarıyla veritabanına eklendi!")
            
        except Exception as e:
            print(f"Hata oluştu: {e}")
            
    conn.close()
    print("\nManuel isim ekleme işlemi tamamlandı.")

def check_name_exists(conn, name):
    """Veritabanında ismin var olup olmadığını kontrol eder ve varsa detaylarını döndürür"""
    cursor = conn.cursor()
    cursor.execute('''
    SELECT isim, ebced_degeri, arapca_yazilis
    FROM isimler
    WHERE isim = ?
    ''', (name,))
    
    result = cursor.fetchone()
    if result:
        return {
            'isim': result[0],
            'ebced_degeri': result[1],
            'arapca_yazilis': result[2]
        }
    return None

def isim_ara(conn, isim):
    """Veritabanında isim arar ve detaylarını döndürür"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT isim, ebced_degeri, arapca_yazilis
        FROM isimler
        WHERE LOWER(isim) = LOWER(?)
        ''', (isim,))
        
        sonuc = cursor.fetchone()
        if sonuc:
            print("\nİsim bulundu!")
            print(f"İsim: {sonuc[0]}")
            print(f"Ebced Değeri: {sonuc[1]}")
            print(f"Arapça Yazılış: {sonuc[2]}")
            return {
                'isim': sonuc[0],
                'ebced_degeri': sonuc[1],
                'arapca_yazilis': sonuc[2]
            }
        else:
            print(f"\n'{isim}' ismi veritabanında bulunamadı.")
            return None
    except Exception as e:
        print(f"İsim arama sırasında hata oluştu: {e}")
        return None

def isimleri_kucuk_harfe_cevir(conn):
    """Veritabanındaki tüm isimleri küçük harfe çevirir"""
    try:
        cursor = conn.cursor()
        
        # Önce tüm isimleri al
        cursor.execute('SELECT id, isim FROM isimler')
        isimler = cursor.fetchall()
        
        guncellenen = 0
        for id, isim in isimler:
            kucuk_isim = isim.lower()
            if isim != kucuk_isim:
                cursor.execute('''
                UPDATE isimler
                SET isim = ?
                WHERE id = ?
                ''', (kucuk_isim, id))
                guncellenen += 1
        
        conn.commit()
        print(f"\nToplam {guncellenen} isim küçük harfe çevrildi.")
        return True
    except Exception as e:
        print(f"İsimleri küçük harfe çevirirken hata oluştu: {e}")
        return False

def main():
    while True:
        print("\n1. Web'den isim verilerini çek")
        print("2. Manuel isim ekle")
        print("3. İsim ara")
        print("4. İsimleri küçük harfe çevir")
        print("5. Çıkış")
        
        secim = input("\nLütfen bir işlem seçin (1-5): ")
        
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
            conn = create_database()
            aranan_isim = input("\nAramak istediğiniz ismi girin: ")
            isim_ara(conn, aranan_isim)
            conn.close()
            
        elif secim == "4":
            conn = create_database()
            isimleri_kucuk_harfe_cevir(conn)
            conn.close()
            
        elif secim == "5":
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

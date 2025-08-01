from veritabani_yonetici import VeriTabaniYonetici

def main():
    vt = VeriTabaniYonetici()
    
    while True:
        print("\nKullanıcı Yönetim Sistemi")
        print("1. Kullanıcı Ekle")
        print("2. Kullanıcı Sil")
        print("3. Kullanıcıyı Deaktive Et")
        print("4. Kullanıcıyı Aktive Et")
        print("5. Tüm Kullanıcıları Listele")
        print("6. Kullanıcı Bilgilerini Göster")
        print("7. Kullanıcı Tarihini Güncelle")
        print("8. Veritabanı İşlemleri")
        print("0. Çıkış")
        
        secim = input("\nLütfen bir işlem seçin (0-8): ")
        
        if secim == "1":
            kullanici_adi = input("Kullanıcı adı: ")
            sifre = input("Şifre: ")
            vt.kullanici_ekle(kullanici_adi, sifre)
        
        elif secim == "2":
            kullanici_adi = input("Silinecek kullanıcı adı: ")
            vt.kullanici_sil(kullanici_adi)
        
        elif secim == "3":
            kullanici_adi = input("Deaktive edilecek kullanıcı adı: ")
            vt.kullaniciyi_deaktive_et(kullanici_adi)
        
        elif secim == "4":
            kullanici_adi = input("Aktive edilecek kullanıcı adı: ")
            vt.kullaniciyi_aktive_et(kullanici_adi)
        
        elif secim == "5":
            vt.butun_kullanici_bilgileri()
        
        elif secim == "6":
            kullanici_adi = input("Bilgileri gösterilecek kullanıcı adı: ")
            vt.kullanici_bilgileri(kullanici_adi)
            
        elif secim == "7":
            kullanici_adi = input("Tarihi güncellenecek kullanıcı adı: ")
            vt.tarih_guncelle(kullanici_adi)
            
        elif secim == "8":
            while True:
                print("\nVeritabanı İşlemleri")
                print("1. Mevcut Veritabanını Yedekle")
                print("2. Yedekten Geri Yükle")
                print("3. Fly.io'dan Veritabanını İndir")
                print("0. Ana Menüye Dön")
                
                db_secim = input("\nLütfen bir işlem seçin (0-3): ")
                
                if db_secim == "1":
                    if vt.veritabani_yedekle():
                        print("Not: Yedek dosyası 'kullanicilar_yedek.db' olarak kaydedildi.")
                
                elif db_secim == "2":
                    onay = input("Bu işlem mevcut veritabanının üzerine yazacak. Emin misiniz? (e/h): ")
                    if onay.lower() == 'e':
                        vt.veritabani_geri_yukle()
                
                elif db_secim == "3":
                    app_name = "ebced-hesaplama"
                    onay = input("Bu işlem mevcut veritabanının üzerine yazacak. Emin misiniz? (e/h): ")
                    if onay.lower() == 'e':
                        vt.flyio_veritabani_indir(app_name)
                
                elif db_secim == "0":
                    break
                
                else:
                    print("Geçersiz seçim! Lütfen 0-3 arasında bir sayı girin.")
        
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen 0-8 arasında bir sayı girin.")

if __name__ == "__main__":
    main() 
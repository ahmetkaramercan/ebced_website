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
        print("0. Çıkış")
        
        secim = input("\nLütfen bir işlem seçin (0-7): ")
        
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
        
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen 0-7 arasında bir sayı girin.")

if __name__ == "__main__":
    main() 
import sqlite3
from datetime import datetime
import shutil
import os

class VeriTabaniYonetici:
    def __init__(self):
        self.baglanti = sqlite3.connect('kullanicilar.db')
        self.cursor = self.baglanti.cursor()
        self.tablo_olustur()
    
    def tablo_olustur(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS kullanicilar (
            kullanici_adi TEXT PRIMARY KEY,
            sifre TEXT NOT NULL,
            aktiflik INTEGER NOT NULL,
            tarih TEXT NOT NULL
        )
        ''')
        self.baglanti.commit()
    
    def kullanici_ekle(self, kullanici_adi, sifre):
        try:
            tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''
            INSERT INTO kullanicilar (kullanici_adi, sifre, aktiflik, tarih)
            VALUES (?, ?, ?, ?)
            ''', (kullanici_adi, sifre, 1, tarih))
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} başarıyla eklendi.")
            return True
        except sqlite3.IntegrityError:
            print(f"Hata: {kullanici_adi} kullanıcı adı zaten mevcut!")
            return False
    
    def kullanici_sil(self, kullanici_adi):
        self.cursor.execute('DELETE FROM kullanicilar WHERE kullanici_adi = ?', (kullanici_adi,))
        if self.cursor.rowcount > 0:
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} başarıyla silindi.")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!.")
            return False
    
    def kullaniciyi_deaktive_et(self, kullanici_adi):
        self.cursor.execute('''
        UPDATE kullanicilar SET aktiflik = 0
        WHERE kullanici_adi = ?
        ''', (kullanici_adi,))
        if self.cursor.rowcount > 0:
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} deaktive edildi.")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!.")
            return False
    
    def kullaniciyi_aktive_et(self, kullanici_adi):
        self.cursor.execute('''
        UPDATE kullanicilar SET aktiflik = 1
        WHERE kullanici_adi = ?
        ''', (kullanici_adi,))
        if self.cursor.rowcount > 0:
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} aktive edildi.")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!.")
            return False
    
    def butun_kullanici_bilgileri(self):
        self.cursor.execute('SELECT * FROM kullanicilar')
        kullanicilar = self.cursor.fetchall()
        if kullanicilar:
            print("\nTüm Kullanıcı Bilgileri:")
            print("Kullanıcı Adı | Şifre | Aktiflik | Tarih")
            print("-" * 50)
            for kullanici in kullanicilar:
                print(f"{kullanici[0]} | {kullanici[1]} | {'Aktif' if kullanici[2] == 1 else 'Deaktif'} | {kullanici[3]}")
        else:
            print("Veritabanında hiç kullanıcı bulunmamaktadır.")
    
    def kullanici_bilgileri(self, kullanici_adi):
        self.cursor.execute('SELECT * FROM kullanicilar WHERE kullanici_adi = ?', (kullanici_adi,))
        kullanici = self.cursor.fetchone()
        if kullanici:
            print(f"\nKullanıcı Bilgileri:")
            print(f"Kullanıcı Adı: {kullanici[0]}")
            print(f"Şifre: {kullanici[1]}")
            print(f"Durum: {'Aktif' if kullanici[2] == 1 else 'Deaktif'}")
            print(f"Kayıt Tarihi: {kullanici[3]}")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!")
            return False
    
    def tarih_guncelle(self, kullanici_adi):
        yeni_tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
        UPDATE kullanicilar SET tarih = ?
        WHERE kullanici_adi = ?
        ''', (yeni_tarih, kullanici_adi))
        if self.cursor.rowcount > 0:
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} tarihi {yeni_tarih} olarak güncellendi.")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!")
            return False
    
    def veritabani_yedekle(self):
        """Mevcut veritabanını yedekler"""
        try:
            # Önce bağlantıyı kapat
            self.baglanti.close()
            
            # Veritabanını yedekle
            shutil.copy2('kullanicilar.db', 'kullanicilar_yedek.db')
            
            # Bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            
            print("Veritabanı başarıyla yedeklendi: kullanicilar_yedek.db")
            return True
        except Exception as e:
            print(f"Yedekleme sırasında hata oluştu: {str(e)}")
            # Hata durumunda bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            return False
    
    def veritabani_geri_yukle(self):
        """Yedek veritabanını mevcut veritabanına geri yükler"""
        try:
            # Önce bağlantıyı kapat
            self.baglanti.close()
            
            # Eğer yedek dosya varsa
            if os.path.exists('kullanicilar_yedek.db'):
                # Mevcut veritabanını yedek dosya ile değiştir
                shutil.copy2('kullanicilar_yedek.db', 'kullanicilar.db')
                
                # Bağlantıyı yeniden aç
                self.baglanti = sqlite3.connect('kullanicilar.db')
                self.cursor = self.baglanti.cursor()
                
                print("Veritabanı başarıyla geri yüklendi")
                return True
            else:
                print("Yedek veritabanı bulunamadı: kullanicilar_yedek.db")
                # Bağlantıyı yeniden aç
                self.baglanti = sqlite3.connect('kullanicilar.db')
                self.cursor = self.baglanti.cursor()
                return False
        except Exception as e:
            print(f"Geri yükleme sırasında hata oluştu: {str(e)}")
            # Hata durumunda bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            return False
    
    def __del__(self):
        self.baglanti.close() 
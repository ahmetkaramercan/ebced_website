import sqlite3
from datetime import datetime
import shutil
import os
import subprocess

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
    
    def flyio_veritabani_indir(self, app_name):
        """Fly.io'dan veritabanını indirir ve mevcut veritabanının üzerine yazar"""
        try:
            # Önce bağlantıyı kapat
            self.baglanti.close()
            
            print("Fly.io'dan veritabanı indiriliyor...")
            
            # Önce VM durumunu kontrol et
            check_cmd = f'fly status -a {app_name}'
            check_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
            
            if "No machines are running" in check_result.stderr or "has no started VMs" in check_result.stderr:
                print(f"Hata: {app_name} uygulaması için çalışan VM bulunamadı.")
                print("Lütfen önce uygulamanın çalıştığından emin olun: fly apps start")
                raise Exception("Çalışan VM bulunamadı")
            
            # Eğer dosya varsa sil
            if os.path.exists('kullanicilar.db'):
                os.remove('kullanicilar.db')
                print("Mevcut veritabanı dosyası silindi")
            
            # SFTP ile dosyayı indir
            cmd = f'fly sftp get /app/kullanicilar.db kullanicilar.db -a {app_name}'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                error_msg = result.stderr.strip()
                if "not found" in error_msg:
                    raise Exception("Uzak sunucuda veritabanı dosyası bulunamadı")
                raise Exception(f"Fly.io'dan indirme başarısız oldu: {error_msg}")
            
            print("Veritabanı başarıyla indirildi ve güncellendi")
            
            # Bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            return True
            
        except Exception as e:
            print(f"Fly.io veritabanı indirme hatası: {str(e)}")
            if "Çalışan VM bulunamadı" in str(e):
                print("\nÇözüm önerileri:")
                print("1. 'fly apps start -a " + app_name + "' komutu ile uygulamayı başlatın")
                print("2. 'fly status -a " + app_name + "' komutu ile durumu kontrol edin")
                print("3. Uygulama başladıktan sonra tekrar deneyin")
            # Hata durumunda bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            return False
    
    def __del__(self):
        self.baglanti.close() 
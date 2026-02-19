import sqlite3
from datetime import datetime, timedelta
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
            tarih TEXT NOT NULL,
            bitis_tarihi TEXT
        )
        ''')
        self.baglanti.commit()
        # Mevcut tabloda bitis_tarihi kolonu yoksa ekle
        try:
            self.cursor.execute('ALTER TABLE kullanicilar ADD COLUMN bitis_tarihi TEXT')
            self.baglanti.commit()
            # Mevcut kullanıcıların bitiş tarihini başlangıç tarihinden 1 yıl sonrasına ayarla
            self.cursor.execute('SELECT kullanici_adi, tarih FROM kullanicilar WHERE bitis_tarihi IS NULL')
            kullanicilar = self.cursor.fetchall()
            for kullanici_adi, tarih in kullanicilar:
                try:
                    baslangic = datetime.strptime(tarih, '%Y-%m-%d %H:%M:%S')
                    bitis = baslangic + timedelta(days=365)
                    bitis_str = bitis.strftime('%Y-%m-%d %H:%M:%S')
                    self.cursor.execute('''
                    UPDATE kullanicilar SET bitis_tarihi = ?
                    WHERE kullanici_adi = ?
                    ''', (bitis_str, kullanici_adi))
                except:
                    # Tarih formatı farklıysa, şu anki tarihten 1 yıl sonrasını kullan
                    bitis = datetime.now() + timedelta(days=365)
                    bitis_str = bitis.strftime('%Y-%m-%d %H:%M:%S')
                    self.cursor.execute('''
                    UPDATE kullanicilar SET bitis_tarihi = ?
                    WHERE kullanici_adi = ?
                    ''', (bitis_str, kullanici_adi))
            self.baglanti.commit()
        except sqlite3.OperationalError:
            # Kolon zaten varsa hata verme
            pass
        
        # Mevcut tabloda sorgu_sayisi kolonu yoksa ekle
        try:
            self.cursor.execute('ALTER TABLE kullanicilar ADD COLUMN sorgu_sayisi INTEGER DEFAULT 0')
            self.baglanti.commit()
            # Mevcut kullanıcıların sorgu sayısını 0 yap
            self.cursor.execute('UPDATE kullanicilar SET sorgu_sayisi = 0 WHERE sorgu_sayisi IS NULL')
            self.baglanti.commit()
        except sqlite3.OperationalError:
            # Kolon zaten varsa hata verme
            pass
        
        # Mevcut tabloda son_sorgu_tarihi kolonu yoksa ekle
        try:
            self.cursor.execute('ALTER TABLE kullanicilar ADD COLUMN son_sorgu_tarihi TEXT')
            self.baglanti.commit()
            # Mevcut kullanıcıların son sorgu tarihini bugün yap
            bugun = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('UPDATE kullanicilar SET son_sorgu_tarihi = ? WHERE son_sorgu_tarihi IS NULL', (bugun,))
            self.baglanti.commit()
        except sqlite3.OperationalError:
            # Kolon zaten varsa hata verme
            pass
    
    def kullanici_ekle(self, kullanici_adi, sifre, ay_sayisi=12):
        try:
            tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            baslangic = datetime.now()
            bitis = baslangic + timedelta(days=ay_sayisi * 30)  # Her ay 30 gün olarak hesaplanıyor
            bitis_tarihi = bitis.strftime('%Y-%m-%d %H:%M:%S')
            bugun = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''
            INSERT INTO kullanicilar (kullanici_adi, sifre, aktiflik, tarih, bitis_tarihi, sorgu_sayisi, son_sorgu_tarihi)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (kullanici_adi, sifre, 1, tarih, bitis_tarihi, 0, bugun))
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} başarıyla eklendi. Bitiş tarihi: {bitis_tarihi} ({ay_sayisi} ay)")
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
    
    def kullanici_suresini_uzat(self, kullanici_adi, ay_sayisi):
        """Kullanıcının bitiş tarihini belirtilen ay sayısı kadar uzatır"""
        # Önce mevcut bitiş tarihini al
        self.cursor.execute('SELECT bitis_tarihi FROM kullanicilar WHERE kullanici_adi = ?', (kullanici_adi,))
        result = self.cursor.fetchone()
        if not result:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!")
            return False
        
        mevcut_bitis = result[0]
        if mevcut_bitis:
            try:
                # Mevcut bitiş tarihinden itibaren uzat
                bitis_datetime = datetime.strptime(mevcut_bitis, '%Y-%m-%d %H:%M:%S')
            except:
                # Tarih formatı hatalıysa, şu anki tarihten itibaren uzat
                bitis_datetime = datetime.now()
        else:
            # Bitiş tarihi yoksa, şu anki tarihten itibaren uzat
            bitis_datetime = datetime.now()
        
        # Yeni bitiş tarihini hesapla
        yeni_bitis = bitis_datetime + timedelta(days=ay_sayisi * 30)
        yeni_bitis_str = yeni_bitis.strftime('%Y-%m-%d %H:%M:%S')
        
        # Güncelle
        self.cursor.execute('''
        UPDATE kullanicilar SET bitis_tarihi = ?, aktiflik = 1
        WHERE kullanici_adi = ?
        ''', (yeni_bitis_str, kullanici_adi))
        if self.cursor.rowcount > 0:
            self.baglanti.commit()
            print(f"Kullanıcı {kullanici_adi} süresi {ay_sayisi} ay uzatıldı. Yeni bitiş tarihi: {yeni_bitis_str}")
            return True
        else:
            print(f"Hata: {kullanici_adi} kullanıcısı bulunamadı!")
            return False
    
    def sorgu_sayisi_artir(self, kullanici_adi):
        """Kullanıcının sorgu sayısını 1 artırır ve son sorgu tarihini günceller"""
        try:
            bugun = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''
            UPDATE kullanicilar 
            SET sorgu_sayisi = COALESCE(sorgu_sayisi, 0) + 1,
                son_sorgu_tarihi = ?
            WHERE kullanici_adi = ?
            ''', (bugun, kullanici_adi))
            self.baglanti.commit()
            return True
        except Exception as e:
            print(f"Sorgu sayısı artırılırken hata: {e}")
            return False
    
    def butun_kullanici_bilgileri(self):
        self.cursor.execute('SELECT * FROM kullanicilar')
        kullanicilar = self.cursor.fetchall()
        if kullanicilar:
            print("\nTüm Kullanıcı Bilgileri:")
            print("Kullanıcı Adı | Şifre | Aktiflik | Başlangıç Tarihi | Bitiş Tarihi | Sorgu Sayısı | Son Sorgu Tarihi")
            print("-" * 120)
            for kullanici in kullanicilar:
                bitis_tarihi = kullanici[4] if len(kullanici) > 4 and kullanici[4] else "Belirtilmemiş"
                sorgu_sayisi = kullanici[5] if len(kullanici) > 5 and kullanici[5] is not None else 0
                son_sorgu = kullanici[6] if len(kullanici) > 6 and kullanici[6] else "Belirtilmemiş"
                print(f"{kullanici[0]} | {kullanici[1]} | {'Aktif' if kullanici[2] == 1 else 'Deaktif'} | {kullanici[3]} | {bitis_tarihi} | {sorgu_sayisi} | {son_sorgu}")
        else:
            print("Veritabanında hiç kullanıcı bulunmamaktadır.")
    
    def kullanici_bilgileri(self, kullanici_adi):
        self.cursor.execute('SELECT * FROM kullanicilar WHERE kullanici_adi = ?', (kullanici_adi,))
        kullanici = self.cursor.fetchone()
        if kullanici:
            bitis_tarihi = kullanici[4] if len(kullanici) > 4 and kullanici[4] else "Belirtilmemiş"
            sorgu_sayisi = kullanici[5] if len(kullanici) > 5 and kullanici[5] is not None else 0
            son_sorgu = kullanici[6] if len(kullanici) > 6 and kullanici[6] else "Belirtilmemiş"
            print(f"\nKullanıcı Bilgileri:")
            print(f"Kullanıcı Adı: {kullanici[0]}")
            print(f"Şifre: {kullanici[1]}")
            print(f"Durum: {'Aktif' if kullanici[2] == 1 else 'Deaktif'}")
            print(f"Başlangıç Tarihi: {kullanici[3]}")
            print(f"Bitiş Tarihi: {bitis_tarihi}")
            print(f"Sorgu Sayısı: {sorgu_sayisi}")
            print(f"Son Sorgu Tarihi: {son_sorgu}")
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
            
            print("Fly.io uygulaması kontrol ediliyor...")
            
            # Önce uygulamanın var olup olmadığını kontrol et
            check_app_cmd = f'fly apps list | grep {app_name}'
            app_result = subprocess.run(check_app_cmd, shell=True, capture_output=True, text=True)
            
            if app_result.returncode != 0:
                raise Exception(f"'{app_name}' adında bir uygulama bulunamadı. Lütfen uygulama adını kontrol edin.")
            
            # VM durumunu kontrol et
            print("VM durumu kontrol ediliyor...")
            check_cmd = f'fly status -a {app_name}'
            check_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
            
            if "Error: app" in check_result.stderr and "has no started VMs" in check_result.stderr:
                print(f"\nHata: {app_name} uygulaması için çalışan VM bulunamadı.")
                print("\nÇözüm adımları:")
                print(f"1. Uygulamayı başlatın: fly apps start -a {app_name}")
                print(f"2. Durumu kontrol edin: fly status -a {app_name}")
                print("3. Uygulama başladıktan sonra tekrar deneyin")
                print("\nEğer sorun devam ederse:")
                print(f"4. Uygulamanın sağlık durumunu kontrol edin: fly status -a {app_name}")
                print(f"5. Deployment durumunu kontrol edin: fly deployments list -a {app_name}")
                print("6. Gerekirse uygulamayı yeniden deploy edin: fly deploy")
                raise Exception("Çalışan VM bulunamadı")
            
            print("Fly.io'dan veritabanı indiriliyor...")
            
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
                print("\nLütfen yukarıdaki çözüm adımlarını takip edin.")
            elif "uygulama bulunamadı" in str(e):
                print("\nLütfen doğru uygulama adını girdiğinizden emin olun.")
            # Hata durumunda bağlantıyı yeniden aç
            self.baglanti = sqlite3.connect('kullanicilar.db')
            self.cursor = self.baglanti.cursor()
            return False
    
    def __del__(self):
        self.baglanti.close() 
from flask_login import UserMixin
from veritabani_yonetici import VeriTabaniYonetici

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username
        self.vt = VeriTabaniYonetici()

    @staticmethod
    def get(username):
        vt = VeriTabaniYonetici()
        vt.cursor.execute('SELECT * FROM kullanicilar WHERE kullanici_adi = ?', (username,))
        user = vt.cursor.fetchone()
        if user and user[2] == 1:  # Kullanıcı varsa ve aktifse
            return User(username)
        return None

    def check_password(self, password):
        self.vt.cursor.execute('SELECT sifre FROM kullanicilar WHERE kullanici_adi = ?', (self.username,))
        result = self.vt.cursor.fetchone()
        if result:
            return result[0] == password
        return False

    def change_password(self, new_password):
        try:
            self.vt.cursor.execute('''
            UPDATE kullanicilar SET sifre = ?
            WHERE kullanici_adi = ?
            ''', (new_password, self.username))
            self.vt.baglanti.commit()
            return True
        except:
            return False

    def change_username(self, new_username):
        # Önce yeni kullanıcı adının kullanımda olup olmadığını kontrol et
        self.vt.cursor.execute('SELECT 1 FROM kullanicilar WHERE kullanici_adi = ?', (new_username,))
        if self.vt.cursor.fetchone():
            return False  # Kullanıcı adı zaten kullanımda
        
        try:
            # Eski kullanıcının bilgilerini al
            self.vt.cursor.execute('SELECT sifre, aktiflik, tarih FROM kullanicilar WHERE kullanici_adi = ?', (self.username,))
            old_data = self.vt.cursor.fetchone()
            if not old_data:
                return False

            # Yeni kullanıcı adıyla bilgileri ekle
            self.vt.cursor.execute('''
            INSERT INTO kullanicilar (kullanici_adi, sifre, aktiflik, tarih)
            VALUES (?, ?, ?, ?)
            ''', (new_username, old_data[0], old_data[1], old_data[2]))

            # Eski kullanıcıyı sil
            self.vt.cursor.execute('DELETE FROM kullanicilar WHERE kullanici_adi = ?', (self.username,))
            
            self.vt.baglanti.commit()
            self.username = new_username
            self.id = new_username
            return True
        except:
            self.vt.baglanti.rollback()
            return False 
# Kullanıcı Yönetim Sistemi

Bu sistem, kullanıcıları SQLite veritabanında yönetmek için basit bir arayüz sunar.

## Özellikler

- Kullanıcı ekleme
- Kullanıcı silme
- Kullanıcı deaktive etme
- Kullanıcı aktive etme
- Tüm kullanıcıları listeleme
- Belirli bir kullanıcının bilgilerini görüntüleme
- Kullanıcı tarihini güncelleme

## Gereksinimler

- Python 3.x
- SQLite3 (Python ile birlikte gelir)

## Kullanım

Programı başlatmak için terminal veya komut istemcisinde şu komutu çalıştırın:

```bash
python kullanici_yonetimi.py
```

Program başladığında, menüden istediğiniz işlemi seçebilirsiniz:

1. Kullanıcı Ekle: Yeni bir kullanıcı ekler (varsayılan olarak aktif)
2. Kullanıcı Sil: Var olan bir kullanıcıyı siler
3. Kullanıcıyı Deaktive Et: Kullanıcının aktiflik durumunu 0 yapar
4. Kullanıcıyı Aktive Et: Kullanıcının aktiflik durumunu 1 yapar
5. Tüm Kullanıcıları Listele: Veritabanındaki tüm kullanıcıları gösterir
6. Kullanıcı Bilgilerini Göster: Belirli bir kullanıcının detaylı bilgilerini gösterir
7. Kullanıcı Tarihini Güncelle: Kullanıcının tarihini şu anki tarih ve saat ile günceller
0. Çıkış: Programdan çıkar

## Veritabanı Yapısı

Kullanıcılar aşağıdaki bilgilerle saklanır:

- kullanici_adi (TEXT, PRIMARY KEY)
- sifre (TEXT)
- aktiflik (INTEGER, 1 veya 0)
- tarih (TEXT, kayıt tarihi)

## Notlar

- Kullanıcı adları benzersiz olmalıdır
- Şifreler açık metin olarak saklanır
- Aktiflik durumu 0 olan kullanıcılar sisteme giriş yapamaz 
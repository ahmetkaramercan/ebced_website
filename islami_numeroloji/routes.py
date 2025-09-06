from flask import Blueprint, render_template, request
from flask_login import login_required
from datetime import datetime
from .hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  donusum_yillari_bulma, ozellik_hesaplama, pin_kodu_yorumlari_algoritmasi)
from .hesaplama_cakra import cakra_metin_hesaplamalari, cocuk_cakra_metin_hesaplamalari
from .hesaplama_merkez_sayi import merkez_sayi_bulma, merkez_sayi_aciklamalari
from .text import yasam_yollari
from .csv_export import generate_csv_export
from .ek_evlilik_metinleri import evlilik_ek_metin

# Blueprint oluştur - templates ve static klasörleri belirt
islami_numeroloji_bp = Blueprint(
    'islami_numeroloji', 
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/islami-numeroloji'  # URL'de tire kullanabiliriz
)

def yas_hesapla(dogum_gunu_str):
    """Doğum tarihinden yaşı hesaplar"""
    try:
        # Doğum tarihini parse et
        dogum_parcalari = dogum_gunu_str.split()
        if len(dogum_parcalari) == 3:
            gun, ay, yil = int(dogum_parcalari[0]), int(dogum_parcalari[1]), int(dogum_parcalari[2])
            dogum_tarihi = datetime(yil, ay, gun)
            bugun = datetime.now()
            
            yas = bugun.year - dogum_tarihi.year
            if bugun.month < dogum_tarihi.month or (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
                yas -= 1
            return yas
    except:
        pass
    return None

@islami_numeroloji_bp.route('/', methods=['GET', 'POST'])
@islami_numeroloji_bp.route('/hesaplama', methods=['GET', 'POST'])
@login_required
def islami_numeroloji_hesaplama():
    results = None
    error_message = None
    
    if request.method == 'POST':
        try:
            # Form verilerini kontrol et
            if 'dogum_gunu' not in request.form:
                error_message = "Doğum tarihi alanı gereklidir"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
            
            if 'isim_soyisim' not in request.form:
                error_message = "Ad soyad alanı gereklidir"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
            
            if 'cinsiyet' not in request.form:
                error_message = "Cinsiyet seçimi gereklidir"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
            
            input_dogum_gunu = request.form['dogum_gunu'].strip()
            if not input_dogum_gunu:
                error_message = "Doğum tarihi boş olamaz"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
            
            dogum_gunu = input_dogum_gunu.replace('.', ' ').replace('/', ' ')
            dogum_gunu = ' '.join(dogum_gunu.split())
            
            # Doğum tarihi formatını kontrol et
            try:
                dogum_parcalari = dogum_gunu.split()
                if len(dogum_parcalari) != 3:
                    error_message = "Doğum tarihi GG AA YYYY formatında olmalıdır (örn: 15 03 1990)"
                    return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
                
                gun, ay, yil = int(dogum_parcalari[0]), int(dogum_parcalari[1]), int(dogum_parcalari[2])
                if not (1 <= gun <= 31 and 1 <= ay <= 12 and 1000 <= yil <= 2200):
                    error_message = "Geçersiz tarih değerleri"
                    return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
                    
            except ValueError:
                error_message = "Doğum tarihi sayısal değerler içermelidir"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
            
            isim_soyisim = request.form['isim_soyisim'].strip()
            if not isim_soyisim:
                error_message = "Ad soyad boş olamaz"
                return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
                
            eklenen_isim = request.form.get('eklenen_isim', '').strip()  # İsteğe bağlı alan
            cinsiyet = request.form['cinsiyet']
            
            # Yaş hesapla
            yas = yas_hesapla(dogum_gunu)
            
            yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
            pin_kodu  = pin_kodu_hesaplama(dogum_gunu)
            arti_sistemi, chakra_result = chakra_hesapla(pin_kodu, isim_soyisim, eklenen_isim)
            pin_kodu_yorumlari = pin_kodu_yorumlari_algoritmasi(pin_kodu, arti_sistemi, cinsiyet, yasam_yolu )
            
            # Yaşa göre çakra hesaplama seç
            if yas is not None and yas <= 5:
                cakra_metinleri = cocuk_cakra_metin_hesaplamalari(arti_sistemi)
                cakra_tipi = "Çocuk çakra hesaplaması"
            else:
                cakra_metinleri = cakra_metin_hesaplamalari(arti_sistemi, cinsiyet)
                cakra_tipi = "Çakra hesaplaması"
                
            # Merkez sayının tuple değerini al
            merkez_sayi_detay, merkez_sayi_integer = merkez_sayi_bulma(isim_soyisim)
            
            donusum_yillari = donusum_yillari_bulma(dogum_gunu)
            pin_kodu_ozellikleri = ozellik_hesaplama(pin_kodu)
            
            # Yaşam yolu açıklamasını al
            yasam_yolu_aciklama = yasam_yollari.get(yasam_yolu, "Bu yaşam yolu için açıklama bulunamadı.")
            
            # Merkez sayı açıklaması artık merkez_sayi_detay içinde geliyor
            merkez_sayi_aciklama = merkez_sayi_detay
            
            # Evlilik ek metinlerini hesapla (eğer eklenen_isim varsa)
            evlilik_ek_metinleri = []
            if eklenen_isim:
                try:
                    evlilik_ek_metinleri = evlilik_ek_metin(eklenen_isim)
                except Exception as e:
                    print(f"Evlilik ek metinleri hesaplanırken hata: {e}")
                    evlilik_ek_metinleri = []
            
            results = {
                'dogum_gunu': dogum_gunu,
                'isim_soyisim': isim_soyisim,
                'eklenen_isim': eklenen_isim,
                'cinsiyet': cinsiyet,
                'yas': yas,
                'pin_kodu_dizilimi': pin_kodu,
                'pin_kodu_yorumlari': pin_kodu_yorumlari,
                'chakra': chakra_result,
                'cakra_metinleri': cakra_metinleri,
                'cakra_tipi': cakra_tipi,
                'yasam_yolu': yasam_yolu,
                'yasam_yolu_aciklama': yasam_yolu_aciklama,
                'merkez_sayi': merkez_sayi_detay,
                'merkez_sayi_integer': merkez_sayi_integer,
                'merkez_sayi_aciklama': merkez_sayi_aciklama,
                'donusum_yillari': donusum_yillari,
                'pin_kodu_ozellikleri': pin_kodu_ozellikleri,
                'evlilik_ek_metinleri': evlilik_ek_metinleri
            }
            
        except Exception as e:
            error_message = f"Hesaplama sırasında hata oluştu: {str(e)}"
            print(f"Hesaplama hatası: {e}")
            return render_template('islami-numeroloji-analiz.html', results=None, error=error_message)
    
    return render_template('islami-numeroloji-analiz.html', results=results, error=error_message)

@islami_numeroloji_bp.route('/pdf-print')
@login_required
def pdf_print():
    """PDF print sayfası - yeni pencerede açılır"""
    return render_template('pdf-print.html')

@islami_numeroloji_bp.route('/csv-export', methods=['POST'])
@login_required
def csv_export():
    """CSV export fonksiyonu - Canva için bulk upload formatında"""
    try:
        # POST verilerini al ve CSV modülüne gönder
        data = request.form.to_dict()
        return generate_csv_export(data)
        
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        print(f"CSV export hatası: {e}")
        return f"Hata: CSV oluşturulurken bir hata oluştu - {str(e)}", 500 
from flask import Blueprint, render_template, request
from flask_login import login_required
from datetime import datetime
from .hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  donusum_yillari_bulma, ozellik_hesaplama, pin_kodu_yorumlari_algoritmasi)
from .hesaplama_cakra import cakra_metin_hesaplamalari, cocuk_cakra_metin_hesaplamalari
from .hesaplama_merkez_sayi import merkez_sayi_bulma, merkez_sayi_aciklamalari
from .text import yasam_yollari

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
    if request.method == 'POST':
        input_dogum_gunu = request.form['dogum_gunu'] 
        dogum_gunu = input_dogum_gunu.replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        isim_soyisim = request.form['isim_soyisim']
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
            'pin_kodu_ozellikleri': pin_kodu_ozellikleri
        }
    
    return render_template('islami-numeroloji-analiz.html', results=results) 
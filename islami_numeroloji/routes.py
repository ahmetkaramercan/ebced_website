from flask import Blueprint, render_template, request
from flask_login import login_required
from ebced import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  bereket_rakami_bulma, ana_kulvar_bulma, yan_kulvar_bulma,
                  donusum_yillari_bulma, ozellik_hesaplama)

# Blueprint oluştur - templates ve static klasörleri belirt
islami_numeroloji_bp = Blueprint(
    'islami_numeroloji', 
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/islami-numeroloji'  # URL'de tire kullanabiliriz
)

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
        
        k_values, pin_kodu_yorumlari = pin_kodu_hesaplama(dogum_gunu)
        chakra_result = chakra_hesapla(k_values, isim_soyisim)
        yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
        bereket_sayisi = bereket_rakami_bulma(dogum_gunu)
        ana_kulvar = ana_kulvar_bulma(isim_soyisim)
        yan_kulvar = yan_kulvar_bulma(isim_soyisim)
        donusum_yillari = donusum_yillari_bulma(dogum_gunu)
        pin_kodu_ozellikleri = ozellik_hesaplama(k_values)
        
        results = {
            'dogum_gunu': dogum_gunu,
            'pin_kodu_dizilimi': k_values,
            'pin_kodu_yorumlari': pin_kodu_yorumlari,
            'chakra': chakra_result,
            'yasam_yolu': yasam_yolu,
            'bereket_sayisi': bereket_sayisi,
            'ana_kulvar': ana_kulvar,
            'yan_kulvar': yan_kulvar,
            'donusum_yillari': donusum_yillari,
            'pin_kodu_ozellikleri': pin_kodu_ozellikleri
        }
    
    return render_template('islami-numeroloji-analiz.html', results=results) 
from flask import Blueprint, render_template, request, make_response
from flask_login import login_required
from datetime import datetime
import csv
import io
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

@islami_numeroloji_bp.route('/csv-export', methods=['POST'])
@login_required
def csv_export():
    """CSV export fonksiyonu - Canva için bulk upload formatında"""
    try:
        # POST verilerini al
        data = request.form.to_dict()
        
        # Gerekli alanları kontrol et
        required_fields = ['dogum_gunu', 'isim_soyisim', 'cinsiyet']
        for field in required_fields:
            if field not in data:
                return f"Hata: {field} alanı gereklidir", 400
        
        # Doğum tarihini düzenle
        dogum_gunu = data['dogum_gunu'].replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        
        isim_soyisim = data['isim_soyisim']
        eklenen_isim = data.get('eklenen_isim', '').strip()
        cinsiyet = data['cinsiyet']
        
        # Hesaplamaları yap
        yas = yas_hesapla(dogum_gunu)
        yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
        pin_kodu = pin_kodu_hesaplama(dogum_gunu)
        arti_sistemi, chakra_result = chakra_hesapla(pin_kodu, isim_soyisim, eklenen_isim)
        pin_kodu_yorumlari = pin_kodu_yorumlari_algoritmasi(pin_kodu, arti_sistemi, cinsiyet, yasam_yolu)
        
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
        
        # Merkez sayı açıklaması
        merkez_sayi_aciklama = merkez_sayi_aciklamalari.get(str(merkez_sayi_integer))
        if merkez_sayi_aciklama and "******" in merkez_sayi_aciklama:
            merkez_sayi_aciklama = merkez_sayi_aciklama.replace("******", isim_soyisim)
        
        # CSV için string buffer oluştur
        output = io.StringIO()
        writer = csv.writer(output)
        
        # CSV başlık satırı (Canva bulk upload için)
        headers = [
            'full_name',
            'pin_kodu',
            'yasam_yolu'
        ]
        
        # Çakra metinleri için başlıklar (her çakra için 2 sayfa - ilk kısım ve ikinci kısım)
        for i in range(1, 10):  # 1-9 çakralar
            headers.append(f'cakra_{i}_sayfa_1')
            headers.append(f'cakra_{i}_sayfa_2')
        
        # Diğer başlıklar
        headers.extend([
            'pin_kodu_yorumlari',
            'yasam_yolu_aciklama',
            'merkez_sayi',
            'merkez_sayi_aciklama',
            'donusum_yillari',
            'pin_kodu_ozellikleri',
            'dogum_tarihi',
            'cinsiyet',
            'yas'
        ])
        
        # Başlık satırını yaz
        writer.writerow(headers)
        
        # Veri satırı
        row_data = [
            isim_soyisim.title(),  # full_name
            ' - '.join(pin_kodu) if pin_kodu else '',  # pin_kodu
            yasam_yolu  # yasam_yolu
        ]
        
        # Çakra metinlerini işle (her çakra için 2 sayfa)
        for i in range(9):
            if cakra_metinleri and i < len(cakra_metinleri):
                metin = cakra_metinleri[i]
                # Metni ~~~ ile ayır
                if "~~~" in metin:
                    metin_parcalari = metin.split("~~~", 1)
                    ilk_kisim = metin_parcalari[0].strip()
                    ikinci_kisim = metin_parcalari[1].strip()
                else:
                    # Eğer ~~~ yoksa, metni yarıya böl
                    metin_uzunluk = len(metin)
                    yarim = metin_uzunluk // 2
                    # En yakın cümle sonunu bul
                    nokta_index = metin.find('.', yarim)
                    if nokta_index != -1 and nokta_index < metin_uzunluk - 50:
                        ilk_kisim = metin[:nokta_index + 1].strip()
                        ikinci_kisim = metin[nokta_index + 1:].strip()
                    else:
                        ilk_kisim = metin[:yarim].strip()
                        ikinci_kisim = metin[yarim:].strip()
                
                row_data.append(ilk_kisim)
                row_data.append(ikinci_kisim)
            else:
                row_data.append('')  # Boş ilk kısım
                row_data.append('')  # Boş ikinci kısım
        
        # Pin kodu yorumları
        if pin_kodu_yorumlari:
            pin_text = '\n\n'.join(pin_kodu_yorumlari) if isinstance(pin_kodu_yorumlari, list) else str(pin_kodu_yorumlari)
            row_data.append(pin_text)
        else:
            row_data.append('')
        
        # Diğer veriler
        row_data.extend([
            yasam_yolu_aciklama or '',
            merkez_sayi_detay or '',
            merkez_sayi_aciklama or '',
            donusum_yillari or '',
            pin_kodu_ozellikleri or '',
            dogum_gunu,
            cinsiyet,
            str(yas) if yas is not None else ''
        ])
        
        # Veri satırını yaz
        writer.writerow(row_data)
        
        # CSV içeriğini al
        csv_content = output.getvalue()
        output.close()
        
        # Response oluştur
        response = make_response(csv_content)
        response.headers['Content-Type'] = 'text/csv; charset=utf-8'
        response.headers['Content-Disposition'] = f'attachment; filename=islami_numeroloji_analiz_{isim_soyisim.replace(" ", "_")}.csv'
        
        return response
        
    except Exception as e:
        print(f"CSV export hatası: {e}")
        return f"Hata: CSV oluşturulurken bir hata oluştu - {str(e)}", 500 
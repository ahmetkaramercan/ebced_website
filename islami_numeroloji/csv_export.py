#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV Export Modülü
İslami Numeroloji analiz sonuçlarını CSV formatında dışa aktarmak için fonksiyonlar
"""

from flask import make_response
import csv
import io
import urllib.parse
from .hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  ozellik_hesaplama, pin_kodu_yorumlari_algoritmasi)
from .hesaplama_cakra import cakra_metin_hesaplamalari, cocuk_cakra_metin_hesaplamalari, cakra_metin_hesaplamalari_ayrintili
from .hesaplama_merkez_sayi import merkez_sayi_bulma, merkez_sayi_aciklamalari
from .text import yasam_yollari


def split_text_by_pages(text, max_chars_per_page=600):
    """
    Uzun metinleri sayfalara böler. Her sayfa maksimum max_chars_per_page karakter içerir.
    Cümle sonlarından böler ve sayfaları _sayfa_1, _sayfa_2, vb. şeklinde adlandırır.
    
    Args:
        text (str): Bölünecek metin
        max_chars_per_page (int): Sayfa başına maksimum karakter sayısı
    
    Returns:
        dict: {'_sayfa_1': 'metin1', '_sayfa_2': 'metin2', ...} formatında dictionary
    """
    if not text or len(text) <= max_chars_per_page:
        return {'_sayfa_1': text}
    
    pages = {}
    remaining_text = text.strip()
    page_num = 1
    
    while remaining_text:
        if len(remaining_text) <= max_chars_per_page:
            # Kalan metin sayfa sınırından küçükse, son sayfa olarak ekle
            pages[f'_sayfa_{page_num}'] = remaining_text
            break
        
        # Sayfa sınırından küçük bir bölüm al
        chunk = remaining_text[:max_chars_per_page]
        
        # Cümle sonu bul (nokta, ünlem, soru işareti)
        sentence_endings = ['.', '!', '?']
        best_split = -1
        
        # Sondan başlayarak en yakın cümle sonunu bul
        for i in range(len(chunk) - 1, max(0, len(chunk) - 100), -1):
            if chunk[i] in sentence_endings:
                # Cümle sonundan sonra boşluk varsa oradan böl
                if i + 1 < len(chunk) and chunk[i + 1] == ' ':
                    best_split = i + 1
                else:
                    best_split = i + 1
                break
        
        if best_split == -1:
            # Cümle sonu bulunamazsa, en yakın boşluktan böl
            space_pos = chunk.rfind(' ')
            if space_pos > max_chars_per_page // 2:  # En az yarı sayfa dolu olsun
                best_split = space_pos
            else:
                # Son çare olarak sayfa sınırından böl
                best_split = max_chars_per_page
        
        # Bu sayfayı kaydet
        current_page = remaining_text[:best_split].strip()
        pages[f'_sayfa_{page_num}'] = current_page
        
        # Kalan metni güncelle
        remaining_text = remaining_text[best_split:].strip()
        page_num += 1
    
    return pages


def yas_hesapla(dogum_gunu_str):
    """Doğum tarihinden yaşı hesaplar"""
    try:
        from datetime import datetime
        # Doğum tarihini parse et
        dogum_parcalari = dogum_gunu_str.split()
        if len(dogum_parcalari) == 3:
            gun, ay, yil = int(dogum_parcalari[0]), int(dogum_parcalari[1]), int(dogum_parcalari[2])
            dogum_tarihi = datetime(yil, ay, gun)
            bugun = datetime.now()
            yas = bugun.year - dogum_tarihi.year
            
            # Doğum günü henüz gelmemişse yaşı bir azalt
            if bugun.month < dogum_tarihi.month or (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
                yas -= 1
                
            return yas
    except (ValueError, IndexError):
        pass

    return None


def generate_csv_export(data):
    """
    Verilen form verilerinden CSV dosyası oluşturur
    Args:
        data (dict): Form verilerini içeren dictionary
        
    Returns:
        Flask Response: CSV dosyasını içeren HTTP response
    """
    # Gerekli alanları kontrol et
    required_fields = ['dogum_gunu', 'isim_soyisim', 'cinsiyet']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Hata: {field} alanı gereklidir")
    
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
        cakra_metinleri, alma_verme_dengesi = cocuk_cakra_metin_hesaplamalari(arti_sistemi)
        evlilik_metinleri = []  # Çocuklar için evlilik metni yok
    else:
        cakra_metinleri, evlilik_metinleri, alma_verme_dengesi = cakra_metin_hesaplamalari_ayrintili(arti_sistemi, cinsiyet)
    
    # Merkez sayının tuple değerini al
    merkez_sayi_detay, merkez_sayi_integer = merkez_sayi_bulma(isim_soyisim)
    pin_kodu_ozellikleri = ozellik_hesaplama(pin_kodu)
    
    # Yaşam yolu açıklamasını al
    yasam_yolu_aciklama = yasam_yollari.get(yasam_yolu, "Bu yaşam yolu için açıklama bulunamadı.")
    
    # Merkez sayı açıklaması - merkez_sayi_detay zaten tam metin içeriyor
    # merkez_sayi_detay uzun detaylı metindir, merkez_sayi_aciklama sadece sayının açıklamasıdır
    merkez_sayi_aciklama = merkez_sayi_detay  # Bu zaten tam metindir
    
    # Çakra metinlerini özel kurallara göre işle
    cakra_pages_data = {}
    
    # Her çakra için maksimum sayfa sayılarını tanımla
    max_pages_per_chakra = {
        0: 4,  # 1. çakra - 4 sayfa
        1: 3,  # 2. çakra - 3 sayfa
        2: 2,  # 3. çakra - 2 sayfa
        3: 4,  # 4. çakra - 4 sayfa
        4: 2,  # 5. çakra - 2 sayfa
        5: 2,  # 6. çakra - 2 sayfa
        6: 3,  # 7. çakra - 3 sayfa
        7: 2,  # 8. çakra - 2 sayfa
        8: 2   # 9. çakra - 2 sayfa
    }
    
    # Önce tüm çakralar için boş sayfaları "." ile doldur
    for i in range(9):
        max_pages = max_pages_per_chakra[i]
        cakra_pages_data[i] = {}
        for page_num in range(1, max_pages + 1):
            cakra_pages_data[i][f'_sayfa_{page_num}'] = "."
    
    # Şimdi çakra metinlerini ekle
    for i in range(9):
        if cakra_metinleri and i < len(cakra_metinleri):
            metin = cakra_metinleri[i]
            
            # Metni ~~~ ile ayır
            if "~~~" in metin:
                metin_parcalari = metin.split("~~~", 1)
                ilk_kisim = metin_parcalari[0].strip()
                ikinci_kisim = metin_parcalari[1].strip()
                
                page_counter = 1
                
                # 1. çakra (i=0): 1. kısım 3 sayfaya kadar, 2. kısım 1 sayfa
                if i == 0:
                    ilk_pages = split_text_by_pages(ilk_kisim, 750)
                    for page_key, page_content in ilk_pages.items():
                        if page_counter <= 4:  # Maksimum 4 sayfa
                            cakra_pages_data[i][f'_sayfa_{page_counter}'] = page_content
                            page_counter += 1
                    
                    # 2. kısım için kalan sayfaya ekle
                    if page_counter <= 4:
                        cakra_pages_data[i][f'_sayfa_{page_counter}'] = ikinci_kisim
                
                # 2. çakra (i=1): 1. kısım için split_text_by_pages kullan
                elif i == 1:
                    ilk_pages = split_text_by_pages(ilk_kisim, 700)
                    for page_key, page_content in ilk_pages.items():
                        if page_counter <= 3:  # Maksimum 3 sayfa
                            cakra_pages_data[i][f'_sayfa_{page_counter}'] = page_content
                            page_counter += 1
                    
                    # 2. kısım için kalan sayfaya ekle
                    if page_counter <= 3:
                        cakra_pages_data[i][f'_sayfa_{page_counter}'] = ikinci_kisim
                
                # 4. çakra (i=3): Hem 1. hem 2. kısım için split_text_by_pages kullan
                elif i == 3:
                    ilk_pages = split_text_by_pages(ilk_kisim, 600)
                    ikinci_pages = split_text_by_pages(ikinci_kisim, 700)
                    
                    # 1. kısım sayfaları
                    for page_key, page_content in ilk_pages.items():
                        if page_counter <= 4:  # Maksimum 4 sayfa
                            cakra_pages_data[i][f'_sayfa_{page_counter}'] = page_content
                            page_counter += 1
                    
                    # 2. kısım sayfaları
                    for page_key, page_content in ikinci_pages.items():
                        if page_counter <= 4:  # Maksimum 4 sayfa
                            cakra_pages_data[i][f'_sayfa_{page_counter}'] = page_content
                            page_counter += 1
                
                # 7. çakra (i=6): Sadece 1. kısım için split_text_by_pages kullan
                elif i == 6:
                    ilk_pages = split_text_by_pages(ilk_kisim, 600)
                    for page_key, page_content in ilk_pages.items():
                        if page_counter <= 3:  # Maksimum 3 sayfa
                            cakra_pages_data[i][f'_sayfa_{page_counter}'] = page_content
                            page_counter += 1
                    
                    # 2. kısım için kalan sayfaya ekle
                    if page_counter <= 3:
                        cakra_pages_data[i][f'_sayfa_{page_counter}'] = ikinci_kisim
                
                # Diğer çakralar (3., 5., 6., 8., 9.): split_text_by_pages kullanma
                else:
                    # 1. kısım ilk sayfaya
                    if page_counter <= max_pages_per_chakra[i]:
                        cakra_pages_data[i][f'_sayfa_{page_counter}'] = ilk_kisim
                        page_counter += 1
                    
                    # 2. kısım ikinci sayfaya
                    if page_counter <= max_pages_per_chakra[i]:
                        cakra_pages_data[i][f'_sayfa_{page_counter}'] = ikinci_kisim
            else:
                # ~~~ yoksa ilk sayfaya ekle
                if max_pages_per_chakra[i] >= 1:
                    cakra_pages_data[i]['_sayfa_1'] = metin
    
    # Pin kodu yorumları - 15 sayfaya kadar doldur
    pin_kodu_pages = {}
    if pin_kodu_yorumlari:
        if isinstance(pin_kodu_yorumlari, list):
            # Boş stringleri filtrele ve temizle
            filtered_yorumlar = [yorum.strip() for yorum in pin_kodu_yorumlari if yorum and yorum.strip()]
            pin_text = '\n\n'.join(filtered_yorumlar)
        else:
            pin_text = str(pin_kodu_yorumlari).strip()
        
        # 750 karakter sınırında böl
        temp_pages = split_text_by_pages(pin_text, 750)
        
        # 15 sayfaya tamamla
        for page_num in range(1, 16):
            page_key = f'_sayfa_{page_num}'
            if page_key in temp_pages:
                pin_kodu_pages[page_key] = temp_pages[page_key]
            else:
                pin_kodu_pages[page_key] = "."
    else:
        # Pin kodu yorumları yoksa 15 boş sayfa
        for page_num in range(1, 16):
            pin_kodu_pages[f'_sayfa_{page_num}'] = "."
    
    # Yaşam yolu açıklaması - 11 sayfaya kadar doldur
    temp_yasam_pages = split_text_by_pages(yasam_yolu_aciklama or '', 650)
    yasam_yolu_pages = {}
    for page_num in range(1, 12):
        page_key = f'_sayfa_{page_num}'
        if page_key in temp_yasam_pages:
            yasam_yolu_pages[page_key] = temp_yasam_pages[page_key]
        else:
            yasam_yolu_pages[page_key] = "."
    
    # Merkez sayı açıklaması - 3 sayfaya kadar doldur
    temp_merkez_pages = split_text_by_pages(merkez_sayi_aciklama or '', 600)
    merkez_sayi_pages = {}
    for page_num in range(1, 4):
        page_key = f'_sayfa_{page_num}'
        if page_key in temp_merkez_pages:
            merkez_sayi_pages[page_key] = temp_merkez_pages[page_key]
        else:
            merkez_sayi_pages[page_key] = "."
    
    pin_kodu_ozellikleri_pages = split_text_by_pages(pin_kodu_ozellikleri or '', 700)
    
    # Alma verme dengesini tek sayfa olarak yaz (bölme yok)
    alma_verme_pages = {'_sayfa_1': alma_verme_dengesi or "."}
    max_alma_verme_pages = len(alma_verme_pages)
    
    # Evlilik metinlerini işle - tüm çakralar için (1-9), her biri 1 sayfa
    evlilik_pages_data = {}
    
    for i in range(9):  # 0-8 (1-9 çakralar)
        evlilik_metin = "."
        if evlilik_metinleri and i < len(evlilik_metinleri) and evlilik_metinleri[i]:
            evlilik_metin = evlilik_metinleri[i]
        
        # Her evlilik metni için 1 sayfa
        evlilik_pages_data[i] = {'_sayfa_1': evlilik_metin}
    
    # CSV için string buffer oluştur
    output = io.StringIO()
    writer = csv.writer(output)
    
    # CSV başlık satırı (sabit sayfa sayılarına göre)
    headers = [
        'full_name',
        'yasam_yolu'
    ]
    
    # Çakra metinleri için başlıklar (sabit sayfa sayılarına göre)
    for i in range(1, 10):  # 1-9 çakralar
        if i == 1:  # 1. çakra - 4 sayfa
            for page_num in range(1, 5):
                headers.append(f'cakra_{i}_sayfa_{page_num}')
        elif i == 2:  # 2. çakra - 3 sayfa
            for page_num in range(1, 4):
                headers.append(f'cakra_{i}_sayfa_{page_num}')
        elif i == 4:  # 4. çakra - 4 sayfa
            for page_num in range(1, 5):
                headers.append(f'cakra_{i}_sayfa_{page_num}')
        elif i == 7:  # 7. çakra - 3 sayfa
            for page_num in range(1, 4):
                headers.append(f'cakra_{i}_sayfa_{page_num}')
        else:  # 3., 5., 6., 8., 9. çakra - 2 sayfa
            for page_num in range(1, 3):
                headers.append(f'cakra_{i}_sayfa_{page_num}')
    
    # Pin kodu yorumları - 15 sayfa
    for page_num in range(1, 16):
        headers.append(f'pin_kodu_yorumlari_sayfa_{page_num}')
    
    # Yaşam yolu açıklaması - 11 sayfa
    for page_num in range(1, 12):
        headers.append(f'yasam_yolu_aciklama_sayfa_{page_num}')
    
    headers.append('merkez_sayi')
    
    # Merkez sayı açıklaması - 3 sayfa
    for page_num in range(1, 4):
        headers.append(f'merkez_sayi_aciklama_sayfa_{page_num}')
    

    
    # Alma verme dengesi başlıkları
    for page_num in range(1, max_alma_verme_pages + 1):
        headers.append(f'alma_verme_dengesi_sayfa_{page_num}')
    
    # Evlilik metinleri başlıkları (tüm çakralar için, her biri 1 sayfa)
    for i in range(1, 10):  # 1-9 çakralar
        headers.append(f'cakra_{i}_evlilik_sayfa_1')
    
    # Sabit alanlar
    headers.extend([
        'dogum_tarihi'
    ])
    
    # Başlık satırını yaz
    writer.writerow(headers)
    
    # Full name'i Türkçe dilbilgisi kurallarına göre düzenle
    def format_full_name(name):
        """İsmi Türkçe dilbilgisi kurallarına göre formatlar"""
        # Türkçe sesli harfler
        sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'A', 'E', 'I', 'İ', 'O', 'Ö', 'U', 'Ü']
        
        # İsmi büyük harfe çevir
        name_upper = name.upper()
        
        # İsmin son harfini kontrol et
        son_harf = name_upper[-1] if name_upper else ''
        
        # Son harf sesli ise 'NIN, sessiz ise 'IN ekle
        if son_harf in sesli_harfler:
            formatted_name = f"{name_upper} 'NIN İÇSEL YOLCULUĞUDUR"
        else:
            formatted_name = f"{name_upper} 'IN İÇSEL YOLCULUĞUDUR"
        
        return formatted_name
    
    # Veri satırı
    row_data = [
        format_full_name(isim_soyisim),  # full_name
        yasam_yolu  # yasam_yolu
    ]
    
    # Çakra metinlerini ekle (sabit sayfa sayılarına göre)
    for i in range(9):
        chakra_pages = cakra_pages_data.get(i, {'_sayfa_1': ''})
        if i == 0:  # 1. çakra - 4 sayfa
            for page_num in range(1, 5):
                page_key = f'_sayfa_{page_num}'
                page_content = chakra_pages.get(page_key, '')
                row_data.append(page_content)
        elif i == 1:  # 2. çakra - 3 sayfa
            for page_num in range(1, 4):
                page_key = f'_sayfa_{page_num}'
                page_content = chakra_pages.get(page_key, '')
                row_data.append(page_content)
        elif i == 3:  # 4. çakra - 4 sayfa
            for page_num in range(1, 5):
                page_key = f'_sayfa_{page_num}'
                page_content = chakra_pages.get(page_key, '')
                row_data.append(page_content)
        elif i == 6:  # 7. çakra - 3 sayfa
            for page_num in range(1, 4):
                page_key = f'_sayfa_{page_num}'
                page_content = chakra_pages.get(page_key, '')
                row_data.append(page_content)
        else:  # 3., 5., 6., 8., 9. çakra - 2 sayfa
            for page_num in range(1, 3):
                page_key = f'_sayfa_{page_num}'
                page_content = chakra_pages.get(page_key, '')
                row_data.append(page_content)
    
    # Pin kodu yorumları sayfalarını ekle (15 sayfa)
    for page_num in range(1, 16):
        page_key = f'_sayfa_{page_num}'
        page_content = pin_kodu_pages.get(page_key, '')
        row_data.append(page_content)
    
    # Yaşam yolu açıklaması sayfalarını ekle (11 sayfa)
    for page_num in range(1, 12):
        page_key = f'_sayfa_{page_num}'
        page_content = yasam_yolu_pages.get(page_key, '')
        row_data.append(page_content)
    
    # Merkez sayı
    row_data.append(merkez_sayi_detay or '')
    
    # Merkez sayı açıklaması sayfalarını ekle (3 sayfa)
    for page_num in range(1, 4):
        page_key = f'_sayfa_{page_num}'
        page_content = merkez_sayi_pages.get(page_key, '')
        row_data.append(page_content)
    

    
    # Alma verme dengesi sayfalarını ekle
    for page_num in range(1, max_alma_verme_pages + 1):
        page_key = f'_sayfa_{page_num}'
        page_content = alma_verme_pages.get(page_key, '')
        row_data.append(page_content)
    
    # Evlilik metinleri sayfalarını ekle (tüm çakralar için, her biri 1 sayfa)
    for i in range(9):  # 0-8 (1-9 çakralar)
        evlilik_pages = evlilik_pages_data.get(i, {'_sayfa_1': ''})
        page_content = evlilik_pages.get('_sayfa_1', '')
        row_data.append(page_content)
    
    # Sabit veriler
    row_data.extend([
        dogum_gunu
    ])
    
    # Veri satırını yaz
    writer.writerow(row_data)
    
    # CSV içeriğini al
    csv_content = output.getvalue()
    output.close()
    
    # Dosya adı için Türkçe karakterleri temizle (sadece dosya adı için, içerik Türkçe kalacak)
    def clean_filename(filename):
        """Türkçe karakterleri ASCII karakterlere çevirir - sadece dosya adı için"""
        turkish_chars = {
            'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
            'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
        }
        for turkish, ascii_char in turkish_chars.items():
            filename = filename.replace(turkish, ascii_char)
        return filename
    
    # Temiz dosya adı oluştur (sadece dosya adı için, CSV içeriği Türkçe kalacak)
    clean_name = clean_filename(isim_soyisim.replace(" ", "_"))
    filename = f'islami_numeroloji_analiz_{clean_name}.csv'
    
    # Response oluştur
    response = make_response(csv_content)
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    
    # RFC 5987 uyumlu dosya adı için URL encoding kullan
    encoded_filename = urllib.parse.quote(filename.encode('utf-8'))
    response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_filename}"
    
    return response

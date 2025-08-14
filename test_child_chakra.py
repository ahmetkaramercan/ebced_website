#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for child chakra functionality
"""

from datetime import datetime
from islami_numeroloji.hesaplama_cakra import cakra_metin_hesaplamalari, cocuk_cakra_metin_hesaplamalari

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

def test_child_chakra():
    """Test child chakra functionality"""
    
    # Test cases
    test_cases = [
        ("15 03 2020", "Çocuk (5 yaş ve altı)"),
        ("15 03 2015", "Çocuk (5 yaş ve altı)"),
        ("15 03 2010", "Yetişkin (5 yaş üstü)"),
        ("15 03 2000", "Yetişkin (5 yaş üstü)")
    ]
    
    # Mock arti_sistemi for testing
    arti_sistemi = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],  # First array
        [2, 1, 3, 0, 1, 2, 1, 0, 2],  # Second array (chakra values)
        [0, 0, 0, 0, 0, 0, 0, 0, 0]   # Third array
    ]
    
    print("=== Çocuk Çakra Test Sonuçları ===\n")
    
    for dogum_tarihi, beklenen_tip in test_cases:
        yas = yas_hesapla(dogum_tarihi)
        
        if yas is not None and yas <= 5:
            cakra_metinleri = cocuk_cakra_metin_hesaplamalari(arti_sistemi)
            cakra_tipi = "Çocuk çakra hesaplaması"
        else:
            cakra_metinleri = cakra_metin_hesaplamalari(arti_sistemi, "erkek")
            cakra_tipi = "Çakra hesaplaması"
        
        print(f"Test: {dogum_tarihi}")
        print(f"Yaş: {yas}")
        print(f"Çakra Tipi: {cakra_tipi}")
        print(f"Beklenen: {beklenen_tip}")
        print(f"Sonuç: {'✓' if (yas <= 5 and cakra_tipi == 'Çocuk çakra hesaplaması') or (yas > 5 and cakra_tipi == 'Çakra hesaplaması') else '✗'}")
        print(f"Çakra Metin Sayısı: {len(cakra_metinleri)}")
        print("-" * 50)

if __name__ == "__main__":
    test_child_chakra()

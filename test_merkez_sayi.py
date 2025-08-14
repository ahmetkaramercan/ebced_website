#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from islami_numeroloji.hesaplama_merkez_sayi import merkez_sayi_bulma

def test_merkez_sayi():
    """Merkez sayı fonksiyonunu test eder"""
    
    test_cases = [
        "muhammed ali kaplan",  # 9 + 1 + 2 = 12, 1+2=3
        "aslı fatma şefteli",   # 1 + 2 + 19 = 22
        "emine akın",           # 19 + 1
        "ahmet karamercan",     # 6 + 8 = 14, 1+4=5
        "payidar tüfekçioğlu",  # 11 + 8 = 19
        "bekir develi",       # 5 + 19
        "mert akalın ahmet"     # 5 + 6 + 11 = 22
    ]
    
    print("=== MERKEZ SAYI TESTLERİ ===\n")
    
    for test_case in test_cases:
        #print(f"Test: {test_case}")
        try:
            sonuc_metni, merkez_sayi = merkez_sayi_bulma(test_case)
            #print(f"Merkez Sayı: {merkez_sayi}")
            print(f"{sonuc_metni}")
            print("-" * 50)
        except Exception as e:
            print(f"Hata: {e}")
            print("-" * 50)

if __name__ == "__main__":
    test_merkez_sayi()

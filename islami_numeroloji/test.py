from hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  merkez_sayi_bulma, donusum_yillari_bulma, ozellik_hesaplama, pin_kodu_yorumlari_algoritmasi)
from hesaplama_cakra import cakra_metin_hesaplamalari
"""pin_kodu = pin_kodu_hesaplama("09 08 2001")
print("Pin Kodu:", pin_kodu)
print("Pin Kodu 1:", pin_kodu[0])
print("Pin Kodu 2:", pin_kodu[4])

print("Pin Kodu Elemanları:")
for i, element in enumerate(pin_kodu):
    print(f"  {i}: '{element}' (type: {type(element)})")
"""

print(merkez_sayi_bulma("emir akalın"))

array = [
    [2,1,2,0,2,5,6,7,8,],
    [2,1,2,0,3,2,4,1,2],
    [0,0,1,2,2,0,0,0,0]
]
cakra_metin_hesaplamalari(array, "kadın")
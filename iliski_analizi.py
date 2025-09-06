k = [""] * 9

# Import necessary functions from ebced.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ebced import chakra_hesapla, yasam_yolu_hesapla, chakra_values

def ebced_toplama(*args):
    """
    Bu fonksiyon, verilen parametrelerin rakamlarını toplar ve tek hane olana kadar bu işlemi tekrarlar.
    String parametrelerin içindeki sayı olan kısımlar tam sayıya çevrilir.
    """
    total_sum = 0
    for arg in args:
        if isinstance(arg, str):
            number_str = ''.join(filter(str.isdigit, arg))
            if number_str:
                total_sum += int(number_str)
        elif isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, float):
            total_sum += int(arg)
    
    # Sayının rakamlarını toplar ve tek hane olana kadar bu işlemi tekrarlar
    while total_sum >= 10:
        if total_sum == 11:
            return "2*"
        total_sum = sum(int(digit) for digit in str(total_sum))
    
    return str(total_sum)

def iliski_pin_kodu_hesaplama(dogum_tarihi1, dogum_tarihi2, isim1="", isim2=""):
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    # Doğum tarihini gün, ay ve yıl olarak ayır
    gun1, ay1, yil1 = dogum_tarihi1.split(' ')
    gun2, ay2, yil2 = dogum_tarihi2.split(' ')

    # Ebced toplam fonksiyonunu kullanarak k değerlerini hesapla
    k[0] = ebced_toplama(ebced_toplama(gun1) , ebced_toplama(gun2))
    k[1] = ebced_toplama(ebced_toplama(ay1) , ebced_toplama(ay2))
    k[2] = ebced_toplama(ebced_toplama(yil1) , ebced_toplama(yil2))
    k[3] = ebced_toplama(k[0] + k[1] + k[2])
    k[4] = ebced_toplama(k[0] + k[3])
    k[5] = ebced_toplama(k[0] + k[1])
    k[6] = ebced_toplama(k[1] + k[2])
    k[7] = ebced_toplama(k[5] + k[6])
    k[8] = ebced_toplama(k[0] + k[1] + k[2] + k[3] + k[4] + k[5] + k[6] + k[7])
    
    # Değerleri şartlara göre güncelle
    for i in range(9):
        if int(k[i][0]) == (i + 1):
            k[i] += '!'

    # Her kişi için ayrı pin kodları hesapla
    k1 = [""] * 9
    k2 = [""] * 9
    
    # Kişi 1 için pin kodu
    k1[0] = ebced_toplama(gun1)
    k1[1] = ebced_toplama(ay1)
    k1[2] = ebced_toplama(yil1)
    k1[3] = ebced_toplama(k1[0] + k1[1] + k1[2])
    k1[4] = ebced_toplama(k1[0] + k1[3])
    k1[5] = ebced_toplama(k1[0] + k1[1])
    k1[6] = ebced_toplama(k1[1] + k1[2])
    k1[7] = ebced_toplama(k1[5] + k1[6])
    k1[8] = ebced_toplama(k1[0] + k1[1] + k1[2] + k1[3] + k1[4] + k1[5] + k1[6] + k1[7])
    
    # Kişi 2 için pin kodu
    k2[0] = ebced_toplama(gun2)
    k2[1] = ebced_toplama(ay2)
    k2[2] = ebced_toplama(yil2)
    k2[3] = ebced_toplama(k2[0] + k2[1] + k2[2])
    k2[4] = ebced_toplama(k2[0] + k2[3])
    k2[5] = ebced_toplama(k2[0] + k2[1])
    k2[6] = ebced_toplama(k2[1] + k2[2])
    k2[7] = ebced_toplama(k2[5] + k2[6])
    k2[8] = ebced_toplama(k2[0] + k2[1] + k2[2] + k2[3] + k2[4] + k2[5] + k2[6] + k2[7])
    
    # Değerleri şartlara göre güncelle
    for i in range(9):
        if int(k1[i][0]) == (i + 1):
            k1[i] += '!'
        if int(k2[i][0]) == (i + 1):
            k2[i] += '!'

    # Yaşam yolu hesaplamaları
    yasam_yolu1 = yasam_yolu_hesapla(dogum_tarihi1)
    yasam_yolu2 = yasam_yolu_hesapla(dogum_tarihi2)
    
    # Çakra analizleri
    chakra1 = chakra_hesapla(k1, isim1) if isim1 else []
    chakra2 = chakra_hesapla(k2, isim2) if isim2 else []
    
    # Sonuçları tek satırda yazdır
    print("İLİŞKİ ANALİZİ SONUÇLARI:")
    print("=" * 80)
    
    # Kişi 1 bilgileri
    print(f"KİŞİ 1 - İsim: {isim1}, Doğum: {dogum_tarihi1}")
    print(f"Pin Kodu: {' '.join(k1)}")
    print(f"Yaşam Yolu: {yasam_yolu1}")
    if chakra1:
        chakra_str1 = " | ".join([f"{c['left_plus']}{c['number']}{c['right_plus']}" for c in chakra1])
        print(f"Çakra: {chakra_str1}")
    print("-" * 40)
    
    # Kişi 2 bilgileri
    print(f"KİŞİ 2 - İsim: {isim2}, Doğum: {dogum_tarihi2}")
    print(f"Pin Kodu: {' '.join(k2)}")
    print(f"Yaşam Yolu: {yasam_yolu2}")
    if chakra2:
        chakra_str2 = " | ".join([f"{c['left_plus']}{c['number']}{c['right_plus']}" for c in chakra2])
        print(f"Çakra: {chakra_str2}")
    print("-" * 40)
    
    # İlişki pin kodu
    print(f"İLİŞKİ PİN KODU: {' '.join(k)}")
    print("=" * 80)

    return {
        'k': k,
        'kisi1': {
            'pin_kodu': k1,
            'yasam_yolu': yasam_yolu1,
            'chakra': chakra1
        },
        'kisi2': {
            'pin_kodu': k2,
            'yasam_yolu': yasam_yolu2,
            'chakra': chakra2
        }
    }



# Örnek kullanım:
if __name__ == "__main__":
    # Test verileri
    dogum_tarihi1 = "15 03 1990"
    dogum_tarihi2 = "22 07 1985"
    isim1 = "Ahmet Yılmaz"
    isim2 = "Ayşe Demir"
    
    # İlişki analizi
    sonuc = iliski_pin_kodu_hesaplama(dogum_tarihi1, dogum_tarihi2, isim1, isim2)
    
    # Alternatif kullanım (sadece doğum tarihleri ile):
    # sonuc = iliski_pin_kodu_hesaplama(dogum_tarihi1, dogum_tarihi2)
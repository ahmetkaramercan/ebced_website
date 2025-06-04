k = [""] * 9


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

def iliski_pin_kodu_hesaplama(dogum_tarihi1, dogum_tarihi2):
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

    return {'k': k}



"""dogum_tarihi1 = input("İlk Doğum tarihini gg.aa.yyyy formatında girin: ")
dogum_tarihi2 = input("İkinci Doğum tarihini gg.aa.yyyy formatında girin: ")
pin_kodu_hesaplama(dogum_tarihi1, dogum_tarihi2)"""
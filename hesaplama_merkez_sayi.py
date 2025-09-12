
merkez_sayi_aciklamalari = {
    "1" : """Merkeziniz kendinizi ifade etmek ve hayallerinizin peşinden gitmektir. Hem isminiz hem de doğum tarihiniz bu konuda sizi destekliyor. Konuşma ve iletişim gerektiren alanlarda başarılı olabilirsiniz. ****** ismi size hedef sahibi olmayı ve kararlılığı vermiştir. İlişkilerinizdeki sorunlara rağmen sezgilerinize güvenerek yolunuza devam etmelisiniz.""",
    "2" : """Hayatınız ilişkilerinizi düzenlemekle başlamış. ****** ismi size sorunları önceden fark etme ve enerjinizi koruma gücü kazandırıyor. Her ilişki, kök sorunlarınızı görmeniz için bir fırsattır.""",
    "3" : """Başlangıcınız kendinizi tanımak ve sorgulamakla olmuş. ****** ismi sizi liderlik yapan ve söz sahibi biri haline getirmiş. Ancak öfkenizi yönetmekte zorlanmak ve fikirlerinize değer beklemek ilişkilerinizde sınavlar yaratmış.""",
    "4" : """****** isminiz öncelikle kalp çakranızı geliştirmiş. Karşılaştığınız sıkıntılar size sabrı, sınır koymayı ve tedbir almayı öğretmiştir. Zorluklar dönüşüm için bir fırsattır. Siz de fikirlerinizle öne çıkmak ve liderlik etmek istiyorsunuz.""",
    "5" : """****** isminiz size öncelikle ilişkilerdeki sorunları çözme gücü veriyor. Depresif hallerden çıkıp olayların mesajını anladığınızda kendinizi güçlü şekilde ifade edebilirsiniz. Hayallerinize ulaşmak için sanat ve özellikle müzik size iyi gelecektir.""",
    "6" : """Hayatınız sorumluluk almakla başlamış. Çevrenizden gelen yükler sezgilerinizi fark etmenizi sağlamış. ****** ismiyle sınır koymayı öğreniyor ve imtihanlardan ders çıkararak yeni yollar açıyorsunuz.""",
    "7" : """Merkeziniz derin düşünmek ve maneviyatınızı geliştirmektir. İlişkilerdeki arayışlar ancak bilinçli bir imanla tatmin bulur. Neden inandığını bilmek sizin için dönüştürücü olacaktır.""",
    "8" : """Merkeziniz auranızı korumak ve ilişkilerde sınırlar belirlemek üzerine kuruludur. Negatif ortamlardan uzak durmalı, sezgilerinizi geliştirmelisiniz. Kendinizi ifade etmenin yolu net sınırlar koymaktan geçer.""",
    "9" : """Merkeziniz enerjinizi korumak ve ilişkilerde denge kurmaktır. Bolluk için olumsuz insanlardan uzaklaşmalı, sezgilerinizi kullanmalısınız. Sınırlarınızı netleştirdiğinizde hem ilişkiler hem de ifade gücünüz güçlenecektir.""",
    "11" : """11 enerjisine sahipsiniz, yani bir İndigosunuz. Bu, size yanlış olanı değiştirme ve dönüştürme gücü verir. Kendinizi iyileştirip liderlik yönünüzü kullanmalı, ilişkilerinizdeki sorunları da dönüştürmeye çalışmalısınız.""",
    "19" : """****** isminiz 19 enerjisi taşır. Bu, zorluklardan ders çıkararak dönüşmeyi ifade eder. Siz aynı zamanda 11 enerjisine sahip bir İndigosunuz. Bu güçle hem kendinizi hem çevrenizi iyileştirme potansiyeliniz vardır.""",
    "22" : """****** isminiz 22 enerjisini içerir. Bu enerji, bilgiyi paylaşmayı, elindekini başkalarına sunmayı ve imtihanlardan ders çıkarmayı temsil eder. Kendinizi iyileştirip üretkenliğinizi insanlık için kullanmalısınız.""",
    "33" : """****** isminiz 33 enerjisine sahiptir. Bu sayı ağır sorumlulukları, olgunlaşmayı ve duyguları yönetmeyi ifade eder. Aileyle ilgili sınavlar yaşamış olabilirsiniz. Nefsinizi terbiye edip geçmişinizi kabullendiğinizde çok daha sağlam adımlar atacaksınız.""",
}

chakra_values = {
    'A': 1, 'S': 1, 'Ş': 1, 'J': 1,
    'B': 2, 'T': 2, 'K': 2,
    'C': 3, 'Ç': 3, 'L': 3, 'U': 3, 'Ü': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5,
    'F': 6, 'O': 6, 'X': 6, 'Ö': 6, 'Q': 6,
    'P': 7, 'Y': 7, 'G': 7, 'Ğ': 7,
    'H': 8, 'Z': 8,
    'I': 9, 'İ': 9, 'R': 9
}
sesli_harfler = {'A', 'E', 'I', 'İ', 'O', 'Ö', 'U', 'Ü'}


def ebced_toplama_merkez_sayi(sayi):
    """
    Bu fonksiyon, verilen sayının rakamlarını toplar ve tek hane olana kadar bu işlemi tekrarlar.
    Özel sayılar (11, 19, 22, 33) korunur.
    """
    if sayi in [11, 19, 22, 33]:
        return str(sayi)
    
    while sayi >= 10:
        if sayi in [11, 19, 22, 33]:
            return str(sayi)
        sayi = sum(int(digit) for digit in str(sayi))
    
    return str(sayi)


def add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, sayi_str, isimler):
    """
    Helper function to ensure consistency between kalan_sayilar and kalan_isimler
    """
    if sayi_str not in kalan_isimler:
        kalan_isimler[sayi_str] = []
    kalan_isimler[sayi_str].extend(isimler)
    if sayi_str not in kalan_sayilar:
        kalan_sayilar.append(sayi_str)


def validate_kalan_consistency(kalan_sayilar, kalan_isimler):
    """
    Validate that kalan_sayilar and kalan_isimler are consistent
    """
    for sayi in kalan_sayilar:
        if sayi not in kalan_isimler:
            print(f"UYARI: {sayi} kalan_sayilar'da var ama kalan_isimler'de yok!")
            # Fix the inconsistency
            kalan_isimler[sayi] = []
    
    for sayi in kalan_isimler:
        if sayi not in kalan_sayilar:
            print(f"UYARI: {sayi} kalan_isimler'de var ama kalan_sayilar'da yok!")
            # Fix the inconsistency
            kalan_sayilar.append(sayi)


def isim_hesaplama(isim):
    """
    Tek bir isim için sesli harflerin toplamını hesaplar
    """
    total_sum = 0
    for char in isim.upper():
        if char in sesli_harfler and char in chakra_values:
            total_sum += chakra_values[char]
    
    # Eğer toplam 0 ise, 1 olarak kabul et
    if total_sum == 0:
        return "1"
    
    # Özel sayı kontrolü
    if total_sum in [11, 19, 22, 33]:
        return str(total_sum)
    
    # Normal sayı ise ebced_toplama_merkez_sayi ile işle
    return ebced_toplama_merkez_sayi(total_sum)


def ozel_sayi_kombinasyonu_bul(sayilar, kalan_isimler):
    """
    Özel sayıların kombinasyonlarını kontrol eder ve toplanabilir olanları bulur
    """
    from itertools import combinations
    
    ozel_sayilar = [11, 19, 22, 33]
    ozel_sayilar_str = []
    
    for sayi_str in sayilar:
        sayi = int(sayi_str)
        if sayi in ozel_sayilar:
            ozel_sayilar_str.append(sayi_str)
    
    # Özel sayıları 2'li gruplar halinde topla
    for combo in combinations(ozel_sayilar_str, 2):
        sayi1_str, sayi2_str = combo
        sayi1 = int(sayi1_str)
        sayi2 = int(sayi2_str)
        
        # 19 özel durumu: 19 + 11 = 22 + 8, 19 + 22 = 33 + 8, 19 + 33 = 44 (normal)
        if sayi1 == 19 or sayi2 == 19:
            if sayi1 == 19:
                diger_sayi = sayi2
            else:
                diger_sayi = sayi1
                
            if diger_sayi in [11, 22, 33]:
                # 19 + 11 = 22 + 8, 19 + 22 = 33 + 8
                if diger_sayi == 11:
                    toplam = 22
                    kalan = 8
                elif diger_sayi == 22:
                    toplam = 33
                    kalan = 8
                else:  # 33
                    toplam = 52  # Normal toplama
                    kalan = None
                
                if kalan is not None:
                    # 19 ve diğer sayıyı kaldır, toplam ve kalan ekle
                    # Key existence check before accessing
                    if sayi1_str in kalan_isimler and sayi2_str in kalan_isimler:
                        kullanilan_isimler = kalan_isimler[sayi1_str] + kalan_isimler[sayi2_str]
                        return True, [sayi1_str, sayi2_str], toplam, kalan, kullanilan_isimler
                    else:
                        # Debug information
                        missing_keys = []
                        if sayi1_str not in kalan_isimler:
                            missing_keys.append(sayi1_str)
                        if sayi2_str not in kalan_isimler:
                            missing_keys.append(sayi2_str)
                        print(f"UYARI: Özel sayı kombinasyonunda eksik anahtarlar: {missing_keys}")
                        print(f"kalan_isimler anahtarları: {list(kalan_isimler.keys())}")
        else:
            # Normal özel sayı toplama
            toplam = sayi1 + sayi2
            if toplam in ozel_sayilar:
                # Key existence check before accessing
                if sayi1_str in kalan_isimler and sayi2_str in kalan_isimler:
                    kullanilan_isimler = kalan_isimler[sayi1_str] + kalan_isimler[sayi2_str]
                    return True, [sayi1_str, sayi2_str], toplam, None, kullanilan_isimler
                else:
                    # Debug information
                    missing_keys = []
                    if sayi1_str not in kalan_isimler:
                        missing_keys.append(sayi1_str)
                    if sayi2_str not in kalan_isimler:
                        missing_keys.append(sayi2_str)
                    print(f"UYARI: Özel sayı kombinasyonunda eksik anahtarlar: {missing_keys}")
                    print(f"kalan_isimler anahtarları: {list(kalan_isimler.keys())}")
    
    return False, None, None, None, None


def normal_sayi_kombinasyonu_bul(sayilar, kalan_isimler):
    """
    Normal sayıların kombinasyonlarını kontrol eder ve özel sayı oluşturanları bulur
    """
    from itertools import combinations
    
    ozel_sayilar = [11, 19, 22, 33]
    normal_sayilar = []
    
    for sayi_str in sayilar:
        sayi = int(sayi_str)
        if sayi not in ozel_sayilar:
            normal_sayilar.append(sayi_str)
    
    # Normal sayıları 2'li gruplar halinde topla
    for combo in combinations(normal_sayilar, 2):
        sayi1_str, sayi2_str = combo
        sayi1 = int(sayi1_str)
        sayi2 = int(sayi2_str)
        toplam = sayi1 + sayi2
        
        if toplam in ozel_sayilar:
            # Key existence check before accessing
            if sayi1_str in kalan_isimler and sayi2_str in kalan_isimler:
                kullanilan_isimler = kalan_isimler[sayi1_str] + kalan_isimler[sayi2_str]
                return True, [sayi1_str, sayi2_str], toplam, None, kullanilan_isimler
            else:
                # Debug information
                missing_keys = []
                if sayi1_str not in kalan_isimler:
                    missing_keys.append(sayi1_str)
                if sayi2_str not in kalan_isimler:
                    missing_keys.append(sayi2_str)
                print(f"UYARI: Normal sayı kombinasyonunda eksik anahtarlar: {missing_keys}")
                print(f"kalan_isimler anahtarları: {list(kalan_isimler.keys())}")
    
    return False, None, None, None, None


def istisna_kontrol(sayilar, kalan_isimler):
    """
    İstisna durumları kontrol eder:
    - 19 + 3 = 22 (19 yakınında 3 varsa)
    - 11 + 8 = 19 (11 yakınında 8 varsa ve başka 11 yoksa)
    """
    # 19 + 3 = 22 kontrolü
    if "19" in sayilar and "3" in sayilar:
        # Key existence check before accessing
        if "19" in kalan_isimler and "3" in kalan_isimler:
            kullanilan_isimler = kalan_isimler["19"] + kalan_isimler["3"]
            return True, ["19", "3"], 22, None, kullanilan_isimler
        else:
            # Debug information
            missing_keys = []
            if "19" not in kalan_isimler:
                missing_keys.append("19")
            if "3" not in kalan_isimler:
                missing_keys.append("3")
            print(f"UYARI: İstisna kontrolünde eksik anahtarlar: {missing_keys}")
            print(f"kalan_isimler anahtarları: {list(kalan_isimler.keys())}")
    
    # 11 + 8 = 19 kontrolü (başka 11 yoksa)
    if "11" in sayilar and "8" in sayilar:
        on_bir_sayisi = sayilar.count("11")
        if on_bir_sayisi == 1:  # Sadece 1 tane 11 varsa
            # Key existence check before accessing
            if "11" in kalan_isimler and "8" in kalan_isimler:
                kullanilan_isimler = kalan_isimler["11"] + kalan_isimler["8"]
                return True, ["11", "8"], 19, None, kullanilan_isimler
            else:
                # Debug information
                missing_keys = []
                if "11" not in kalan_isimler:
                    missing_keys.append("11")
                if "8" not in kalan_isimler:
                    missing_keys.append("8")
                print(f"UYARI: İstisna kontrolünde eksik anahtarlar: {missing_keys}")
                print(f"kalan_isimler anahtarları: {list(kalan_isimler.keys())}")
    
    return False, None, None, None, None


def merkez_sayi_bulma(isim_soyisim):
    """
    Merkez sayı hesaplama fonksiyonu.
    
    Her isim için ayrı hesaplama yapılır. Özel sayılar (11, 19, 22, 33) kendi aralarında toplanabilir.
    19 diğerleriyle toplanırken 11 + 8 olarak ayrılır.
    
    Algoritma:
    1. Her isim için ayrı hesaplama yapılır
    2. While döngüsünde toplanacak şey kalmayana kadar devam eder
    3. Her döngüde öncelik sırası:
       - Normal sayı kombinasyonları (özel sayı oluşturan)
       - İstisna durumlar (19+3=22, 11+8=19)
       - Özel sayı kombinasyonları
    4. 19'un özel özellikleri (19+11=22+8, 19+22=33+8)
    5. Hiçbir metin birden fazla kez yazılmayacak
    """
    # İsmi boşluklara göre ayır
    isimler = [isim.strip() for isim in isim_soyisim.split() if isim.strip()]
    
    if not isimler:
        return "İsim bulunamadı", ""
    
    # Her isim için hesaplama yap
    isim_sayilari = []
    isim_sayilari_str = []
    isim_eslesmesi = {}  # Hangi sayının hangi isimden geldiğini tut
    
    for isim in isimler:
        sayi = isim_hesaplama(isim)
        isim_sayilari.append(int(sayi))
        isim_sayilari_str.append(sayi)
        
        # Aynı sayıya sahip isimlerin üzerine yazılmaması için
        if sayi in isim_eslesmesi:
            isim_eslesmesi[sayi].append(isim)
        else:
            isim_eslesmesi[sayi] = [isim]
    
    # 19 kontrolü - hesaplamanın herhangi bir yerinde 19 var mı?
    on_dokuz_var = "19" in isim_sayilari_str
    on_dokuz_isimleri = []
    if on_dokuz_var:
        for i, sayi in enumerate(isim_sayilari_str):
            if sayi == "19":
                on_dokuz_isimleri.append(isimler[i])
    
    # While döngüsü - toplanacak şey kalmayana kadar devam et
    # Aynı sayıya sahip isimlerin sayısını da hesaba kat
    sayi_sayilari = {}
    for sayi in isim_sayilari_str:
        if sayi in sayi_sayilari:
            sayi_sayilari[sayi] += 1
        else:
            sayi_sayilari[sayi] = 1
    
    kalan_sayilar = list(sayi_sayilari.keys())  # Unique sayılar
    kalan_isimler = isim_eslesmesi.copy()
    
    dongu_sayisi = 1
    sonuc = ""
    
    while len(kalan_sayilar) > 1:
        # Validate consistency at the start of each iteration
        validate_kalan_consistency(kalan_sayilar, kalan_isimler)
        
        # 1. Öncelik: Normal sayı kombinasyonları (özel sayı oluşturan)
        normal_kombinasyon, normal_sayilar, normal_sonuc, normal_kalan, normal_isimler = normal_sayi_kombinasyonu_bul(kalan_sayilar, kalan_isimler)
        
        if normal_kombinasyon:
            # Kullanılan sayıları kalan sayılardan çıkar
            for sayi in normal_sayilar:
                if sayi in kalan_sayilar:
                    kalan_sayilar.remove(sayi)
                if sayi in kalan_isimler:
                    del kalan_isimler[sayi]
            
            # Sonucu ekle
            add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(normal_sonuc), normal_isimler)
            
            dongu_sayisi += 1
            continue
        
        # 1.5. Öncelik: Normal sayıları topla (özel sayı oluşturmasa bile)
        ozel_sayilar = [11, 19, 22, 33]
        normal_sayilar = []
        
        for sayi_str in kalan_sayilar:
            sayi = int(sayi_str)
            if sayi not in ozel_sayilar:
                normal_sayilar.append(sayi_str)
        
        if len(normal_sayilar) >= 2:
            # En küçük iki normal sayıyı topla
            normal_sayilar.sort(key=lambda x: int(x))
            sayi1_str = normal_sayilar[0]
            sayi2_str = normal_sayilar[1]
            sayi1 = int(sayi1_str)
            sayi2 = int(sayi2_str)
            
            # Aynı sayıdan kaç tane kullanacağımızı hesapla
            sayi1_adedi = sayi_sayilari.get(sayi1_str, 1)
            sayi2_adedi = sayi_sayilari.get(sayi2_str, 1)
            
            toplam = (sayi1 * sayi1_adedi) + (sayi2 * sayi2_adedi)
            
            # İsimleri sakla (silmeden önce)
            isimler1 = kalan_isimler.get(sayi1_str, [])
            isimler2 = kalan_isimler.get(sayi2_str, [])
            tum_isimler = isimler1 + isimler2
            
            # Kullanılan sayıları kalan sayılardan çıkar
            kalan_sayilar.remove(sayi1_str)
            kalan_sayilar.remove(sayi2_str)
            if sayi1_str in kalan_isimler:
                del kalan_isimler[sayi1_str]
            if sayi2_str in kalan_isimler:
                del kalan_isimler[sayi2_str]
            
            # Sonucu ekle - sadece ebced sonucunu ekle, orijinal toplamı ekleme
            ebced_sonuc = ebced_toplama_merkez_sayi(toplam)
            add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(ebced_sonuc), tum_isimler)
            
            dongu_sayisi += 1
            continue
        
        # 2. Öncelik: İstisna durumlar
        istisna_bulundu, istisna_sayilar, istisna_sonuc, istisna_kalan, istisna_isimler = istisna_kontrol(kalan_sayilar, kalan_isimler)
        
        if istisna_bulundu:
            # Kullanılan sayıları kalan sayılardan çıkar
            for sayi in istisna_sayilar:
                if sayi in kalan_sayilar:
                    kalan_sayilar.remove(sayi)
                if sayi in kalan_isimler:
                    del kalan_isimler[sayi]
            
            # Sonucu ekle
            add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(istisna_sonuc), istisna_isimler)
            
            # Kalan varsa ekle (19+11=22+8 gibi durumlar için)
            if istisna_kalan is not None:
                add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(istisna_kalan), istisna_isimler)
            
            dongu_sayisi += 1
            continue
        
        # 3. Özel sayı kombinasyonları
        ozel_kombinasyon, ozel_sayilar, ozel_sonuc, ozel_kalan, ozel_isimler = ozel_sayi_kombinasyonu_bul(kalan_sayilar, kalan_isimler)
        
        if ozel_kombinasyon:
            # Kullanılan sayıları kalan sayılardan çıkar
            for sayi in ozel_sayilar:
                if sayi in kalan_sayilar:
                    kalan_sayilar.remove(sayi)
                if sayi in kalan_isimler:
                    del kalan_isimler[sayi]
            
            # Sonucu ekle
            add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(ozel_sonuc), ozel_isimler)
            
            # Kalan varsa ekle (19+11=22+8 gibi durumlar için)
            if ozel_kalan is not None:
                add_to_kalan_sayilar_and_isimler(kalan_sayilar, kalan_isimler, str(ozel_kalan), ozel_isimler)
            
            dongu_sayisi += 1
            continue
        
        # Eğer hiçbir toplama yapılamadıysa döngüden çık
        break
    
    # İsim sayıları özeti ekle
    sonuc += f"\n--- İSİM SAYILARI ---\n"
    for isim in isimler:
        isim_sayisi = isim_hesaplama(isim)
        sonuc += f"{isim} = {isim_sayisi}    "
    
    # Final sonuç
    sonuc += f"\n--- MERKEZ SAYI ---\n"
    sonuc += f"Kalan sayılar: {', '.join(kalan_sayilar)}"
    
    # Merkez sayıyı belirle ve sadeleştir
    if len(kalan_sayilar) == 1:
        # Eğer birden fazla isim varsa ve tek benzersiz sayı kaldıysa,
        # tüm isim sayılarını toplayıp ebced ile sadeleştir
        if len(isim_sayilari_str) > 1:
            final_sayi = sum(int(s) for s in isim_sayilari_str)
            merkez_sayi = ebced_toplama_merkez_sayi(final_sayi)
        else:
            final_sayi = int(kalan_sayilar[0])
            merkez_sayi = ebced_toplama_merkez_sayi(final_sayi)
    else:
        # Eğer 19 varsa ve başka sayılar varsa, 19 hariç diğer sayıları topla
        if "19" in kalan_sayilar:
            # 19 hariç diğer sayıları topla
            final_sayi = 0
            for sayi_str in kalan_sayilar:
                if sayi_str != "19":
                    final_sayi += int(sayi_str)
            merkez_sayi = ebced_toplama_merkez_sayi(final_sayi)
        else:
            # Kalan sayıları topla
            final_sayi = 0
            for sayi_str in kalan_sayilar:
                final_sayi += int(sayi_str)
            merkez_sayi = ebced_toplama_merkez_sayi(final_sayi)
    
    # Sonuç metni oluştur - önce merkez sayının metni, sonra özel sayıların metinleri
    sonuc_metni = ""
    
    # Önce merkez sayının metnini yaz
    if merkez_sayi in merkez_sayi_aciklamalari:
        metin = merkez_sayi_aciklamalari[merkez_sayi]
        
        # Orijinal isim listesini kullan (duplicate önlemek için)
        isim_listesi = " ".join(isimler)
        metin = metin.replace("******", isim_listesi)
        sonuc_metni += metin + "\n\n"
    else:
        print(f"UYARI: merkez_sayi {merkez_sayi} dictionary'de bulunamadı!")
    
    # Sonra özel sayıların metinlerini ekle (11, 19, 22, 33)
    # Ama merkez sayı olarak kullanılan özel sayıyı tekrar yazdırma
    ozel_sayilar = ["11", "19", "22", "33"]
    for ozel_sayi in ozel_sayilar:
        if ozel_sayi in kalan_sayilar and ozel_sayi != merkez_sayi:
            # Özel sayının metnini bul (merkez sayı değilse)
            if ozel_sayi in merkez_sayi_aciklamalari:
                metin = merkez_sayi_aciklamalari[ozel_sayi]
                
                # Bu özel sayıya ait isimleri bul
                ozel_isimler = kalan_isimler.get(ozel_sayi, [])
                if ozel_isimler:
                    isim_listesi = " ".join(ozel_isimler)
                    metin = metin.replace("******", isim_listesi)
                    sonuc_metni += metin + "\n\n"
                else:
                    # Eğer özel sayıya ait isim yoksa, tüm isimleri kullan
                    tum_isimler = []
                    for isim_listesi in kalan_isimler.values():
                        tum_isimler.extend(isim_listesi)
                    if tum_isimler:
                        isim_listesi = " ".join(tum_isimler)
                        metin = metin.replace("******", isim_listesi)
                        sonuc_metni += metin + "\n\n"
                    else:
                        sonuc_metni += metin + "\n\n"
    
    # 19 metni ekle (eğer başlangıçta 19 varsa ve henüz yazdırılmadıysa)
    if on_dokuz_var and "19" not in kalan_sayilar:
        on_dokuz_metni = merkez_sayi_aciklamalari["19"]
        on_dokuz_isim_listesi = " ".join(on_dokuz_isimleri)
        on_dokuz_metni = on_dokuz_metni.replace("******", on_dokuz_isim_listesi)
        sonuc_metni += on_dokuz_metni + "\n\n"
    
    # Detay analizi ve sonuç metnini birleştir
    final_sonuc = sonuc + "\n"  + "\n" + sonuc_metni
    
    return final_sonuc.strip(), merkez_sayi
# Harflerin çakra değerlerini belirten sözlük
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

pin_kodu_yorumu = [
    [  # 1. hane - DÜŞÜNCELER
        "Kendini beğenmeme.. Kendisi ile sorun yaşama.. Aşırı ego ya da özgüven eksikliği..Tartışmacı lider.",
        "Bağımlılıklarına bak. Duygusal bağımlılıklarını bağa çevir.",
        "Kendini doğru ifade etme/edememe.. Kendini tam anlatamıyor olabilir.. Kendisi hakkında iç alemini bir şekilde dile getirmeli. Gelişirse iyi bir hatip olabilir. Feminist",
        "İmtihan sabır sebat. Ağır bir imtihan olabilir. Kuralcı",
        "Korku, kendine güvensizlik..Eğlenceli, özgür",
        "Sezgiseldir. Aile odaklıdır",
        "Sürekli gezdirir hayat ve ilmin birinde arayışı durur. Hayat boyu kararsız olmakla uğraşabilir.. Tahkiki iman şart. Çok zeki.",
        "Bolluk bereket, Kendi işini kurma.. Otorite kurmaya, kendini ifade/ispat etmeye, asil olmaya ihtiyaç var. Zenginlik enerjisi.",
        "Saf temiz kalpli... Sınırlar koymalı.. Olayların arka planını araştırmalı.. Her koşula uyum sağlayan"
    ],
    [  # 2. hane - DUYGULAR
        "Önden gitmeyi arzu eder..neden öne çıkmayı istemiş? Duygu dünyası hakkında kökenine inip kendini değerli göremediği alanı bulması, kendiyle barışması gerekir.",
        "En zoru..Üreme organları sıkıntı..Duygusal terapiye muhtaç..Regresyon..Duygusal baskı hissediyor olabilir..",
        "Kendini ifade etme tanıma.. Tıkalıysa içe kapanış..",
        "Zorluk..Sabır. Üretim merkezi kalp.",
        "Cesaretli, Duygular kosunda pozitif. Üretim gücü kuvvetli.",
        "Sevgiyi babadan bekliyor",
        "Doyumsuzluktan dolayı değersizlik..anne babaya doymamış.arayış içinde.",
        "Aurayı korursa zengin olur..duygusal zaafiyete dikkat etmeli.. Edebiyat ve şiir, edebi yeteneklere meyilli olabilir.",
        "Ya duygularını çok frenliyor, ya da aşırı sınırları açık.. Anlaşılmayacak kadar saf ve iyi niyetli olabilir.."
    ],
    [  # 3. hane - HİTABET VE TİCARET
        "Kendi işinin patronu. Emir almayı sevmez",
        "Ortaklıkta iyidir.Hayata duygusal bakar",
        "Yaşadığı baskıları çözmek zorunda.. dil sivri ise düzeltmeli. Lider, konuşmacı.",
        "Erken yaşta kayıplar olabilir.. Dilinde sabrı ve olumlu konuşmayı sürdürmeli..Cümle kurarken de İşi hakkında karar verirken de sabırlı olmalı, acele etmemeli..",
        "Sevdiği işi yapmalı.Rutinler yorar.",
        "Öğretmenlik enerjisi. Disiplini öğrenmesi gerekir.",
        "Spiritüel alandan para kazanma. İş arayışları.",
        "Otorite para ticaret... Ticarette nasibi var..",
        "Şifacı..İletişimde had bilmek."
    ],
    [  # 4. hane - SEVGİ, OLGUNLUK
        "Bedensel hastalıklar olabilir.",
        "Duygusal zaafiyet",
        "Sıkıntıları konuşarak aşar",
        "Kalbî imtihanlar",
        "İmtihanlarını şükrederek aşacak. Polyannacılık oynayacak.",
        "İmtihan sebebi aile ve otoritedir",
        "Kalbini İnançla bütünleştirmeli.. Sevginin kaynağının Yaradan olduğunu bilmeli.. sevgi arayışları riskine girmemeli",
        "Güç ve otoriteyi kullanarak sorunları aşar",
        "Kalbine duygusal hatalara düşmemek için söz geçirmeli."
    ],
    [  # 5. hane - ŞÜKÜR VE DOYUM
        "Mütevazi olmayı öğrenmeli.",
        "Romantiklik",
        "İletişimden keyif alır",
        "Aşırı merhametli.",
        "Sevilmediğini düşünür",
        "Aileye karşı çok fedakar",
        "Sevgi arayışı.",
        "Mutluluğu maddiyatta arar.",
        "Sevgide sınırlara dikkat.. Ruhani rehberlerle vakit geçir"
    ],
    [  # 6. hane - AİLE, BABA
        "Babayla liderlik çatışması.",
        "Aileye bağımlı",
        "Aile ile bilhassa baba/eril yapı ile kendisini ifade ederek temas kurmalı. Aileden gelen müdahale/dedikodulara dikkat..",
        "Sevgide sabır öğrenmeli..Erken yaşta baba kaybı verebilir.",
        "Sorumluluk almakta zorlanmaz.",
        "Sorumluluk almakta zorlanır. Kontrolcü olur.",
        "Anne rolü üstlenen baba.",
        "Babayla/Aileyle parasal ilişki..babayla ilişkisini düzeltirse bolluk ve bereket olur..",
        "Ailede sınırlara dikkat edilmeli. Aile ilişkileri şifalanmalı."
    ],
    [  # 7. hane - ANNE, İMAN
        "Anneye benzer. Kişiye manevi aktarımlar vardır.",
        "Sevgi kaynağı anne. Dişil figürlere zaafiyet.",
        "Söz sihirbazı.",
        "Erken yaşta anne kaybı olabilir. Anne sabır meselesi.",
        "Boğaz hassasiyeti. İştahlı.",
        "Baba rolü üstlenmiş anne.",
        "Hakedişlerden maneviyatla arınması gerek.",
        "Maddiyatı maneviyattan üstün görme.",
        "Yaradanın sınırlarına dikkat et. Anne müdahalesine dikkat.."
    ],
    [  # 8. hane - KAZANÇ VE BEREKET
        "Kendi işini kur.",
        "Yıldız düşüklüğü. Çocukluk travmaları.",
        "Konuşarak bir yerlere gelecek..",
        "Parayı sabırla kazanır, acele etmeden yatırım yapmalı...",
        "Yurtdışı işlerde ve sanal alemde para kazanır.",
        "Babayla helalleşmesi gerek. Bereket kaynağı aile.",
        "Spiritüel alandan para kazanma.",
        "Nazara açık",
        "Aurayı koruması gerek."
    ],
    [  # 9. hane - HAYAT AMACI
        "Kök çakra şifalanması gerek. Liderlik isteği.",
        "Duygusal sınırlarını korumalı...",
        "İletişimde sınırlara dikkat etme. Meslekte prensiplere dikkat.",
        "Kalbin sınırlarını, olgun-esnek olmayı ve sabrı öğrenecek",
        "Özgürlüğün sınırlarını bilecek",
        "Kurban psikolojisi",
        "Halk içinde Hakk ile olmayı başarmalı.",
        "Dünyevi başarıları önceler.",
        "Alanını korumayı öğrenmeli."
    ]
]

unlemli_yorumlar = [
    "1'i 1 ile açıyorsa bir kişi: Kendine dönüp kendini sorgulayıcı bir tutum içerisinde olup kendisini çözmesi lazım. Kendisine her an ayna tutması gerekir. Kendi bedenini beğenmeme sebebiyle aşırı özgüven yahut çok içine kapanma problemi mümkündür.",
    "2'yi 2 ile açıyorsa bir kişi: Duygusal anlamda sorun yaşadığı yerlere bakmalı. Hormonlar ve cinsel sağlığa çok dikkat etmeli. Üreme organları sıkıntılı olabilir. Duygusal terapiye ve içini dökmeye ihtiyacı var. Duygusal baskı altında olması ve etrafına duygusal baskı kurmuş olma ihtimali yüksektir.",
    "3'ü 3 ile açıyorsa bir kişi: Ya sivri dillidir, incitici konuşmayı bırakması gerekir ya da konuşma problemleri yaşıyordur. Telaffuzu geliştirmesi gerekir. Ticari alanda da sıkıntı yaşaması muhtemeldir. Yaşadığı baskıları çözerse ve kendini geliştirirse iyi bir hatip olur.",
    "4'ü 4 ile açıyorsa bir kişi: Sabır gerektiren ağır imtihanlardan geçer. Bu imtihanlar onun olgun ve esnek olmasını sağlamalıdır. Yaşadığı imtihanları kalbinin kılavuzluğunda aşar. Kalp sağlığına da ziyadesiyle dikkat etmesi gerekir.",
    "5'i 5 ile açıyorsa bir kişi: Bu kişinin en büyük imtihanı şükürsüzlüktür. Bir şeyden memnun olmaz. Pozitif bakış tavsiye edilmeli. Buna rağmen bu çakrayı dengelerse dahice kararlar alır. Nimetler içinde yüzer.",
    "6'yı 6 ile açıyorsa bir kişi: Otorite ile çatışma verir. Kişiyi aşırı korumacı olmaya itebilir. Bu kişilerin öğretmen, asker gibi işlerde yani insan yetiştirmede görevlendirilmeleri isabetli olur. Allah'tan gelene rıza göstermeyi öğrenirse çok güzel bir aile kurar.",
    "7'yi 7 ile açıyorsa bir kişi: İnanç boyutunda sınanma yaşayabilir. Maneviyata önem vermeli, Yaradanın sınırlarına dikkat etmelidir. Kalbine akan ilhamları ve ruhunun sesini dinlemelidir.",
    "8'i 8 ile açıyorsa bir kişi: Helal haram noktasına (yeme, içme, ilişkiler yani bedeni ve ruhi helaller) çok dikkat etmeli. Arkadaşlıklarına ve ilişkilerine Rahmani sınırlar koymalı. Ruhunu bu şekilde korursa maddi, manevi zengin olur. Çokça Ayetel Kürsi ve koruma duaları okuması tavsiye edilmelidir.",
    "9'u 9 ile açıyorsa bir kişi: Önce kendisini iyileştirirse iyi bir şifacı olur. Aynı zamanda sınır çizme konusunu dengelemelidir. Yani aşırı sınır koymak da, hiç sınır çizmemek de aynı kapıya çıkacağı için önemli olan nerede ne kadar sınır koyma gerekliliğinin tam olarak farkına varması olduğu kişiye anlatılmalıdır."
]

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

def ebced_toplama_asamali(*args):
    """
    Bu fonksiyon, verilen sayının rakamlarını toplar.
    Bu işlemi, sayı tek haneli olana kadar tekrarlar.
    Her aşamayı '/' işaretiyle ayırır.
    """
    total_sum = 0
    for arg in args:
        if isinstance(arg, str):
            # Stringdeki sayı olan kısmı al ve tam sayıya çevir
            number_str = ''.join(filter(str.isdigit, arg))
            if number_str:
                total_sum += int(number_str)
        elif isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, float):
            total_sum += int(arg)
            
    steps = []  # Her aşamayı kaydetmek için liste
    number = total_sum

    while number >= 10:
        steps.append(str(number))
        if number == 11:
            steps.append(str("2*"))
            return "/ ".join(steps)
        number = sum(int(digit) for digit in str(number))
    
    steps.append(str(number))
    return "/ ".join(steps)

#ayrı yaptım fonksiyonları ayrı ayrı göstermem gerekebilir.
def chakra_hesapla(k_values, text):
    chakra_houses = [""] * 9
    chakra_houses = chakra_add_pin_kodu(chakra_houses, k_values)
    chakra_houses = chakra_add_numbers(chakra_houses)
    chakra_houses = chakra_add_name(chakra_houses, text)

    result = ""
    for i in range(9, 0, -1):
        result += f"{chakra_houses[i - 1]}\n"

    return result

def chakra_add_pin_kodu(chakra_houses, k):
    # Rakam sayacı oluştur
    sayac = [0] * 9

    # Her elemanın ilk harfine göre sayacı güncelle
    for eleman in k:
        sayac[int(eleman[0])-1] += 1

    # Chakra_houses dizisini güncelle
    for i in range(len(chakra_houses)):
        chakra_houses[i] += '  ' * (5 - sayac[i])
        chakra_houses[i] += '+ ' * sayac[i]

    return chakra_houses


def chakra_add_numbers(chakra_houses):
    for i in range(1,10):
        chakra_houses[i-1] += " " + str(i) + "  "

    return chakra_houses

def chakra_add_name(chakra_houses, text):
    # Metindeki her harfin sayısal karşılığını bul ve uygun haneye + ekle
    for letter in text.upper():
        if letter in chakra_values:
            index = chakra_values[letter] - 1
            chakra_houses[index] += "+ "
    
    return chakra_houses

def normalize_date(date_str):
    """
    Farklı formatlardaki tarih girişlerini standart formata çevirir.
    Kabul edilen formatlar:
    - DD.MM.YYYY
    - DD/MM/YYYY
    - DD MM YYYY
    - DD-MM-YYYY
    """
    # Boşlukları temizle
    date_str = ' '.join(date_str.split())
    
    # Nokta, slash veya tire ile ayrılmış tarihleri boşluğa çevir
    date_str = date_str.replace('.', ' ').replace('/', ' ').replace('-', ' ')
    
    # Birden fazla boşluğu tek boşluğa çevir
    date_str = ' '.join(date_str.split())
    
    # Tarihi parçalara ayır
    parts = date_str.split(' ')
    
    if len(parts) != 3:
        raise ValueError("Tarih formatı hatalı. Lütfen GG.AA.YYYY, GG/AA/YYYY veya GG AA YYYY formatında giriniz.")
    
    # Her bir parçanın sayı olduğunu kontrol et
    try:
        gun = int(parts[0])
        ay = int(parts[1])
        yil = int(parts[2])
    except ValueError:
        raise ValueError("Tarih değerleri sayı olmalıdır.")
    
    # Değerlerin geçerli aralıkta olduğunu kontrol et
    if not (1 <= gun <= 31 and 1 <= ay <= 12 and 1000 <= yil <= 9999):
        raise ValueError("Geçersiz tarih değerleri.")
    
    # Tek haneli gün ve ayları iki haneye tamamla
    gun_str = str(gun).zfill(2)
    ay_str = str(ay).zfill(2)
    
    return f"{gun_str} {ay_str} {yil}"

def pin_kodu_hesaplama(dogum_tarihi):
    # Tarihi normalize et
    try:
        dogum_tarihi = normalize_date(dogum_tarihi)
    except ValueError as e:
        return str(e), None
    
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    # Doğum tarihini gün, ay ve yıl olarak ayır
    gun, ay, yil = dogum_tarihi.split(' ')
    
    # Ebced toplam fonksiyonunu kullanarak k değerlerini hesapla
    k = [""] * 9
    k[0] = ebced_toplama(gun)
    k[1] = ebced_toplama(ay)
    k[2] = ebced_toplama(yil)
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

    # Değerleri ekrana yazdır
    result = ""
    result += f"{k[0]}       {k[1]}       {k[2]}      {k[3]}      {k[4]}\n"
    result += f"     {k[5]}       {k[6]}\n"
    result += f"         {k[7]}\n"
    result += f"         {k[8]}\n\n"
    
    # Pin kodu yorumlarını ekle
    result += "Pin Kodu Yorumları:\n"
    result += "-------------------\n"
    for i in range(9):
        # k[i] değerinin ilk karakterini al ve int'e çevir (örn: "4!" -> 4)
        index = int(k[i][0]) - 1  # 0-based index için -1
        result += f"{i+1}. Hane: {pin_kodu_yorumu[i][index]}\n"
        
        # Eğer k[i] değerinde ünlem işareti varsa, özel yorumu ekle
        if k[i].endswith('!'):
            sayi = int(k[i][0]) - 1  # 0-based index için -1
            result += f"\nDikkat etmesi lazım: {unlemli_yorumlar[sayi]}\n\n"
    
    return result, k




def ana_kulvar_bulma(isim_soyisim):
    #Bu fonksiyon, verilen isim soyisimin bütün harflerinin rakamsal karşılığını bulup toplar.
    total_sum = 0
    for char in isim_soyisim.upper():
        if char in chakra_values:
            total_sum += chakra_values[char]
    
    return ebced_toplama_asamali(total_sum)

def yan_kulvar_bulma(isim_soyisim):
    #Bu fonksiyon, verilen isim soyisimin bütün sesli harflerinin rakamsal karşılığını bulup toplar.
    total_sum = 0
    for char in isim_soyisim.upper():
        if char in sesli_harfler and char in chakra_values:
            total_sum += chakra_values[char]
    
    return ebced_toplama_asamali(total_sum)




def yasam_yolu_hesapla(birthdate):
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    total_sum = 0
    for char in birthdate:
        if char.isdigit():
            total_sum += int(char)
    
    return ebced_toplama_asamali(total_sum)

def bereket_rakami_bulma(birthdate):
 # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    gun, ay, _ = birthdate.split(' ')

    toplam = int(gun) + int(ay)
    return ebced_toplama_asamali(toplam)


def donusum_yillari_bulma(dogum_tarihi):
    gun, ay, yil = dogum_tarihi.split(' ')

    dogum_yili = int(yil)
    yil = dogum_yili
    yas = 0

    result = ""
    while yas <= 70:
        yil_rakam_toplami = sum(map(int, str(yil)))
        yeni_yil = yil + yil_rakam_toplami
        yas = yeni_yil - dogum_yili

        donusum_rakami = ebced_toplama_asamali(ebced_toplama(yeni_yil), ebced_toplama(gun), ebced_toplama(ay))
        result += f"{yeni_yil} / {yas} yaş / dönüşüm rakamı: {yeni_yil} + {gun} + {ay} = {donusum_rakami} \n"

        yil = yeni_yil

    return result



def ozellik_hesaplama(k):
    # Özellik sözlükleri
    ozellikler = {
        'esnek': [1, 2, 3, 4],
        'katı': [5, 6, 7, 8],
        'Etken/Baskın': [1, 3, 6, 8],
        'edilgen': [2, 4, 5, 7],
        'hava': [1, 5],
        'su': [2, 7],
        'toprak': [4, 8],
        'ateş': [3, 6]
    }
    
    # Özellik sayacı
    sayac = {key: 0 for key in ozellikler.keys()}
    rakam_dizisi = [0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        rakam_dizisi[i] = int(k[i][0])

    # Her rakamı kontrol ederek ilgili özellik sayısını artır
    for rakam in rakam_dizisi:
        for ozellik, degerler in ozellikler.items():
            if rakam in degerler:
                sayac[ozellik] += 1

    result = ""
    for ozellik, deger in sayac.items():
        result += f"{ozellik}: {deger}    "

    return result


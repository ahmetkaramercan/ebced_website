import sqlite3
import arabic_reshaper
from bidi.algorithm import get_display


sureler = {
    11: "HACC",
    14: "TAHA",
    15: "HUD",
    26: "HADID",
    36: "BELED",
    51: "MAIDE",
    54: "NEBE",
    57: "HUMEZE",
    63: "SEBE",
    64: "NUH",
    65: "ENBIYA",
    70: "YASIN, LEYL",
    72: "SECDE",
    75: "ZILZAL",
    77: "BEYYINE",
    83: "MUCADDELE",
    88: "NAHL",
    90: "MULK, SAD",
    93: "NECM",
    100: "KAF",
    103: "CIN",
    105: "KEHF",
    111: "ALA, NAS",
    112: "NISA",
    118: "CUMA",
    120: "NEML, FIL",
    124: "MUZZEMMIL",
    126: "YUNUS",
    132: "MUHAMMED, ABESE",
    137: "MU-MIN",
    140: "TALAK",
    155: "KIYAMET",
    156: "YUSUF",
    162: "ENFAL, INSAN, ENAM",
    167: "MAUN",
    170: "KALEM",
    182: "VAKIA",
    190: "AHKAF",
    193: "MUMINUN",
    200: "ALAK",
    210: "FELAK",
    211: "HICR, BURUC",
    214: "HAKKA",
    215: "TUR",
    221: "LOKMAN",
    246: "RUM",
    247: "ZUMER",
    250: "SAFF",
    256: "NUR",
    258: "IBRAHIM",
    263: "ISRA",
    274: "RAD",
    280: "KASAS",
    283: "FECR",
    290: "MERYEM, FATIR",
    298: "RAHMAN",
    304: "KADIR",
    307: "BAKARA",
    310: "TARIK",
    314: "MEARIC",
    327: "MUNAFIKUN",
    340: "KAMER, NASR",
    341: "INFITAR",
    349: "MUTAFFIFIN",
    352: "A RAF",
    357: "KAFIRUN",
    360: "ASR",
    376: "KARIA",
    391: "ALI IMRAN",
    400: "ŞEMS",
    413: "TEVBE",
    431: "FURKAN",
    460: "TIN",
    486: "ADIYAT",
    488: "FETIH",
    494: "FATIHA",
    508: "HAŞR",
    516: "ŞURA",
    519: "CASIYE",
    529: "NAZIAT",
    543: "MUMTEHINE",
    548: "ANKEBUT",
    552: "INŞIKAK",
    559: "INŞIRAH",
    572: "ŞUARA",
    610: "KUREYŞ",
    612: "HUCURAT",
    636: "TEKVIR",
    652: "SAFFAT",
    655: "DUHAN",
    658: "TAHRIM",
    690: "FUSSILET",
    712: "AHZAB",
    722: "IHLAS",
    726: "KEVSER",
    731: "MURSELAT",
    804: "TEBBET",
    818: "DUHA",
    893: "ZUHRUF",
    1121: "TEKASUR",
    1248: "MUDDESSIR",
    1312: "ZARIYAT",
    1316: "GAŞIYE",
    1453: "TEGABUN"
}

esmalar = {
    13: {
        "esma": "Ya Ehad",
        "anlam": "Hibe eden demektir. Allah'ın güzel isimlerini zikretmeye başlayınca sizde güzellikler açığa çıkıyorsa, doğru yoldasınız demektir. Tek olandır. İlk demektir. Herhangi bir durumda en iyisini yapmaya çalışan insanların bu ismi zikretmeye ihtiyacı vardır. Özellikle lider ruha ihtiyacı olan kişilere çıkması muhtemeldir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Tam cuma namazı saati. Gece okumalarında yatsıdan sonra ve sabah namazının girmesiyle başlayan ve güneş doğana kadar."
    },
    14: {
        "esma": "Ya Vehhab",
        "anlam": "Hibe eden demektir. İnsanların isteğini bedel istemeksizin verendir. Bu zikir insanda Allah'ın karşılıksız verdiği nimetlerin farkında olmayı sağlar. Böylelikle nimetlere şükrü ve o nimetlerin artmasını da beraberinde getirir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah güneş doğumu vaktinde. İkindinin son vaktinde. Akşam namazından bir saat sonraki vaktinde. Gece yarısından sonraki ilk vakitlerde."
    },
    14.1: {
        "esma": "Ya Vacid",
        "anlam": "İstediğini istediği an bulup huzuruna getiren demektir. Emek verdiğimizde, istediğimiz şeylere ulaşmamızın anahtarlarından biridir. Aynı zamanda kulun kendini ve Rabb'ini bulmasını sağlar. Allah beni görmüyor mu, duymuyor mu diye neredeyse isyana gitmeye meyleden insanlara çokça çıktığı görülür. Bu isim kulda tecelli etmezse, yalnız, görülmeyen, duyulmayan ve istediklerine ulaşamayan biri olduğunu düşünür. Bu ismin idrak edilmesi kulun her an Allah'la olduğunun farkındalığını kazandırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah erken gün doğarken ve ikindi sonrası. Gece okumalarında akşamdan sonraki ikinci saat ile gece yarısı."
    },
    18: {
        "esma": "Ya Hayy",
        "anlam": "Ezeli ve ebedi diri olan demektir. Kul olarak biz sürekli ölür, diriliriz. Allah için ölüm yoktur, her an diridir. İnsanda açığa çıkarsa her an her şeyin kontrol altında olduğunu ve her şeyin yeniden dirileceğini idrak eder. Çokça zikreden ölü hücrelerden kurtulur, canlanır ve enerji ile dolar.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi namazı sonrası."
    },
    19: {
        "esma": "Ya Vahid",
        "anlam": "Birinci demektir. Kul bu zikrin idrakine ulaştığında her şeyin ilk kaynağının Allah olduğunun farkına varır ve adım attığı hemen her işten başarıyla çıkar. Çünkü o başarının asıl kaynağının Allah olduğunu bilir ve şükür içindedir. Kul olduğunun ve acziyetinin farkındadır.",
        "zikir_gunu": "",
        "zikir_saati": ""
    },
    20: {
        "esma": "Ya Vedud",
        "anlam": "Seven, sevilen demektir. Kainat sevgi üzerine yaratılmıştır. Bu isim bir insanda tecelli ederse kainatta bir kuşun kanat çırpışında bile sevgiyi derinden hisseder. Allah'ın kendisini sevdiğine olan inanç diğer insanlardan beklediği sevgi sebebiyle yaptığı yanlışların da önüne geçer. Ya Vedud esması aşkın ilmine talip olmaktır.",
        "zikir_gunu": "Pazartesi",
        "zikir_saati": "Öğlen ezanına iki saat kala, ikindinin son vaktinde, gece teheccüd vaktinde."
    },
    20.1: {
        "esma": "Ya Hadi",
        "anlam": "Hidayet veren demektir. Bir şeyi yaparken dosdoğru yapabilecek güce ve ilme sahip olmak bu ismin tecellisidir. Bütün uzuvların bir çalışma prensibi var. Bunları anlayabilmek hep bu ismin tecellisi ile olur. Allah hidayet vermezse uzuvlarımız görevlerini yerine getiremez. Akıl ettiğiniz bir şeyi kalbinize sindirerek şuurla hareket etmek bu ismin tecellisinin en güzel göstergesidir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi namazı sonrası"
    },
    37: {
        "esma": "Ya Evvel",
        "anlam": "Tek önceliğin Allah olduğunu hatırlatan isimdir. Kendinizde önceliklerinizi fark etmenize vesile olur. Her şeyden önce Allah'a ihtiyacımız olduğunun bilincini verir. Boğulma noktasına gelen insanların en büyük ilaçlarındandır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi namazı sonrası"
    },
    46: {
        "esma": "Ya Veliyy",
        "anlam": "İnanan insanın dostu ve sahibi demektir. Yalnızlık dehlizine düşen insanın kurtuluş reçetesidir. Evhamları ve vesveseleri bitirme vesilesidir. Bu ismi çokça zikretmek Allah'ın dostluğunu kazanmaya vesile olur.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası. Gece okumalarında tam gece yarısı."
    },
    47: {
        "esma": "Ya Vali",
        "anlam": "Her şeyin yöneticisi demektir. Bu ismi zikretmek yöneticilik yeteneği kazandırır. Kendi nefsini yönetebilme gücü için bu isme çokça emek vermek gerekir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası. Gece okumalarında tam gece yarısı."
    },
    48: {
        "esma": "Ya Macid",
        "anlam": "Allah'ın en zirvede olması demektir. Kulda bu isim tecelli ederse zirvede olanın Allah olduğunu anlar. Kibirlenmekten muhafaza eder.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah erken güneş doğarken ve ikindi namazı sonrası. Gece okumalarında akşamdan sonraki ikinci saat ve gece yarısı."
    },
    55: {
        "esma": "Ya Mucib",
        "anlam": "Dualara karşılık veren demektir. Allah'la sohbet edebileceğinin farkına varmayı sağlar. Dile dökebilmeyi ve fiiliyata dökmeyi kolaylaştırır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah gün doğduğu vakitte, ikindi namazı sonrasında"
    },
    56: {
        "esma": "Ya Mubdi",
        "anlam": "İlk olarak yapan demektir. Allah'ın yarattığı şeyi ilk ve benzersiz olarak yaratmasını anlatır. İcat yeteneği verir. Özellikle mühendisler için idealdir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah gün doğarken, ikindi namazı sonrası, gece yarısı"
    },
    57: {
        "esma": "Ya Mecid",
        "anlam": "Kulunu zirvede yaratması demektir. Kendisindeki yüceliği fark ettirir. Ön yargılardan kurtulmaya vesile olur. Güven duygusu ve teslimiyet verir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Güneş doğarken ve ikindi namazı sonrası. Gece okumalarında yatsıya doğru ve tam gece yarısı."
    },
    62: {
        "esma": "Ya Bâtın",
        "anlam": "Yüceliği her yaratılan şeyde gizli olan demektir. Olayların arka planındaki güzellikleri anlamaya vesile olur. Bu esma ile kişideki içsel güzellikler açığa çıkar.",
        "zikir_gunu": "Pazartesi",
        "zikir_saati": "Gün doğduğu ilk saatlerde, ikindi sonrası, yatsı namazına yakın, gece yarısı."
    },
    62.1: {
        "esma": "Ya Hamid",
        "anlam": "Övülmeye layık olan demektir. Teşekkür edilecek işler yapmaya muvaffak eder. Şükür bilincini artırır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah erken gün doğarken ve ikindi sonrası. Gece okumalarında tam gece yarısı."
    },
    66: {
        "esma": "Ya Vekil",
        "anlam": "Tevekkül edenlerin işlerini en güzel şekilde sonuçlandıran demektir. Bu isme emek verenler Allah'ı vekil tayin etmenin tadını çıkarır. Sabır ve teslimiyet kazandırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gün doğduğu vakitte, ikindi sonrası, akşam namazından sonra, gece teheccüd vaktinde."
    },
    66.1: {
        "esma": "Ya Allah",
        "anlam": "Lafza-i Celal'dir. Celalinden cemaline sığınılarak zikredilir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi namazı sonrası."
    },
    68: {
        "esma": "Ya Muhyi",
        "anlam": "İhya eden demektir. Zorluklardan sonra gelen kolaylığı idrak ettirir. Hamd ve şükür bilincine erdirir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah erken gün doğarken ve ikindi sonrası. Gece okumalarında tam gece yarısı."
    },
    68.1: {
        "esma": "Ya Hakem",
        "anlam": "Her şeyi en doğru şekilde takdir eden demektir. Allah'ın kararına teslimiyet kazandırır. Teslimiyeti ve kabulü kolaylaştırır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gün doğduğu vakitte."
    },
    72: {
        "esma": "Ya Basıt",
        "anlam": "Genişleten, lütfuyla acizliği gideren Rabbimizdir. Borçları kolay ödemeye, bolluğa erişmeye, ataletten kurtulmaya vesile olur.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası. Akşamdan sonra yatsıya doğru ve gece yarısı."
    },
    73: {
        "esma": "Ya Celil",
        "anlam": "Allah'ın büyüklüğünü mekandan ve zamandan münezzeh olarak gösterir. Korkulardan emin olmaya ve boyun eğmenin anlamını kavramaya vesile olur.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gün doğarken, ikindi sonrası."
    },
    78: {
        "esma": "Ya Hakim",
        "anlam": "Hikmet sahibi demektir. Kalbe ferahlık, göğse genişlik, teslimiyet ve sükunet verir. Kurban bilinci, sabır ve huzur etkisini artırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gün doğarken, ikindi sonrası, akşamdan sonra, gece yarısı."
    },
    80: {
        "esma": "Ya Hasib",
        "anlam": "Her şeyin hesabını gören demektir. Doğruyu ve yanlışı ayırt etmeyi öğretir. Sorumluluk bilinci kazandırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gün doğarken, ikindi sonrası, akşam sonrası, gece yarısı."
    },
    86: {
        "esma": "Ya Bedi'",
        "anlam": "Yoktan var eden, tefekküre yönlendiren, eksiksiz yaratandır. Kaybolduğumuzda yolumuzu bulmaya ve işleri en güzel şekilde yapmaya yardım eder.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah gün doğarken, ikindi sonrası, gece yarısı."
    },
    88: {
        "esma": "Ya Halim",
        "anlam": "Allah'ın kudretli olduğu halde zaman tanımasıdır. Bu esma hoşgörü ve tevazu sahibi olmayı, anlayışlı olmayı kolaylaştırır.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah güneş doğarken ve yaklaşık ikindi namazı sonrasıdır. Gece okumalarında tam gece yarısı."
    },
    90: {
        "esma": "Ya Melik",
        "anlam": "Mülkün sahibi, canlı ve cansız her şeye hükmedici olan Allahtır. Şükür lezzetini tattırır, detaylara dikkat kazandırır.",
        "zikir_gunu": "Çarşamba",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası ve gece yarısı."
    },
    94: {
        "esma": "Ya Aziz",
        "anlam": "Büyüklük sadece ona aittir. Dünyanın bize hizmet etmesine vesile olur. Kibrin yok edilmesini sağlar.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Öğleden 2 saat ve akşamdan 1 saat önce. Gece okumalarında tam gece yarısı."
    },
    104: {
        "esma": "Ya Adl",
        "anlam": "Adaletli olan demektir. Tecellisiyle dünyada adaletle hükmetmeyi öğretir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gün doğunca"
    },
    108: {
        "esma": "Ya Hakk",
        "anlam": "Varlığı sabittir. Kainatın hakikatlerini ve kendi gerçeğimizi anlamaya yardımcı olur.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, akşam sonrası, gece yarısı."
    },
    110: {
        "esma": "Ya Aliyy",
        "anlam": "En üstün, en yüce demektir. İnsanları kibirden korur.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğduğu vakit, ikindi vakti"
    },
    113: {
        "esma": "Ya Baki",
        "anlam": "Ebedi olan demektir. Hayattaki önemsiz şeyleri ilahlaştırmaktan uzaklaştırır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, gece yarısı."
    },
    114: {
        "esma": "Ya Cami'",
        "anlam": "Her şeyi bir araya toplayan demektir. Büyük nimetleri fark ettirir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası. Gece tam gece yarısı."
    },
    116: {
        "esma": "Ya Kaviyy",
        "anlam": "Güç kaynağıdır. Hoşgörü ve tevazu kazandırır. Güçlüklerle baş etmeyi kolaylaştırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası. Akşam sonrası ve gece yarısı."
    },
    117: {
        "esma": "Ya Muizz",
        "anlam": "İzzetimizi artırır. Kibri azaltır. Yaptıklarımızın Rabbimiz sayesinde olduğunu fark ettirir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğarken ve tam gece yarısı."
    },
    124: {
        "esma": "Ya Muid",
        "anlam": "Öldükten sonra dirilten demektir. Sorumluluk alıp emeğimizi verince kaybettiklerimiz geri döner.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah gündoğarken, ikindinin son vaktinde, gece yarısı."
    },
    129: {
        "esma": "Ya Latif",
        "anlam": "Lütuf ve ihsan sahibi olandır. Her şeyin içinde bir lütuf olduğunu idrak ettirir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gündoğarken, ikindi sonu, akşamdan sonra, gece teheccüd vaktinde."
    },
    131: {
        "esma": "Ya Selam",
        "anlam": "Selametle koruyandır. Akıl ve selim düşünceyle işleri çözmeyi sağlar.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası"
    },
    134: {
        "esma": "Ya Samed",
        "anlam": "Hiçbir şeye muhtaç olmayandır. Kendi iç gücünü anlamaya ve haddimizi bilmeyi sağlar.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, gece yarısı."
    },
    136: {
        "esma": "Ya Mü'min",
        "anlam": "Koruyandır. Huzur verir. Korkulardan emin olmamıza ve Allah'a sığınmayı öğretir.",
        "zikir_gunu": "Pazartesi",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, gece yarısı"
    },
    137: {
        "esma": "Ya Vasi'",
        "anlam": "İlmiyle her şeyi kuşatandır. Teslimiyetle yeniden düzlüğe çıkmaya vesile olur.",
        "zikir_gunu": "Pazartesi",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, gece yarısından sonraki bir vakit"
    },
    145: {
        "esma": "Ya Müheymin",
        "anlam": "Koruyan, kollayan ve her şeyden haberdar olandır. Kabullenmeyi ve olayların hayra olduğunu idrak ettirir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası, gece yarısı."
    },
    148: {
        "esma": "Ya Muhsi",
        "anlam": "Her şeyin sayısını ve miktarını bilen demektir. Bilinçli ve farkında yaşamayı öğretir.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah erken gün doğarken, ikindi sonrası, gece yarısı."
    },
    150: {
        "esma": "Ya Alim",
        "anlam": "Her şeyi bilen olandır. Öğrendiklerimizle içsel sırlarımızı fark ettirir. Edeple davranmayı öğretir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Güneş doğarken, ikindi sonrası, gece yarısı."
    },
    156: {
        "esma": "Ya Kayyum",
        "anlam": "Her zaman diri olan ve her şeyi diri tutandır. Allah'ın bizimle olduğunu idrak ettirir, dirilik kazandırır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah"
    },
    156.1: {
        "esma": "Ya Afuvv",
        "anlam": "Affı çok olan, affederken unutturandır. Günah işlememeye çalışmayı öğretir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Güneş"
    },
    161: {
        "esma": "Ya Mani'",
        "anlam": "Engelleyen, mümin kullarını koruyandır. Her şeyin kontrol altında olduğunu fark ettirir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası"
    },
    170: {
        "esma": "Ya Kuddüs",
        "anlam": "Pak ve arı olan demektir. Arınma sürecini başlatır, merhametle temizler.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası, tam gece yarısı"
    },
    180: {
        "esma": "Ya Semi'",
        "anlam": "Her şeyi işiten, duaları kabul edendir. Korkulardan emin eder, güven kazandırır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah erken, ikindi sonrası, gece yarısı"
    },
    184: {
        "esma": "Ya Mukaddim",
        "anlam": "Dilediğini öne geçirendir. İhtiyaçlara uygun şekilde hayatı düzenler.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası, gece yarısı"
    },
    201: {
        "esma": "Ya Nafi'",
        "anlam": "Fayda veren şeyleri yaratandır. Ümit ve faydalı amellere yönlendirir.",
        "zikir_gunu": "Cuma veya Cumartesi",
        "zikir_saati": "Sabah"
    },
    202: {
        "esma": "Ya Berr",
        "anlam": "Fıtrata uygunlukla iyilik eden demektir. Hak edişe göre davranmayı sağlar.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah"
    },
    206: {
        "esma": "Ya Cebbar",
        "anlam": "Dilediğini yaptıran demektir. Yanlışları yoldan kaldırır, engelleri temizler.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası, gece yarısı"
    },
    209: {
        "esma": "Ya Muksit",
        "anlam": "Her işi denk yapan, ölçüyle hükmedendir. Uyumlu yaşamayı sağlar.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah"
    },
    212: {
        "esma": "Ya Malikul Mülk",
        "anlam": "Bütün mülkün sahibi demektir. Şükür ve sahiplik bilinci kazandırır.",
        "zikir_gunu": "Çarşamba",
        "zikir_saati": "Sabah"
    },
    214: {
        "esma": "Ya Bari'",
        "anlam": "Benzersiz yaratan demektir. Özgün üretim ve fayda bilinci verir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası"
    },
    232: {
        "esma": "Ya Kebir",
        "anlam": "En büyük olandır. Büyüklük duygusunu yüce anlamda yaşatır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    256: {
        "esma": "Ya Nur",
        "anlam": "Işığın ruhudur. Güzellikleri kalple görmeyi sağlar.",
        "zikir_gunu": "Perşembe veya Cuma",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    258: {
        "esma": "Ya Rahim",
        "anlam": "Merhamet ve rahmet demektir. Öfke ve hırsın merhamete dönüşmesini sağlar.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası"
    },
    270: {
        "esma": "Ya Kerim",
        "anlam": "Sebepsizce veren demektir. Yardım etmeyi, değeri fark etmeyi sağlar.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah, ikindi, akşamdan sonra, gece yarısı"
    },
    287: {
        "esma": "Ya Rauf",
        "anlam": "Çok merhametli. Her canlıya sevgiyle bakmayı sağlar.",
        "zikir_gunu": "Çarşamba veya Cumartesi",
        "zikir_saati": "Sabah"
    },
    298: {
        "esma": "Ya Rahman",
        "anlam": "Merhamet ve şefkat sahibidir. Olayları hikmetle görmeyi sağlar.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası"
    },
    298.1: {
        "esma": "Ya Sabur",
        "anlam": "Sabır tohumu eken, istikrar ve düzenle işlerin olgunlaşmasını sağlayandır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    302: {
        "esma": "Ya Basir",
        "anlam": "Her şeyi gören, kontrol eden demektir. Helal dairede yaşamayı öğretir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah erken, ikindi sonrası"
    },
    305: {
        "esma": "Ya Kadir",
        "anlam": "Her an sınırsız ilimle yaratan ve hükmeden demektir. Bir şey istediğinizde bu isimle kolaylıkla vesile olur.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası"
    },
    306: {
        "esma": "Ya Kahhar",
        "anlam": "Zorlukları kolaylaştıran, çaresizliğe çözüm getiren. Kudretiyle her şeyi bastırandır.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Sabah gün doğumu, ikindinin son vakti, gece yarısından sonraki vakit"
    },
    308: {
        "esma": "Ya Rezzak",
        "anlam": "Maddi ve manevi rızkı veren odur. Bereket ve şükrün kaynağıdır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah güneş doğumu, ikindi tepe vakti, akşam sonrası, teheccüd vakti"
    },
    312: {
        "esma": "Ya Rakib",
        "anlam": "Koruyan, kollayan. Nazar ve kötü niyetlerden muhafaza eder.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah gündoğarken, ikindi sonrası, akşam sonrası, gece yarısı"
    },
    319: {
        "esma": "Ya Şehîd",
        "anlam": "Her yerde hazır ve nazır olan. Olayların öncesini ve sonrasını bilip takdir edendir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah, ikindi sonrası, akşamdan sonra, gece yarısı"
    },
    336: {
        "esma": "Ya Musavvir",
        "anlam": "Benzersizce şekil verendir. Detaylardaki mükemmelliği fark ettirir.",
        "zikir_gunu": "Pazartesi",
        "zikir_saati": "Güneş doğarken, ikindi sonrası, tam gece yarısı"
    },
    351: {
        "esma": "Ya Rafi'",
        "anlam": "Şeref ve mevkileri yükselten. Hakkaniyetle saygı kazandırır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah erken, ikindi sonrası"
    },
    409: {
        "esma": "Ya Tevvab",
        "anlam": "Tevbeleri çokça kabul eden. Ruh ve bedenle yapılan hataların idrakini sağlar.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    489: {
        "esma": "Ya Fettah",
        "anlam": "Kapıları açan, işleri kolaylaştıran. Yolunda gitmeyen işleri düzene sokar.",
        "zikir_gunu": "Çarşamba",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    490: {
        "esma": "Ya Mümît",
        "anlam": "Öldüren, yok edendir. Nefsi kötü alışkanlıklardan arındırır.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Öğleden 2 saat önce, akşamdan 1 saat önce, gece yarısı"
    },
    500: {
        "esma": "Ya Metîn",
        "anlam": "Sarsılmaz kudret sahibidir. Ruhsal ve zihinsel dayanıklılığı artırır.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah, ikindi sonu, akşam-yatsı arası, gece yarısı"
    },
    514: {
        "esma": "Ya Reşîd",
        "anlam": "Doğruya ulaştıran, hidayeti kalbe yerleştirendir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    526: {
        "esma": "Ya Şekûr",
        "anlam": "Az ibadete çok mükafat verendir. İyiliklere bolca karşılık verir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası"
    },
    550: {
        "esma": "Ya Mukît",
        "anlam": "Her varlığa ihtiyacını veren. Rızık endişesini giderir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Gündoğarken, ikindi sonrası"
    },
    551: {
        "esma": "Ya Mütealî",
        "anlam": "En yüce olan. İlim ve idrak seviyesinin artmasına vesile olur.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah erken, ikindi sonrası, gece yarısı"
    },
    573: {
        "esma": "Ya Bais",
        "anlam": "Dirilten, canlandırandır. Farkındalık, iyileşme ve değişimi başlatır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken, ikindi sonrası"
    },
    630: {
        "esma": "Ya Muntakim",
        "anlam": "Zalimleri cezalandıran. Her şeyin hesabının görüleceği idrakini verir.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Öğleden 2 saat önce, akşamdan 1 saat önce, gece yarısı"
    },
    662: {
        "esma": "Ya Mütekebbir",
        "anlam": "Yüceliğin, büyüklüğün yalnızca Allah'a ait olduğunu öğretir. Mükemmeliyetçilikten kurtarır.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısından sonra"
    },
    707: {
        "esma": "Ya Varis",
        "anlam": "Mülkün gerçek sahibi olan. Teslimiyet ve tevekkül bilinci kazandırır.",
        "zikir_gunu": "Perşembe ve Cuma",
        "zikir_saati": "Sabah (Perşembe), Öğle (Cuma)"
    },
    731: {
        "esma": "Ya Hâlık",
        "anlam": "Yoktan var eden demektir. Başladığı işi bitirme azmini, ataletten çıkmayı sağlar.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ilk bir saat ve ikindi sonrası bir saat"
    },
    744: {
        "esma": "Ya Muktedir",
        "anlam": "Her şeye gücü yeten. Sonsuz kudreti anlamamıza ve kibirden uzaklaşmamıza vesile olur.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah güneş doğarken ve ikindi sonrası"
    },
    770: {
        "esma": "Ya Muzill",
        "anlam": "Alçaltan, rahmetinden uzaklaştırandır. Haddimizi bilmemizi sağlar.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    801: {
        "esma": "Ya Ahir",
        "anlam": "Her şeyin sonunda O vardır. Kalıcı gücün Allah'ta olduğunu idrak ettirir.",
        "zikir_gunu": "Salı veya Cuma",
        "zikir_saati": "Salı: Öğleden 2 saat önce ve akşamdan 1 saat önce, gece yarısı. Cuma: Güneş doğarken, ikindi sonrası, yatsıya doğru ve gece yarısı."
    },
    812: {
        "esma": "Ya Habir",
        "anlam": "Her şeyin iç yüzünü bilendir. İç huzur ve teslimiyet kazandırır.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi tepe vakti, gece teheccüd vakti"
    },
    847: {
        "esma": "Ya Muahhir",
        "anlam": "Dilediğini sona bırakandır. En güzel zamanı en güzel şekilde tayin eder.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    903: {
        "esma": "Ya Kabid",
        "anlam": "Sıkan ve daraltan. Mevcut nimetlerin kıymetini öğretir.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Sabah, ikindinin son vakti"
    },
    998: {
        "esma": "Ya Hâfız",
        "anlam": "Koruyan, kollayan ve muhafaza eden. Maddi-manevi korunmayı sağlar.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    1001: {
        "esma": "Ya Darr",
        "anlam": "Elem verenleri yaratandır. Yanlışlarımızı fark etmemizi ve dönüşü sağlar.",
        "zikir_gunu": "Salı",
        "zikir_saati": "Sabah"
    },
    1020: {
        "esma": "Ya Azîm",
        "anlam": "En yüce ve en büyük. Yüceliğini idrak ettirir, sınırlarımızı öğretir.",
        "zikir_gunu": "Çarşamba",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    1060: {
        "esma": "Ya Ğaniyy",
        "anlam": "Mutlak zenginlik sahibidir. Muhtaçlığımızı fark ettirir, istemeyi öğretir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah namazı sonrası, güneş vaktinde"
    },
    1100: {
        "esma": "Ya Zül-Celâli Vel-İkram",
        "anlam": "Celal ve ikram sahibi. Nimetlerin içindeki nimetleri görmemizi sağlar.",
        "zikir_gunu": "Perşembe",
        "zikir_saati": "Güneş doğarken, ikindi sonrası, gece yarısı"
    },
    1100.1: {
        "esma": "Ya Muğni",
        "anlam": "Dilediğini zengin eden. Maddi-manevi zenginliğin farkına varmayı sağlar.",
        "zikir_gunu": "Cuma",
        "zikir_saati": "Sabah"
    },
    1106: {
        "esma": "Ya Zahir",
        "anlam": "Varlığı açık olandır. Ahlakın güzelleşmesini, kibirden uzaklaşmayı sağlar.",
        "zikir_gunu": "Cumartesi",
        "zikir_saati": "Sabah, ikindi sonrası, gece yarısı"
    },
    1286: {
        "esma": "Ya Ğafûr",
        "anlam": "Çokça bağışlayandır. Günahları örter, affeder ve mahcubiyeti giderir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası"
    },
    1481: {
        "esma": "Ya Hâfid",
        "anlam": "Zalimleri, kibirlileri alçaltandır. Müminleri yükseltendir.",
        "zikir_gunu": "Pazar",
        "zikir_saati": "Sabah, ikindi sonrası"
    }
}


def get_ebced_and_arabic(isim):
    """Veritabanından ismin ebced değerini ve Arapça yazılışını çeker"""
    if not isim:
        print("İsim parametresi boş!")
        return None, None
        
    try:
        conn = sqlite3.connect('isimler.db')
        cursor = conn.cursor()
        
        # Debug için sorguyu yazdır
        query = 'SELECT ebced_degeri, arapca_yazilis FROM isimler WHERE isim = ? COLLATE NOCASE'
        print(f"Aranan isim: {isim}")
        
        cursor.execute(query, (isim,))
        result = cursor.fetchone()
        
        if result:
            print(f"Bulunan sonuç: {result}")
            ebced_value = str(result[0]) if result[0] is not None else None
            arabic_text = result[1]
            if arabic_text:
                try:
                    reshaped_text = arabic_reshaper.reshape(arabic_text)
                    arabic_text = get_display(reshaped_text)
                except Exception as e:
                    print(f"Arapça metin dönüştürme hatası: {e}")
            return ebced_value, arabic_text
        else:
            print(f"'{isim}' için sonuç bulunamadı!")
            return None, None
        
    except sqlite3.Error as e:
        print(f"SQLite hatası: {e}")
        return None, None
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return None, None
    finally:
        if conn:
            conn.close()


def dogumGunuToplama(birthdate):
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    total_sum = 0
    for char in birthdate:
        if char.isdigit():
            total_sum += int(char)
    
    return total_sum

def en_yakin_esma_bul(kisi_ebced, anne_ebced, dogum_gunu_toplam):
    # Gelen değerleri integer'a çeviriyoruz
    try:
        kisi_ebced = int(kisi_ebced)
        anne_ebced = int(anne_ebced)
        dogum_gunu_toplam = int(dogum_gunu_toplam)
    except (ValueError, TypeError):
        # Eğer çevrilemezse varsayılan değer olarak 0 kullanıyoruz
        kisi_ebced = 0
        anne_ebced = 0
        dogum_gunu_toplam = 0
    
    toplam = kisi_ebced + anne_ebced + dogum_gunu_toplam
    en_yakin = float('inf')
    en_yakin_esma = None
    en_yakin_deger = None
    
    for ebced_degeri, esma_detay in esmalar.items():
        fark = abs(float(ebced_degeri) - toplam)
        if fark < en_yakin:
            en_yakin = fark
            en_yakin_esma = esma_detay
            en_yakin_deger = ebced_degeri
    
    return {
        'esma': en_yakin_esma['esma'],
        'ebced_degeri': en_yakin_deger,
        'anlam': en_yakin_esma['anlam'],
        'zikir_gunu': en_yakin_esma['zikir_gunu'],
        'zikir_saati': en_yakin_esma['zikir_saati']
    }

def en_yakin_sure_bul(kisi_ebced, anne_ebced, dogum_gunu_toplam):
    try:
        kisi_ebced = int(kisi_ebced)
        anne_ebced = int(anne_ebced)
        dogum_gunu_toplam = int(dogum_gunu_toplam)
    except (ValueError, TypeError):
        kisi_ebced = 0
        anne_ebced = 0
        dogum_gunu_toplam = 0
    
    toplam = kisi_ebced + anne_ebced + dogum_gunu_toplam
    en_yakin = float('inf')
    en_yakin_sure = None
    en_yakin_deger = None
    
    for ebced_degeri, sure_ismi in sureler.items():
        fark = abs(float(ebced_degeri) - toplam)
        if fark < en_yakin:
            en_yakin = fark
            en_yakin_sure = sure_ismi
            en_yakin_deger = ebced_degeri
    
    return {
        'sure': en_yakin_sure,
        'ebced_degeri': en_yakin_deger
    }


def akil_fikir_sayisi_hesaplama(number1, number2):
    """
    İki sayının toplamının 9'a bölümünden kalanı hesaplar.
    Eğer kalan 0 ise 9 döner.
    """
    # None veya geçersiz değer kontrolü
    if number1 is None or number2 is None:
        return 0
        
    try:
        # Sayıya dönüştürülebilir string mi kontrol et
        if isinstance(number1, str):
            number1 = int(number1)
        if isinstance(number2, str):
            number2 = int(number2)
            
        # Sayı değilse veya dönüştürülemezse
        if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
            return 0
            
        toplam = number1 + number2
        kalan = toplam % 9
        if kalan == 0:
            kalan = 9
            
        return kalan
        
    except (ValueError, TypeError):
        return 0

def get_name_details_from_db(isim):
    """Veritabanından isim detaylarını çeker"""
    try:
        conn = sqlite3.connect('isimler.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT ebced_degeri, arapca_yazilis FROM isimler WHERE isim = ? COLLATE NOCASE', (isim,))
        result = cursor.fetchone()
        
        if result:
            return {
                'ebced_degeri': result[0],
                'arapca_yazilis': result[1]
            }
        return None
        
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
        return None
    finally:
        if conn:
            conn.close()

def calculate_arabic_ebced(name):
    """
    İsmin Arapça yazılışını ve ebced değerini veritabanından çeker
    """
    details = get_name_details_from_db(name)
    if details:
        return details['arapca_yazilis'], details['ebced_degeri']
    return None, None


def calculate_sure_esma(dogum_gunu, isim, anne_ismi, baba_ismi):
    """
    Tüm Sure ve Esma hesaplamalarını yapar
    """
    # İsmin Arapça yazılışı ve ebced değeri
    arabic_text, ebced_value = calculate_arabic_ebced(isim)
    
    results = {
        'isim': isim,
        'arabic_text': arabic_text,
        'ebced_value': ebced_value,
        'fikir_sayisi': akil_fikir_sayisi_hesaplama(dogum_gunu),
        'akil_zeka_sayisi': akil_fikir_sayisi_hesaplama(dogum_gunu),
        'esma': get_esma(dogum_gunu, isim),
        'sure': get_sure(dogum_gunu, isim)
    }
    
    return results

def test_db_connection():
    """Veritabanı bağlantısını ve tablo yapısını kontrol eder"""
    try:
        conn = sqlite3.connect('isimler.db')
        cursor = conn.cursor()
        
        # Tablo yapısını kontrol et
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='isimler'")
        if not cursor.fetchone():
            print("'isimler' tablosu bulunamadı!")
            return False
            
        # Tablo sütunlarını kontrol et
        cursor.execute("PRAGMA table_info(isimler)")
        columns = cursor.fetchall()
        print("Tablo sütunları:", columns)
        
        # Örnek bir kayıt sayısı al
        cursor.execute("SELECT COUNT(*) FROM isimler")
        count = cursor.fetchone()[0]
        print(f"Toplam kayıt sayısı: {count}")
        
        return True
        
    except sqlite3.Error as e:
        print(f"Veritabanı hatası: {e}")
        return False
    finally:
        if conn:
            conn.close()

# Test fonksiyonunu çağır
if __name__ == "__main__":
    print("Veritabanı bağlantısı test ediliyor...")
    test_db_connection()
    
    # Örnek bir isim ile test et
    print("\nÖrnek isim sorgusu test ediliyor...")
    ebced, arabic = get_ebced_and_arabic("Ahmet")
    print(f"Test sonucu - Ebced: {ebced}, Arapça: {arabic}")

import sqlite3
import arabic_reshaper
from bidi.algorithm import get_display

sureler = {
    11: {"isim": "HACC", "anlam": "Zalimin zulmünden emin olmak ve zalimden kurtulmak niyetiyle okunabilir. Okuyanın hac sevabı aldığı rivayet edilir."},
    14: {"isim": "TAHA", "anlam": "Kısmetin açılması, dildeki konuşma kusurlarının düzelmesi için okunur."},
    15: {"isim": "HUD", "anlam": "Sabırla ilerlemek, zalimden intikam almak için kuvvetli olmak, bir mücadelede başarılı olmak için okunur."},
    26: {"isim": "HADID", "anlam": "Bu sure bir kişide tecelli ederse,olmaz işlerini oldurmak hususunda Allahın yardımınıkendisine çeker. Sure içerisinde İsmi Azam esmasının bulunduğu da rivayet edilir."},
    36: {"isim": "BELED", "anlam": "Bu sure bir kişide tecelli ederse, gittiği her yerde izzet ve itibar görmesine aracılık eder. Göz ağrısının şifası niyetiyle, bağırsak rahatsızlıklarından arınmak niyetiyle, aynı zamanda ev sahibi olmak niyetiyle okunabileceği rivayet edilmiştir."},
    51: {"isim": "MAIDE", "anlam": "Rızık konusunda doğru ile yanlışı ayırt etmek, her türlü zarardan korunmak için okunur."},
    54: {"isim": "NEBE", "anlam": "Bu sure bir kişide tecelli ederse, kendisi için bilinmezliklerin ortadan kalkmasına, birçok işinin netleşmesine aracılık edeceği rivayet edilir. Aynı zamanda meşru olan her ne niyetle okunursa kabul edileceği rivayet edilir."},
    57: {"isim": "HUMEZE", "anlam": "Bu sure bir kişide tecelli ederse, dilini güzel kullanması öğütlenir. Gıybetçi ve kınayıcıların, laf taşıyanların, cimrilerin şerrinden korunmak niyetiyle de bu sure okunabilir."},
    63: {"isim": "SEBE", "anlam": "Okuyan kişi metafizik varlıkların şerrinden emin olur. Epilepsi hastalığının şifasıniyetiyle ve kötülük yapmayı planlayan kişilerin hilelerinin boşa çıkması niyetiyle okunur."},
    64: {"isim": "NUH", "anlam": "Bu sure bir kişide tecelli ederse, ailesine rağmen başarması gereken önemli görevleri başarıyla yürütebilmesi konusunda desteklenir. Ayrıca zulmedenlerin doğru yolu bulması niyetiyle de okunabilir."},
    65: {"isim": "ENBIYA", "anlam": "Yangından ve yanarak can vermekten korunmak için okunur. Tecelli eden kişiyi tembellikten korur. Ataletten ve evhamdan korunmak için de okunur."},
    70: {"isim": "YASIN", "anlam": "Yasin suresi ne niyetle okunursa karşılığı alınır. Bu sure bir kişide tecelli ederse o kişinin mükemmel donanımının farkına varmasının gerekliliğini anlatır." }, 
    70.1:{"isim": "LEYL", "anlam":"Bu sure bir kişide tecelli ederse, güzel işlerin kendisine kolaylaştırılması ile ödüllendirilir. Aynı zamanda bol rızık, bereket ve zenginlik niyetiyle de okunabilir."},
    
    72: {"isim": "SECDE", "anlam": "Okuyan kişi Allah'a kulluk yapmanın manevi huzurunu hisseder. Sebebi bilinmeyen hastalıklar ve baş ağrıları için okunur."},
    75: {"isim": "ZILZAL", "anlam": "Bu sure bir kişide tecelli ederse, tembellik ve erteleme hastalığından arındırır. Aynı zamanda bu sureyi okuyan kişi iyilik ve kötülüklerin eksiksiz karşılık bulacağı düşüncesiyle tevekkül etmeyi öğrenir."},
    77: {"isim": "BEYYINE", "anlam": "Bu sure bir kişide tecelli ederse, kamil insan makamına ereceği rivayet edilir. Ayrıca iyi ve kötüyü ayırt etmek için, dünya ve ahiretini muhafaza etmek için kişi bu sureyi okuyabilir. Sarılık hastalığının şifası için de okunur."},
    83: {"isim": "MÜCADELE", "anlam": "Bu sure bir kişide tecelli ederse, dünyada Allahın hükümlerinin yaygınlaşmasında görevli olur. Aynı zamanda sükunet bulup uyuyabilmek niyetiyle, düşmana galip olmak niyetiyle ve Allahın tarafında yer almak niyetiyle okunabilir."},
    88: {"isim": "NAHL", "anlam": "Fitne ve fesadın kaldırılması, ilham kapısının açılması ve şifacılık kazanmak niyetiyle okunur."},
    90: {"isim": "MULK", "anlam": "Bu sure bir kişide tecelli ederse, gelecek kaygısından arınır. İşleri yoluna girer. Ayrıca mülkün hakiki sahibinin Allah olduğunu unutmadan okunursa okuyan kişiye kibirden arındırılmış bir zenginlik nasip olacağı rivayet edilir. Ataletten korunmak niyetiyle de okunabilir."},
    90.1: {"isim": "SAD", "anlam": "Bu sure bir kişide tecelli ederse, ses güzelliği ve etkili hitabet niyetiyle okunur. Su elementi eksikliği bulunan kişinin bu elementini dengeler ve kişiye sakinlik verir. Aynı zamanda gerçek anlamda da su bulmak niyetinde olan kişinin suya ulaşmasına vesile"},
    
    93: {"isim": "NECM", "anlam": "Bu sure bir kişide tecelli ederse, dualarının kabulüne aracılık etmesi niyetiyle necm suresini okuyabilir. Ayrıca ideallerine kavuşmak isteyen, makam-mevki sahibi olmak isteyen, bir yere naklini yaptırmak isteyen ve her türlü meşru isteklerinin gerçekleşmesini dileyen, teheccüt vakti bu sureyi okuyabilir."},
    100: {"isim": "KAF", "anlam": "Bolluk ve bereket niyetiyle, yapılan işlerden güzel sonuçlar alınması için okunur. Kaf suresi bir kişide tecelli ederse, kişinin göz ve batın hastalıklarına yatkın olduğunu, bu bölgelerin hassasiyetinden korunmak niyetiyle okunması gerektiğini söyleyebiliriz. Ayrıca ölmek üzere olan kişilere okunması alimlerimiz tarafından tavsiye edilmiştir."},
    103: {"isim": "CIN", "anlam": "Bu sure bir kişide tecelli ederse, metafizik alemlere yatkın olduğu düşünülebilir. Aynı zamanda bu sure nazar ve şeytanın şerrinden korunmak, küçük çocukların her türlü kötülüklerden korunması ve manevi rahatsızlıklardan korunmak niyetiyle okunabilir."},
    105: {"isim": "KEHF", "anlam": "Burun hastalıklarından şifalanmak, kalabalıklar içerisinde yalnızlık hissinden kurtulmak ve ahir zaman fitnelerinden emin olmak için okunur."},
    111: {"isim": "ALA", "anlam": "Bu sure bir kişide tecelli ederse, iç dünyasındaki güzelliklerin açığa çıkarak kişinin yücelmesine aracılık eder. Aynı zamanda sınavlarda başarı elde etmek, yüce mevkilere ulaşmak niyetiyle okunduğu rivayet edilmiştir."},
    111.1: {"isim": "NAS", "anlam": "Bu sure bir kişide tecelli ederse, insanlardan gelecek her türlü zararın Allahın desteği ile giderilmesine aracılık eder. Bu niyetle başkaları tarafından da okunabilir."},
    112: {"isim": "NISA", "anlam": "Akrabalar arasındaki anlaşmazlığı ortadan kaldırmak ve dirlik,düzen, muhabbetin tekrar kurulması amacıyla okunur. Yaşama sevinci verilir."},
    118: {"isim": "CUMA", "anlam": "Bu sure bir kişide tecelli ederse, okuyarak Allaha sığındığı zaman Allah onun kusurlarını ve noksanlarını örter. Maddi ve manevi kısmetin açılması ve müjdelere nail olmak niyetiyle de okunabilir. Ticaretle uğraşan insanların her Cuma günü okuması tavsiye edilebilir."},
    120: {"isim": "NEML", "anlam": "Bu sure bir kişide tecelli ederse o kişiye yüksek makam ve mevkilerin ikram edileceğine işarettir. İlim ve fen'de ilerlemek, insanların arasında saygınlığının artmasını dilemek için okunur. Bu surenin okunması, bereketli yağmurları çeker ve eşyanın hakikatini tanımaya vesile olur."},
    120.1: {"isim": "FIL", "anlam": "Bu sure bir kişide tecelli ederse, gücünün üzerindeki yüklerini Allaha bırakması kendisine tavsiye edilir. Aynı zamanda düşmanını mağlup etmek ve zafer elde etmek isteyen kişi düşmanının yüzüne karşı okursa galip gelir diye rivayet etmiştir."},
    
    124: {"isim": "MUZZEMMIL", "anlam": "Bu sure bir kişide tecelli ederse, zor işlerinin kolaylaşmasına ve her türlü şiddetten muhafaza edilmesine aracılık eder. Ayrıca ürkmüş çocuğun üzerine okunursa korkusundan arınır. Bu sureyi okuyanın tahmin edemeyeceği yerlerden rızıklanacağı rivayet edilmiştir."},
    126: {"isim": "YUNUS", "anlam": "Düşmanın şerrinden korunmak, gönül darlığı çekenlerin rahatlaması, kolay doğum yapmak için okunur. Teslimiyetin sembolüdür."},
    132: {"isim": "MUHAMMED", "anlam": "Zarar verici şeylerden kurtulup, saadete nail olmak, işlerin yoluna girmesi niyetiyle okunabilir. Okuyan kişi çevresinde itibar görür ve kişinin düşmanlarından arınmasına vesile olur. "},
    132.1: {"isim": "ABESE", "anlam": "Bu sure bir kişide tecelli ederse, o kişiye güler yüzlü olmanın önemi hatırlatılır. Aynı zamanda yola gelmeyecek insanlar ve güzel söze kulak tıkayanlar için emek vermenin boş olduğunu, daha ziyade öğrenmeye açık insanlar için emek vermek gerektiğini anlatır. Kişiye hayatındaki kişi/olayların önem sırasını gözetebilme yeteneği katar."},
    
    137: {"isim": "MU-MIN", "anlam": "Bu sure bir kişide tecelli ederse, o kişinin güvenilir olmaya ve güvende olduğunu bilmeye ihtiyacı vardır."},
    140: {"isim": "TALAK", "anlam": "Bu sure bir kişide tecelli ederse, o kişiye eşler arası arabuluculuk görevi verilebilir. Aynı zamanda doğru ve yanlışı ayırdetmek niyetiyle de okunabilir."},
    155: {"isim": "KIYAMET", "anlam": "Bu sure bir kişide tecelli ederse, kötü alışkanlıklarından arınmasına aracılık eder. Günah işlemekten uzak durmak isteyenler bu sureden destek alabilirler. Ayrıca kişiyi başıboş olmadığı bilincine ulaştırır."},
    156: {"isim": "YUSUF", "anlam": "Hasreti çekilen kimseye kavuşmak, izzet ve saadete nail olup bahtın açılması, yakınlarından gelecek zarardan korunmak ve ruhun kolaylıkla teslimi için okunur."},
    162: {"isim": "ENFAL, INSAN, ENAM", "anlam": "Hapisten, iftira ve musibetten kurtulmak, iyi ve kötüyü ayırt etmek, katı kalpli kişilerin kendilerine yapılan nasihati anlamaları için okunur. | Bu sure bir kişide tecelli ederse, insanın yaradılışı üzerine tefekkür etmesi kendisine öğütlenir. Dünya nimetlerini saplantı haline getirmekten korunmak için de zikredilebilir."},
    167: {"isim": "MAUN", "anlam": "Bu sure bir kişide tecelli ederse, kişinin cömertliği konusunda desteklendiği anlaşılır. Aynı zamanda riya ve gösterişten korunmak , ibadetlerini düzenli yapmak isteyen kişi bu süreyi okuyabilir."},
    170: {"isim": "KALEM", "anlam": "Bu sure bir kişide tecelli ederse, o kimsede yazarlık potansiyeli olduğunu bildirir. Ayrıca zihin açıklığı ve nazardan korunmak niyetiyle de okunabilir."},
    182: {"isim": "VAKIA", "anlam": "Bu sure bir kişide tecelli ederse, o kişi kalıcı eserler bırakır. Zenginlik suresi olarak bilinir. Okuyan kişiyi zinadan koruduğu da rivayet edilir."},
    190: {"isim": "AHKAF", "anlam": "Bu sure bir kişide tecelli ederse, aile içi mutluluğun önemini anlatır. Kişinin hakiki iyiliği ailesine yapması gerektiğini vurgular. Aile içi ilişkilerin düzelmesi niyetiyle okunabilir. Aynı zamanda acil olarak kabul edilmesini istediği duası varsa öncesinde Ahkaf suresini okuyarak sonrasında dua etmeyi tercih edebilir."},
    193: {"isim": "MUMINUN", "anlam": "Ruhi bunalımdan ve cilt hastalıklarından korunmak niyetiyle okunabilir. Güzel ahlak kazanmak ve yolcululuğun selameti için de okunur."},
    200: {"isim": "ALAK", "anlam": "Bu sure bir kişide tecelli ederse, kainatın mesajlarını okuyabilmek kişiye nasip olur. İlmiyle amel etmek ve ön yargılarından kurtulmak isteyen kişi bu sureyi okuyabilir."},
    210: {"isim": "FELAK", "anlam": "Bu sure bir kişide tecelli ederse, kıskançlıktan ve büyü-sihir gibi metafizik etkilerden korunmaya ihtiyacı vardır. Bu sure kendisinde tecelli etmeyen kişi de işlerinin başarıya ulaşması ve sıkıntılı hallerden kurtuluş niyetiyle okuyabilir."},
    211: {"isim": "HICR", "anlam": "Ticaretin kazançlı olması için, kalplerin yumuşaması için, Allahın koruması altında olmak için okunur. "},
    211.1:{"isim": "BURUC", "anlam": " Bu sure bir kişide tecelli ederse, o kişinin astroloji alanında yeteneği vardır denilebilir. Sütten kesilmek istenen çocuğun üzerine bu sure okunur. Yatmadan önce okuyan kişinin de Allahın himayesinde olarak sabahladığı ve Levh-i Mahfuzun hikmetini idrak edeceği rivayet edilmiştir."},

    214: {"isim": "HAKKA", "anlam": "Bu sure bir kişide tecelli ederse, hakkında kötülük düşünen ve konuşanların helak olmasına aracılık eder. Ayrıca doğru ve yanlışı ayırt etmek, kendini hesaba çekmek ve Allah katından desteklenmek isteyen kişiler de bu sureyi okuyabilir."},
    215: {"isim": "TUR", "anlam": "Bu sure bir kişide tecelli ederse, aile için küskünlüklere yatkın olduğunu söyleyebiliriz. Bu dargınlıkların kalkması niyetiyle Tûr suresini okuması sulhu sağlar. Yolculuğun şerlerinden emin olmak niyetiyle okunur. Ayrıca haksız yere maruz kalınan suçlamalardan kurtulmak isteyen kişiye okuması tavsiye edilir."},
    221: {"isim": "LOKMAN", "anlam": "Ebeveyn ile çocuklar arasındaki ilişkilerin güzelleşmesi, üslubun geliştirilip güzelleşmesi ve ahlaki meziyetlerin gelişmesine katkıda bulunur."},
    246: {"isim": "RUM", "anlam": "İstenilen başarılara erişmek için sabretmenin önemi hatırlatılır. Bu sure kimde tecelli ederse, eninde sonuna imkansız gibi görünen başarılara ulaşacağı söylenebilir."},
    247: {"isim": "ZUMER", "anlam": "Bu sure bir kişide tecelli ederse, iki cihanda aziz olmaya ihtiyacı vardır. Okuyan kişiye heybet ve şeref katar. Ayak ağrılarının şifalanması niyetiyle de okunabilir."},
    250: {"isim": "SAFF", "anlam": "Bu sure bir kişide tecelli ederse, söz verdiğinde sözünü tutabilmesi konusunda kendisini destekler. Ayrıca aile saadeti için de okunabilir."},
    256: {"isim": "NUR", "anlam": "Dil ile yapılan günahlardan kurtulmak için ve aynı zamanda vesveseden kurtulup imanı kamile ulaşmak için okunur. Aile saadetini korumak niyetiyle okunur."},
    258: {"isim": "IBRAHIM", "anlam": "Ahlakın güzelleşmesi, tevhid inancının yerleşmesi ve anne baba rızasını almak için okunur."},
    263: {"isim": "ISRA", "anlam": "Kötülüğünden korkulan bir kişinin yanına girmeden önce okunursa kötülüğünden korunmuş olur. Ayrıca manevi zenginlik ve teselli için de okunur."},
    274: {"isim": "RAD", "anlam": "Düşmanın zelil olması, semavi afetlerden korunmak ve hareketli çocuğun sakinleşmesi için okunur."},
    280: {"isim": "KASAS", "anlam": "Esaretten kurtulmak için, karın ve karaciğer hastalıklarından şifa bulmak için ve yalancı şahitlerin şerrinden korunmak için okunur. Bu sure bir kişide tecelli ederse o kişi adaletin ve doğrunun temsilcisi olur."},
    283: {"isim": "FECR", "anlam": "Bu sure bir kişide tecelli ederse, geleceğe ümitle bakmasına vesile olur. Okuyan kişiyi cömertliğe ve nimetlere şükretmeye yöneltir. Aynı zamanda nefis mertebelerinin kolayca geçilmesi için okunabileceği rivayet edilmiştir."},
    290: {"isim": "MERYEM", "anlam": "Kadınların çocuk sahibi olmaları için okunur. Tecelli ettiği kişide iffetin korunmasını ifade eder."},
    290.1:{"isim": "FATIR", "anlam": "Bu sure bir kişide tecelli ederse o kişinin ömrü bereketli olur ve mahlukat tarafından sevilir. Hırsızlardan korunmak niyetiyle ve güvenilir bir şekilde seyahat etmek niyetiyle okunabilir."},

    298: {"isim": "RAHMAN", "anlam": "Bu sure bir kişide tecelli ederse, kainatta var olan tüm eril dişil alanlarda dengeye ihtiyacı vardır. Aynı zamanda bu sureyi okuyan kişi fakirken zengin olur, günahları bağışlanır, ruhani hastalıklarından arınır, korkularından emin olur ve Allahın rızasını kazanır diye rivayet edilmiştir."},
    304: {"isim": "KADIR", "anlam": "Bu sure bir kişide tecelli ederse, kişinin kendi değerini bilmesine ve o kişinin az bir çabayla büyük karşılıklar alacağına işaret eder. Aynı zamanda dualarının kabul olmasını isteyen kişi öncesinde bu sureyi okuyabilir."},
    307: {"isim": "BAKARA", "anlam": "Metafizik saldırılardan korunmaya aracılık eder. Aile huzuru verir."},
    310: {"isim": "TARIK", "anlam": "Bu sure bir kişide tecelli ederse, öngörüsünün artmasına vesile olur. Ayrıca şüpheli bir ilaç içen kimse ilacın zararından korunmak için bu sureyi okuyabilir. Ayrıca uykuda şeytanın vesveselerinden korur."},
    314: {"isim": "MEARIC", "anlam": "Bu sure bir kişide tecelli ederse, güvenilir olarak bu ahlakla derece derece yükselmesi konusunda kendisini destekler. Ayrıca korkulardan emin olmak ve başarıya ulaşmak niyetiyle de okunabilir. Kabus görmekten korunmak niyetiyle de okunabilir."},
    327: {"isim": "MUNAFIKUN", "anlam": "Bu sure bir kişide tecelli ederse, göz sağlığını korumak niyetiyle ve her türlü sancılı hastalıklardan korunmak niyetiyle okumalıdır. Ayrıca nifaktan kurtulmak, birlik ve beraberliğin lezzetini tatmak niyetiyle de okunabilir."},
    340: {"isim": "KAMER", "anlam": "Bu sure bir kişide tecelli ederse, onun zor işleri kolay olacaktır. Birlik ve beraberliğin sağlanması niyetiyle de bu sure okunabilir."},
    340.1: {"isim": "NASR", "anlam": "Bu sure bir kişide tecelli ederse, gücü yetmediği halde Allah tarafından desteklenerek başarıya ulaşır. Aynı zamanda fetih suresini okumaya o anda imkanı olmayan kişi aynı niyetlerle nasr suresini okuyabilir."},

    341: {"isim": "INFITAR", "anlam": "Bu sure bir kişide tecelli ederse, kişiye gerçekçi bir bakış açısı kazandırır. Ayrıca doğum yapmak üzere olan kişinin kolay doğum yapması niyetiyle okunabilir."},
    349: {"isim": "MUTAFFIFIN", "anlam": "Bu sure bir kişide tecelli ederse, ticarete yatkınlığına işaret etmekle birlikte, ticaret adabına uyması konusunda da uyarır. Aynı zamanda ticaretteki kazancın bereketli olması için okunabilir diye rivayet edilmiştir. Her kim sıkıntı ve stresli anlarında bu sureyi okursa kısa zamanda sıkıntıları çözülür."},
    352: {"isim": "ARAF", "anlam": "Verdiği kararda isabetli olarak yükselmek, geçmiş ve gelecek arasında denge kurmak için okunur."},
    357: {"isim": "KAFIRUN", "anlam": "Bu sure bir kişide tecelli ederse, sınırlarını korumak konusunda ve Allahın koyduğu kurallara uymak hususunda desteklenir. Ayrıca iman konusunda tartışan insanlara galip gelmek niyetiyle de bu sure okunabilir."},
    360: {"isim": "ASR", "anlam": "Bu sure bir kişide tecelli ederse, ânı yaşamak kişiye tembihlenir. Erteleme hastalığından kurtulmak niyetiyle ve Allahın verdiği herşeye razı olmak niyetiyle okunabilir."},
    376: {"isim": "KARIA", "anlam": "Bu sure bir kişide tecelli ederse, kişi hayatındaki birçok alanı dengelemeye başlar. Ayrıca ani gelişmelere karşı hazırlıklı ve soğukkanlı olmayı destekler."},
    391: {"isim": "ALI IMRAN", "anlam": "Okunulan evde bereket çoğalır. Manevi hediyeler verilir. Gelecek kaygısından arındırır."},
    400: {"isim": "ŞEMS", "anlam": "Bu sure bir kişide tecelli ederse, saygın bir kişi haline gelmesi için aracılık eder. Bu sureyi okuyanın nasibi bol olur, gittiği yerlerde iltifat görür ve başarılı olur. Aynı zamanda babası ile arası bozuk olanın ilişkisinin şifalanacağı da rivayet edilmiştir."},
    413: {"isim": "TEVBE", "anlam": "Hakedişlerden kurtulmak, hastalıklara şifa, gerçek doğru ve yanlışı ayırt etmek niyetiyle okunur."},
    431: {"isim": "FURKAN", "anlam": "Düşmanın perişan olması için, zirai verim için ve hayırlı bir evlat sahibi olmak, doğruyu yanlışı ayırt edecek iradeye sahip olmak niyetiyle okunur."},
    460: {"isim": "TIN", "anlam": "Bu sure bir kişide tecelli ederse, eril-dişil dengesini sağlamasına destek olur. Aynı zamanda yaşadığı müddetçe fıtrat üzere yaşamak isteyen, halkın gözünde heybetli ve gösterişli olmak isteyen ve insanlara sevimli görünmek isteyen kişi bu sureyi okuyabilir."},
    486: {"isim": "ADIYAT", "anlam": "Bu sure bir kişide tecelli ederse, hakkın tarafında olmayı ve islamın inklabında yer alacağını haber verir. Kişiyi dünyevi telaşlardan arındırarak mücadele gücüyle donatır."},
    488: {"isim": "FETIH", "anlam": "Fayda sağlamak ve yaşanılan herhangi bir zorluğun içerisinden kazançla çıkmak niyetiyle okunur. Bu şekilde çözüme ulaştıracak kapıların açılmasına vesile olurken kişiyi başarıya ulaştırır."},
    494: {"isim": "FATIHA", "anlam": "Güzel başlangıçları temsil eder. Güzel ahlakı canlandırmak ve yeni işlere başlamak konusunda kolaylık verir."},
    508: {"isim": "HAŞR", "anlam": "Bu sure bir kişide tecelli ederse, o kişinin dünya ahiret dengesini kurmasına, hatalardan uzak kalmasına, bela ve musibetlerden korunmasına vesile olur."},
    516: {"isim": "ŞURA", "anlam": "Bu sure ciğer rahatsızlığı olanların şifası niyetiyle, hafıza kuvvetlendirmek niyetiyle ve ticareti canlandırmak niyetiyle okunabilir. Aynı zamanda şerri büyük düşmanın şerrinden emin olup onu mağlup etmek niyetiyle okunabilir. Yağmur dualarında da bu sureye yer verilir."},
    519: {"isim": "CASIYE", "anlam": "Bu sure bir kişide tecelli ederse, heyecanını yatıştırmaya ve varsa panik atak durumundan kurtulmasına vesile olur. Bu sure kişin geçmişte işlediği ve pişmanolduğu hataların örtülmesi niyetiyle de okunabilir. İftiradan koruduğu ve yol güvenliği sağladığı da rivayet edilir."},
    529: {"isim": "NAZIAT", "anlam": "Bu sure bir kişide tecelli ederse, o kişide muhakeme yeteneğini arttırır. Aynı zamanda sezgilerin artması, dikkat dağınıklığının giderilmesi, kuvvetli bir hafıza, diri bir zeka, idrak ve irfan dolu sezgi gücü niyetiyle okunabilir."},
    543: {"isim": "MUMTEHINE", "anlam": "Bu sure bir kişide tecelli ederse, en yakınları arasında dahi adil olması konusunda desteklenir. Bu sureyi okuyan kişi kin nefret ve bozgunculuk duygularından arınmak niyetiyle okuyabilir."},
    548: {"isim": "ANKEBUT", "anlam": "Bu sure bir kişide tecelli ederse, tedbir almanın önemini öğrenmesi gerekir. Hafızanın kuvvetlenmesi için de okunabilir."},
    552: {"isim": "INŞIKAK", "anlam": "Bu sure bir kişide tecelli ederse, etkili bir hitabet yeteneğine sahip olur. Aynı zamanda konuşma güçlüğü çeken çocuklar için de okunabilir. Kolay doğum ve baş ağrısının şifası için okunduğu da rivayet edilmiştir."},
    559: {"isim": "INŞIRAH", "anlam": "Bu sure bir kişide tecelli ederse, kişiye kuvvetli bir hafıza ve psikolojik dayanıklılık sağlar. Bununla birlikte her gün okuyan kişi tembellik ve unutkanlıktan kurtulur. Kalp sıkıntıları geçer ve yaşadığı zorluklar kolaylaşır diye rivayet edilmiştir."},
    572: {"isim": "ŞUARA", "anlam": "Bu sure bir kişide tecelli ederse, o kişiye şairlik yeteneği verir. Kabakulak hastalığının şifası niyetiyle okunabilir. Her türlü güncel kötülükten ve inanç sıkıntılarından kendimizi ve ailemizi korumak niyetiyle okunur."},
    610: {"isim": "KUREYŞ", "anlam": "Bu sure bir kişide tecelli ederse, zorluk yaşadığı yeri değiştirmesi tavsiye edilir. İtibar kazanmak ve güzel ahlaka nail olmak için okunur. Ayrıca böbrek hastalıklarının şifası için okunacağı rivayet edilmiştir."},
    612: {"isim": "HUCURAT", "anlam": "Bu sure, ilmin bütün derinliklerine ulaşmaya çalışan kişilere kolaylık sağlar. Kötülük ve hastalıklardan kurtulmaya, toplumda olması gereken güzel ahlakın kişiye yerleşmesine vesile olur."},
    636: {"isim": "TEKVIR", "anlam": "Bu sureyi okuyan kişinin mahcup olmaktan, korku ve evhamlardan korunacağı rivayet edilir."},
    652: {"isim": "SAFFAT", "anlam": "Bu sure bir kişide tecelli ederse, kişiye insanları güzel bir amaç etrafında toplama potansiyelini verir. Zarar verici haşeratın şerrinden korunman niyetiyle de okunur"},
    655: {"isim": "DUHAN", "anlam": "Metafizik varlıkların şerrinden korunmak niyetiyle okunur. Kişinin sempati duyulan birahlaka kavuşmasına vesile olur. Özellikle Cuma gecelerinde (Perşembe akşamı) bu surenin bereketinden istifade edilmesi tavsiye edilir."},
    658: {"isim": "TAHRIM", "anlam": "Bu sure bir kişide tecelli ederse, ağzından çıkacak sözlere çok dikkat etmesi vurgulanır. Sır tutamamak ve diliyle kendine belayı çekmek gibi manevi rahatsızlıklardan kurtulmak niyetiylede okunabilir. Kocası zalim olan bir kadın tarafından okunursa o zulümden kurtulmasına aracılıkedeceği rivayet edilmiştir."},
    690: {"isim": "FUSSILET", "anlam": "Bu sure bir kişide tecelli ederse, göz rahatsızlıklarına şifa olması niyetiyle okunur. Aynı zamanda okuyan kişiyi yolculuk tehlikelerinden ve hırsızlardan korumaya vesile olduğu rivayet edilir."},
    712: {"isim": "AHZAB", "anlam": "Bu sure bir kişide tecelli ederse o kişiye şükrün önemini anlatır. Ticari kazancın bol ve bereketli olması niyetiyle, ayrıca uyku problemi olan kişi uykuyu dengelemek niyetiyle okuyabilir."},
    722: {"isim": "IHLAS", "anlam": "Bu sure bir kişide tecelli ederse ve bu kişi her türlü işini samimiyetle yaparsa, kimseye ihtiyaç duymayacağı bir hayat yaşar. Ayrıca inanç sistemindeki sıkıntıları gidermek niyetiyle de okunabilir."},
    726: {"isim": "KEVSER", "anlam": "Bu sure bir kişide tecelli ederse, neslinin devamlı olacağına, neslinden güzel ahlaklı kimseler çıkacağına işaret eder. Rızkının bollaşmasını isteyen bu sureyi okuyabilir."},
    731: {"isim": "MURSELAT", "anlam": "Tecelli ettiği kişiye dünyaya ne için gönderildiğini hatırlatır. Ayrıca karaciğerrahatsızlıklarından şifa bulmak niyetiyle okunabileceği rivayet edilir. İnsanın hayatına prensip ve düzen getirmesi niyetiyle okunabilir."},
    804: {"isim": "TEBBET", "anlam": "Bu sure bir kişide tecelli ederse, akrabanın eziyetinden korunur. Haklı olduğu davayı kazanmak isteyen kişiye de tebbet suresi okuması tavsiye edilir."},
    818: {"isim": "DUHA", "anlam": "Bu sure bir kişide tecelli ederse, kalabalıklar içerisinde yalnız kalma hissinden arınır. Aynı zamanda iç huzuru ve ruhsal dinginlik için okunabilir."},
    893: {"isim": "ZUHRUF", "anlam": "Bu sure bir kişide tecelli ederse, vesveseden korunmaya ihtiyacı olduğuna, bolluk ve berekete ihtiyacı olduğuna ve eşiyle muhabbetinin artmasına ihtiyacı olduğuna işaret eder. Bu sure cilt hastalıklarının şifası niyetiyle ve öfkenin bastırılıp aklın galip gelmesi niyetiyle okunabilir. Okuyan kişiye dünyanın geçici olduğu bilincini verir."},
    1121: {"isim": "TEKASUR", "anlam": "Bu sure bir kişide tecelli ederse, o kişinin çokça şükretmesinin gerekliliğine vurgu yapar. Ayrıca maddi manevi rızkın artmasına vesile olur."},
    1248: {"isim": "MUDDESSIR", "anlam": "Bu sure bir kişide tecelli ederse, harekete geçmesi konusunda ve insanlığı güzel işlere yönlendirmesi konusunda desteklenir. Aynı zamanda zihnini olumsuz düşüncelerden temizlemek isteyen kimse bu sureyi okuyabilir."},
    1312: {"isim": "ZARIYAT", "anlam": "Zariyat suresi bir kişide tecelli ederse, kıtlık bilincinden çıkması gerektiğini anlatır. Doğum sancılarının azalması niyetiyle, bolluk ve bereket niyetiyle bu sure okunabilir. Özellikle toprak mahsullerinde berekete vesile olur."},
    1316: {"isim": "GAŞIYE", "anlam": "Bu sure bir kişide tecelli ederse, hayatını bir plan ve program içerisinde yürütmesine aracılık eder. Aynı zamanda başlattığı bir şeyin yayılmasını isteyen kişi bu sureden destek alabilir. Bir teftişin kolay geçmesi niyetiyle okunabilir."},
    1453: {"isim": "TEGABUN", "anlam": "Bu sure bir kişide tecelli ederse, o kişi aldanmaktan korunur. Bir yerde muhafaza etmek istediğimiz eşyaya okuyup muhafazasına niyet edebiliriz. Aynı zamanda şerrinden korktuğumuz insanın yanına girerken okumak da muhafaza edilmemizi sağlayabilir."},
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
    en_yakin_esmalar = []
    en_yakin_deger = None
    
    for ebced_degeri, esma_detay in esmalar.items():
        fark = abs(float(str(ebced_degeri).split('.')[0]) - toplam)
        if fark < en_yakin:
            en_yakin = fark
            en_yakin_deger = int(float(str(ebced_degeri).split('.')[0]))
            en_yakin_esmalar = []
            
        if fark == en_yakin:
            en_yakin_esmalar.append({
                'esma': esma_detay['esma'],
                'anlam': esma_detay['anlam'],
                'zikir_gunu': esma_detay['zikir_gunu'],
                'zikir_saati': esma_detay['zikir_saati'],
                'ebced_degeri': ebced_degeri
            })
    
    return {
        'esmalar': en_yakin_esmalar,
        'ebced_degeri': en_yakin_deger
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
    en_yakin_sureler = []
    en_yakin_deger = None
    
    for ebced_degeri, sure_detay in sureler.items():
        fark = abs(float(str(ebced_degeri).split('.')[0]) - toplam)
        if fark < en_yakin:
            en_yakin = fark
            en_yakin_deger = int(float(str(ebced_degeri).split('.')[0]))
            en_yakin_sureler = []
            
        if fark == en_yakin:
            en_yakin_sureler.append({
                'sure': sure_detay['isim'],
                'anlam': sure_detay['anlam'],
                'ebced_degeri': ebced_degeri
            })
    
    return {
        'sureler': en_yakin_sureler,
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

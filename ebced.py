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
        "Köken problemi güçlüdür. Kişi, ilk açılımını '1' ile yaparak liderlik, bireysellik ve özgüven meselelerine doğrudan temas eder. Bu durum, kök çakradaki blokajların ve içsel çatışmaların bir yansıması olabilir. Tartışmacı liderlik enerjisi vardır. Kendini beğenmeme özgüven eksiliği yetersizlik veya tam tersi Aşırı ego ile mecadele edebilir. Tartışmacı lider.",
        "Düşünceler duygu temellidir. Bu da karar vermeyi zorlaştırır.  Bu kişilerin dişil enerjisi yüksektir. Erkeklerin, çoğunluğunda beta erkek olma eğilimi gözlemlenir. Hem duygusal hem fiziksel bağımlıklıklara yatkınlıkları fazla olabilir. diplomasi ve arabuluculuk vardır. Küsme huyu olabilir.",
        "Kendini doğru ifade etme/edememe.. Kendini tam anlatamıyor olabilir.. Kendisi hakkında iç alemini bir şekilde dile getirmeli. Gelişirse iyi bir hatip olabilir. Feminist",
        "Zihin yapısı kurallarla çalışır. 'Ya hep ya hiç' düşüncesi baskındır. Kendisini de başkalarını da yargılayabilir. Esneklik azdır; dogmatik fikir yapısına kayma riski yüksektir. Sabır ve sebatla desteklenirse, sağlam, prensipli ve adil bir düşünsel yapı kurabilir.",
        "Zihni korkularla, kendine güvensizlikle sınanır. Cesareti zihinsel olarak üretemediği sürece kararsızlık ve ertelemeler görülür. Risk almaz, bu da gelişimi engeller. Cesaret geliştirdiğinde, yaratıcı, özgür düşünen ve yaşamla daha barışık bir zihinsel düzey yakalayabilir. Eğlencelidir",
        "Düşünceleri sezgisel ama aynı zamanda duygusal yüklerle doludur. Aileden gelen etkiler zihinsel kalıplarını oluşturur. Kararlarında duygusal geçmiş baskındır. İç sesiyle temas kurduğunda, başkalarının iyiliğine odaklanan vicdanlı ve derinlikli bir akıl yapısı geliştirir. Aile odaklıdır",
        "Sürekli gezdirir hayat ve ilmin birinde arayışı durur. Hayat boyu kararsız olmakla uğraşabilir. Tahkiki iman şart. Zihin sürekli sorgular, Çok zeki.",
        "Zihni başarıya, güç kazanmaya ve kendini ispat etmeye odaklıdır. Ancak düşünceler çoğu zaman ya hırsla yönlenir. Düşünsel alanda “ya kazanırım ya ezilirim” inancı vardır. Bolluk bereket, Kendi işini kurma.. Otorite kurmaya, kendini ifade/ispat etmeye, asil olmaya ihtiyaç var. Zenginlik enerjisi.",
        "Saf temiz kalpli... Zihinsel yapısı aşırı uyumlu olabilir. Olayların arka planını araştırmalı.. Her koşula uyum sağlayan.  kendi fikirlerini korumakta zorlanır. Sürekli başkalarını düşünmek ya da memnun etmeye çalışmak zihinsel bulanıklık yaratır. Sınırlar koymalı. Sınırlarını belirlediğinde, zihinsel gücü artar. Olayların ardını sezen farkındalıklı bir düşünür olur."
    ],
    [  # 2. hane - DUYGULAR
        "Önden gitmeyi arzu eder..neden öne çıkmayı istemiş? Duygu dünyası hakkında kökenine inip kendini değerli göremediği alanı bulması, kendiyle barışması gerekir.",
        "En zoru..Üreme organları sıkıntı..Duygusal terapiye muhtaç..Regresyon..Duygusal baskı hissediyor olabilir..",
        "Kendini ifade etme tanıma.. Tıkalıysa içe kapanış..",
        "Duygusal gelişim ağır ilerler. Zorluklar karşısında güçlü görünür ama içte sabırla büyüyen bir yük taşır. Duygularını kolay kolay açmaz. Soğuk, mesafeli ya da aşırı kuralcı davranabilir. Kalpten şifa bulduğunda, duygusal dayanıklılığı ve derinliğiyle güvenilir bir bağ kurar.",
        "Cesaretli, Duygular kosunda pozitif. Üretim gücü kuvvetli.",
        "Sezgisel bir sevgi anlayışı vardır. Yardım etmeye eğilimlidir ama bu çoğu zaman kendi ihtiyaçlarını bastırarak olur. 'Güzin Abla' rolüne sıkışabilir. Sevgiyi babadan bekliyor olabilir. dengelediğinde, şefkatli ama kendini tüketmeyen bir denge oluşturur.",
        "Duygusal olarak kolay tatmin olmayan bir yapıya sahiptir. Anne-baba sevgisine doyamamış olabilir. Bu eksiklik, ilişkilerde sürekli daha fazlasını istemesine yol açar. Değersizlik duygusu derinlere işlemiş olabilir. arayış içinde.",
        "Aurayı korursa zengin olur.. Otoriter olabilir; kontrol ve güç ihtiyacıyla duygular bastırılabilir. Edebiyat ve şiir, edebi yeteneklere meyilli olabilir.",
        "Ya duygularını çok frenliyor, ya da aşırı sınırları açık.. Anlaşılmayacak kadar saf ve iyi niyetli olabilir..Şifacı bir kalptir. Duygusal olarak çok saf, çok açık olabilir."
    ],
    [  # 3. hane - HİTABET VE TİCARET
        "Bu kişi dünyaya bir iş kurmak, temeller atmak ve kendi ayakları üzerinde durmak için gelmiştir. Emir almayı sevmez; kendi yolunu kendi çizer. Ancak önce kendi kökenindeki sorunları temizlemesi gerekir. Liderlik ruhu vardır, ama bu liderliği sağlam zemine oturtmak için içsel dönüşüm yaşamalıdır.",
        "Hitabet ve ticaret hanesi, sevgiyi bulmakla açılmış. 'Yunusça' sevmeyi öğrenmek zorundadır. Ortaklık enerjisi güçlüdür; işlerini ortaklıkla büyütebilir. Ancak ilişkilerde fazla yumuşak olabilir. Duygusal dengeyi sağlarsa iş yaşamında da dengeli ilişkiler kurabilir.",
        "Dil sivriliği, baskı altında kalan ifade enerjisi ve güçlü liderlik potansiyeli bu kişinin içindedir. Eğer yaşadığı baskıları çözerse çok etkili bir konuşmacı veya yazar olabilir. Ancak önce dili terbiye etmeli, öfke ya da sabırsızlıkla konuşmaktan kaçınmalıdır. Bu kişi için kelimeler hem şifa hem yıkım olabilir.",
        "Bu kişi erken yaşta büyük kayıplar yaşamış olabilir. Anne-baba eksikliği ya da duygusal boşluklar, onun hitabetini ve karar verme yetisini şekillendirmiştir. Sabırla, yavaş yavaş kendi yolunu çizer. Hayatta aceleye yer yoktur onun için. Ağır, sağlam ve kalpten konuşur; ama konuşmadan önce çok düşünür.",
        "Ruhunda neşe ve canlılık vardır. Ancak bu hane negatif frekansa geçtiğinde içe kapanma, nazar ve enerji düşüklüğü yaşanabilir. Cesaret ve özgüven, bu kişinin potansiyelini ortaya çıkarır. Sevdiği işi yapmalı, rutinler onu yorar. Ruhsal olarak özgür hissettiğinde parlayacaktır..",
        "Ailesel yüklerle ticari ya da ifade alanı iç içedir. Bu kişi sezgisel zekâya sahiptir ve iyi bir öğretmen, danışman ya da ebeveyn olabilir. Ancak ailesinden gelen korkular veya beklentiler, onun dış dünyaya açılımını zorlaştırabilir. İçsel özgürlükle ifade gücü arasında bir köprü kurmalıdır. Disiplin onun için önemlidir.",
        "İfade alanında sürekli tatminsizlik ve arayış olabilir. Birden fazla üniversite okuyabilir. Alan değiştirebilir. Hep bir iş arayışı içinde olabilir. Matematiksel zekâ ve analitik düşünceye yatkındır. Ancak duygusal doygunluk sağlanmadan konuşmaları tatmin edici olmaz. Kendini yeniden inşa etmesi gerekir.Spiritüel alandan para kazanma.",
        "Doğuştan ticaret, para ve otorite enerjisi taşır. Ancak bu gücü dengeli kullanmak önemlidir. Para kazanma isteği güçlüdür; ticarette başarılı olabilir. Fakat kibirli bir tutum sergilememeli. Zenginlik enerjisi aura korunduğunda tam anlamıyla çalışır. Otorite para ticarette nasibi var..",
        "Derin bir şifa potansiyeli taşır. Kelimeleriyle insanlara iyi gelebilir. Ancak önce kendi yaralarını sarmalıdır. Hitabeti güçlüdür ama bu güç, ruhsal olgunlukla birleştiğinde gerçek şifaya dönüşür. Bu kişi bir öğretmen, ilahiyatçı, danışman ya da doğal bir rehber olabilir."
    ],
    [  # 4. hane - SEVGİ, OLGUNLUK
        "Bedensel hastalıklar olabilir. Kendiyle ilgili zorluk. (kendi kalıplarıyla)",
        "Hayatındaki dişil figürlerle veya yakın ilişkilerle zorluklar yaşamaya meyillidir. Çünkü duygularını bastırır ve zamanla biriktirir; bu da ani veya kontrolsüz tepkilere neden olabilir. Duygusal yakınlıklarda ciddi ilkesizlik ya da aşırı fedakârlık görülebilir. Huzur bulması için önce duygu kontrolünü öğrenmesi gerekir.",
        "İç dünyasını paylaşmaya, konuşarak anlaşılmaya ihtiyaç duyar. Sıkıntıları bastırmak yerine ifade ettikçe kalben rahatlar. Anlaşılmama korkusu taşıyorsa bunu yapamaz. Taşımıyorsa duygusal ifadesi güçlüdür. Anlaşıldıkça iyileşir.",
        "Kararlarında kararlıdır; zorluklar karşısında net ve tutarlıdır. Ağır kalbî imtihanlar yaşayabilirler. İmtihanı aşarken kendi başlarına kalırlar. ",
        "İmtihanlarını şükrederek aşacak. Polyannacılık oynayacak. Hayata açık ve öğrenmeye istekli bir ruha sahiptir.",
        "İmtihan sebebi aile ve otoritedir. Aile, özellikle baba figürüyle ilgili yükler kalp merkezinde taşınır. Bu kişi sevgiyi sezgisel yollarla anlamaya çalışır ama korkularının ve geçmişten gelen kontrolcülüğün etkisiyle sevgiye teslim olmakta zorlanır. Aileden öğrendiği modelleri kırması şarttır. Yoksa aynı döngüleri tekrarlar.",
        "Sevginin kaynağının Yaratıcı olduğunu bilmeli. Sahte sevgi arayışları riskine girmemeli. Zihinsel sorgulama, maneviyat arayışı ve sürekli anlam peşinde koşmak bu kişinin sevgi alanına da yansır. Kalbiyle bağlantıya geçmek yerine analiz etmeyi tercih eder. Sevgiye teslim olmakta zorluk çeker çünkü kontrolsüzlük hissi onu rahatsız eder. Olgunluğu, teslimiyetten geçer.",
        "Güç ve otoriteyi kullanarak sorunları aşar. 'Beni olduğum gibi kabul et, yoksa çekil' tavrı baskındır. Bu yaklaşım, gerçek bağ kurmayı zorlaştırır. Sevgiyi paylaşmak yerine, hakimiyet alanı kurmaya çalışır. Zenginlik ve bereket enerjisini kalp alanına taşıyabilmesi için yumuşaması gerekir. Zorluklar karşısında yönetici ve toparlayıcı bir karakter sergiler",
        "Kalbine duygusal hatalara düşmemek için söz geçirmeli. Ya sınır koyamayan aşırı saf bir yapı ya da aşırı sınır koyan, mesafeli biri olabilir. Bu kişide ya hayır diyememe problemi ya da aşırı hayır deme eğilimi görülür. "
    ],
    [  # 5. hane - ŞÜKÜR VE DOYUM
        "Bu kişi doyumu hep daha büyük hedeflerde arayabilir. Kendine dair yüksek beklentiler taşır. 'Oldu ama daha iyisi olmalıydı' diyerek düşüncesinde olabilir. Ego, mükemmeliyetçilik ve kendine yönelttiği sert eleştiriler, içsel huzurunu sabote eder.  Şükrü yaşam tarzına çevirdiğinde sade bir huzur mümkün olur.Mütevazi olmayı öğrenmeli.",
        "Bağ kurma yeteneği çok yüksektir. Sevgi ve ilgi açlığı baskındır. Duygusal ilişkilerde bağımlılık geliştirme eğilimi vardır. Sevgi alma konusunda doyum yaşamadığı için, geçmişte özellikle anneyle olan ilişkiden kaynaklı bir eksiklik taşır. Romantik ilişkilerde fazlasıyla verici ya da yapışkan olabilir. Sürekli bir 'doyurulma' beklentisi taşıyabilir.",
        "İletişimden keyif alır. Konuşmak, paylaşmak ve anlatmak bu kişinin en büyük keyif kaynaklarıdır. Konuşurken çevresine ilham ve neşe vericidir (3. cakrası iyiyse). Ancak anlatmanın arkasında görünme, onay alma ihtiyacı olabilir. Şükür alanı, dışsal etkileşimlere bağlıysa içsel huzur zor sağlanır. Her zaman çevreden bir etkileşim bekler; yalnız kalınca doyumu kaybedebilir.",
        "Aşırı merhametli olabilir ama bu onu tüketebilir. Başkalarının acılarına aşırı odaklanmak, kendi sınırlarını yok saymasına neden olur. Hayattan memnuniyet duymak için önce kendine dönmesi gerekir. Aksi halde hep başkalarının yükünü taşır ve tükenmişlik hissi taşıyabilir.",
        "Hayatta sevilmediğini düşünebilir, özgürlük arayışı ve iç huzursuzluk arasında gidip gelir. Sürekli bir şeylerin eksik olduğu hissi taşıyabilir. Şükürsüzlüğe doğru kayabilir. Bu durumu kendi çabalarıyla çözmesi lazımdır(5!). Bunu çözerse başkalarının kalbine kolayca ulaşır. Doyum, ancak bu eski kayıtlar temizlenirse mümkündür. Aksi halde, şükür hali yüzeysel kalır.",
        "Güven veren, sadık sahibi bir yapıdadır. Aileye yönelik aşırı sorumluluk duygusu, bu kişiyi sürekli veren pozisyonda tutar. Doyum yaşamaktan çok, başkalarının ihtiyaçlarını karşılamaya odaklıdır. Özellikle baba figürüyle ilişkisi belirleyici olabilir. Şükretmek yerine 'vermek zorundayım' hissiyle hareket etme ihtimali vardır.",
        "Sevgi arayışı vardır. Bu sevgi arayışı ruhsaldır ama bu, kişinin gerçek doyumu yaşadığı anlamına gelmez. Sık sık 'neden bana yetmiyor?' sorusuyla baş başa kalır , ama tatminsizlik hissi içini kemirebilir. Derin düşünebilme ve sezgisel analiz becerisi gelişmiştir.",
        "Ara ara doyumu maddi mutlulukla özdeşleştirme hatasına düşebilir.  Sahip olmak, kazanç elde etmek ve konfor alanları yaratmak önceliklidir. Girişimci bir ruha sahiptir",
        "Sevgide sınırlara dikkat.. Şefkatlidir ama sınır koymakta zorlanır. Ruhsal rehberlik, danışmanlık hizmeti ve yalnız zamanlar, içsel doyumu artırır."
    ],
    [  # 6. hane - AİLE, BABA
        "'Beni dinleyeceksin!' mesajı veren bir yapıdadır. Düşüncelerine aşırı değer verir ve otorite kurmak ister. Çocuklukta sesinin duyulmaması, ailede yeterince ciddiye alınmaması bu tepkinin kaynağı olabilir. Baba ile çatışma yaşanmış ya da babadan onay alınamamış olabilir. Aile içinde bireysel kimliğini ortaya koymak için savaş vermiştir.",
        "Aileye ve ailesi olarak gördüğü insanlara, özellikle ebeveynlerine duygusal olarak bağımlı olabilir. Çoğu zaman çocuklukta sevgiyi eksik almıştır ve bunu yetişkinlikte telafi etmeye çalışır. İlişkilerde sürekli onay arayışıyla davranabilir. Kendi sınırlarını çizmekte zorlanır. Duygusal olarak doyumsuz ve kararsız bir yapı gelişebilir.",
        "Aileyle özellikle baba ya da diğer “eril” figürlerle iletişim kurma becerisi gelişmeli, kendisini ifade ederek temas kurmalı. Bu kişi, müdahaleci aile yapılarında büyümüş olabilir. Dedikodular, yönlendirmeler veya otorite baskısı yaşamış olabilir. Konuşarak çözüm arar. Aynı zamanda bu açılım, “aile içinde konuşarak var olma”, fikir beyan etme, kendini ifade ederek ailede konum kazanma gibi dinamiklere de işaret eder.  Kişinin ailesiyle –özellikle babasıyla– olan ilişkisinin, mesleki yönelimini doğrudan etkilediğini gösterir. Çoğu zaman bu kişi, babasının mesleğine benzer bir alana yönelir ya da babanın iş anlayışı, vizyonu, yöntemleri üzerinde güçlü bir etkide bulunur.",
        "Sert ve sabır gerektiren bir aile yapısından gelir. Erken yaşta baba kaybı (4ü de 6 ile açmışsa), babanın yokluğu ya da duygusal erişilemezliği görülebilir. Sevgiye ulaşmak için ciddi çaba sarf etmiştir. Aileyle ilişkilerdeki kuralcılık ve katılık kişiye de geçmiş olabilir. Sevgi onun için “hak edilmesi gereken” bir şey haline gelmiştir.",
        "Sorumluluk almaktan çekinmeyen bir yapıdadır. Ancak bu özelliği çoğu zaman otomatikleşmiştir. Aile içinde erkenden olgunlaşmak zorunda kalmış olabilir. Bu da kişinin içsel çocuk enerjisini bastırmasına neden olabilir. Hayatta ilerlerken şükürle sorumluluğu dengelemek onun için önemlidir.",
        "Aileden gelen sorumluluk yükü altında ezilmiş olabilir. Ve sorumluluk almak istemeyebilir. Kontrolcü, detaycı, aşırı müdahaleci bir yapı geliştirme riski taşır. Baba figüründen yeterince destek alamadıysa, aile içindeki boşluğu kendisi doldurmaya çalışır. Sıklıkla kendi aile modelini tekrar eder. Duygusal esneklik gelişmediyse bu durum onu ilişkilerde zorlayabilir.",
        "Baba figüründe dişil bir enerji olabilir. Ya da kişi, ailede “anne” rolünü üstlenmiş olabilir. Manevi temalar baskındır, ancak bu ruhsallık çoğu zaman kaçış halini alabilir. Gerçek sorunlarla yüzleşmek yerine idealleştirme eğilimi vardır. Kişinin ailedeki rollerle kendi kimliğini ayırt etmesi gerekir..",
        "Aileyle, özellikle babayla maddi ilişkiler öne çıkabilir. Parasal konularla aile içi bağlar iç içe geçmiş olabilir. Eğer kişinin babasıyla arası iyi değilse bolluk ve bereket enerjisi akmaz. Güç ve para ilişkileri üzerinden sevgi tanımı oluşmuş olabilir. Aileyle iyi geçinmek, sadece duygusal değil, enerjisel ve parasal düzeyde de bir açılım sağlar. Babayla arası iyise babadan parasal destek görebilir.",
        "Aile içinde sınır problemleri yaşamış olabilir. Kendi alanını korumakta zorlanır. Suistimal ya da aşırı fedakârlık döngüsü görülebilir. Aile ilişkilerinde şifa ancak net sınırlarla mümkün olur. Kendi bireysel alanını belirlemeden ilişkilerde huzur bulması zordur."
    ],
    [  # 7. hane - ANNE, İMAN
        "Kişi anneye benzeyebilir. Kökten gelen sorunları ancak güçlü bir iradeyle aşabilir. Anneyle ilişkisi ya mesafelidir ya da rekabetlidir. Bu kişi için “kendi ayakları üzerinde durmak” temel inanç haline gelmiştir. Maneviyatı güçlenmeden içsel huzura ulaşması zordur. Kişiye manevi aktarımlar vardır.",
        "Sevgi beklentisini anneden veya dişil figürlerden karşılamak ister. Dişil figürlere zaafiyeti olabilir. sevilmek için kendinden ödün verebilir. “Ben değerli miyim?” sorusu içten içe onu yorar. Sevgiyi bulduğunda çok derin bağlar kurabilir. Empati gücü gelişmiştir.",
        "Sözel ifade, onun anneyle ya da hayatındaki kadınlarla bağını oluşturur. Anlatma, öğretme, yazma gibi alanlarda doğuştan yeteneklidir. Sözü değerlidir (Söz sihirbazı). Kadınlarla iletişimi iyi olabilir.",
        "Anne sabır meselesi olabilir. Anne kaybı(özellikle 4 ü de 7yle açmışsa) veya annenin duygusal olarak eksikliği mevcut olabilir. Bu kişi duygusal olarak erken olgunlaşmak zorunda kalmıştır. “Hayat beni zorla büyüttü” duygusu baskın olabilir. Derin sabır ve manevî farkındalık geliştirir.",
        "İştahlı. Boğaz bölgesi hassas olabilir; ifade sorunları, yutulmuş duygular görülür. Psikolojik dengesizliklere yatkın olabilir. Doyum hissi kolay oluşmaz. Hevesli bir yapısı vardır. Yaşam sevgisi yüksektir.",
        "Kendini ailesine veya çevresine “anne” gibi konumlandırabilir. Başkalarını kurtarma eğilimindedir. Sorumluluk bilinci yüksek ama bu onu duygusal olarak yalnız bırakabilir. Sezgisel rehberdir. Gerçekten dinlemeyi bilen, koruyucu ve dönüştürücü bir figür olabilir.",
        "Bu hanede 7 olması zordur. Kişi çoğu zaman inanç krizi yaşar. Kendine, hayata, sisteme ya da Yaratıcıya güven duymakta zorlanabilir. Melankoli ve yalnızlık hissi baskındır. Tahkiki iman geliştirirse, çok güçlü bir içsel merkez kurar. Derin bilgi ve manevî sezgi ile donanır.",
        "Maddiyatı maneviyattan üstün görme.",
        "Sürekli sınır ihlallerine açık olabilir (Anne müdahalesine dikkat). Anneyle ya da kadın figürlerle arasındaki sınır çizgileri bulanıktır. Ya aşırı teslim olur ya da tamamen uzaklaşır. Ruhsal sezgileri ve temiz kalbiyle gerçek maneviyatı deneyimlemeye açıktır. Şifacı potansiyeli güçlüdür."
    ],
    [  # 8. hane - KAZANÇ VE BEREKET
        "Kendi işini kurmak ister, başkalarının yanında uzun süreli çalışmakta zorlanır. Bağımsızlık arzusu maddi alanda baskın şekilde görülür. Ancak bu özgürlük isteği yüzünden istikrar sağlamakta zorlanabilir. Doğru temelde ilerlerse, kendi yolunu çizen, üretken ve girişimci olabilir.",
        "Kazanç hayatında çoğu zaman duygulara bağımlıdır. Yıldız düşüklüğü ve Çocukluk travmaları olabilir (özellikle 11den 2yse). Sevildiğinde üretken olur; sevilmediğinde içe çekilir, motivasyonu düşer. Aurasını sevgiyle beslemeyi öğrenirse, hem manevî hem maddi tatmin sağlar.",
        "İletişim ve konuşma üzerinden gelir elde etme potansiyeli vardır. Ancak dikkat dağınıklığı ve kararsızlık kazanç sürekliliğini etkileyebilir. Konuşmak, anlatmak onun doğal yeteneğidir ama bunu paraya çevirmeyi öğrenmesi gerekir. Anlatım gücünü işe dönüştürebilirse, hayatını kelimelerle kurabilir.(özellikle 3.hanede de sıkıntı yoksa)",
        "Sabır en büyük sınavıdır. Aceleci davranırsa parasal ve güçsel kayıplar yaşar. Kazancını kalıcı kılmak için ciddi emek ve zaman yatırımı gerekir. Ticarette kolay güvenmemeli; özellikle ortaklıklarda dikkatli olmalıdır. Sıkı disiplinle hareket ederse, sabırla gelen kazancı sağlamlaştırabilir.",
        "Yurtdışı işlerde ve sanal alemde para kazanır.",
        "Ticarette sezgileri iyi güçlüdür. Ancak aileden gelen karmik borçlar, özellikle baba kaynaklı sorunlar kazanç yolunu tıkayabilir. Babayla helalleşmesi gerekir. Bu durumları aşarsa Aile/Baba bereket kaynağıdır. Kendi kararlarını vermediği sürece sürekli başkalarının etkisinde kalabilir. Sezgilerine güvenip bireysel kararlar alırsa, bereket alanı genişler. ",
        "Spiritüel alandan para kazanma ihtimali yüksektir. Maneviyat, kazançta doğrudan belirleyicidir. Ruhsal temelli bir iş yaparsa, kalıcı bolluğu yakalayabilir. Aurayı imanla koruyamadığında sık sık maddi kayıplar yaşayabilir. Düşünce yapısı maddiyata odaklanmayı zorlaştırabilir."
        "Doğuştan bolluk ve ticaret enerjisi taşır. Fakat bu güç, beraberinde sorumluluk ve dikkat ister. Nazara çok açıktır. Maddi gücünü iyi kullanırsa, hem bereketli hem de etkileyici bir figür olur. Kendine ait bir iş kurduğunda (özellikle 3 ü 1 ile açıyorsa), maddi olarak hızla büyüyebilir. Ama bu yolda biraz tek başınadır.",
        "Kazancı çoğu zaman şifalandırıcı mesleklerden gelir. Ancak bu kişi önce kendi yaralarını sarmadan başkasına fayda sağlayamaz. Aurası güçlüdür ama korunmazsa başkalarının yüklerini taşımaya başlar. Kendi iyileşme yolculuğunu tamamladığında, başkalarına da bolluk aktarır."
    ],
    [  # 9. hane - HAYAT AMACI
        "Bu kişi öne çıkmak, liderlik etmek, bir şeyin öncüsü olmak için gelmiştir. Ancak bu yükselişin temeli kökten gelirse (kök çakrayı düzgün kullanıyorsa) kalıcı olur. Kökenindeki sorunlar iyileştirilmeden toplumsal alanda görünürlük aramak, kibir ve dengesizlik üretir. Kendini dönüştürüp sağlam temeller kurduğunda ilham verici bir lider olabilir.",
        "Hayat amacı sevgidir ama bu sevgi, bağımlılıktan arınmış bir sevgidir diğer türlü kendini tüketir. Duygusal sınırlarını bilmeli, fedakârlık adı altında kendini tüketmemelidir. Sakral çakra blokajı varsa kendini aşırı feda etme eğilimindedir. Yunusça sevgiyi yaşadığında, bulunduğu ortamı yumuşatır ve huzur taşır.",
        "Üretmek, anlatmak, aktarmak bu kişinin yaşam amacıdır. Ancak bu üretim “onay almak için” değil, kendini gerçekleştirmek içindir.  İletişimde sınırlara dikkat edemezse dağılır, yönsüzleşir.  Meslekte prensiplere dikkat.Ne yapmak istediğini netleştirdiğinde hem kendine hem topluma değer üretir.",
        "Esneklik, olgunluk ve sabır onun hayat boyu öğrenmesi gereken kavramlardır. Kuralları kendine karşı bile katı olabilir. Bu da hayatta ilerlemesini zorlaştırır. Kendine karşı yumuşamayı öğrenmelidir. Olgunlukla buluştuğunda, ve sabrı öğrendiğinde hem kendine hem başkalarına yol gösterebilir."
        "Özgürlüğün sınırlarını bilecek",
        "Bu kişinin yaşam amacı sorumluluk üstlenmeyi öğrenmektir. Bunu öğrenemezse Kurban psikolojisine girebilir. Hem kendine hem başkalarına karşı taşıdığı görev duygusu yoğun olabilir. Ancak başkalarının yükünü sürekli sırtlanmak onu tüketir. Sorumluluktaki sınırlarını belirlediğinde toplumsal ya da ruhsal hizmet alanında büyük katkı sunar.",        
        "Hayatın anlamını sorgulamak, inançlarını test etmek ve teslimiyet geliştirmek onun ana yolculuğudur. Sürekli tatmin arar ama bunu dışarıda bulamaz. Doyumu içeride aramayı öğrenmelidir. Gerçek imanı ve içsel huzuru bulduğunda, derin bir ruhsal olgunluk taşır. Halk içinde Hakk ile olmayı başarmalı.",
        "Maddi başarı, otorite kurma ve gücü doğru yönetme onun ana temasıdır. Ama bu güç doğru niyetle yönlendirilmezse kontrolcü, aşırı hırslı ve doyumsuz bir kişiliğe dönüşebilir. Otoritesini ruhsal değerlerle birleştirirse, güçlü bir vizyoner olur.",
        "Sınır çizmeyi, kendi alanını korumayı, gerektiğinde vaz geçmeyi ve bitirebilmeyi öğrenmesi gerekir. Başkalarının ihtiyaçlarına aşırı açıldığında enerjisi tükenir. Şifa potansiyeli çok yüksek ama önce kendi yaralarını sarmalıdır. Kendi içsel düzenini kurduğunda, topluma ruhsal hizmet sunabilecek bir bilgelik geliştirir."
    ]
]

pin_kodu_yorumu_giris_cumlesi = [
    "KENDİNİ NASIL GÖRÜYOR. Bu hane, kişinin düşünce sistemini, karar alma mekanizmasını ve kendilik algısını temsil eder. Kişinin dış dünyayı nasıl algıladığı ve içsel diyaloğu burada belirginleşir. Ego, özgüven, zihinsel liderlik ve bireysel farkındalık bu alanın temel temalarıdır. Aynı zamanda hangi frekansta düşündüğü, zihinsel filtrelerinin nasıl çalıştığı da bu hanede görünür.",
    "DUYGULAR ve YAKIN İLİSKİLER. Bu hane, kişinin duygusal dünyasını, yakın ilişkilerinde sevgiyi nasıl algıladığını ve duygusal bağ kurma kapasitesini temsil eder. Sevme/sevilme ihtiyacı, duygusal bağımlılıklar, kırgınlıklar, özdeğer duygusu ve duygulara dair içgörü bu alanda belirginleşir. Aynı zamanda sakral çakrayla ilişkilidir; kişinin yaratım gücünü ve duygusal hareketliliğini gösterir.",
    "DÜNYAYA AÇILMA, HİTABET ve TİCARET. Bu hane kişinin: Kendini sözlü ya da yazılı olarak nasıl ifade ettiğini, İletişim becerilerini, Meslek seçimindeki eğilimlerini, Ve hayatla kurduğu ticari ya da duygusal alışveriş dengesini temsil eder.",
    "SEVGİ ,OLGUNLUK ve SINAV. Dördüncü hane sevgi, olgunluk ve kalbin sınavları ile doğrudan ilişkilidir. Bu hanede kişinin sevgi alma-verme biçimi, duygusal olgunluğu ve kalp merkezinden gelen tavırları ortaya çıkar.",
    "ŞÜKÜR ve DOYUM. Bu hane kişinin hayattan ne kadar tatmin olduğu, sahip olduklarıyla ne yaptığı ve içsel şükrü ne ölçüde deneyimlediğiyle ilgilidir. Aynı zamanda kişinin değer görme, sevme/sevilme biçimi ve doyum düzeyini doğrudan yansıtır.",
    "AİLE, BABA. Bu hane, kişinin aile yapısı, özellikle baba figürü ve eril otoriteyle kurduğu ilişkiyi temsil eder. Aynı zamanda sorumluluk alma becerisi, kontrol eğilimi ve aile içi rollerin nasıl deneyimlendiğini yansıtır. Sorunlar sadece babayla değil; aile içindeki dengeyle de ilgilidir.",
    "ANNE, İNANÇ. Bu hane, kişinin anneyle ilişkisini, iman boyutunu, içsel rehberlik kapasitesini ve sezgisel yönlerini yansıtır. Aynı zamanda duygusal kökler, teslimiyet, ruhsal olgunluk ve içsel bağlılık burada saklıdır. Geçmişten gelen dişil enerji aktarımı (özellikle anne ve kadın atalar) bu hanede iz bırakır.",
    "KAZANÇ ve BEREKET. Bu hane, kişinin maddi dünyayla ilişkisini, parayla kurduğu bağı, emanet ve değer üretme anlayışını, aynı zamanda aurasının ne kadar güçlü ya da sızdıran olduğunu gösterir.",
    "HAYAT AMACI. Bu hane, kişinin bu hayata ne için geldiğini, hangi tema üzerinden tamamlanacağını ve yaşam boyu yönelmesi gereken asıl amacı temsil eder. Ruhsal olarak buradaki sayı, kişinin olgunluk sınavlarını, kendisini gerçekleştirme biçimini ve kalıcı etkisini yansıtır."
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
    chakra_houses = chakra_add_name(chakra_houses, text)

    # Her çakra için bir sözlük oluştur
    chakra_data = []
    for i in range(9, 0, -1):
        # Artıları say
        plus_count_right = chakra_houses[i-1].count('+')
        plus_count_left = chakra_houses[i-1].count('-')
        # Çakra numarasını al
        number = str(i)
        # Sözlük oluştur
        chakra_data.append({
            'left_plus': ' +' * plus_count_left,  # Sol taraftaki artılar
            'number': number,               # Çakra numarası
            'right_plus': '+ ' * plus_count_right  # Sağ taraftaki artılar
        })

    return chakra_data

def chakra_add_pin_kodu(chakra_houses, k):
    sayac = [0] * 9

    # Her elemanın ilk harfine göre sayacı güncelle
    for eleman in k:
        sayac[int(eleman[0])-1] += 1

    # Chakra_houses dizisini güncelle
    for i in range(len(chakra_houses)):
        chakra_houses[i] = '-' * sayac[i] #farklılık olması lazım sağ ile solu ayırt etmesi içn

    return chakra_houses



def chakra_add_name(chakra_houses, text):
    # Metindeki her harfin sayısal karşılığını bul ve uygun haneye + ekle
    for letter in text.upper():
        if letter in chakra_values:
            index = chakra_values[letter] - 1
            chakra_houses[index] += '+'
    
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
        return str(e), None, None
    
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    # Doğum tarihini gün, ay ve yıl olarak ayır
    gun, ay, yil = dogum_tarihi.split(' ')
    
    # Ebced toplam fonksiyonunu kullanarak k değerlerini hesapla
    k = [""] * 9
    k[0] = ebced_toplama(gun)
    k[1] = ebced_toplama(ay)
    k[2] = ebced_toplama(yil)
    k[3] = ebced_toplama(k[0] , k[1] , k[2])
    k[4] = ebced_toplama(k[0] , k[3])
    k[5] = ebced_toplama(k[0] , k[1])
    k[6] = ebced_toplama(k[1] , k[2])
    k[7] = ebced_toplama(k[5] , k[6])
    k[8] = ebced_toplama(k[0] , k[1] , k[2] , k[3] , k[4] , k[5] , k[6] , k[7])
    
    # Değerleri şartlara göre güncelle
    for i in range(9):
        if int(k[i][0]) == (i + 1):
            k[i] += '!'

    # Pin kodu yorumlarını hazırla
    pin_kodu_yorumlari = []
    for i in range(9):
        yorum = f"{i+1}. Hane: {pin_kodu_yorumu_giris_cumlesi[i]}<br><br>"
        # k[i] değerinin ilk karakterini al ve int'e çevir (örn: "4!" -> 4)
        index = int(k[i][0]) - 1  # 0-based index için -1
        yorum += f"{index+1}. ile açılmış: {pin_kodu_yorumu[i][index]}"
        
        # Eğer k[i] değerinde ünlem işareti varsa, özel yorumu ekle
        if k[i].endswith('!'):
            sayi = int(k[i][0]) - 1  # 0-based index için -1
            yorum += f"<br>Dikkat etmesi lazım: {unlemli_yorumlar[sayi]}"
        
        pin_kodu_yorumlari.append(yorum)
    
    # Pin kodu görsel dizilimini hazırla    
    return  k, pin_kodu_yorumlari

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
    birthdate_without_year = gun + ay
    total_sum = 0
    for char in birthdate_without_year:
        if char.isdigit():
            total_sum += int(char)

    return ebced_toplama_asamali(total_sum)

def donusum_yillari_bulma(dogum_tarihi):
    gun, ay, yil = dogum_tarihi.split(' ')

    dogum_yili = int(yil)
    yil = dogum_yili
    yas = 0

    result = ""

    from datetime import datetime
    current_year = datetime.now().year

    donusum_rakami = ebced_toplama_asamali(ebced_toplama(current_year), ebced_toplama(gun), ebced_toplama(ay))
    result += f"Bu yıl {int(ay)}.ayın {int(gun)}.günü sonrası dönüşüm rakamı {donusum_rakami}.(Doğum gününe kadarki dönüşüm rakamı: {ebced_toplama(ebced_toplama(current_year-1), ebced_toplama(gun), ebced_toplama(ay))}) \n\n"

    while yas <= 70:
        yil_rakam_toplami = sum(map(int, str(yil)))
        yeni_yil = yil + yil_rakam_toplami
        yas = yeni_yil - dogum_yili

        donusum_rakami = ebced_toplama_asamali(ebced_toplama(yeni_yil), ebced_toplama(gun), ebced_toplama(ay))
        result += f"{yeni_yil} / {yas} yaş / dönüşüm rakamı: {donusum_rakami} \n"

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


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
        "Sizin doğum tarihiniz kök çakranızda olan blokeleri çözerek sizi hayatta dimdik tutarak başlamıştır. Siz kendinizi otoriter kendini ifade eden bir insan olarak bilirken insanlar da sizi konuşkan bir insan olarak bilirler lakin bazen sivrilebilir olduğunuzu da bilirler.\n Siz hayata başlarken liderlik etmek öne çıkmak arzusu ile başlamışsınız. Bunun için  otorite kurma, toplumda sözü geçen bir insan olma sizin için önemlidir.",
        "Sizin doğum tarihiniz size; ikili ilişkilerinizdeki sıkıntıları anlatarak başlamıştır. Bilhassa annenizin yüklerini yüklenerek onun sıkıntılarına çare bulmaya çalışarak hayata başlamışsınız.\n Siz kendinizi duygusal bir insan olarak bilirken insanlar sizi konuşkan kendini ifade eden bir kişi olarak tanırlar.",
        "Siz kendinizi konuşkan fakat kendinizi tam ifade etmediğinizi zaman zaman düşünür ve daha iyi ifade etmek için anlaşılmaya çalışmak istersiniz. Sınırlar koymanız aşırı derecede fedakarlıklar yapmamanız oldukça önemlidir. Ayrıca konuşmak üretmek sizin için oldukça önemlidir. Fakat bunun için ani şekilde sivrilmemelisiniz. Aileniz tarafından bastırılmış hissediyor iseniz lütfen çocukluğunuzu ailenizi olduğu gibi kabul edip olandaki hayrı fark edin.",
        "Sizin doğum tarihiniz ilk olarak kalp çakranızı açarak sizi sabırla sebatla olgunluk göstereceğiniz hareketlerle imtihan etmek istemiştir. Size esnek olmayı katı olmamayı öğretmiştir. Siz kendinizi kuralları olan, disiplinli otorite kurabilen bir insan olarak bilirsiniz. Sorumluluğunuzu aldığınız insanları koruyarak gözeterek her daim onların ne yaptığını takip ederek yaşarsınız. İkili ilişkilerinizde bağımlılıklar olabilir ve bu bağımlılıklarınızı ancak kendi içinizde kendinize dahi sınır koyarak çözebilirsiniz. Sizin en büyük imtihanlarınız öfkenizden ve ani acil verdiğiniz kararlarınızdan olur. Lütfen aceleci olmayın sabırla 40 kere düşüne düşüne hareket etmeye çalışın. İnsanlarla iletişim kurarken özellikle negatif enerji hissedebilirsiniz. Bu anlamda ikili ilişkilerinizde sivrilebilir ve bastırılmış olduğunuzu düşünebilirsiniz.",
        "Sizin doğum tarihiniz sizin harekete geçmenizi istemiştir. Hayata dair konfor alanlarınız var ise bunlardan kurtulup hedeflerinizin olması için desteklemiştir.",
        "Sizin doğum tarihiniz sezgilerinizi açmak, sağ beyninizi aktif etmek için desteklemektedir. Siz maneviyatla öngörülü, kimsenin düşünemeyeceğini düşünebilen, farklı halleri sezebilen bir insansınız. \n Hem sağ hem sol beyninizi aktif bir şekilde kullanmanız gerektiği için gelişime çok açık kendini yenileyebilen bir insansınız. Bu anlamda korkularınız var mı? Hayata karşı insanlara karşı aşırı derecede merhamet duyduğunuz halleriniz var mı? Bunları kontrol etmenizi tavsiye ederim.\n Buna rağmen sağ beyniniz güzel çalışır, sezgileriniz kuvvetlidir ve önsezileriniz güçlüdür. İnsanlara yardım etmeyi seversiniz. Sorumluluk almayı sorumluluklarınızı yerine getirmeyi önemsersiniz.",
        "Sizin genellikle derin arayışlarınız ve  derin düşünceleriniz olabilir. Hayatı sorgulayabilir ve niçin buradayım gibi düşünceleriniz olabilir. Bu anlamda maneviyatınızı kuvvetlendirmeli ve kendinizi keşfetmelisiniz. Yunus gibi 'Bir ben var benden içeru' sözünü iyi idrak etmeli ve egonuzu yani olumlu olumsuz özelliklerinizi çok iyi tanımalısınız.",
        "Sizin doğum tarihiniz ilk olarak auranızı temizlemeye çalışarak üzerinizde olan negatif enerjilerden kurtulmaya çalışmıştır. Siz otoriter kendini ifade eden bir insansınız.",
        "Sizin doğum tarihiniz size; öne çıkmayı, kendinizi ifade etmeyi ve öğrendiğiniz hayatta ne varsa onları öğretmeyi anlatır. Ayrıca maneviyatınızı yükselterek Yunusça Yaradan'dan ötürü yaradılanı sevmeyi anlatır. Ve insanlara şifa sunmanızı gösterir. Fakat daha önce yani insanlara şifaya vesile olmadan önce kendi nefsinizi tezkiye etmeli, kendinizi çok iyi tanımalı, olumsuz özelliklerinizi olumlularla değiştirmeli, hayatın gidişatından memnun olarak her daim şükürle yaşamayı öğrenmelisiniz. Siz kendinizi yardımsever bir kişi olarak bilirken insanlar da sizi duygusal sevgi dolu bir insan olarak görürler.",
        #11 19 22
        "Sizin doğum tarihiniz ilişkilerinizde prensip koyarak hayır demesini bilerek adeta kendini korumak için 11 enerjisi ile başlamıştır. 11 enerjisi kişide inatlık, bildiğinde ısrar, hayallere hedeflere ilerlemek gibi özellikler verir. İkili ilişkilerinizde yaşayacağınız sıkıntılar sizi  haklarınızı daha çok aramaya itmiş ve üzerinizde ciddi bir baskı hissederek kendinizi değersiz hissetmiş olabilirsiniz.\n Sıkıntılarınızı çözerken toplumda ve birlikte bulduğunuz insanlara karşı otorite kurar liderlik yaparsınız, öne çıkar kendinizi çok güzel ifade edersiniz.\n Fakat çocukluktan gelen ciddi anlamda sıkıntılarınız olduğu için kök çakranızı bloke etmiş, duygularınızı ifade edememişsiniz ve duygularınızı anlatmak size belki de çocukluk ya da eziklik gibi hissettirmiş olabilir. Çünkü oldukça baskın, ne yapmak istediğini bilen bir karakteriniz olduğu kesindir.",
        "Sizin doğum tarihiniz ilk olarak 19 enerjisi ile başlayarak hayatta hem öne çıkmayı liderlik yapmayı hem de bunun için ciddi imtihanlardan geçmeyi anlatır.\n Bu 19 sayısı kişide imtihan ile dönüşmeyi anlatır. Sıkıntıları fark edip olayın altındaki mesajları çözmenizi anlatır. Enerjinizi fark edin. Olaylardan ders çıkarıp, iyileşmeye niyet edin ve daha sonra yaralı bir şifalı gibi insanlığın hayrına çalışın!..\n Fakat daha önce yani insanlara şifa vermeden önce kendi nefsimizi tezkiye etmeli, kendimizi çok iyi tanımalı, olumsuz özelliklerimizi olumlularla değiştirmeli, hayatın gidişatından memnun olarak her daim şükürle yaşamayı öğrenmeliyiz.",
        "Sizin doğum tarihiniz ilk olarak 22 enerjisi ile hayata başlatarak sizi sabırla sebatla olgunluk göstereceğiniz hareketlerle imtihan etmek istemiştir. Size esnek olmayı katı olmamayı öğretmiştir. İnsanlar sizi öne çıkan, lider karakterli bir insan olarak algılarken, siz kendinizi kuralları olan, disiplinli, otorite kurabilen bir insan olarak bilirsiniz. Siz evrensel esnek sabırlı sebatlı bir kişisiniz. Sorumluluğunuzu aldığınız insanları koruyarak gözeterek her daim onların ne yaptığını takip ederek yaşarsınız. Sizin en büyük imtihanlarınız öfkenizden ve ani acil verdiğiniz kararlarınızdan olur. Lütfen aceleci olmayın sabırla 40 kere düşüne düşüne hareket etmeye çalışın. İnsanlarla iletişim kurarken özellikle negatif enerji hissedebilirsiniz. Bu anlamda ikili ilişkilerinizde sivrilebilir ve bastırılmış olduğunuzu düşünebilirsiniz."
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
        "Sizin dünyaya açılma haliniz kök çakranızla olduğu için öne çıkar, otorite kurmak ister ve liderlik yapmak istersiniz. Bununla birlikte çocuklukta yaşadığınız travmalarınız varsa mutlaka çalışmalı kendinizi, çocukluğunuzu yaşanan sıkıntıları sevgiyle kabule geçmelisiniz.",
        "Sizin dünyaya açılış şekliniz yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidir fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir.",
        "Sizin dünyaya açılma şekliniz konuşarak kendinizi ifade ederek olacağı için üzerinizdeki baskıyı fark edip, kökenlerden gelen duygularınızı ifade etmediğiniz hangi olaylar varsa bunları çözmelisiniz. Bunlar çözülmediği müddetçe 3. çakranız size ciddi anlamda sıkıntılar yaşatabilir, bastırılmış hissettirebilir ve mide diyabet gibi gastrointestinal sistem hastalıklarına sebep olabilir.",
        "Sizin dünyaya açılış şekliniz kalp çakranızla olduğu için ciddi imtihanlar, manevi krizler ve arkadaşlarınızla ilişkilerinizde ortada kalma gibi durumlar yaşayabilirsiniz. Bu yüzden aşırı derecede sevmek aşırı derecede ilgi göstermek ilişkilerinizde sıkıntıya neden olabilir. Kalbin sahibi Allah'tır ve en büyük sevgi ilk olarak ona olmalıdır. Bu yüzden başkalarına aşırı derecede sevgi, değer verdikçe kendimizi daha değersizleştirir ve imtihanlara düçar oluruz.",
        "Sizin dünyaya açılma prensibiniz; hayatta  keşfederek olmuştur. Fakat ikili ilişkilerinizdeki sıkıntılar ve fedakarlıklar yapmanız buna mani olmuştur. Bütün dersinizi bütün imtihanınızı burayla alakalı verdiğiniz için ilişkilerde kendinizi suçlamışsınızdır. Bu da sizi yormuş ve frekansınızı düşürerek depresyonvari olaylar yaşamanıza neden olmuştur.",
        "Sizin dünyaya açılma haliniz 6.çakranızla olduğu için ebeveynliği çok önemser, sorumluluk alacağınız işlerde çokça bulunursunuz. Çevrenizdeki kişilere karşı aşırı derecede korumacılık yapabilirsiniz",
        "Sizin dünyaya açılma prensibiniz 7. çakranızla olduğu için arayışlarınız olur. İlişkilerinizde doymayı bilmeyebilirsiniz. Her daim yetinmediğiniz için herkes benimle ilgilensin, beni sürekli sevdiğini söylesin, ilgi göstersin gibi bir yaklaşımda bulunabilirsiniz. Bunları düzeltip kronik şikayetçi bir haliniz varsa bunlardan uzaklaşarak Şükür içinde yaşayıp kanaat etmeyi öğrenmelisiniz. Her daim kendi istediğinizin olmasını isterseniz, zamanla ilişkilerinizde doyumsuzluk meydana gelir ve kronik şikayetçi haline gelirsiniz. Bilhassa yaşınız ilerledikçe arayışlarınız artar ve işinizde, beraber kurduğunuz ilişkilerinizde asla mutlu olmazsınız. Hep mutluluğu ararsınız. Hayat, yaşadığınız çevre, işiniz sizi tatmin etmemeye başlar. Ne kadar mükemmel olursa da size yetmez. İşte bunun en büyük sebebi egomuzdur. Yani kendimiz... Nefsi emaremizdir. Nefsi emare yalnızca heva ve heveslerinin peşinde koşar. Her zaman mutlu olup şımarmak ister. Bunu yaptıkça aşırı derecede hastalıklarımız, içimizdeki boşluk artar. Depresyona gireriz. Hayattan tat almayız. Bu yüzden elimizdeki ile yetinmeyi ve mutlu olmayı şükretmeyi unutmamalıyız.",
        "Sizin dünyaya açılma haliniz insanlar üzerinde bir otorite kurarak liderlik yaparak olacağı için kendinizi çok iyi tanımalı auranızı korumalı nazar negatif enerji negatif insanlardan ve ortamdan uzak durmalısınız. Ayrıca haram olan her şeyden uzak kalmalı mümkün mertebe rızkınızın helal olmasına çokça dikkat etmelisiniz.  Ayetel Kürsi suresini ağzınızdan düşürmemelisiniz.",
        "Sizin dünyaya açılma şekliniz insanlara hizmet ederek onların şifası için çalışarak olacaktır. Fakat bunun için önce kendinizi iyileştirmeli, maneviyatınızı kuvvetlendirmelisiniz. Ayrıca 40 kere düşünüp bir kere hareket etmeli, her şeye hemen inanmamalısınız.",
        #11 19 22
        "Duygularınızı ifade etmediğiniz takdirde; içinize bastırdığınızda ve biriktirdiğinizde ciddi bir patlama ile bunu dışarıya doğru duyurabilirsiniz. İnsanlar neden, niçin olduğunu anlamayabilir ve siz çok haklı sebeplerle ikili ilişkilerinizde anlaşılmadığınızı düşünerek büyük tepkiler verebilirsiniz.",
        "Ve sizin dünyaya açılma haliniz 19 enerjisi ile olduğu için imtihanlar sizi dönüştürür, manevi anlamda eğitir ve nefs tezkiyesi yaptırır.\n Bu 19 sayısı kişide imtihan ile dönüşmeyi anlatır. Sıkıntıları fark edip olayın altındaki mesajları çözmenizi anlatır. Enerjinizi fark edin. Olaylardan ders çıkarıp, iyileşmeye niyet edin ve daha sonra yaralı bir şifalı gibi insanlığın hayrına çalışın!..",
        "Sizin dünyaya açılış şekliniz 22 sayısı ile olduğu için ciddi sıkıntılar yaşamış olma ihtimaliniz yüksektir. Bunlar elbette sizin kalp çakranızı açmak, imanınızı kuvvetlendirmek, maneviyatınızı arttırmak için başınıza gelmiştir. Ama elbette imtihanlardan mesaj almayı bilip kendinizi düzeltip hayatı olanı olduğu gibi kabul ederseniz sizin makamınız daha da yükselir."
    ],
    [  # 4. hane - SEVGİ, OLGUNLUK
        "Sıkıntıları aşma şekliniz kök çakranızla olurken her zaman öne çıkmak, kendinizi ifade etmek, düşüncelerinizi anlatmak istersiniz. Bir ortamda dinlenilmek ve saygı görmek en çok istediğiniz şeydir. Bunun için çocuklukta yaşadığınız travmalarınız varsa bunları iyileştirmeli anne baba ile alakalı kabul etmediğiniz haller varsa bunları kabul ederek iyileşmenizi hızlandırmalısınız.",
        "Sizin sıkıntıları aşma şekliniz yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidir. Fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir.",
        "Sizin sıkıntıları aşma şekliniz konuşarak kendinizi ifade ederek olacağı için üzerinizdeki baskıyı fark edip kökenlerden gelen duygularınızı ifade etmediğiniz hangi olaylar varsa bunları çözmelisiniz. Bunlar çözülmediği müddetçe 3. çakranız size ciddi anlamda sıkıntılar yaşatabilir, bastırılmış hissettirebilir ve mide diyabet gibi gastrointestinal sistem hastalıklarına sebep olabilir.",
        "Sizin sıkıntıları aşma şekliniz kurallarınıza, hayattaki sınırlara çok iyi bağlanarak olacaktır. Bunu öğrenmek için öncelikle kendinizi tanıyacaksınız. Bu hayatta var olmak isteyeceksiniz. Böylelikle kalp çakranızı açmaya çalışacaksınız. Kalp çakranızı açmadığınız her daim sizin için sıkıntılar, yanlış insanlar, aşırı derecede yapılan fedakarlıklar ve sürekli kendinizi değersiz hissetmek gündemde olacaktır. Dolayısıyla mutlaka sınırlarınızın olması, hayır demeyi öğrenmeniz sizin için oldukça gereklidir.",
        "Sıkıntıları da aşma şekliniz yeniliklerle her gün yeni bir şey öğrenerek konfor alanınızdan çıkarak olacağı için ek olarak yaptığınız hatalardan, verdiğiniz tavizlerden dolayı, kendinizi suçlamamayı öğrenmeniz gerekir. Eğer tiroid hastalığınız varsa ya da bununla alakalı hiçbir şekilde test yaptırmadıysanız, mutlaka bir tiroid tahlil testi öneririm. Çünkü sizin tiroidlerde tıkanıklık olabilir.",
        "Sizin için bu dünyada sorumluluk alarak yapacağınız işler, insanlara yardım edeceğiniz hatta şifa meslekleri oldukça iyi olur. Sağlık personeli ya da insanları koruyup gözeteceğiniz işler yapmak sizin için harika bir seçim olur. Bununla alakalı olarak mutlaka çalışın. Gönüle iyi gelen, insanları ferahlatan ve iyi eden her meslek sizin için çok büyük kapılar açar ve sizin iyileşmenize faydası olur.",
        "Siz zeki bir insansınız. Bu yüzden ilişkilerde olan sıkıntıları gidermek için size verilmekte olan mesajı anlayın. Mesajlar alındıkça aynı olaylar tekrar tekrar gelmez. Bu yüzden derin düşünüp tefekkür etmelisiniz.",
        "Sizin sıkıntıları aşma şekliniz haliniz insanlar üzerinde bir otorite kurarak liderlik yaparak olacağı için kendinizi çok iyi tanımalı, auranızı korumalı nazar, negatif enerji, negatif insanlardan ve ortamdan uzak durmalısınız. Ayrıca haram olan her şeyden uzak kalmalı, mümkün mertebe rızkınızın helal olmasına çokça dikkat etmelisiniz. Ayetel Kürsi suresini ağzınızdan düşürmemelisiniz.",
        "Sizin sıkıntıları aşma şekliniz 9. çakranızda olacaktır. Bu yüzden insanlara yardım etmeli, mutlaka elinizde avucunuzda olan her şeyi paylaşmaya çalışmalısınız. Ayrıca sınırlarınızı korumalı, gerektiğinde mutlaka hayır demeyi bilmelisiniz. Bunun yanında şifa meslekleri ile ilgilenmeniz sizin için güzel olur.",
        #11 19 22
        "İlişkilerinizde prensip koyarak, hayır demesini bilerek kendinizi korumalısınız. Sizin sıkıntıları aşma şekliniz 11 enerjisi ile olur. 11 enerjisi kişide inatlık, bildiğinde ısrar, hayallere hedeflere ilerlemek gibi özellikler verir. Kalp çakranızın gelişmemesi nedeniyle ikili ilişkilerinizde yaşayacağınız sıkıntılar, sizi kendi haklarınızı daha çok aramaya itmiştir ve üzerinizde ciddi bir baskı hissederek kendinizi değersiz hissetmiş olabilirsiniz.",
        "Sizin sıkıntıları aşma şekliniz 19 enerjisiyle olur. Bu 19 sayısı kişide imtihan ile dönüşmeyi anlatır. Sıkıntıları fark edip olayın altındaki mesajları çözmenizi anlatır. Enerjinizi fark edin. Olaylardan ders çıkarıp, iyileşmeye niyet edin ve daha sonra yaralı bir şifalı gibi insanlığın hayrına çalışın!...",
        "Sizin sıkıntıları aşma şekliniz 22 sayısı ile olduğu için kurallarınız vardır. Sınırlar koymayı hayır demeyi bilirsiniz."
    ],
    [  # 5. hane - ŞÜKÜR VE DOYUM
        "Yaşadığınız her neyse küçükken; ilk olarak annenizi babanızı ya da sizi yetiştirenleri olduğu gibi kabul etmekle başlayın!. Bunları kabul etmedikçe ilişkilerinizde sürekli sıkıntılar yaşarsınız. Çünkü bilinçaltı böyle çalışır. Kökenlerde bastırdığı sorunları diğer ilişkilerde ortaya çıkararak iyileştirmeye çalışır. Amacı sahibine mesaj vermektir. Fakat bu mesajı alamayanlar için ilişkileri hep sorunludur. Kendini ifade edemediğini düşünür. Yani kısaca imtihanlar insana olgunlaşmayı öğretmek için çaba harcar. İnsan küçükken yaşadığı olaylar bilinçaltında birikir ve daha sonra ilişkilerinde ortaya çıkar. Bilinçaltı bunu sahibini iyileştirmek için yapar fakat bu ona ciddi yanlış ilişkilere sebep olur. Bu yüzden bilinçaltımızla yaşamamamız gerekir. İşte sizde köklerdeki sizi yetiştirenlerle aranızdaki problemi çözmek için zaman zaman bilinçaltınız devreye giriyor ve o problemler yeniden açığa çıkıyor ve ilişkilerinizde sivrilebiliyorsunuz. Bu yüzden daha güzel konuşmaya, kendinizi daha iyi ifade etmeye çalışın. Aşırı derecede bağlanmayın. Mümkün mertebe sağ duyulu davranın, öngörülü olun ve bilinçaltı ile ilgili okumalar yapın.",
        "Siz sevmeyi, sevilmeyi, ilişkilerde duygularınızı doğru kullanmayı öğrenmelisiniz. Çocuklukta oyun kurduğunuzda ve ebeveynlerle ilişkilerde yaşadığınız problemleri fark etmelisiniz. Olanı olduğu gibi kabul edip anda duygularınızı ifade etmeye çalışmalısınız.",
        "Sizin çocukluktan itibaren ciddi anlamda bastırılmış olduğunuzu ifade etmeliyim. Özellikle sessiz, çekingen bir haliniz olabilir, kökenlerde yaşadığınız sorunları öğrenin, kendinizi ifade etmeye çalışın. Böylelikle kendinizi ifade ettikçe sindirim sistemi sorunlarınız da ortadan kalkar.",
        "Öfkenizi kontrol etmek anlamında ciddi şekilde çalışma yapmanız gerekir. Bunun yanında insanlara çabuk güvenmemeli verici olmamalısınız. Kalbinizle düşünüp daha tedbirli daha akıllıca hareket etmelisiniz eğer böyle olmazsa kandırılabilir ve çabucak insanlara inandığınız için aldatılabilirsiniz.",
        "Bağlandığınız insana aşırı derecede bağlanabilir, bunu tiryakilik seviyesine getirerek belli şeylere bu seviyede bağlanabilirsiniz. Bunun nedeni kökenden gelen sorunları ilişkilerimizde tekrar tekrar görmekten olur. Ve aynı şeylerin döngülerinde olabilirsiniz.",
        "Siz imanınızı mutlaka artırmalı, maneviyatınızı kuvvetlendirmelisiniz.  Eğer babanızla sorunlar varsa olduğu gibi kabul etmelisiniz. Ailenizde ciddi problemler varsa bunlarla yüzleşerek sevgiyle kabule geçmelisiniz.",
        "Bağlandığınız insana aşırı derecede bağlanabilir, bunu tiryakilik seviyesine getirerek belli şeylere bu seviyede bağlanabilirsiniz. Bunun nedeni kökenden gelen sorunları ilişkilerimizde tekrar tekrar görmekten olur. Ve aynı şeylerin döngülerinde olabilirsiniz. \n 7.çakranızda olan blokeler akletmemenize, olayların içinde yatan mesajları çözememenize neden olabilir. Bu yüzden farkındalıkla yaşamanızı, her olaydan önce 40 kere düşünüp bir kere hareket etmenizi tavsiye ederim.",
        "Ciddi bir anlamda aura probleminiz var ve buna çalışmak zorunda olduğunuzu doğum tarihiniz bize söylüyor. Öncelikle 8. çakradaki yazdıklarımı önemseyin ve mutlak surette yardımlaşmaya, elinizdeki avucunuzdaki ne varsa paylaşmaya özen gösterin. Bununla beraber önce kendinize daha sonra etrafınızda olan herkese karşı sınır koymasını bilin, kendi değerinizi bilerek ölçülü hareket edin, ani ve hızlı kararlar vermeyin.",
        "İlişkilerinizde gerektiğinde hayır demeyi bilmenizi, beklentili yaşamaya son vermenizi, sevginizi değer verdiğiniz kişilere göstermenizi, duyguları içinizde yaşamamanızı ve seviyorsanız sevdiğinizi sevmiyorsanız sevmediğinizi yani duygunuz neyse bunu ifade etmenizi size tavsiye ederim. Çünkü yaşadığımız duygular içimizde kaldıkça bir bomba etkisindedir ve her an aşırı derecede patlayabilir. Bu da ilişkilerinize zarar verir. Ve sınırlar koymayı unutmamalı, kendinizi hissettiklerinizi anlatmalısınız.",
        #11 erkekler  11 kadınlar için
        "Sizin doğum tarihiniz ciddi anlamda ilişkilerinizde sıkıntıları göstermekle beraber, annenizin ciddi travmaları ya da ailenizdeki dişilerin ciddi travmalarını siz barındırmaktasınız. Bunun için öncelikle ailenizi öğrenmeli, annenizin, anneannenizin, teyzenizin hatta babaannenizin dahi hayatını bilip ona göre onları anımsamalı, onları güzel bir şekilde anmalı ve kendi hayatınıza daha çok dikkat etmelisiniz. Çünkü bu travmalar sizde yansımış olabilir ve bu yansımalar sonucunda hak edilmişlikler kalabilir. Bunu ancak sadaka, kurban yoluyla çözmeye çalışır ve sakral çakranızı iyileştirirsiniz. Özellikle duygusal krizleriniz varsa bunların kök sebeplerine inerek çözmeye çalışmalı, mutlaka fark ederek duygu boşaltım teknikleriyle iyileşmeye çalışmalısınız.",
        "Sizin doğum tarihiniz ciddi anlamda ilişkilerinizde sıkıntıları göstermekle beraber, annenizin ciddi travmaları ya da ailenizdeki dişilerin ciddi travmalarını siz barındırmaktasınız. Bunun için öncelikle ailenizi öğrenmeli, annenizin, anneannenizin, teyzenizin hatta babaannenizin dahi hayatını bilip ona göre onları anımsamalı, onları güzel bir şekilde anmalı ve kendi hayatınıza daha çok dikkat etmelisiniz. Çünkü bu travmalar sizde yansımış olabilir ve bu yansımalar sonucunda hak edilmişlikler kalabilir. Bunu ancak sadaka, kurban yoluyla çözmeye çalışır ve sakral çakranızı iyileştirirsiniz. Özellikle kadın hastalıklarınız varsa bunların kök sebeplerine inerek çözmeye çalışmalı, mutlaka fark ederek duygu boşaltım teknikleriyle iyileşmeye çalışmalısınız."
    ],
    [  # 6. hane - AİLE, BABA
        "İlişkilerde otorite kurmayı sever kendi sözünüzün dinlenilmesini istersiniz.",
        "Sizin ilişki kurma şekliniz yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidir fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir.",
        "Siz kendinizi konuşkan görürken zaman zaman da kendinizi tam ifade etmediğinizi düşünür ve daha iyi ifade etmek için anlaşılmaya çalışmak istersiniz. Sınırlar koymanız, aşırı derecede fedakarlıklar yapmamanız oldukça önemlidir. Ayrıca konuşmak, üretmek sizin için oldukça önemlidir. Fakat bunun için ani şekilde sivrilmemelisiniz. Aileniz tarafından bastırılmış hissediyor iseniz lütfen çocukluğunuzu, ailenizi olduğu gibi kabul edip olandaki hayrı fark edin.",
        "Sizin ilişki kurma şekliniz  kurallarınıza, hayattaki sınırlara çok iyi bağlanarak olacaktır. Bunu öğrenmek için öncelikle kendinizi tanıyacaksınız. Bu hayatta var olmak isteyeceksiniz. Böylelikle kalp çakranızı açmaya çalışacaksınız. Kalp çakranızı açmadığınız her daim sizin için sıkıntılar, yanlış insanlar, aşırı derecede yapılan fedakarlıklar ve sürekli kendinizi değersiz hissetmek gündemde olacaktır. Dolayısıyla mutlaka sınırlarınızın olması ve hayır demeyi öğrenmeniz sizin için oldukça gereklidir.",
        "En büyük imtihanınız ikili ilişkilerinizde yaşadığınız sorunlar ile düşen frekansınızdır. Negatif enerji ile moraliniz alt üst olur. Bunun en büyük nedeni annenizle olan ilişkileriniz, kökenlerde yatan sizi yetiştirenlerle yaşadığınız sorunlardan kaynaklanır. Hayata tutunamayışınız ve duygularınızı ifade edemeyişiniz içinize duygularınızı bastırmanızdır.",
        "İlişkilerde insanlara korumacı davranır, onlara ebeveynlik yapmak istersiniz.",
        "İlişki kurma şekliniz 7.çakranızla olduğu için ve 7.çakranız tıkanık olduğu için ilişkilerde aradığınızı bulamayabilirsiniz",
        "İlişkilerde otorite kurmayı sever kendi sözünüzün dinlenilmesini istersiniz.",
        "İlişkilerinizde gerektiğinde hayır demeyi bilmenizi, beklentili yaşamaya son vermenizi, sevginizi değer verdiğiniz kişilere göstermenizi, duyguları içinizde yaşamamanızı ve seviyorsanız sevdiğinizi sevmiyorsanız sevmediğinizi yani duygunuz neyse bunu ifade etmenizi size tavsiye ederim. Çünkü yaşadığımız duygular içimizde kaldıkça bir bomba etkisindedir ve her an aşırı derecede patlayabilir. Bu da ilişkilerinize zarar verir. Ve sınırlar koymayı unutmamalı, kendinizi hissettiklerinizi anlatmalısınız.",
        # 11
        "İlişkilerinizde prensip koyarak, hayır demesini bilerek kendinizi korumalısınız. Sizin sıkıntıları aşma şekliniz 11 enerjisi ile olur. 11 enerjisi kişide inatlık, bildiğinde ısrar, hayallere hedeflere ilerlemek gibi özellikler verir. Kalp çakranızın gelişmemesi nedeniyle ikili ilişkilerinizde yaşayacağınız sıkıntılar, sizi kendi haklarınızı daha çok aramaya itmiştir ve üzerinizde ciddi bir baskı hissederek kendinizi değersiz hissetmiş olabilirsiniz."
    ],
    [  # 7. hane - ANNE, İMAN
        "Yaşadığınız her neyse küçükken; ilk olarak annenizi, babanızı ya da sizi yetiştirenleri olduğu gibi kabul etmekle başlayın!. Bunları kabul etmedikçe ilişkilerinizde sürekli sıkıntılar yaşarsınız. Çünkü bilinçaltı böyle çalışır. Kökenlerde bastırdığı sorunları diğer ilişkilerde ortaya çıkararak iyileştirmeye çalışır. Amacı sahibine mesaj vermektir. Fakat bu mesajı alamayanlar için ilişkileri hep sorunludur. Kendini ifade edemediğini düşünür. Yani kısaca imtihanlar insana olgunlaşmayı öğretmek için çaba harcar. İnsan küçükken yaşadığı olaylar bilinçaltında birikir ve daha sonra ilişkilerinde ortaya çıkar. Bilinçaltı bunu sahibini iyileştirmek için yapar fakat bu ona ciddi yanlış ilişkilere sebep olur. Bu yüzden bilinçaltımızla yaşamamamız gerekir. İşte sizde köklerdeki sizi yetiştirenlerle aranızdaki problemi çözmek için zaman zaman bilinçaltınız devreye giriyor ve o problemler yeniden açığa çıkıyor ve ilişkilerinizde sivrilebiliyorsunuz. Bu yüzden daha güzel konuşmaya, kendinizi daha iyi ifade etmeye çalışın. Aşırı derecede bağlanmayın. Mümkün mertebe sağ duyulu davranın, öngörülü olun ve bilinçaltı ile ilgili okumalar yapın.",
        "Siz sevmeyi, sevilmeyi, ilişkilerde duygularınızı doğru kullanmayı öğrenmelisiniz. Çocuklukta oyun kurduğunuzda ve ebeveynlerle ilişkilerde yaşadığınız problemleri fark etmelisiniz. Olanı olduğu gibi kabul edip anda duygularınızı ifade etmeye çalışmalısınız.",
        "Sizin çocukluktan itibaren ciddi anlamda bastırılmış olduğunuzu ifade etmeliyim. Özellikle sessiz, çekingen bir haliniz olabilir. Kökenlerde yaşadığınız sorunları öğrenin, kendinizi ifade etmeye çalışın. Böylelikle kendinizi ifade ettikçe sindirim sistemi sorunlarınız da ortadan kalkar.",
        "Kalp Allah'ın makamıdır. Eğer bu makamı olur olmaz aşklar ilişkilerle mahveder, kendi değerimizi bilmez, kendimizi sevmezsek işte o zaman imtihan olarak geri döner. Bu yüzden sizde 4-7 ilişkisi vardır ki taklit iman tahkiki imana geçmesi elzemdir. İmanınızı maneviyatınızı kuvvetlendirin!... Allah'la olan irtibatınızı artırmanız sizi daha iyi eder.",
        "Sizin olgunluğu bulmanız keşfederek olmuştur. Fakat ikili ilişkilerinizdeki sıkıntılar ve fedakarlıklar yapmanız buna mani olmuştur. Bütün dersinizi bütün imtihanınızı burayla alakalı verdiğiniz için kendinizi suçlamışsınızdır. Bu da sizi yormuş ve frekansınızı düşürerek depresyonvari olaylar yaşamanıza neden olmuştur. Huzura geçme haliniz yeniliklerle, her gün yeni bir şey öğrenerek, konfor alanınızdan çıkarak olacağı için ek olarak yaptığınız hatalardan verdiğiniz tavizlerden dolayı kendinizi suçlamamayı öğrenmeniz gerekir. Eğer tiroid hastalığınız varsa ya da bununla alakalı hiçbir şekilde test yaptırmadıysanız, mutlaka bir tiroid tahlil testi öneririm. Çünkü sizin tiroidlerde tıkanıklık olabilir.",
        "Bununla birlikte babanızla ve hayatınızdaki erillerle olan iletişiminizi kuvvetlendirmeli, aranızda olan problemleri mutlaka gidermeli bu konuda  iletişime geçmeli ve onlardan alamadığınız destek vesaire ne varsa bunu ifade etmelisiniz.",
        "Taç çakranızın bloke olması sizi karamsar bir yapıda tutmuş ve bu karamsarlıklar arayışlar içinde yaşamanıza neden olmuştur. Bilhassa aileniz tarafından destek alamamış gibi hissederek olaylardan dolayı hep kendinizi suçlamışsınız.",
        "Ciddi bir anlamda aura probleminiz var ve buna çalışmak zorunda olduğunuzu doğum tarihiniz bize söylüyor. Öncelikle 8. çakradaki yazdıklarımı önemseyin ve mutlak surette yardımlaşmaya elinizdeki avucunuzdaki ne varsa paylaşmaya özen gösterin. Bununla beraber önce kendinize daha sonra etrafınızda olan herkese karşı sınır koymasını bilin, kendi değerinizi bilerek ölçülü hareket edin, ani ve hızlı kararlar vermeyin.",
        "İlişkilerinizde gerektiğinde hayır demeyi bilmenizi, beklentili yaşamaya son vermenizi, sevginizi değer verdiğiniz kişilere göstermenizi, duyguları içinizde yaşamamanızı ve seviyorsanız sevdiğinizi sevmiyorsanız sevmediğinizi yani duygunuz neyse bunu ifade etmenizi size tavsiye ederim. Çünkü yaşadığımız duygular içimizde kaldıkça bir bomba etkisindedir ve her an aşırı derecede patlayabilir. Bu da ilişkilerinize zarar verir. Ve sınırlar koymayı unutmamalı, kendinizi hissettiklerinizi anlatmalısınız.",
        #11 ERKEKLER  11 Kadınlar
        "Sizin doğum tarihiniz ciddi anlamda ilişkilerinizde sıkıntıları göstermekle beraber, annenizin ciddi travmaları ya da ailenizdeki dişilerin ciddi travmalarını siz barındırmaktasınız. Bunun için öncelikle ailenizi öğrenmeli, annenizin, anneannenizin, teyzenizin hatta babaannenizin dahi hayatını bilip ona göre onları anımsamalı, onları güzel bir şekilde anmalı ve kendi hayatınıza daha çok dikkat etmelisiniz. Çünkü bu travmalar sizde yansımış olabilir ve bu yansımalar sonucunda hak edilmişlikler kalabilir. Bunu ancak sadaka, kurban yoluyla çözmeye çalışır ve sakral çakranızı iyileştirirsiniz. Özellikle duygusal krizleriniz varsa bunların kök sebeplerine inerek çözmeye çalışmalı, mutlaka fark ederek duygu boşaltım teknikleriyle iyileşmeye çalışmalısınız.",
        "Sizin doğum tarihiniz ciddi anlamda ilişkilerinizde sıkıntıları göstermekle beraber, annenizin ciddi travmaları ya da ailenizdeki dişilerin ciddi travmalarını siz barındırmaktasınız. Bunun için öncelikle ailenizi öğrenmeli, annenizin, anneannenizin, teyzenizin hatta babaannenizin dahi hayatını bilip ona göre onları anımsamalı, onları güzel bir şekilde anmalı ve kendi hayatınıza daha çok dikkat etmelisiniz. Çünkü bu travmalar sizde yansımış olabilir ve bu yansımalar sonucunda hak edilmişlikler kalabilir. Bunu ancak sadaka, kurban yoluyla çözmeye çalışır ve sakral çakranızı iyileştirirsiniz. Özellikle kadın hastalıklarınız varsa bunların kök sebeplerine inerek çözmeye çalışmalı, mutlaka fark ederek duygu boşaltım teknikleriyle iyileşmeye çalışmalısınız."
    ],
    [  # 8. hane - KAZANÇ VE BEREKET
        "Sizin aura açma haliniz kök çakranızla olduğu için öne çıkar, otorite kurmak ister ve liderlik yapmak istersiniz. Bununla birlikte çocuklukta yaşadığınız travmalarınız varsa mutlaka çalışmalı kendinizi, çocukluğunuzu, yaşanan sıkıntıları sevgiyle kabule geçmelisiniz.",
        "Sizin aura açma şekliniz yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidir fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir.",
        "Siz kendinizi konuşkan görürken zaman zaman da kendinizi tam ifade etmediğinizi düşünür ve daha iyi ifade etmek için anlaşılmaya çalışmak istersiniz. Sınırlar koymanız, aşırı derecede fedakarlıklar yapmamanız oldukça önemlidir. Ayrıca konuşmak, üretmek sizin için oldukça önemlidir. Fakat bunun için ani şekilde sivrilmemelisiniz. Aileniz tarafından bastırılmış hissediyor iseniz lütfen çocukluğunuzu, ailenizi olduğu gibi kabul edip olandaki hayrı fark edin.",
        "Sizin hedefiniz kalp çakranızı açmak olduğu için daima namazla dua ile ALLAH'ımızdan yardım istemeli maneviyatınızı yükseltmelisiniz.",
        "Auranızı açma şekliniz yine yeniliklerle her gün yeni bir şey öğrenerek, konfor alanınızdan çıkarak olacağı için ek olarak yaptığınız hatalardan, verdiğiniz tavizlerden dolayı kendinizi suçlamamayı öğrenmeniz gerekir. Gezin dolaşın. Yeni yerler görün. Bağımlılıklardan kurtulup kendi merkezinize dönün.",
        "Sizin için bu dünyada sorumluluk alarak yapacağınız işler, insanlara yardım edeceğiniz hatta şifa meslekleri oldukça iyi olur. Sağlık personeli ya da insanları koruyup gözeteceğiniz işler yapmak sizin için harika bir seçim olur. Bununla alakalı olarak mutlaka çalışın. Gönüle iyi gelen, insanları ferahlatan ve iyi eden her meslek sizin için çok büyük kapılar açar ve sizin iyileşmenize faydası olur.",
        "Auranızı 7.çakranızla açtığınız için maneviyatınızı kuvvetlendirmeli, tahkiki imana ermeli ve nefsinizi tezkiye etmelisiniz. Ayrıca hayatınızı tefekkür etmeli, derin düşünüp analitik etmelisiniz.",
        "İlk olarak sizin dünyaya açılma şekliniz; kendinizi tanıtmak, otorite kurmak ve ticaret gibi işler yaparak olur. Sizin için insanlar arasında lider olmak, fikirlerini ifade etmek oldukça önemlidir. Bu yüzden kendinize güvenin önce auranızı koruyun ve bununla alakalı olarak öne çıkacağınız liderlik yapacağınız işler yapın!... Bunlardan asla geri durmayın. Elbette bunlar için ilk olarak kök çakranızı çok iyi korumanız gerekir. Daha sonra ise auranızı korumak gerekir ki bununla alakalı 8. çakrada dediklerimi mutlaka hayata geçirmeniz gerekir.",
        "Sizin için bu dünyada sorumluluk alarak yapacağınız işler, insanlara yardım edeceğiniz hatta şifa meslekleri oldukça iyi olur. Sağlık personeli ya da insanları koruyup gözeteceğiniz işler yapmak sizin için harika bir seçim olur. Bununla alakalı olarak mutlaka çalışın. Gönüle iyi gelen, insanları ferahlatan ve iyi eden her meslek sizin için çok büyük kapılar açar ve sizin iyileşmenize faydası olur.",
        #11
        "Duygularınızı ifade etmediğiniz  ve biriktirdiğinizde ciddi bir patlama ile bunu dışarıya doğru yansıtabilirsiniz. İnsanlar neden, niçin olduğunu anlamayabilir. Bu yüzden siz çok haklı sebeplerle ikili ilişkilerinizde anlaşılmadığınızı düşünerek büyük tepkiler verebilirsiniz."        
    ],
    [  # 9. hane - HAYAT AMACI
        "Siz bu karanlıklardan aydınlığı bulmayı ilk olarak kendinize otorite koyarak, olumsuz özelliklerinizi fark ederek ve onları olumluya dönüştürerek aşarsınız. Bunun yanında insanları adaletle yöneterek aşarsınız. Fakat bunu aşırı derecede bencillik haline getirirseniz, herkes benim dediğimi yapsın derseniz, bu sefer kök çakranız bloke olur ve böylelikle hayata tutunamaz hale gelirsiniz. İnsanlara karşı direktif vererek, emir vererek benim dediğim olsun diyerek ilişkilerinizde EGO savaşları yaşarsınız. Bu anlamda daha dikkatli olmalısınız ve en önemlisi imanınızı kuvvetlendirmeli tahkiki imanınızı artırmalısınız. İlişkilerinizde arayışlarınız neden bunları düşünmelisiniz. Doymak bilmeyen nefis ancak nefsi emareden gelir. Kötülüğü emredici nefis terbiye edilmeli, böylelikle kalp çakranızı koruyup kalbi gerçek sahibine vermelisiniz.",
        "Sizin hayat amacınız yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidirı fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir.",
        "Kendiniz olmayı, kendinizi fark etmeyi, tanımayı, kendini bilen Rabbini bilir hitabınca kendinizi nasıl terbiye edip nasıl düzelteceğinizi anlatmayı hedefler. Kendini tanımak ne demek bunu bilmelisiniz. Kendini tanımak demek nefsimizi tezkiye etmek, olumsuz yönlerimizi ayıklamak demektir. Ve üslubunuzu düzelterek tatlı dille konuşmayı, kendinizi güzel ifade etmeyi öğrenmelisiniz. Bunun yanında kalbinizi açıp, sıkıntılarınızı, özellikle ikili ilişkilerinizi, imtihanlarınızı önceden fark etmeli ve önlem almalısınız. Bunun için her zaman öngörülü olmalı, öngörülerinizi geliştirmeli, sorumluluklarınızı yerine getirmelisiniz.",
        "Sizin hedefiniz kalp çakranızı açmak olduğu için daima namazla dua ile ALLAH'ımızdan yardım istemeli maneviyatınızı yükseltmelisiniz.",
        "Hayat amacınız yeniliklerle her gün yeni bir şey öğrenerek konfor alanınızdan çıkarak olacağı için ek olarak yaptığınız hatalardan verdiğiniz tavizlerden dolayı kendinizi suçlamamayı öğrenmeniz gerekir. Gezin dolaşın. Yeni yerler görün. Bağımlılıklardan kurtulup kendi merkezinize dönün.",
        "Tüm bunları anlamak değiştirmek için sağ beyninizi kullanarak kendinizi aşmalı, sezgilerinizi fark etmeli, varsa korku ve evhamlarınızı yenmelisiniz. Bunları yenmediğiniz takdirde, ciddi anlamda sorumluluklar üzerinize yüklenebilir.",
        "Derin düşünün, hayatı yaşadıklarınızı ayrıştırarak inceleyin. Bilinçaltının sizi yönetmesine izin vermeyin. Anda kalın. Farkındalık ile yaşayın çünkü farkındalık ile ego bir bedende barınmaz.",
        "Sizin hedeflere ulaşmanız; kendinizi tanıtmak, otorite kurmak ve ticaret gibi işler yaparak olur. Sizin için insanlar arasında lider olmak, fikirlerini ifade etmek oldukça önemlidir. Bu yüzden kendinize güvenin önce auranızı koruyun ve bununla alakalı olarak öne çıkacağınız liderlik yapacağınız işler yapın!... Bunlardan asla geri durmayın. Elbette bunlar için ilk olarak kök çakranızı çok iyi korumanız gerekir. Daha sonra ise auranızı korumak gerekir ki bununla alakalı 8. çakrada dediklerimi mutlaka hayata geçirmeniz gerekir.",
        "Unutmayın siz şifa bulmak için elinizde avucunuzda ne varsa paylaşmayı bilmeli, maneviyatınızı kuvvetlendirmeli ve insanlara hizmet etmelisiniz.",
        #11 19 22 33
        "Eğer duygularınızı kontrol edebilirseniz hedeflerinize hayallerinize ulaşabilirsiniz. Bu yüzden olumlu düşünüp harekete geçin.",
        "Sizin hayat amacınız 19 enerjisi ile olduğu için imtihanlar sizi dönüştürür, manevi anlamda eğitir ve nefs tezkiyesi yaptırır.\n Bu 19 sayısı kişide imtihan ile dönüşmeyi anlatır. Sıkıntıları fark edip olayın altındaki mesajları çözmenizi anlatır. Enerjinizi fark edin. Olaylardan ders çıkarıp, iyileşmeye niyet edin ve daha sonra yaralı bir şifalı gibi insanlığın hayrına çalışın!..",
        "Sizin hayat amacınız  22 sayısı ile olduğu için ciddi sıkıntılar yaşamış olma ihtimaliniz yüksektir. Bunlar elbette sizin kalp çakranızı açmak, imanınızı kuvvetlendirmek, maneviyatınızı arttırmak için başınıza gelmiştir. Ama elbette imtihanlardan mesaj almayı bilip kendinizi düzeltip hayatı olanı olduğu gibi kabul ederseniz sizin makamınız daha da yükselir.",
        "Tüm bunları anlamak değiştirmek için sağ beyninizi kullanarak kendinizi aşmalı, sezgilerinizi fark etmeli, varsa korku ve evhamlarınızı yenmelisiniz. Bunları yenmediğiniz takdirde, ciddi anlamda sorumluluklar üzerinize yüklenebilir. Çünkü sizin yaşam amacınız nefsinizi tezkiye etmek, olumsuz hallerinizi olumluya dönüştürmek ve insanlığın faydasına çalışmaktır."
    ]
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
        elif total_sum == 19:
            return "1*"
        elif total_sum == 22:
            return "4*"
        elif total_sum == 33:
            return "6*"
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
        elif number == 19:
            steps.append(str("1*"))
            return "/ ".join(steps)
        elif number == 22:
            steps.append(str("4*"))
            return "/ ".join(steps)
        elif number == 33:
            steps.append(str("6*"))
            return "/ ".join(steps)
        number = sum(int(digit) for digit in str(number))
    
    steps.append(str(number))
    return "/ ".join(steps)

def ebced_toplama_asamali_isaretsiz(*args):
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
        number = sum(int(digit) for digit in str(number))
    
    steps.append(str(number))
    return "/ ".join(steps)

#ayrı yaptım fonksiyonları ayrı ayrı göstermem gerekebilir.
def chakra_hesapla(pin_kodu, isim_soyisim, ek_isim):
    """
    Çakra hesaplaması yapan fonksiyon.
    3 farklı sistem kullanır:
    0: Pin kodu (sol taraf)
    1: İsim soyisim (sağ taraf) 
    2: Ek isim (ek alan, varsa)
    """
    #0 pin kodu  1 isim soyisim  2 ek soyisim/isim den gelen artılar.
    arti_sistemi = [[0 for _ in range(9)] for _ in range(3)]
    # Pin kodundan sol taraf artılarını doldur
    arti_sistemi[0] = chakra_add_pin_kodu(pin_kodu)
    # İsim soyisimden sağ taraf artılarını doldur
    for letter in isim_soyisim.upper():
        if letter in chakra_values:
            index = chakra_values[letter] - 1
            arti_sistemi[1][index] += 1
    
    # Ek isim varsa, 3. sistemi doldur
    has_ek_isim = False
    if ek_isim and len(ek_isim.strip()) > 0:
        has_ek_isim = True
        for letter in ek_isim.upper():
            if letter in chakra_values:
                index = chakra_values[letter] - 1
                arti_sistemi[2][index] += 1

    # Her çakra için bir sözlük oluştur
    chakra_data = []
    for i in range(9, 0, -1):
        number = str(i)
        # Sözlük oluştur
        chakra_item = {
            'left_plus': ' +' * arti_sistemi[0][i-1],  # Pin kodundan gelen artılar
            'number': number,                           # Çakra numarası
            'right_plus': '+ ' * arti_sistemi[1][i-1], # İsim soyisimden gelen artılar
            'has_ek_isim': has_ek_isim                  # Ek isim var mı?
        }
        
        # Ek isim varsa, ek artıları da ekle
        if has_ek_isim:
            chakra_item['ek_plus'] = '+ ' * arti_sistemi[2][i-1]
        
        chakra_data.append(chakra_item)

    return arti_sistemi, chakra_data

def chakra_add_pin_kodu( pin_kodu):
    """ Pin kodundaki sayıların ilk rakamlarına göre çakra evlerini günceller."""
    # 9 çakra evi için sayaç (1. çakra = index 0, 2. çakra = index 1, ...)
    chakra_sayaci = [0] * 9

    # Pin kodundaki her değerin ilk rakamına göre ilgili çakra evinin sayacını artır
    for pin_degeri in pin_kodu:
        # Pin değerinin ilk karakterini al (örn: '3!' -> '3', '7' -> '7')
        ilk_rakam = int(pin_degeri[0])
        
        # İlk rakam 1-9 arasında olmalı (çakra numarası)
        if 1 <= ilk_rakam <= 9:
            # İlgili çakra evinin sayacını 1 artır (0-based index için -1)
            chakra_sayaci[ilk_rakam - 1] += 1

    return chakra_sayaci


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
    date_str = date_str.replace('.', ' ').replace('/', ' ').replace('-', ' ')
    
    # Birden fazla boşluğu tek boşluğa çevir
    date_str = ' '.join(date_str.split())
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
    if not (1 <= gun <= 31 and 1 <= ay <= 12 and 100 <= yil <= 9999):
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
    
    print("kkkkk")
    print(k)
    # Değerleri şartlara göre güncelle
    for i in range(9):
        if int(k[i][0]) == (i + 1):
            k[i] += '!'
    return  k

  # ALGORİTMA
def pin_kodu_yorumlari_algoritmasi(pin_kodu, arti_sistemi, cinsiyet, yasam_yolu):
    """Pin kodu yorumları algoritması"""
    # Güvenli pin kodu erişimi için helper fonksiyon
    def safe_pin_access(index):
        """Pin kodu elemanına güvenli erişim"""
        if index < len(pin_kodu) and pin_kodu[index] and len(pin_kodu[index]) > 0:
            return pin_kodu[index][0]
        return ""
    
    pin_kodu_yorumlari = []
    
    # Özel durumları kontrol etmek için flag'ler
    hane_3_4_3 = False  # 3. ve 4. hane 3 ise
    hane_3_4_8 = False  # 3. ve 4. hane 8 ise
    hane_3_8_1 = False  # 3. hane 1 ve 8. hane 1 ise
    hane_5_7_2 = False  # 5. ve 7. hane 2 ise
    hane_5_7_1 = False  # 5. ve 7. hane 1 ise
    hane_8_9_4 = False  # 8. ve 9. hane 4 ise
    hane_2_tekrari = False  # 2 rakamı tekrarlanıyorsa
    
    # Özel durumları kontrol et
    if safe_pin_access(2) == "3" and safe_pin_access(3) == "3":
        hane_3_4_3 = True
    
    if safe_pin_access(2) == "8" and safe_pin_access(3) == "8":
        hane_3_4_8 = True
    
    if safe_pin_access(2) == "1" and safe_pin_access(7) == "1":
        hane_3_8_1 = True
    
    if safe_pin_access(4) == "2" and safe_pin_access(6) == "2":
        hane_5_7_2 = True
    
    if safe_pin_access(4) == "1" and safe_pin_access(6) == "1":
        hane_5_7_1 = True
    
    if safe_pin_access(7) == "4" and safe_pin_access(8) == "4":
        hane_8_9_4 = True
    
    

    #1.hane yorumu
    if pin_kodu[0] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[0][9])
    elif pin_kodu[0] == "1*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[0][10])
    elif pin_kodu[0] == "4*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[0][11])
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[0][int(pin_kodu[0][0])-1])

    #kök çakra
    if arti_sistemi[1][0] == 0:
        pin_kodu_yorumlari.append("Kök çakranızın tıkalı olması size  ciddi anlamda sıkıntıları getirmiştir çünkü kök çakra hayata bağlandığımız, var olduğumuz yerdir. Eğer bu çakra tıkanık olursa kendimizi bu hayata ait hissetmekte zorlanabilir ve her koşulda işlerimiz çok kolay yürümeyebilir. Bu yüzden de zorlanabiliriz. Dolayısıyla kök çakrası tıkalı olan insanlar kendilerini ifade etmek varlıklarını ispatlamak için daha bencilce hayata bakabilirler. Bencilliğin bir kısmı iyi ama bu konuda biraz dikkatli olup kararında olması oldukça önemlidir.")
    elif arti_sistemi[1][0] == 1:
        pin_kodu_yorumlari.append("Kök çakranızın az çalışması sizde ciddi anlamda sıkıntıları getirmiştir çünkü kök çakra hayata bağlandığımız, var olduğumuz yerdir. Eğer bu çakra bloke olursa kendimizi bu hayata ait hissetmekte zorlanabiliriz ve her koşulda işlerimiz çok kolay yürümeyebilir. Dolayısıyla kök çakrası tıkalı olan insanlar kendilerini ifade etmek, varlıklarını ispatlamak için daha bencilce hayata bakabilirler. Bencilliğin bir kısmı iyi ama bu konuda biraz dikkatli olup kararında olması oldukça önemlidir.")
    elif arti_sistemi[1][0] >= 4:
        pin_kodu_yorumlari.append("Kök çakranızın aşırı çalışması sizde şikayetçi bir hâl oluşturur. Hayatı güzel görmeyi şükretmeyi öğrenmeli ve her defasında haklı olmaya çalışmamalısınız. Olanı olduğu gibi kabul etmeli elindekiniz ile yetinmelisiniz.")
    if arti_sistemi[1][0] != 0 and (pin_kodu[0] == "1!" or safe_pin_access(4) == "1" or safe_pin_access(6) == "1"):
        pin_kodu_yorumlari.append("Kök çakranızın blokesi sizin hayatta tutunmakta zorluk yaşamanıza neden olmuş bununla birlikte istediğiniz şeyleri elde ederken zorlanmanıza sebep olmuştur. Ayrıca kendinizi ispat etmek için daha çok çabalamış yorulmuş ve zaman zaman karamsarlığa kapılmış olabilirsiniz.")


    #sakral çakra
    if arti_sistemi[1][1] == 0:
        pin_kodu_yorumlari.append("Sakral çakranızın tıkalı olmasından dolayı ikili ilişkilerinizde hep sıkıntı yaşarsınız. Bunun en büyük nedeni bilinçaltımızla ilişkileri çekmemizden kaynaklanır.Siz çocukluktan itibaren kendinizi değersiz hissediyor olabilirsiniz. Ve ikili ilişkilerinizde eş  flört yakın arkadaş tüm hepsinde bu değersiz hissetmeler gündeme geliyor olabilir. Bunu yaşamamak için önce kendi değerinizi bilecek ve koruyacaksınız. Sınırlarınız belli olmalı ve gerektiğinde hayır demeyi bilmelisiniz. Seçimlerinizde oldukça dikkatli olmalısınız. En çok hayatın size zor geldiği nokta burasıdır. Ve imtihanlarınız buradan olabilir.Ayrıca ikili ilişkilerinizdeki bu sıkıntılar auranızı bozabilir ve sizin işlerinizin yolunda gitmemesi, bazen paranızda bereket olmaması gibi sorunlara neden olabilir. Bunun için ikili ilişkilerinizi düzeltmek sizin için oldukça önemlidir.")
    elif arti_sistemi[1][1] == 1:
        pin_kodu_yorumlari.append("Bunun yanında sakral çakranızın az çalışması; duygularınızı ifade ederken zorlanırsınız.  Duygularınızı biriktirdikçe dolar taşar, büyük patlamalar yaşarsınız. Bu yüzden duyguyu anında ifade etmeyi, biriktirmemeyi öğrenmelisiniz.")
    if safe_pin_access(1) == "2" or safe_pin_access(1) == "7" or safe_pin_access(1) == "9" or safe_pin_access(4) == "2" or safe_pin_access(6) == "2":
        pin_kodu_yorumlari.append("Değersizlik hissinden dolayı insanlara aşırı derecede değer verir, her istediklerini yapmaya şartlanırsınız. Fakat insanlar sizin kökeninizde yatan değersizliği ortaya çıkararak size değersizliği yaşatır. Böylelikle siz ilişkilerinizde tam doyuma ulaşamazsınız. Değerli olmak istedikçe daha çok değersizleşirsiniz. Aşırı fedakarlıklar yaparak değerli olmaya çalışırsınız. Bu yüzden bu hissi fark edip kendi değerinizi kendiniz vermeyi unutmamalısınız. Kimse size istediğiniz değeri vermeyecektir ve ilk kez sizi ne değersiz hissettirdi ise fark etmelisiniz. Bu anlamda kitaplar okumanızı tavsiye ederim.")
    if arti_sistemi[1][1] > arti_sistemi[1][0]:
        pin_kodu_yorumlari.append("Sakral çakranızın kök çakraya göre daha fazla çalışması  fedakarlıklar yaptığınızı alma verme dengesini bozduğunuzu gösterir.")
    if (arti_sistemi[1][1] == 2 or arti_sistemi[1][1] == 3) and (safe_pin_access(1) == "2" or safe_pin_access(4) == "2" or safe_pin_access(6) == "2"):
        pin_kodu_yorumlari.append("Sizin sakral çakranızda olan problemler yüzünden sorunlu ilişkileri kendinize çekebilir, duygularınızı ifade etmekte zorlanabilirsiniz. İlişkilerde anlaşılmayı beklersiniz.")
    

    # 3. çakra
    pin_kodu_yorumlari.append("Nasıl halı döve döve temizlenir ise  insanoğlu hatalarla hayatta bir şeyler öğreniyor. Bu yüzden imtihanlar bizim öğretmenimizdir.")
    if arti_sistemi[1][2] <= 1 or arti_sistemi[1][2] >= 4 or safe_pin_access(4) == "3" or safe_pin_access(6) == "3" :
        pin_kodu_yorumlari.append("Sizin en büyük imtihanınız genellikle dilinizden konuşmalarınızdan gelir. Bunun nedeni de kökeninizde yaşadığınız sıkıntıları bir türlü çözüme kavuşturamamanızdan kaynaklanır. Kökende yaşanan sıkıntılar değişik ilişkilerde tekrar tekrar mesaj alıncaya kadar devam eder.Bu sıkıntıların temeli ise kökenden itibaren bastırılmışlığa ve kendinizi ifade ettirilmediğinize dayandığını söylemek isterim. İlk kez ne zaman konuşturulmadınız!. Sizi yetiştirilenler tarafından ne zaman kendinizi anlatmanıza izin verilmedi. Bunları fark ettiğiniz takdirde iyileşme başlar.")
    if arti_sistemi[1][2] == 0:
        pin_kodu_yorumlari.append("3. çakranızın tıkalı olması çocukluktan itibaren bastırılmış olduğunuzu ve kendinizi ifade etmeye çalıştığınızda her daim çocuklukta yaşadığınız anların bilinçaltınıza gelip sizi tekrar bastıracaklarını hissetmenize neden olur. Böylelikle her olayda kendinizi savunurken bulabilirsiniz. Bu çakranın tıkanıklığı kişilerde mide ve sindirim sistemi rahatsızlıklarına neden olurken bazen içe kapanıklığa sebep olur. Bu çakranın iyileşmesiyle kişi derin bir tefekkür eden insan haline dönüşerek içindeki mucizevi yapıya şahit olur.")
    elif arti_sistemi[1][2] >= 4:
        pin_kodu_yorumlari.append("3. çakranızın aşırı çalışması çocukluktan itibaren bastırılmış olduğunuzu ve kendinizi ifade etmeye çalıştığınızda her daim çocuklukta yaşadığınız anların bilinçaltınıza gelip sizi tekrar bastıracaklarını hissetmenize neden olur. Böylelikle her olayda kendinizi savunurken bulabilirsiniz. Bu çakranın tıkanıklığı kişilerde mide ve sindirim sistemi rahatsızlıklarına neden olurken bazen içe kapanıklığa sebep olur. Bu çakranın iyileşmesiyle kişi derin bir tefekkür eden insan haline dönüşerek içindeki mucizevi yapıya şahit olur.")
    

    # 4. çakra
    if arti_sistemi[1][3] == 0:
        pin_kodu_yorumlari.append("Kalp çakranızın aşırı derecede tıkanık olması sizde ciddi imtihanları hayatınıza çekmenize sebep olmuştur. Bunun için imanınızı kuvvetlendirmeli, kalbinize çokça dikkat etmelisiniz. Sizin için aşırı sevmek, aşırı bağlanma söz konusu olabilir. Bunları iptal etmelisiniz. Kalbin aşırı tıkanıklığı kişide ilerleyen zamanlarda kalp hastalıklarına, dolaşım bozukluklarına neden olabilir. Bunu çözmek için kendinizi tanımalı, içinize dönmeli, kendinizi çok iyi bilmelisiniz.\n Kalp çakranız sıkıntılı olduğu için ciddi anlamda seçimlerinizde ani acil kararlar verebilir ve yanlış tercihler yapabilirsiniz. Ayrıca imtihanlarınız olabilir bu imtihanlar genellikle kendi elinizle yaptığınız ettiğiniz ile olur ilişkilerinizde sıkıntı olur duygularınızı belirtmediğiniz için olabilir. İlişkileri sadece kadın erkek ilişkisi olarak düşünmeyip, tüm iş ilişkilerinde bile çok dikkatli adım atmalı, insanlara çabucak güvenmemeli ve her neye karar verecekseniz 40 kere düşünüp öyle hareket etmelisiniz. Çünkü genellikle ortaklarınız beraber yola çıktıklarınız sizi ortada bırakabilir.")
        if arti_sistemi[0][3] == 0:  #iki taraftan da tıkalı
            pin_kodu_yorumlari.append("Bunun yanında imtihanlara çok açık bir insansınız. Hem de ciddi imtihanlar olabilir. Bunlar sizi güçlendirir ama dayanmak zordur. Hayatınızı alt üst eder lakin belki hayatın altı üstünden daha iyidir. Önemli olan sağ salim çıkmışsanız bunlarla ayağa kalkmaktır.")
    elif safe_pin_access(4) == "4" or safe_pin_access(6) == "4":
        pin_kodu_yorumlari.append("Kalp çakranız açık fakat ilişkilerde olan sıkıntılar nedeniyle bloke olmuş bu da sizde öfke krizleri yaşamanıza neden olmuştur.Kalp çakranızın bloke olmasından ötürü insanlara aşırı güvenir ve insanlara aşırı derecede vericilik, fedakarlık yaparsınız. Bu tutumunuz o kadar ileri bir boyuta varır ki artık çevrenizdeki kişilerin ebeveyni olma konumuna gelirsiniz. Onları onlardan daha iyi düşünür ve sahiplenmek istersiniz fakat insanın sahibi yalnızca Allah'tır. Kimsenin kimse tarafından korunmasına ihtiyacı yoktur. Bu anlamda yaşadığınız ve yaptığınız, kendinizde yaşadığınız bu sorunu fark etmenizi tavsiye ederim. İşte bu sizin frekansınızı düşürmeye negatif hissetmenize yeter!... Çünkü insanoğlu nankördür ve asla sizin yaptığınızı takdir etmez. Size nankörlükle dönüş yapacağı için yorulur ve çok pişman olursunuz.\n Kalp çakranız bloke olduğu için ciddi anlamda seçimlerinizde ani acil kararlar verebilir ve yanlış tercihler yapabilirsiniz. Ayrıca imtihanlarınız olabilir bu imtihanlar genellikle kendi elinizle yaptığınız ettiğiniz ile olur ilişkilerinizde sıkıntı olur duygularınızı belirtmediğiniz için olabilir. İlişkileri sadece kadın erkek ilişkisi olarak düşünmeyip, tüm iş ilişkilerinde bile çok dikkatli adım atmalı, insanlara çabucak güvenmemeli ve her neye karar verecekseniz 40 kere düşünüp öyle hareket etmelisiniz. Çünkü genellikle ortaklarınız beraber yola çıktıklarınız sizi ortada bırakabilir.")


    #5. çakra
    if arti_sistemi[1][4] >= 4:
        pin_kodu_yorumlari.append("Sizin boğaz çakranız fazla çalıştığı için hatalardan ders çıkarmayı bilmeyebilir, kendinizi suçlayabilirsiniz. Bu aşırılık ilişkilerinizde aşırı derecede bağımlılıklara neden olabilir. Bu yüzden öncelikle frekansınızı düşüren insanlarla ilişkinizi sınırlandırın, kendinizi tanıyın ve hatalardan ders çıkarmasını öğrenip daha dikkatli bir şekilde hayatı yaşayın.")
    elif arti_sistemi[1][4] == 1:
        pin_kodu_yorumlari.append("Boğaz çakranız az çalıştığı için frekansınız düşük genellikle moralsiz bir yapıda olabilirsiniz. Bunun en önemli nedeni ilişkilerde yaşadığınız sorunlar ve aura tıkanıklığından kaynaklıdır. Bu yüzden kendi değerinizi bilmeli, ilişkilerde bilinçaltı ile iletişim kurmamalı ve 8.çakra için verdiğim tavsiyeleri hayata geçirmelisiniz.")
    elif arti_sistemi[1][4] == 0:
        pin_kodu_yorumlari.append("Sizin boğaz çakranızın tıkalı olması ciddi anlamda negatif hissetmenize, depresif ataklar yaşamanıza neden olmaktadır. Bununla birlikte aşırı kontrolcü olabilirsiniz. Her şeyin istediğiniz gibi ve mükemmel olmasını isteyebilirsiniz. Bunun yanında psikolojik rahatsızlıklarınız da olabilir. Bu yüzden bol bol gezin tozun kendinizi keşfedin. Yeniliğe açık olun asla içinize kapanmayın, yeni şeyler denemekten yorulmayın ve frekansınızı düşüren sizin negatif hissetmenize sebep olan herkesten, her ortamdan uzak durun. Ayrıca 5. çakrada yazdığım tavsiyeleri mutlaka hayata geçirin.")

    # 2 rakamının tekrarlanıp tekrarlanmadığını kontrol et
    hane_2_sayisi = 0
    for i in [2, 3, 5, 7, 8]:  # 3, 4, 6, 8, 9. haneler (0-indexed)
        if  pin_kodu[i] == "2":
            hane_2_sayisi += 1
    
    if hane_2_sayisi > 1:
        hane_2_tekrari = True
        
        # 2 rakamının bulunduğu haneleri tespit et
        hane_2_pozisyonlari = []
        for i in [2, 3, 5, 7, 8]:  # 3, 4, 6, 8, 9. haneler (0-indexed)
            if pin_kodu[i] == "2":
                hane_2_pozisyonlari.append(i)
        
        # Birleşik metin oluştur
        if len(hane_2_pozisyonlari) > 1:
            metin_parcalari = []
            for poz in hane_2_pozisyonlari:
                if poz == 2:  # 3. hane
                    metin_parcalari.append("Dünyaya açılış şekliniz")
                elif poz == 3:  # 4. hane
                    metin_parcalari.append("Sıkıntıları aşma şekliniz")
                elif poz == 5:  # 6. hane
                    metin_parcalari.append("İlişki kurma şekliniz")
                elif poz == 7:  # 8. hane
                    metin_parcalari.append("Aura açma şekliniz")
                elif poz == 8:  # 9. hane
                    metin_parcalari.append("Hayat amacınız")
            
            # Birleşik metni oluştur ve ekle
            birlesik_metin = " ve ".join(metin_parcalari) + " yunusça Yaradan'dan ötürü yaradılanı severek olacaktır. Dolayısıyla sevmeyi sevilmeyi önemsemeniz oldukça önemlidir fakat aşırı fedakarlıklar yapıyor iseniz sevmeyi sadece vermek olarak algılıyor iseniz bu dengeyi bozar. Bu yüzden bu dengeyi gözetmeniz çok önemlidir."
            pin_kodu_yorumlari.append(birlesik_metin)
            
    #3.hane yorumu
    if pin_kodu[2] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[2][9])
    elif pin_kodu[2] == "1*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[2][10])
    elif pin_kodu[2] == "4*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[2][11])
    elif hane_3_4_3:
        # 3. ve 4. hane 3 ise özel metin
        pin_kodu_yorumlari.append("Sizin dünyaya açılma ve sıkıntıları aşma şekliniz konuşarak kendinizi ifade ederek olacağı için üzerinizdeki baskıyı fark edip, kökenlerden gelen duygularınızı ifade etmediğiniz hangi olaylar varsa bunları çözmelisiniz. Bunlar çözülmediği müddetçe 3. çakranız size ciddi anlamda sıkıntılar yaşatabilir, bastırılmış hissettirebilir ve mide diyabet gibi gastrointestinal sistem hastalıklarına sebep olabilir.")
    elif hane_3_4_8:
        # 3. ve 4. hane 8 ise özel metin
        pin_kodu_yorumlari.append("Sizin dünyaya açılma şekliniz ve sıkıntıları aşma hâliniz insanlar üzerinde bir otorite kurarak liderlik yaparak olacağı için kendinizi çok iyi tanımalı auranızı korumalı nazar negatif enerji negatif insanlardan ve ortamdan uzak durmalısınız. Ayrıca haram olan her şeyden uzak kalmalı mümkün mertebe rızkınızın helal olmasına çokça dikkat etmelisiniz. Ayetel Kürsi suresini ağzınızdan düşürmemelisiniz.")
    elif hane_3_8_1:
        # 3. hane 1 ve 8. hane 1 ise özel metin
        pin_kodu_yorumlari.append("Sizin dünyaya açılma ve auranızı açma haliniz kök çakranızla olduğu için öne çıkar, otorite kurmak ister ve liderlik yapmak istersiniz. Bununla birlikte çocuklukta yaşadığınız travmalarınız varsa mutlaka çalışmalı kendinizi, çocukluğunuzu yaşanan sıkıntıları sevgiyle kabule geçmelisiniz.")
    elif hane_2_tekrari and safe_pin_access(2) == "2":
        # 2 rakamı tekrarlanıyorsa ve 3. hane 2 ise
        pass
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[2][int(pin_kodu[2][0])-1])

    #4.hane yorumu
    if pin_kodu[3] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[3][9])
    elif pin_kodu[3] == "1*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[3][10])
    elif pin_kodu[3] == "4*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[3][11]) 
    elif hane_3_4_3 or hane_3_4_8:
        # 3. ve 4. hane aynı ise tekrar ekleme
        pass
    elif hane_2_tekrari and safe_pin_access(3) == "2":
        # 2 rakamı tekrarlanıyorsa ve 4. hane 2 ise
        pass
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[3][int(pin_kodu[3][0])-1])

    #5.hane yorumu
    if pin_kodu[4] == "2*":
        if cinsiyet == "erkek":
            pin_kodu_yorumlari.append(pin_kodu_yorumu[4][9])
        elif cinsiyet == "kadın":
            pin_kodu_yorumlari.append(pin_kodu_yorumu[4][10])
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[4][int(pin_kodu[4][0])-1])

    #6.hane yorumu
    if pin_kodu[5] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[5][9])
    elif hane_2_tekrari and safe_pin_access(5) == "2":
        # 2 rakamı tekrarlanıyorsa ve 6. hane 2 ise
        pass
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[5][int(pin_kodu[5][0])-1])

    #7.hane yorumu
    if hane_5_7_2:
        # 5. ve 7. hane 2 ise tekrar ekleme
        pass
    elif hane_5_7_1:
        # 5. ve 7. hane 1 ise tekrar ekleme
        pass
    elif pin_kodu[6] == "2*":
        if cinsiyet == "erkek":
            pin_kodu_yorumlari.append(pin_kodu_yorumu[6][9])
        elif cinsiyet == "kadın":
            pin_kodu_yorumlari.append(pin_kodu_yorumu[6][10])
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[6][int(pin_kodu[6][0])-1])


    #6. çakra
    if arti_sistemi[1][5] == 0 and  safe_pin_access(3) != "6" and  safe_pin_access(7) != "6":
        pin_kodu_yorumlari.append("Sizin 6. çakranız oldukça tıkalı olduğu için imanınızı mutlaka artırmalı maneviyatınızı kuvvetlendirmelisiniz. Eğer babanızı, hayatınızda olan erilleri olduğu gibi kabul edemiyorsanız kabul edin. Ailede ciddi problemler varsa bunlarla yüzleşerek sevgiyle kabule geçmelisiniz. 6.çakranızdaki aşırı tıkanıklık sizin sezgilerinizin gelişmemesine ve ebeveynlik noktasında sorunlar yaşamanıza ayrıca babanızla alakalı imtihanlarınız, sıkıntılarınız, anlaşamadığınız konular varsa bunların büyümesine neden olmuştur. Bu yüzden bir an önce babanızla, ebeveynlerinizle alakalı sıkıntılar varsa bunları aşmalı, korku vesvese varsa onların üzerine gitmeli, 6.çakra tavsiyelerini hayatınıza geçirmelisiniz.")
    if arti_sistemi[1][5] == 0 and ( safe_pin_access(3) == "6" or  safe_pin_access(7) == "6"):
        pin_kodu_yorumlari.append("Hem sağ hem sol beyninizi aktif bir şekilde kullanmanız gerektiği için gelişime çok açık kendini yenileyebilen bir insansınız. Bu anlamda korkularınız var mı? Hayata karşı insanlara karşı aşırı derecede merhamet duyduğunuz halleriniz var mı? Bunları kontrol etmenizi tavsiye ederim.\n Buna rağmen sağ beyniniz güzel çalışır, sezgileriniz kuvvetlidir ve önsezileriniz güçlüdür. İnsanlara yardım etmeyi seversiniz. Sorumluluk almayı sorumluluklarınızı yerine getirmeyi önemsersiniz.")
    if arti_sistemi[1][5] == 0 and arti_sistemi[1][8] == 0:
        pin_kodu_yorumlari.append("6. ve 9. çakranız tıkalı olduğu için ileri görüşlü olmakta zorluk çekebilirsiniz. İnsanlar tarafından ortada bırakılabilirsiniz. Yanlış kararlar alabilirsiniz. Bu yüzden seçimlerde istişare yapmanız önemlidir.")
    if arti_sistemi[1][5] == 1 or safe_pin_access(0) == "6" or safe_pin_access(2) == "6" or safe_pin_access(4) == "6" or  safe_pin_access(6) == "6":
        pin_kodu_yorumlari.append("Bunun yanında siz genellikle ailevi konularda imtihan olabilirsiniz. 6.çakranızın geliştirilmesi gerektiğinden aşırı derecede korku vesvese gibi durumlarınız olabilir. Ayrıca sevdiklerinize karşı aşırı mükemmeliyetçilik, korumacılık gözükebilir. Bunu değiştirip dönüştürmelisiniz. Korkularınızı yenmelisiniz. Mükemmeliyetçilik yerine her halimizle ailemizi kendimizi kabul etmeyi öğrenmeliyiz.")


    #7. çakra
    if arti_sistemi[1][6] == 0:
        pin_kodu_yorumlari.append("7.çakranız tıkalı olduğu için arayışlarınız olur. Hayata karamsar bir halde bakabilirsiniz. İlişkilerinizde doymayı bilmeyebilirsiniz. Her daim yetinmediğiniz için herkes benimle ilgilensin, beni sürekli sevdiğini söylesin, ilgi göstersin gibi bir yaklaşımda bulunabilirsiniz. Bunları düzeltip kronik şikayetçi bir haliniz varsa bunlardan uzaklaşarak şükür içinde yaşayıp kanaat etmeyi öğrenmelisiniz. Her olayı derinlemesine düşünmeli, maneviyatınızı kuvvetlendirmelisiniz.\n 7.çakranızda olan tıkanıklık akletmemenize, olayların içinde yatan mesajları çözememenize neden olmuş. Bu yüzden farkındalıkla yaşamanızı, her olaydan önce 40 kere düşünüp bir kere hareket etmenizi tavsiye ederim.")
    elif arti_sistemi[1][6] == 1 or  safe_pin_access(4) == "7" or safe_pin_access(6) == "7" or safe_pin_access(5) == "7" or safe_pin_access(0) == "7" or safe_pin_access(2) == "7":
        pin_kodu_yorumlari.append("Ayrıca taç çakranızın blokeli olmasından ötürü ilişkilerinizde doymayı bilmek, kanaat etmek noktasında sıkıntılarınız olabilir. İnsanlar sizinle daha çok ilgilensin daha çok sizi sevsin daha çok sevdiğini söylesin diyebilirsiniz. Bu anlamda ilk olarak ilişkilerinizde doymayı yetinmeyi öğrenmelisiniz. Sizin pin kodunuz en çok size bunu hatırlatır, doymayı yetinmeyi öğrenmeyi anlatır. Eğer gerçekten tam manasıyla tatmin olmak istiyor iseniz  tahkiki imanı fark etmeli ve gerçek aşkın ve sevginin Allah'ta olduğunu anlamalısınız.\n İşte bu yüzden ilişkilerinizdeki doyumsuzluğun nedenini keşfedin!... Kökende yatan değersizlik inancı buna sebep olur. Siz doymak bilmezsiniz. İşinizi, eşinizi başka her şeyin daha iyisini isterken bulursunuz kendinizi!... Arayışlarınız olur. Bunu ancak kalbinizi sahibine vererek, imanınızı artırarak aşarsınız.\n Siz arayışlarınızı çözdüğünüzde varsa ilişkilerinizde kanaatsizlik doyumsuzluk sorunlarınızı hallettiğinizde, kronik şikayetçi haliniz varsa şüküre geçtiğinizde maneviyatı kuvvetli hale getirdiğinizde olgunluğa ulaşırsınız.")
    if arti_sistemi[1][0] == 1:
        pin_kodu_yorumlari.append("Kök çakranızın az çalışması yüzünden taç çakranız bloke olmuş. Bu yüzden ilişkilerde doyumsuzluk ve karamsarlık yaşanabilir.")
    if arti_sistemi[0][6] == 0 and arti_sistemi[1][6] == 0:
        pin_kodu_yorumlari.append("Taç çakranızın desteksiz olması sizi karamsar bir yapıda tutmuş ve bu karamsarlıklar arayışlar içinde yaşamanıza neden olmuştur. Bilhassa aileniz tarafından destek alamamış gibi hissederek olaylardan dolayı hep kendinizi suçlamışsınız.")
    if arti_sistemi[1][6] <= 1 and arti_sistemi[0][6] >= 0:
        pin_kodu_yorumlari.append("Taç çakranızın bloke olması kök çakranızı bloke etmiş. İşte bu yüzden her olayda daha dikkatli olmalı ve mesajları okumalısınız. Ayrıca elinizde olana şükretmeli, yetinmeyi bilmelisiniz.")
    if (arti_sistemi[1][6] <= 1 and arti_sistemi[1][4] <= 1) or ((arti_sistemi[1][6] == 2 or arti_sistemi[1][6] == 3) and (safe_pin_access(4) == "7" or safe_pin_access(6) == "5" or safe_pin_access(8) == "5" or safe_pin_access(8) == "7"  )) :
        pin_kodu_yorumlari.append("Siz 7. çakranızla, 5. çakranızın bloke olması hasebiyle ciddi anlamda ruhsal krizler yaşarsınız. Sanki çok büyük bir boşlukta gibi hissedersiniz ve bu boşluk sizi korkutur. Ve sizi ele geçirecek gibi hissettirir. Fakat korktukça bu boşluk büyür. Bu yüzden özellikle korkmamaya ve onu önemsememeye çalışmanız gerekir. Elbette bunu aşmak için öncelikle kökende yani küçüklüğünüzde yaşadığınız olaylara bakmak gerekir. Bunun için bir terapi almak şarttır. Özellikle duygularınızı boşaltmak önemlidir. Bunlar olmadan tam bir temizlik mümkün olmaz. Ama eğer ki bunu yapacak maddi bir imkanınız yoksa ilk olarak size tavsiyem YouTube'da veya kitaplarda öncelikle duygusal boşaltma ile ilgili bilgiler edinelim. Bunlar tam manasıyla boşalmadan insanın rahat bir hayat yaşaması zordur.\n Eğer böyle imkanlarınız da yoksa en güzel yöntem güzel bir tövbedir. Allah'a yönelmektir. İmanınızı artırmak ve dualarda dertlerinizi Allah'a anlatmaktır. Bu da en güzel duygusal boşaltımdır. Böylelikle hem imanınız artar hem korkularınıza karşı direnme gücünüz artar.")
    if arti_sistemi[1][6] == 0 and arti_sistemi[1][0] == 0:
        pin_kodu_yorumlari.append("7. çakranızdaki aşırı derecede tıkanıklık ve kök çakranızdaki tıkanıklık, her ikisi birleşmiş ve sizde aşırı derecede şikayet, ilişkilerde doymamak, sürekli arayışlarda bulunmak gibi olaylara neden olmuş olabilir.Bu da ilişkilerinizde sürekli kendini ispat, EGO, benlik, sürekli haklı olmaya çalışmak ve başkalarında kabahat aramak gibi olaylara neden olabilir.")


    #8. çakra
    if arti_sistemi[1][7] == 0 or safe_pin_access(4) == "8" or safe_pin_access(6) == "8" or safe_pin_access(7) == "8":
        pin_kodu_yorumlari.append("Ciddi bir anlamda aura probleminiz var ve buna çalışmak zorunda olduğunuzu doğum tarihiniz bize söylüyor. Öncelikle 8. çakradaki yazdıklarımı önemseyin ve mutlak surette yardımlaşmaya, elinizdeki avucunuzdaki ne varsa paylaşmaya özen gösterin. Bununla beraber önce kendinize daha sonra etrafınızda olan herkese karşı sınır koymasını bilin, kendi değerinizi bilerek ölçülü hareket edin, ani ve hızlı kararlar vermeyin. Duygularınızı kontrol etmeyi öğrenin.\n Auranızda bu ciddi anlamda sıkıntılar yüzünden nazardan negatif enerjiden ciddi anlamda etkilenirsiniz. Bu yüzden size mutlaka 'Z' harfinden oluşan mahlas almanızı tavsiye ederim. Mahlas eski bir inanış olup kişilerin sadece Allah ile arasında olacağı bir isimdir. Hiç kimsenin bilmemesi elzemdir. Bunun için detaylı bilgiyi analizden sonra benden alabilirsiniz.")
    if (arti_sistemi[1][7] == 0 and arti_sistemi[1][8] == 0):    
        pin_kodu_yorumlari.append("Hem 8 hem 9.çakranızın tıkalı olmasından kaynaklı işleriniz kolayca olmaz. Bunun en büyük nedeni beden evinizi koruyan auranızın delinmesidir. Bu delinme sizin frekans düşüklüğünüzden kaynaklanır. Negatif düşündükçe daha çok frekans düşer ve daha çok delinir. Öyle ise bunun tam tersini yaparak önce olumlu düşünerek, negatif olan düşüncelere tövbe ederek başlamalısınız. Yani kısaca nazardan negatif enerjiden ciddi anlamda etkilenirsiniz. Bu yüzden size mutlaka 'Z' ve 'I, İ, R' (harflerinden herhangi birini yada ikisini kullanabilirsiniz) harflerinden oluşan mahlas almanızı tavsiye ederim. Mahlas eski bir inanış olup kişilerin sadece Allah ile arasında olacağı bir isimdir. Hiç kimsenin bilmemesi elzemdir. Bunun için detaylı bilgiyi analizden sonra benden alabilirsiniz.")

    #9. çakra
    if arti_sistemi[1][7] >= 0 and(arti_sistemi[1][8] == 0 or  safe_pin_access(4) == "9" or  safe_pin_access(6) == "9" or  safe_pin_access(8) == "9"):
        pin_kodu_yorumlari.append("9.tıkalı blokeli olmasından kaynaklı işleriniz kolayca olmaz. Bunun en büyük nedeni beden evinizi koruyan auranızın delinmesidir. Bu delinme sizin frekans düşüklüğünüzden kaynaklanır. Negatif düşündükçe daha çok frekans düşer ve daha çok delinir. Öyle ise bunun tam tersini yaparak önce olumlu düşünerek, negatif olan düşüncelere tövbe ederek başlamalısınız. Yani kısaca nazardan negatif enerjiden ciddi anlamda etkilenirsiniz. Bu yüzden size mutlaka 'I, İ, R' (harflerinden herhangi birini yada ikisini kullanabilirsiniz) harflerinden oluşan mahlas almanızı tavsiye ederim. Mahlas eski bir inanış olup kişilerin sadece Allah ile arasında olacağı bir isimdir. Hiç kimsenin bilmemesi elzemdir. Bunun için detaylı bilgiyi analizden sonra benden alabilirsiniz.")


    #yasam yolunun ikinci hanesi 5 ise
    if yasam_yolu == "15/ 6" or yasam_yolu == "25/ 7" or   yasam_yolu == "35/ 8" or yasam_yolu == "45/ 9": 
        pin_kodu_yorumlari.append("Sizin için ciddi anlamda depresyon problemi vardır. Zaman zaman dibe çökebilirsiniz. Bunun en büyük sebebi auranızın delik olmasıdır. Bu yüzden hayatta her şeyi kontrol edemeyeceğinizi bilmeli ve akışa teslim olmalısınız.")

    # 3, 6, 9 haricindeki rakamları kontrol et, kurban psikolojisi
    has_other_numbers = False
    for k_value in pin_kodu:
        if k_value and len(k_value) > 0:
            first_digit = k_value[0]
            if first_digit.isdigit() and first_digit not in ['3','6','9']:
                has_other_numbers = True
                break
    if not has_other_numbers:
        pin_kodu_yorumlari.append("Sizde kurban, zorba, kurtarıcı üçgeni dediğimiz kurban üçgeni vardır. Özellikle annenizden öğrendiğiniz kurban olma psikolojisi ilişkilerde devam ediyor olabilir. Anneniz kendi evliliğinde kurban rolü oynuyor ise ve siz çocukken annenizi kurtarmayı, babanıza karşı savunmayı ya da tam tersi de olabilir kısaca kurtarıcı rolü oynamış olabilirsiniz. Şimdi ise annenizden öğrendiğiniz kurban rolünü devam ettirirsiniz. Kimse kurban ya da kurtarıcı olmak zorunda değildir. Bu psikoloji toplumda evliliklerin ciddi anlamda sıkıntı almasına neden olmaktadır. Kişi kendi sorumluluğunu almalı, kendi sıkıntılarını imtihanlarını fark etmeli, kendisini iyileştirmeyi bilmelidir. Birilerinin yarasından ya da hastalıklarından dolayı acıyıp onu sürekli el üstünde tutmaya çalışmak çok küçük ve basit bir yaklaşımdır. Bu hal bizim toplumumuzda sıklıkla görülür ve elbette yardım etmeyince, yani eşleriniz genellikle size göre zorba olunca olur. Bu da ciddi anlamda sıkıntılara neden olur. Böyle evliliklerde ben her zaman ortak bir paydada buluşup kendinizi tanımanızı, konuşarak sorunlarınızı halletmenizi tavsiye ediyorum.")

    #8.hane yorumu
    if pin_kodu[7] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[7][9])
    elif hane_8_9_4 or hane_3_8_1 or (hane_2_tekrari and safe_pin_access(7) == "2"):
        pass
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[7][int(pin_kodu[7][0])-1])

    #9.hane yorumu
    if pin_kodu[8] == "2*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[8][9])
    elif pin_kodu[8] == "1*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[8][10])
    elif pin_kodu[8] == "4*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[8][11])
    elif pin_kodu[8] == "6*":
        pin_kodu_yorumlari.append(pin_kodu_yorumu[8][12])
    elif hane_2_tekrari and safe_pin_access(8) == "2":
        # 2 rakamı tekrarlanıyorsa ve 9. hane 2 ise
        pass
    elif hane_8_9_4:
        # 8. ve 9. hane 4 ise tekrar ekleme
        pass
    else:
        pin_kodu_yorumlari.append(pin_kodu_yorumu[8][int(pin_kodu[8][0])-1])

    return pin_kodu_yorumlari



def yasam_yolu_hesapla(birthdate):
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    total_sum = 0
    for char in birthdate:
        if char.isdigit():
            total_sum += int(char)

    return ebced_toplama_asamali_isaretsiz(total_sum)

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
    """Pin kodu özellik hesaplama fonksiyonu"""
    # Güvenli erişim için helper fonksiyon
    def safe_get_first_digit(pin_value):
        """Pin değerinin ilk rakamını güvenli şekilde al"""
        if pin_value and len(pin_value) > 0 and pin_value[0].isdigit():
            return int(pin_value[0])
        return 0  # Varsayılan değer
    
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
    
    # Güvenli erişimle rakam dizisini doldur
    for i in range(0, min(9, len(k))):
        rakam_dizisi[i] = safe_get_first_digit(k[i])

    # Her rakamı kontrol ederek ilgili özellik sayısını artır
    for rakam in rakam_dizisi:
        for ozellik, degerler in ozellikler.items():
            if rakam in degerler:
                sayac[ozellik] += 1

    result = ""
    for ozellik, deger in sayac.items():
        result += f"{ozellik}: {deger}    "

    return result


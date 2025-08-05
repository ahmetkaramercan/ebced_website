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
        "zort birisiniz",
        "Kendiniz olmayı, kendinizi fark etmeyi, tanımayı, kendini bilen Rabbini bilir hitabınca kendinizi nasıl terbiye edip nasıl düzelteceğinizi anlatmayı hedefler. Kendini tanımak ne demek bunu bilmelisiniz. Kendini tanımak demek nefsimizi tezkiye etmek, olumsuz yönlerimizi ayıklamak demektir. Ve üslubunuzu düzelterek tatlı dille konuşmayı, kendinizi güzel ifade etmeyi öğrenmelisiniz. Bunun yanında kalbinizi açıp, sıkıntılarınızı, özellikle ikili ilişkilerinizi, imtihanlarınızı önceden fark etmeli ve önlem almalısınız. Bunun için her zaman öngörülü olmalı, öngörülerinizi geliştirmeli, sorumluluklarınızı yerine getirmelisiniz.",
        "Sizin hedefiniz kalp çakranızı açmak olduğu için daima namazla dua ile ALLAH'ımızdan yardım istemeli maneviyatınızı yükseltmelisiniz.",
        "Hayat amacınız yeniliklerle her gün yeni bir şey öğrenerek konfor alanınızdan çıkarak olacağı için ek olarak yaptığınız hatalardan verdiğiniz tavizlerden dolayı kendinizi suçlamamayı öğrenmeniz gerekir. Gezin dolaşın. Yeni yerler görün. Bağımlılıklardan kurtulup kendi merkezinize dönün.",
        "Tüm bunları anlamak değiştirmek için sağ beyninizi kullanarak kendinizi aşmalı, sezgilerinizi fark etmeli, varsa korku ve evhamlarınızı yenmelisiniz. Bunları yenmediğiniz takdirde, ciddi anlamda sorumluluklar üzerinize yüklenebilir.",
        "Derin düşünün, hayatı yaşadıklarınızı ayrıştırarak inceleyin. Bilinçaltının sizi yönetmesine izin vermeyin. Anda kalın. Farkındalık ile yaşayın çünkü farkındalık ile ego bir bedende barınmaz.",
        "Sizin hedeflere ulaşmanız; kendinizi tanıtmak, otorite kurmak ve ticaret gibi işler yaparak olur. Sizin için insanlar arasında lider olmak, fikirlerini ifade etmek oldukça önemlidir. Bu yüzden kendinize güvenin önce auranızı koruyun ve bununla alakalı olarak öne çıkacağınız liderlik yapacağınız işler yapın!... Bunlardan asla geri durmayın. Elbette bunlar için ilk olarak kök çakranızı çok iyi korumanız gerekir. Daha sonra ise auranızı korumak gerekir ki bununla alakalı 8. çakrada dediklerimi mutlaka hayata geçirmeniz gerekir.",
        "Unutmayın siz şifa bulmak için elinizde avucunuzda ne varsa paylaşmayı bilmeli, maneviyatınızı kuvvetlendirmeli ve insanlara hizmet etmelisiniz.",
        #11
        "Eğer duygularınızı kontrol edebilirseniz hedeflerinize hayallerinize ulaşabilirsiniz. Bu yüzden olumlu düşünüp harekete geçin."
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
        elif total_sum == 19:
            return "1*"
            return "/ ".join(steps)
        elif total_sum == 22:
            return "4*"
            return "/ ".join(steps)
        elif total_sum == 33:
            return "6*"
            return "/ ".join(steps)
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
        
        # İndeks kontrolü ekle
        if 0 <= index < len(pin_kodu_yorumu[i]):
            yorum += f"{index+1}. ile açılmış: {pin_kodu_yorumu[i][index]}"
        else:
            yorum += f"Geçersiz sayı: {index+1} (Bu hane için 1-9 arası bir sayı olmalıdır)"
        
        # Eğer k[i] değerinde ünlem işareti varsa, özel yorumu ekle
        if k[i].endswith('!'):
            sayi = int(k[i][0]) - 1  # 0-based index için -1
            if 0 <= sayi < len(unlemli_yorumlar):
                yorum += f"<br>Dikkat etmesi lazım: {unlemli_yorumlar[sayi]}"
        
        pin_kodu_yorumlari.append(yorum)
    
    # Pin kodu görsel dizilimini hazırla    
    return  k, pin_kodu_yorumlari


def merkez_sayi_bulma(isim_soyisim):
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


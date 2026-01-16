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
        "Güçlü bir liderlik enerjisi, bireysellik arayışı ve özgüven meselelerini gündeme taşır. Kişi hayata iddialı, otoriter ve öne çıkma isteğiyle başlar; toplumda sözü geçen biri olmayı önemser. Çoğunlukla sosyal, dışa dönük, dikkat çekici bir tavrı vardır; konuşmalarıyla insanları etkiler ve saygı uyandırır. Ancak özgüven eksikliği veya aşırı ego arasında gidip gelebilir, bu da tartışmacı ya da sivri bir üslup sergilemesine yol açabilir. Takdir ve onay görmediğinde enerjisini kaybedebilir, hatta bunalıma sürüklenebilir. Fazla güç arayışı ise çevresindekileri zorlayabilir ve baskıcı bir karaktere dönüşmesine sebep olabilir. Bu nedenle en büyük dersi, özgüveni dengelemek, egoyu sağlıklı kullanmak ve liderlik enerjisini yapıcı bir şekilde yönlendirmek olacaktır.",
        "2 rakamı, kişiye derin bir duygusal hassasiyet ve yüksek bir empati gücü kazandırır. Düşüncelerin duygu temelli olması, karar vermeyi zaman zaman zorlaştırabilir ve kişiyi kararsız ya da fazla temkinli gösterebilir. Bu enerji, anaçlık, koruyuculuk ve sorumluluk bilinci ile birleşerek çevresindekilere adeta bir “duygusal yara bandı” olma rolünü getirir. Dişil enerjisi yüksek olduğundan, diplomasi, arabuluculuk ve insan ilişkilerinde yumuşak bir dil kullanma becerisi öne çıkar. Ancak küsme, alınganlık ve bağımlılıklara yatkınlık gibi gölge yönleri de olabilir. İnsanlar, sevecen ve şefkatli tavrı nedeniyle ona kolayca yaklaşır, güven duyar ve yanında huzur bulur. Asıl ders, duygulara kapılmadan daha sağlam kararlar alabilmek ve başkalarıyla ilgilenirken kendi ihtiyaçlarını da koruyabilmektir.",
        "Kişinin kendini ifade etme arzusunu ama aynı zamanda bastırılmışlık hissini gösterir. Konuşkan olsa bile  çoğu zaman yeterince anlaşılmadığını düşünebilir. Kendini anlatmakta zorlandığında öfke patlamaları yaşayabilir veya ani çıkışlarla sivrilebilir. Çocukluktan gelen baskılar, özgüvenini zedeleyerek kendini sürekli daha iyi ifade etme arayışına itebilir. Katı, talepkâr ve disiplinli tavırları çevresinde hem saygı hem de mesafe yaratır. Duygusal derinliklerini dile getirmekte zorlandığı için, içsel dünyası ile dışa yansıttıkları arasında kopukluk yaşayabilir. Bu durumları aşamazsa zorba birine dönüşebilir. Aşarsa güçlü, hakkını savunuan, üretken, hitabeti iyi olan birine dönüşürsünüz. ",
        "Kişinin zihinsel yapısı katı kurallarla çalışır ve “ya hep ya hiç” bakış açısı baskındır. Kendi kurallarınız vardır. Bu durum esneklik eksikliği ve başkalarını yargılama eğilimini beraberinde getirir. Doğum tarihi, kişiyi sabır ve sebat yoluyla olgunlaştırmak, daha esnek ve anlayışlı olmaya yöneltmek ister. İlişkilerinde bağımlılıklar ve bastırılmışlık hissi yaşayabilir, özellikle öfke ve aceleci kararlar en büyük sınavlarıdır. Sorumluluk duygusu güçlüdür, çevresindekileri koruyup gözetme eğilimindedir. Ancak dengeli bir şekilde sınırlar koymayı ve sabırla hareket etmeyi öğrenmesi gerekir.",
        "Küçük yaşlarda korku ve güvensizlikle sınansa da, cesaretini geliştirdiğinde yaratıcı, özgür ve hayatla barışık bir yapıya dönüşür. Zeki, sıra dışı ve dikkat çekici bir enerjisi vardır; hem insanlarla iletişimi güçlüdür hem de yalnızlığını sever. Mizah duygusu kuvvetlidir fakat değişken ve tepkisel davranışları zaman zaman kırıcı olabilir. Adrenalin ve heyecan arayışıyla hareketli bir yaşam sürerken, stratejik zekâsı ve problem çözme becerisiyle de öne çıkar. Korkudan cesarete geçmeyi öğrenmeli. Hayat boyu hep cesaret ister.",
        "Düşünceleri sezgisel ama aynı zamanda duygusal yüklerle doludur. Aileden gelen etkiler zihinsel kalıplarını oluşturur. Kararlarında duygusal geçmiş belirleyicidir. Bu yüzden evham ve endişe sorunlarıyla karşılaşabilir. Bu durumu yönetmesi kafasında büyütmemelidir. Vesveseyi dikkate almamalı içinde büyütmemelidir. Başkalarının iyiliğine odaklanan vicdanlı ve derinlikli bir akıl yapısı geliştirir. Aileye ve sevdiklerine bağlıdır; sorumluluk almayı ve görevlerini yerine getirmeyi önemser. Sezgileri kuvvetlidir ve insanlara yardım etmeyi sever, aynı zamanda sağ ve sol beynini dengeli kullanarak gelişime açıktır. Sanatsal, mistik ve derin bir ruhunuz vardır.",
        "Sürekli bir arayış ve sorgulama içindesiniz; hayat boyu kararsızlık ve zihinsel mücadelelerle uğraşabilirsiniz. Zekânız çok gelişkindir. Düşüncelere ve fikirlere mantıksal kanıtlar istersiniz. İnsanlar ilk tanıştığında sizi soğuk ve mesafeli bulabilir, fakat aslında utangaç ve kendi halinde bir yapınız vardır. Duygularınızı genellikle maskelersiniz ve yalnız kaldığınızda içsel çığlıklar atabilirsiniz. Başkalarının duygusal yüklerini alma eğiliminiz vardır; bu bazen sizi yıpratabilir. 7. çakra tıkalıysa hayata dair doyumsuzluk ve tatminsizlik yaşayabilirsiniz.  ",
        "Zihniniz başarıya, güç kazanmaya ve kendini ispat etmeye odaklıdır. Ancak düşünceler çoğu zaman ya hırsla yönlenir. Düşünsel alanda “ya kazanırım ya ezilirim” inancı vardır. Heybetli ve dikkat çeken bir auraya sahipsiniz. Sabırlı ve çalışkan bir yapınız vardır. İnsanlar sizi güçlü, otoriter ve zaman zaman kontrolcü bulabilir, ama bu sizi rahatsız etmez. Zamanınızı verimli kullanır, sürekli meşgul görünmeyi tercih edersiniz. Otorite kurmaya, kendini ifade/ispat etmeye, asil olmaya ihtiyaç var.  Buyurganlık, inatçılık ve kontrolcülük gibi zayıf yanlarınız olsa da samimiyet, sadakat ve dayanıklılığınızla bunları dengeleyebilirsiniz.",
        "Saf temiz kalpli yardımsever bir yapınız vardır. Çocuksu ve safi enerjinizden dolayı insanlara samimi gelirsiniz. Olayların arka planını araştırmalı.. Her koşula uyum sağlayan bir yapınız var ama zihinsel yapı fazla uyumlu olabilir. Bu yüzden ilk yıllarda kendi fikirlerini korumakta ve sınır çizmekte zorlanır. Sürekli başkalarını düşünmek ya da memnun etmeye çalışmak zihinsel bulanıklık yaratır. Sınırlar koymalı. Sınırlarını belirlediğinde, zihinsel gücü artar ve bilgeleşir. Olayların ardını sezen farkındalıklı bir düşünür olur. Tembelliğe düşmemelisiniz.",
        #11 , 19 , 22
        "Bu hanede 11/2 enerjisi, kişinin kendini güçlü göstermekle değersizlik hisleri arasında sıkıştığını ortaya koyar. Çocuklukta bastırılmış duygular, kök çakra blokajı ve kendini ifade edememe eğilimi baskın olabilir. İnatçılık, bildiğini savunma ve hedeflerine odaklanma isteği güçlüdür; ancak bu tavır zaman zaman sivri bir üslup ve tartışmacı bir tutuma dönüşebilir. Özgüven eksikliği ya da aşırı ego arasında gidip gelmesi, ilişkilerinde baskı yaratır. Toplum içinde öne çıkma isteği olsa da, takdir ve onay görmediğinde hızla enerjisini kaybedebilir. Bu durum onu ya baskıcı bir karaktere ya da içsel bir bunalıma sürükleyebilir.",
        "Bu hanede 19/1 enerjisi, kişinin kendini güçlü bir lider olarak görme isteğini ama aynı zamanda ağır imtihanlardan geçme zorunluluğunu gösterir. Hayat ona sık sık engeller ve sınavlar çıkarır; bu da zihinsel dünyasında mücadele ve dönüşüm temalarını öne çıkarır. Kendi nefsini tanımadan başkalarına yol gösteremez ve bu süreçte bencillik, kibir ya da tatminsizlik gibi tuzaklarla yüzleşmek zorunda kalır. Sürekli ders çıkarması gereken olaylarla karşılaşır, aksi halde aynı döngüler tekrar eder. Bu hane, kişinin düşüncelerinde hem liderlik arzusu hem de sınavlarla törpülenme zorunluluğunu yansıtır.",
        "22/4 enerjisi, zihninizde disiplin, sabır ve güçlü bir sorumluluk duygusu getirir. Kurallara sıkı bağlılık ve “ya hep ya hiç” yaklaşımı esnekliği azaltıp çevreyi çabuk yargılamanıza yol açabilir. Çevreniz sizi doğal bir lider ve koruyucu olarak görür; fakat otoriter tutumlar yakın ilişkilerde gerilim yaratabilir. En büyük imtihanlarınız öfke kontrolü ve aceleyle verilen kararlar; bu eğilimleri fark edip karar öncesi beklemeyi öğrenmeniz gerekiyor. Negatif enerji ve kişiler karşısında hassasiyetiniz olduğundan, sınırlar koyma ve kendi auranızı koruma pratiği hayati önem taşır. Kurallarınızı korurken empatiyi ve sabrı artırmak, liderliğinizin hem kalıcı hem de kabul görür olmasını sağlar."    
    ],
    [  # 2. hane - DUYGULAR
        "Önden gitmeyi arzu eder… neden öne çıkmayı istemiş? Duygu dünyası hakkında kökenine inip kendini değerli göremediği alanı bulması, kendiyle barışması gerekir. Ayrıca kişinin güçlü ve etkileyici bir ses tonuna sahip olduğunu gösterir. Konuşmalarında netlik vardır; düşüncelerini kelimelere dökme ve iletişimi yönlendirme yeteneği yüksektir. Ancak eleştirilere karşı hassas olabilir ve saygısızlık durumunda tepkili davranabilir. Diğer insanlar tarafından lider gibi görülebilir.",
        "Kişinin duygusal dünyasında şefkat, yumuşaklık ve anaç bir enerji taşıdığını gösterir. Konuştuğunuzda sesiniz huzur verici ve rahatlatıcıdır; insanlar doğal olarak size güven duyar ve ilgilenmenizi ister. Duygusal bağ kurma yeteneğiniz güçlüdür, ancak aşırı koruyucu veya takıntılı tavırlar bazen karşınızdakiler tarafından boğucu algılanabilir. Özellikle sevdiklerinizi koruma içgüdünüz yoğun olup gerektiğinde ses tonunuz sertleşebilir ve baskın bir etki yaratabilir. Hayatınızda duygusal terapi ve kendini ifade fırsatları önemlidir; hormonlar ve cinsel sağlık konularına dikkat etmeniz faydalıdır. Alma verme dengesine dikkat etmelisiniz. ",
        "Ses tonu ve konuşma biçiminizin güçlü, kararlı ve doğrudan olduğunu gösterir. Konuşurken net ve açık olmayı tercih eder, doğrudan konuya girersiniz; bu bazen karşınızdakiler tarafından sert veya zorlayıcı algılanabilir. Sözlü meydan okumaları kabul eder ve projelerde tam hakimiyet sağlamak istersiniz. Mesajınızı daha etkili iletmek için gülümsemeyi ve söyleminizi biraz yumuşatmayı öğrenirseniz iletişiminiz çok daha başarılı olur.",
        "Duygusal gelişim ağır ilerler. Zorluklar karşısında güçlü görünür ama içte sabırla büyüyen bir yük taşır. Duygularını kolay kolay açmaz. Soğuk, mesafeli ya da aşırı kuralcı davranabilir.  Kalpten şifa bulduğunda, duygusal dayanıklılığı ve derinliğiyle güvenilir bir bağ kurar. Aceleci bir yapınız ve ses tonunuz olabilir. Dürüst ve bazen de dobrasınız.",
        "Ses tonunuzun cesur, enerjik ve zeki olduğunu gösterir. İnsanlar sizin hızlı, eğlenceli ve yaratıcıdır olduğunuzu düşünür. Mizah anlayışınız ve kıvrak zekânız dikkat çekersiniz. Kelimeleri ustaca kullanır, doğrudan ve özgürce ifade edersiniz; bazen bu sert veya asi algılanabilir. Hızlı zihniniz ve sabırsız yapınız, konuşmalarınızı tempolu ve dinamik kılar. İnsanlarla iletişiminizde entelektüel bir etki bırakırken, bazen aşırı konuşkanlık nedeniyle karşı tarafı şaşırtabilirsiniz.",
        "Sezgisel bir sevgi anlayışı vardır. Yardım etmeye eğilimlidir ama bu çoğu zaman kendi ihtiyaçlarını bastırarak olur. 'Güzin Abla' rolüne sıkışabilir. Sevgiyi babadan bekliyor olabilir. dengelediğinde, şefkatli ama kendini tüketmeyen bir denge oluşturur. İnsanlar sizi samimi sorumluluk sahibi ve öğretici olarak görebilir.",
        "Duygusal olarak kolay tatmin olmayan bir yapıya sahiptir. Anne-baba sevgisine doyamamış olabilir. Bu eksiklik, ilişkilerde sürekli daha fazlasını istemesine yol açar. Değersizlik duygusu derinlere işlemiş olabilir. arayış içinde. Sesiniz genellikle kısık, sakin ve utangaç bir tonda çıkar; bu nedenle insanlar söylediklerinizi sık sık tekrar ettirir. Konuşmalarınız başta soğuk ve mesafeli algılansa da, kendinizi rahat hissettiğinizde sesiniz bilgeleşir, eğlenceli ve içten bir hâl alır. ",
        "Aurayı korursa zengin olur.. Otoriter olabilir; kontrol ve güç ihtiyacıyla duygular bastırılabilir. Sesiniz güçlü, otoriter, kararlı ve etkileyici bir tonda çıkar; konuştuğunuz anda herkesin dikkati size yönelir. Zaman zaman konuşmalarınız emir verir gibi algılansa da, aslında siz sabırlı, sorumluluk sahibi ve rehberlik etmeye odaklısınız.",
        "Ya duygularını çok frenliyor, ya da aşırı sınırları açık.. Anlaşılmayacak kadar saf ve iyi niyetli olabilir..Şifacı bir kalptir. Duygusal olarak çok saf, çok açık olabilir. Duygular konusunda sınırlarınızı çizmelisiniz ve netleşmelisiniz. Çocuksu , yardımsever bir ses tonununuz olabilir. Aynı zamanda hizmet ehli ve yardımsever bir yapınız vardır",
        #11
        "Hanedeki 11/2 rakamı, duygularını içinde yaşayan ve belli etmeyen bir yapıyı gösterir. Bu nedenle duygularını biriktirir ve zamanla patlamalara yol açabilir. Yakın ilişkilerde aşırı koruyucu ya da takıntılı tavırlar sergileyerek karşı tarafı boğabilir. İçsel baskı ve duygusal gerilim sık görülür; bu da bedensel olarak üreme organlarıyla ilgili sorunlara yansıyabilir. Alma–verme dengesini kurmakta zorlanır, çoğu zaman kendini geri plana atar. Duygusal terapi ve kendini ifade etme yolları bulmadıkça içsel huzursuzluğu artar. Görünürde anneye bağımlı gözükmese bile anneye bağımlı bir yapısı olabilir. Bu konuda farkındalık oluşturmalı."
    ],
    [  # 3. hane - HİTABET VE TİCARET
        "Kişinin dünyaya açılma ve ifade tarzında liderlik, bağımsızlık ve kendi yolunu çizme arzusu taşıdığını gösterir. Bu kişi dünyaya bir iş kurmak, temeller atmak ve kendi ayakları üzerinde durmak için gelmiştir. Emir almayı sevmez; kendi yolunu kendi çizer. Ancak önce kendi kökenindeki sorunları temizlemesi gerekir. Liderlik ruhu vardır, ama bu liderliği sağlam zemine oturtmak için içsel dönüşüm yaşamalıdır. İletişiminde net, güçlü ve yönlendirici bir tavır sergiler. Ticari ya da sosyal hayatta bağımsız olmak ister; en uygun meslekler kendi işini kurabileceği ya da liderlik rolü üstlenebileceği alanlardır. Ancak kalıcı başarı için kibirden uzaklaşıp, iş birliğiyle ve empatiyle hareket etmesi gerekir.",
        "Hitabet ve ticaret hanesi, sevgi ve duygularla açılmış. Bu kişilerin yaptıkları işte duygularını ortaya koyabilmeleri, işlerini sevmeleri lazımdır. Sevmeyi öğrenmek zorundadır. Ortaklık enerjisi güçlüdür; işlerini ortaklıkla büyütebilir. Ancak ilişkilerde fazla yumuşak olabilir. Duygusal dengeyi sağlarsa iş yaşamında da dengeli ilişkiler kurabilir. Bu hane iş birliği geliştirme ve empati becerisi verir. İçindeki şefkat çevresine güvenli bir alan oluşturmasına yardım eder. Fakat başkaları için fazlaca fedakârlık yapmak, kendi ihtiyaçlarını görmezden gelmesine neden olabilir. Gerçek denge, hem sevmeyi hem de sağlıklı sınırlar koymayı öğrenmekle oluşur.",
        "3 enerjisi kişinin dünyaya kendini ifade ederek açıldığını gösterir. Güçlü bir hitabet ve ifade enerjisi taşır; ancak dili sivri ya da kırıcı olabileceği için sözlerini dengelemeyi öğrenmelidir. Yaşadığı baskıları çözmesi halinde etkili bir konuşmacı veya yazar olabilir. Bastırılmış duygular ifade edilmezse hem iletişimde sorunlar yaşatır hem de mide ve sindirimle ilgili rahatsızlıklara yol açabilir. Gerçek gücü, duygularını yapıcı bir dille ifade edebilmesinde saklıdır. Bu sınavı aşma yolunda tek başına kalabilir.",
        "Kalp çakrasıyla dünyaya açılan bu kişi, ilişkilerinde yoğun sevgi ve ilgi gösterme eğilimindedir; ancak bu, zaman zaman sıkıntılara yol açabilir. Erken yaşta yaşadığı kayıplar ya da duygusal boşluklar, onun hitabetini ve karar verme yetisini derinden etkilemiştir. Sabırla, ağır adımlarla ilerler ve konuşmadan önce çok düşünür. Gerçek dengeyi bulması, sevgiyi önce ilahi kaynağa yöneltmesiyle mümkün olur; aksi halde başkalarına fazla değer vererek kendi değerini zedeleyebilir. ",
        "Bu kişi özgürlüğe büyük önem verir; kısıtlandığını hissettiğinde asileşebilir ve anında hareket etmeyi ister. Rutin işler onu yorar. Hareket halinde olmalı. Kendini ifade etme, fikir üretme ve iletişimde çok yeteneklidir; kelimeleri etkili ve ikna edici kullanabilir. İşlerini ve projelerini bağımsız yürütmekten hoşlanır, müdahaleye tahammülü yoktur. Seyahat, keşfetmek ve yeni deneyimler yaşamak onun enerjisini yükseltir; cesur ve özgür olduğu sürece yaratıcılığı ve zekası maksimum düzeyde çalışır.” Ancak etraftan hızlı etkilenebilir. Negatif frekansa geçtiğinde içe kapanma, depresyon ve enerji düşüklüğü yaşanabilir.",
        "Ailesel yüklerle ticari ya da ifade alanı iç içedir. Bu kişi sezgisel zekâya sahiptir, sorumluluk alma yeteneği gelişmiştir ve disiplinidir. Bu yüzden iyi bir öğretmen, danışman ya da ebeveyn olabilir.  Ancak ailesinden gelen korkular veya beklentiler, onun dış dünyaya açılımını zorlaştırabilir. Bu yüzden de etrafındakilere fazla korumacı davranabilir. İçsel özgürlükle ifade gücü arasında bir köprü kurmalıdır. ",
        "İfade ve iş alanında sürekli tatminsizlik ve arayış olabilir. Birden fazla üniversite okuyabilir. Alan değiştirebilir. Hep farklı iş ve eğitim yolları arayabilir. Bu durum ilişkilerde doyumsuzluk olarak da yansıyabilir. Matematiksel ve analitik zekâya sahip olsa da, duygusal tatmin sağlanmadan ifadeleri yeterince tatmin edici olmaz. Spiritüel alandan kazanç sağlama veya kendini yeniden inşa etme temalarına da sahiptir. Şükür ve kanaat duygusunu öğrenmek, iç huzur ve tatmin için gereklidir.",
        "Doğuştan ticaret, para ve otorite enerjiniz ve isteğiniz vardır; sorumluluk alma ve yönetme yeteneğiniz güçlüdür. İş ve ilişkilerde sınırlar koymak sizin için önemlidir, bu sayede başarılı ve güvenilir bir lider olabilirsiniz. Ticarette ve gelir elde etmede başarılı olabilirsiniz, ancak kibirli veya aşırı kontrolcü davranmaktan kaçınmalısınız. Zenginlik enerjisi, aura korunup denge sağlandığında tam olarak işler. Nazara, negatif enerjiye ve helal rızka dikkat etmek önemlidir. Ayet-el Kürsi okunmalı.",
        "İletişimiz derin bir şifa potansiyeli taşır. Kelimeleriyle insanlara iyi gelebilir. Hitabetiniz ve bilginiz, ruhsal olgunlukla birleştiğinde bu etkiyi açığa çıkarırsınız. Kazancınız doktorluk hemşirelik gibi şifalandırıcı mesleklerden gelebilir (8.haneye de bakılmalı), ancak unutmayın ki önce kendi yaralarınızı sarmadan başkalarına fayda sağlayamazsınız. İşiniz ve ilişkileriniz arasındaki sınırlara dikkat etmelisiniz. Hayal gücünüz geniş, çocuksu ve iyimser bir yapınız vardır; dünyayı keşfetmek ve insanlara fayda sağlamak ister, ancak günlük işlerde kolayca kaybolabilirsiniz. Bilgiye aç ve paylaşımcı bir insansınız; ilginizi çeken konulara büyük bir inat ve kararlılıkla yönelirsiniz. ",
        #11 19 22
        "11/2 rakamı, kişinin iletişiminde derinlik ve yoğunluk taşıdığını ama bunu dengede tutmakta zorlandığını gösterir. Duygularını bastırdığında biriktirir ve sonunda ani patlamalarla dışarı vurur; bu da çevresinde anlaşılmazlık ve çatışma yaratır. Bağımsız hareket etme ve kendi yolunu çizme arzusu belirgindir, ancak çocuklukta yaşadığı travmalar bu süreci zorlaştırabilir. İletişimini düzelttiğinde güzel ortaklıklar kurar ama yine de Emir almayı sevmez, otoriteye karşı koyma eğilimindedir ve bu durum hem iş hem ilişkilerde sürtüşmelere yol açabilir. Ticari ve sosyal alanda güçlü adımlar atmak ister fakat sabırsızlık ve kibir, ilişkilerini zedeleyebilir. Kalıcı bir başarı için içsel dönüşümünü tamamlaması ve iş birliğiyle hareket etmesi şarttır.",
        "19/1 rakamı, kişinin dünyaya açılırken liderlik ve bağımsızlık arzusu taşıdığını gösterir. Öne çıkmak, otorite kurmak ve kendi yolunu çizmek ister; ancak bu süreçte çocuklukta yaşanan travmaları fark edip kabullenmesi gerekir. İmtihanlar yoluyla dönüşüm ve manevi olgunluk kazanır; olayların altındaki mesajları çözmek ve ders çıkarmak onun için önemlidir. İletişimde net, güçlü ve yönlendirici bir tavır sergiler, ancak kibir ve aşırı kontrolcülükten kaçınmalıdır. Ticari veya sosyal hayatta bağımsızlık arzusu baskındır; kendi işini kurmak veya liderlik rolü üstlenmek için uygundur. Manevi farkındalık geliştirmediği sürece hatalı kararlar ve ilişkilerde sorunlar yaşayabilir. İyileşmeye niyet ettiğinde, şifalı ve insanlığın hayrına çalışacak bir potansiyel ortaya çıkar.",
        "22/4 rakamı, kişinin dünyaya kalp çakrası üzerinden açıldığını ve yoğun duygusal deneyimler yaşadığını gösterir. Bu kişi ilişkilerinde derin sevgi ve ilgi gösterir, ancak erken yaşta yaşadığı kayıplar ve duygusal boşluklar hitabetini ve karar alma yetisini zorlamıştır. Sabırla ve ağır adımlarla ilerler, konuşmadan önce derin düşünür. Aşırı değer verme eğilimi, kendi iç dengesi bozulduğunda sıkıntılara yol açabilir. Bu imtihanlar, kalp çakrasını açmak ve maneviyatını güçlendirmek için verilmiştir; mesaj almayı bilmezse ilişkilerinde ve kararlarında sorunlar yaşar. Ancak, olanı olduğu gibi kabul edip ilahi kaynağa yöneldiğinde, hem makamı hem de etkisi yükselir."    
    ],
    [  # 4. hane - SEVGİ, OLGUNLUK
        "Sevgi alanında güçlü bir şekilde öne çıkma, fark edilme ve kendi varlığını ortaya koyma isteğiniz vardır (köklenme problemi). Kalbinizden gelen bu enerji, hem sevme biçiminizde hem de ilişkilerinizde özgünlük arayışıyla kendini gösterir. Başkalarının yöntemlerini benimsemek yerine, kendi yolunuzu çizmekten hoşlanırsınız. Denetimi kaybetmek sizi zorlayabilir; kontrolün sizde olduğu ortamlarda daha huzurlusunuzdur. Çocuklukta aileyle yaşanmış duygusal yaralar sevgi alışverişinizi etkileyebilir; bunları kabul edip dönüştürdükçe kalbinizdeki sevgi daha olgun ve akışkan hale gelir. Ara ara kafanızdaki kalıplarınızı sorgulamalısınız. İskelet sistemi ve kas sistemi ile ilgili hastalıklara yatkınlığınız olabilir.",
        "Kalbinizdeki sevgi çoğunlukla başkalarını gözetmek, onların iyiliğine katkı sağlamak üzerinden akar. Hayatındaki dişil figürlerle veya yakın ilişkilerle zorluklar yaşamaya meyillidir. Çünkü duygularını bastırır ve zamanla biriktirir; bu da ani veya kontrolsüz tepkilere neden olabilir. Duygusal yakınlıklarda ciddi ilkesizlik ya da aşırı fedakârlık görülebilir. Huzur bulması için önce duygu kontrolünü öğrenmesi gerekir. Sevgide dengeyi bulmak, yalnızca vermek değil aynı zamanda almayı da kabul etmektir. Sahip olduklarınızı koruma içgüdünüz güçlüdür; bu yüzden güven duygusu sizin için çok önemlidir. Negatiflikleri açtığınızda yakın ilişkileriniz sizin yeteneğiniz haline gelir.(Hızlı bağ kurma, empati)",
        "İç dünyanızı paylaşmak ve anlaşılmak sizin için çok önemlidir. Duygularınızı bastırdığınızda sıkışır, ifade ettikçe ise rahatlar ve güçlenirsiniz. Konuşup anlaşıldıkça iyileşir, kendinizi daha özgür hissedersiniz. Ancak anlaşılmama korkusu sizi suskun bırakabilir. Konuşarak, paylaşarak ve bastırılmış duyguların kaynağına inerek ilerlediğinizde hem içiniz hem bedeniniz rahat eder. İfade etmek, kendiniz için bir şifa kapısıdır. Mide problemine yatkınlığınız olabilir. Bunun için hazmedemediğiniz duygularla yüzleşmelisiniz ve hazmedememenin kibirden olduğunu bilmelisiniz.",
        "Hayat yolculuğunuzda kararlılık ve sabır sizin en güçlü yanınızdır. Zorluklar karşısında kolay kolay yıkılmaz, istikrarlı bir şekilde yolunuza devam edersiniz. Ancak bu süreçte çoğu kez yalnız hissedebilir, ağır kalbî sınavlardan geçebilirsiniz. İmtihanlar sizi olgunlaştırmak, esneklik kazandırmak için gelir. Bu nedenle kalp sağlığınıza, hem bedensel hem duygusal olarak özen göstermeniz çok önemlidir. Sınırlarınızı bilmek, gerektiğinde ‘hayır’ diyebilmek ve kendinizi değersiz hissettiren fedakârlıklardan uzak durmak sizin için şifalı bir dengeyi getirir.",
        "Kalpteki sınavları, imtihanları şükrederek aşar.  Şükür pratiği ve olumlu bakış, zor duyguları yumuşatır; geçmiş hatalar ve gereksiz tavizler için kendini suçlamayı bırakmak duygusal olgunluğu hızlandırır. Baskı altında tepkisel olabileceğin için nefes/gevşeme gibi araçlarla stresi regüle etmek ilişkilere de iyi gelir.  Bu insanlar öğrenmeye açıktır ve yeni bir şey öğrenip konfor alanından çıkarak rahatlar; bu yenilik ruhu sevgiyi taze tutar.  Ek olarak, tiroid hassasiyetine dikkat (5. Çakra tıkalıysa) ve düzenli kontrol, duygusal dengeyi destekleyen önemli bir adım olabilir.",
        "İmtihan sebebi aile ve otoritedir. Aile, özellikle baba figürüyle ilgili yükler kalp merkezinde taşınır. Bu kişi sevgiyi sezgisel yollarla anlamaya çalışır ama korkularının ve geçmişten gelen kontrolcülüğün(evham, korku mu desem) etkisiyle sevgiye teslim olmakta zorlanır. Aileden öğrendiği modelleri kırması şarttır. Yoksa aynı döngüleri tekrarlar. Sevdiğinde fazla sorumluluk altına girebilir. Bu sıkıntıları aştığında çok güzel bir öğretici olur. Sezgileri çok açık olur. Feraset sahibi olur.",
        "Bu kişiler sevginin gerçek kaynağının İlâhî olduğunu kabul etmeli. Böylelikle yüzeysel bağlılıklardan ve sahte sevgi arayışlarından korururlar; olgunlaşmanız büyük ölçüde teslimiyeti öğrenmekle gerçekleşir. Zekanızdan dolayı bunda zorlanabilirsiniz. Zihinsel sorgulama, maneviyat arayışı ve sürekli anlam peşinde koşmak bu kişinin sevgi alanına da yansır. Duygularınızı yalnızca analiz etmek yerine arada kalben deneyimlemeyi öğrenirseniz ilişkileriniz derinleşir ve daha az çatışma yaşanır. Zekânız, yaşadığınız sınavların mesajını çözmede en büyük dayanağınızdır. Tefekkür edip ders çıkardıkça aynı döngüler azalır. Hislerinizi ifade etmek ve üzerinde düşünmek, hem içsel şifaya hem de olgun bir sevgi alışverişine götürecek pratik bir yoldur.",
        "Güç ve otoriteyi kullanarak sorunları aşar. 'Beni olduğum gibi kabul et, yoksa çekil' tavrı baskın olabilir. Bu yaklaşım, gerçek bağ kurmayı zorlaştırır. Sevgiyi paylaşmak yerine, hakimiyet alanı kurmaya çalışır. Zenginlik ve bereket enerjisini kalp alanına taşıyabilmesi için yumuşaması gerekir. Zorluklar karşısında yönetici ve toparlayıcı bir karakter sergiler. Bu durum çevrenize düzen ve güven getirebilir ama bunu sevgiyle birleştirdiğinizde hem siz hem de etrafınızdakiler şifa bulur. Bu süreçte Kendinizi iyi tanıyın, enerjinizi koruyun ve olumsuz ortamlardan uzak durun ki auranız güçlü olsun. ",
        "kalbinizde saflık ve sınır sorunlarını beraber getirir. Fazla saf olup herkese evet diyebilir veya aşırı mesafe koyarak sürekli hayır diyebilirsiniz; bu yüzden dengeyi bulmak kritik önemdedir. İnsanlara yardım etmek ve paylaşmak size büyük tatmin sağlar, ancak sınırlarınızı koruyup gerektiğinde hayır demeyi öğrenmelisiniz. İyi niyetiniz, hayata meraklı ve taptaze bir gözle bakmanıza olanak tanır, fakat bu bazen kandırılmanıza veya asıl meseleyi gözden kaçırmanıza yol açabilir. Yeni başlangıçlara hızlı uyum sağlarsınız, ancak aşırı tutku ve inatçılık kendinize zorluk yaratabilir. Hayat sizin için bir oyun alanıdır; keşfetmeyi ve eğlenmeyi seversiniz. Bu hanedeki yeteneğiniz, insanlara şifa ve destek sunma kapasitenizdir. Kalbinizi koruyup dengeyi sağlamak, olgunlaşmanız için şarttır. Olgunlaştığınızda bilge bir yapınız olur",
        #11 19 22
        "11/2 enerjisi, kalbin sevgiyi başkalarının iyiliğine hizmet ederek gösterdiğini ve ilişkilerde derin bir empati yeteneği sunduğunu gösterir. Ancak duygularını bastırma eğilimi, ani tepkilere ve aşırı fedakârlığa yol açabilir. Bu kişi, prensiplerini koruyarak ve gerektiğinde hayır demeyi öğrenerek kendini savunmalıdır. Kalp çakrasının tam açılmaması, ilişkilerde sıkıntılar ve değersizlik hissi yaratabilir. 11 enerjisi, inatçılık, hedeflerine odaklanma ve hayallere sıkı bağlılık getirir; bu, hem kişisel gücünü hem de ilişkilerdeki kararlılığını destekler. Yeteneği, hızlı bağ kurabilme ve empati yoluyla başkalarına rehberlik etmesidir. Sevgiyle dengeyi bulduğunda, hem kendini hem de çevresindekileri olumlu etkileyebilir.",
        "19/1 enerjisi, kişinin sevgi ve ilişkilerde öne çıkma, fark edilme ve kendi yolunu çizme isteğini gösterir. Bu kişi başkalarının yöntemlerini benimsemek yerine özgünlüğünü korur ve denetimin kendisinde olduğu ortamda daha huzurludur. Çocuklukta yaşanan duygusal yaralar, sevgi alışverişini etkileyebilir; bunları kabul edip dönüştürdükçe kalbi olgunlaşır ve akışkanlaşır. Sıkıntıları fark edip olayların altındaki mesajları çözme yeteneğine sahiptir. Enerjisini iyileşmeye ve başkalarına şifa vermeye yönlendirebilir. Bunun yanında, iskelet ve kas sistemiyle ilgili hassasiyetler olabilir. Bu hane, kişinin sevgi alanındaki yeteneğini, farkındalık ve dönüşümle birleştirerek güçlü bir şifa ve rehberlik kapasitesi sunar.",
        "22/4, kişinin sevgi ve olgunluk yolculuğunda sabır ve kararlılıkla ilerlediğini gösterir. Ağır kalbî sınavlardan geçebilir ve bu süreçte zaman zaman yalnız hissedebilir. Bu imtihanlar, onun olgunlaşmasını ve esneklik kazanmasını sağlar. Sınırlar koymayı ve gerektiğinde “hayır” demeyi bilen kişi, kendini değersiz hissettiren fedakârlıklardan uzak durarak duygusal dengesini korur. Kalp sağlığına hem bedensel hem de duygusal olarak özen göstermesi çok önemlidir. Bu hanede kişi, hem içsel rehberlik yeteneğine hem de başkalarıyla dengeli ilişkiler kurma becerisine sahiptir."
    ],
    [  # 5. hane - ŞÜKÜR VE DOYUM
        "Doyum ve şükrü bulmayı zorlaştırabilir. Bu kişi çoğunlukla tatmini hep daha ileri bir hedefte arar ve hiçbir şeyle kolay kolay yetinmez. Kendisine dair yüksek beklentiler taşır. İçsel eleştirileri çok güçlüdür; kendine sürekli yüklenir, “daha iyisi olmalıydı” diyerek huzurunu bozar. Ego, kibir ve sabırsızlık nedeniyle ilişkilerde sorunlar yaşayabilir. Duygularını bastırdıkça öfke ve saldırganlık ortaya çıkabilir. Bilinçaltındaki aile kökenli yaralar, ilişkilerinde tekrar tekrar yüzeye çıkıp doyumu engeller. Önce tepkilerini bilinçaltından bilinç düzeyine çıkarmalıdır. Aşırı kontrolcü ya da emredici tavırlar, değer görme ihtiyacını daha da zedeler. Gerçek şükrü öğrenmedikçe hep huzursuzluk ve tatminsizlik döngüsü yaşar.",
        "Bağ kurma yeteneği çok yüksektir. Sevgi ve ilgi açlığı baskındır. Duygusal ilişkilerde bağımlılık geliştirme eğilimi vardır. Sevgi alma konusunda doyum yaşamadığı için, geçmişte özellikle anneyle olan ilişkiden kaynaklı bir eksiklik taşır. Romantik ilişkilerde fazlasıyla verici ya da yapışkan olabilir. Sürekli bir 'doyurulma' beklentisi taşıyabilir.",
        "Çocuklukta yer yer bastırılmış ve çekingen bir yapıyı gösterir; bu durum, kendinizi ifade etmekte ve içsel huzuru bulmakta zorluk yaratır. Konuşmak ve paylaşmak keyif kaynağı olsa da, çoğu zaman bunun arkasında onay alma ve görünme ihtiyacı bulunur. İçsel doyumunuz büyük ölçüde dışsal etkileşimlere bağlıdır; yalnız kaldığınızda huzursuzluk ve tatminsizlik hissi artar. Bastırılmış duygular ve kibir, çevrenizle ilişkilerde zaman zaman iğneleyici ve sivri tavırlara yol açabilir. Yine de iletişim yeteneğiniz ve başkalarına ilham verme kapasiteniz, sizin güçlü yanınızdır. Kendinizi ifade etmeyi öğrenmeniz, hem zihinsel hem de bedensel olarak rahatlamanızı sağlar. Bu sayede şükür ve doyumu daha gerçek bir şekilde deneyimleyebilirsiniz.",
        "Aşırı merhamet ve verici bir yapının sınırlarını gösterir; başkalarının acılarına odaklanmak kendi ihtiyaçlarınızı görmezden gelmenize ve tükenmişlik hissetmenize yol açabilir. Hayır demekte zorlanmak, sınır çizme konusunda sıkıntı yaratır ve sorumluluklar altında ezilmenize neden olabilir. İnsanlara çabuk güvenmek ve aşırı verici olmak, aldatılma ve kandırılma riskinizi yükseltir. Öfkenizi ve tepkilerinizi kontrol etmeyi öğrenmezseniz, ilişkileriniz zarar görebilir. Kendinizi öncelikle korumayı ve gücünüzü kendi yararınıza kullanmayı öğrenmelisiniz. Yine de bu hanedeki olumlu yönünüz, güçlü bir merhamet kapasitesine sahip olmanızdır; başkalarına yardım etmekten gerçek bir tatmin alabilirsiniz. Hayatınızda alma verme dengesini sağladığınızda şükür ve doyumu daha sağlıklı deneyimleyebilirsiniz.",
        "Şükürsüzlük ve doyumsuzluk temalarını öne çıkarır; kişi sık sık sevilmediğini hissedebilir ve sürekli bir eksiklik duygusu taşıyabilir. Bu durum, aşırı bağlanmalar ve bağımlılıklara yol açabilir, ilişkilerde aynı döngülerin tekrarını yaşamasına neden olur. İç huzursuzluk ve stres yönetememe, yanlış kararlar almasına ve potansiyelini tam kullanamamasına sebep olabilir. Hayatta şükretmeyi öğrenmek ve hatalardan ders çıkarmak, bu imtihanı aşmanın anahtarıdır. 5 i 5 ile açtığını için bu durumu kendi başına çözmesi gerekebilir.  Aksi halde şükür hali yüzeysel kalır ve doyum elde edilemez. Ancak hızlı düşünme ve analiz yeteneği, doğru şekilde kullanıldığında, stresli durumlarda bile çözüm bulmasını sağlar. Kendi çabasıyla bu dersi alırsa, başkalarının kalbine dokunma ve nimetten faydalanma kapasitesi artar. Bu sayede hem içsel huzur hem de gerçek doyum deneyimlenebilir. ",
        "Güven veren, sadık sahibi bir yapıyı verir. Aileye yönelik aşırı sorumluluk duygusu, bu kişiyi sürekli veren pozisyonda tutar. Doyum yaşamaktan çok, başkalarının ihtiyaçlarını karşılamaya odaklıdır. Özellikle baba figürüyle ilişkisi belirleyici olabilir.  Şükretmek yerine 'vermek zorundayım' hissiyle hareket etme ihtimali vardır. Kendinizi aşırı verme döngüsünden kurtarmak ve dengeli sınırlar koymak önemlidir. Maneviyatınızı güçlendirmek ve aile sorunlarını kabullenmek, şükür ve tatmini artırır. Kişi bu durumları aşamıyorsa evham ve vesvese sıkıntısı yaşar.",
        "Derin bir sevgi arayışına ve tatminsizlik hissine işaret eder; kişi sık sık “neden bana yetmiyor?” sorusuyla baş başa kalır. Tatminsizlik hissi içini kemirebilir. Bağımlılıklar ve ilişkilerde tekrar eden döngüler, içsel huzuru zorlaştırır. Utangaçlık kendinizi göstermekte ve yeteneklerinizi kullanmakta engel olabilir. Dış dünyanın etkisi arttığında somurtkan ve aksi tavırlar ortaya çıkabilir, mutluluğun sorumluluğunu başkalarına yükleme eğilimi görülebilir. Farkındalık ve analitik düşünme eksiliği olayların mesajlarını doğru algılamayı engeller. ",
        "Bu hanedeki 8 rakamı aura problemini verir. Bu insanlar doyumu; otorite, güç ve maddi mutlulukla özdeşleştirme hatasına düşebilir. Sahip olmak, yönetmek, kazanç elde etmek ve konfor alanları yaratmak önceliklidir. Zaafı da budur. Bu durum, çevrenize karşı baskıcı ve zorlayıcı davranışlara yol açabilir. farkında olmadan insanları kırabilirsiniz.  Aura problemini çözerlerse girişimci ve fırsatları değerlendiren bir yapıya sahiptir. Ayet el kürsi önerilir. ",
        "Sevgide sınırlara dikkat.. Şefkatlidir ama sınır koymakta zorlanır. Ruhsal rehberlik, danışmanlık hizmeti ve yalnız zamanlar, içsel doyumu artırır.",
        #11
        "11/2 kişinin ilişkiler ve doyum konularında en büyük imtihanını simgeler. Bağ kurma yeteneği yüksek olsa da, sevgi ve ilgi açlığı kolayca bağımlılığa dönüşebilir. Anneyle güçlü ya da zayıf bağlar, yetişkinlikte tatminsizlik ve sürekli beslenme beklentisi yaratır. Dışarıya pek belli etmses de duygusal krizleri ve patlamaları ilişkilerde sağlıksız döngülere yol açabilir. Kişi bazen başkalarının duygularını anlamak yerine kendi kurgusuna göre tepki verebilir; bu durum hem özel hem iş yaşamında kriz ve baskıcı tavırlara neden olur. İçsel şükür ve tatmin gelişmediğinde sürekli boşluk hissi yaşar. Ailenin ve geçmişteki dişil figürlerin travmalarını anlamak ve şifa yöntemleriyle işlem yapmak ve sakral çakrayı iyileştirmek, bu döngüyü kırmada önemlidir."    
    ],
    [  # 6. hane - AİLE, BABA
        "Beni dinleyeceksin!' mesajı veren bir yapıdadır. Düşüncelerine aşırı değer verir ve otorite kurmak ister. Çocuklukta sesinin duyulmaması, ailede yeterince ciddiye alınmaması bu tepkinin kaynağı olabilir. Baba ile çatışma yaşanmış ya da babadan onay alınamamış olabilir. Aile içinde bireysel kimliğini ortaya koymak için savaş vermiştir.",
        "Aileye ve ailesi olarak gördüğü insanlara, özellikle ebeveynlerine duygusal olarak bağımlı olabilir. Çoğu zaman çocuklukta sevgiyi eksik almıştır ve bunu yetişkinlikte telafi etmeye çalışır. İlişkilerde sürekli onay arayışıyla davranabilir. Kendi sınırlarını çizmekte zorlanır. Duygusal olarak doyumsuz ve kararsız bir yapı gelişebilir.",
        "Aileyle özellikle baba ya da diğer “eril” figürlerle iletişim kurma becerisi gelişmeli, kendisini ifade ederek temas kurmalı. Bu kişi, müdahaleci aile yapılarında büyümüş olabilir. Dedikodular, yönlendirmeler veya otorite baskısı yaşamış olabilir. Konuşarak çözüm arar. Aynı zamanda bu açılım, “aile içinde konuşarak var olma”, fikir beyan etme, kendini ifade ederek ailede konum kazanma gibi dinamiklere de işaret eder.  Kişinin ailesiyle –özellikle babasıyla– olan ilişkisinin, mesleki yönelimini doğrudan etkilediğini gösterir. Çoğu zaman bu kişi, babasının mesleğine benzer bir alana yönelir ya da babanın iş anlayışı, vizyonu, yöntemleri üzerinde güçlü bir etkide bulunur.",
        "Sert ve sabır gerektiren bir aile yapısından gelir. Bu yüzden sizin de ilişkilenme kuralcı bir yapıda olabilir. Erken yaşta baba ile imtihan (4ü de 6 ile açmışsa çok ciddi olabilir), babanın yokluğu ya da duygusal erişilemezliği görülebilir. Sevgiye ulaşmak için ciddi çaba sarf etmiştir. Aileyle ilişkilerdeki kuralcılık ve katılık kişiye de geçmiş olabilir. Sevgi onun için “hak edilmesi gereken” bir şey haline gelmiştir. Ailede sabırlı ve kararlı bir yapıya sahipsiniz. ",
        "Sorumluluk almaktan çekinmeyen bir yapıdadır. Ancak bu özelliği çoğu zaman otomatikleşmiştir. Aile içinde erkenden olgunlaşmak zorunda kalmış olabilir. Bu da kişinin içsel çocuk enerjisini bastırmasına neden olabilir. Hayatta ilerlerken şükürle sorumluluğu dengelemek onun için önemlidir.  Stress ve aildeki sorunlar modunuzu ve frekansınızı çok hızlı düşürür. Bağlanmaktan ve kendinizi kısıtlanmış hissetmekten hiç hoşlanmazsınız. ",
        "Aile ve baba figürüyle ilişkilerde sorumluluk yükünü ağır hissetmeye eğilimli bir yapıyı gösterir. Kişi, aile içinde ve ailesi olarak gördüğü insanlara karşı fazla kontrolcü ve müdahaleci davranabilir, boşlukları kendisi doldurmaya çalışabilir ve bu durum ilişkilerde gerilim yaratabilir. Aşırı korumacılık ve çatışma eğilimi, özellikle otorite figürleriyle ilişkilerde belirginleşir. Duygusal esneklik geliştirilmezse, bu tavır hem aile hem de çevrede sorunlara yol açabilir. Olumlu yön olarak, başkalarını koruma ve destekleme isteği, insan yetiştirme veya rehberlik gerektiren alanlarda başarı sağlar.",
        "Baba figüründe dişil bir enerji olabilir. Ya da kişi, ailede “anne” rolünü üstlenmiş olabilir. Ailede manevi temalar baskındır, ancak bu ruhsallık ve maneviyat bazen kaçış halini alabilir. Gerçek sorunlarla yüzleşmek yerine idealleştirme eğilimi vardır. Kişinin ailedeki rollerle kendi kimliğini ayırt etmesi gerekir. Bu insanlarda ailevi ve yakın ilişkilerinde tatmin olamama ve beklentiye girme durumları olabilir. Bunun bilincinde hareket etmeli. Tatminsizlik oluştuğunda, beklentiyi bırakmalı, kanaatkar olmalı, bardağın dolu tarafını görmeli,  ve maneviyatını güçlü tutmalı.",
        "Aileyle, özellikle babayla maddi ilişkiler öne çıkabilir. Parasal konularla aile içi bağlar iç içe geçmiş olabilir. Eğer kişinin babasıyla arası iyi değilse bolluk ve bereket enerjisi akmaz. Güç ve para ilişkileri üzerinden sevgi tanımı oluşmuş olabilir. Aileyle iyi geçinmek, sadece duygusal değil, enerjisel ve parasal düzeyde de bir açılım sağlar. Ailevi ve yakın ilişkilerinizde otoriter ve baskın olabilirsiniz.  Babayla arası iyiyse babadan parasal destek görebilir. Çoğu zaman bu kişi, babasının mesleğine benzer bir alana yönelir ya da babanın iş anlayışı, vizyonu, yöntemleri üzerinde güçlü bir etkide bulunur.",
        "Aile içinde, babasıyla veya otoriteyle sınır problemleri yaşayabilir. Kendi alanını korumakta zorlanır. Bu alanda hayır öğrenmesi gerekir.  Suistimal ya da aşırı fedakârlık döngüsü görülebilir. Aile ilişkilerinde şifa ancak net sınırlarla mümkün olur. Kendi bireysel alanını belirlemeden ilişkilerde huzur bulması zordur.",
        #11
        "Bu hanedeki 11/2 açılımı aile ve babayla ilgili derin duygusal krizler taşır; çocuklukta eksik kalan sevgi yetişkinlikte onay arayışına ve duygusal bağımlılık eğilimine dönüşebilir. Baba figürünün koşullu sevgi ve manipülasyonları (“bunu yaparsan seni severim”) güven duygusunu zedelemiş, sınır koymayı zorlaştırmıştır. Bunun sonucu olarak ilişkilerde kararsızlık, duygusal yorgunluk ve sık sık kendini değersiz hissetme görülebilir. Öte yandan 11 enerjisi inatçı bir kararlılık ve vizyon verir; hayallerine tutunma, dirayet ve hedefe odaklanma kapasiteniz yüksektir. En güçlü yeteneğiniz, empati ve sezgisel anlayışınızı kullanarak başkalarına rehberlik edebilmenizdir — fakat bunun sürdürülebilir olması için net sınırlar koyup gerektiğinde “hayır” demeyi öğrenmelisiniz.",
    ],
    [  # 7. hane - ANNE, İMAN
        "Kişi anneye benzeyebilir. Kökten gelen sorunları ancak güçlü bir iradeyle aşabilir. Anneyle ilişkisi ya mesafelidir ya da rekabetlidir. Bu kişi için “kendi ayakları üzerinde durmak” temel inanç haline gelmiştir. Maneviyatı güçlenmeden içsel huzura ulaşması zordur. Kişiye manevi aktarımlar vardır.",
        "Sevgi beklentisini anneden veya dişil figürlerden karşılamak ister. Dişil figürlere zaafiyeti olabilir. sevilmek için kendinden ödün verebilir. “Ben değerli miyim?” sorusu içten içe onu yorar. Sevgiyi bulduğunda çok derin bağlar kurabilir. Empati gücü gelişmiştir.",
        "Sözel ifade, onun anneyle ya da hayatındaki kadınlarla bağını oluşturur. Anlatma, öğretme, yazma gibi alanlarda doğuştan yeteneklidir. Sözü değerlidir (Söz sihirbazı). Kadınlarla iletişimi iyi olabilir.",
        "Anne sabır meselesi olabilir(özellikle 4 ü de 7yle açmışsa). Veya annenin duygusal olarak eksikliği mevcut olabilir. Bu kişi duygusal olarak erken olgunlaşmak zorunda kalmıştır. “Hayat beni zorla büyüttü” duygusu baskın olabilir. Derin sabır ve manevî farkındalık geliştirir.",
        "İştahlı. Boğaz bölgesi hassas olabilir; ifade sorunları, yutulmuş duygular görülür. Psikolojik dengesizliklere yatkın olabilir. Doyum hissi kolay oluşmaz. Hevesli bir yapısı vardır. Yaşam sevgisi yüksektir.",
        "Kendini ailesine veya çevresine “anne” gibi konumlandırabilir. Başkalarını kurtarma eğilimindedir. Sorumluluk bilinci yüksek ama bu onu duygusal olarak yalnız bırakabilir. Sezgisel rehberdir. Gerçekten dinlemeyi bilen, koruyucu ve dönüştürücü bir figür olabilir.",
        "Bu hanede 7 olması zordur. Kişi çoğu zaman inanç krizi yaşar. Kendine, hayata, sisteme ya da Yaratıcıya güven duymakta zorlanabilir. Melankoli ve yalnızlık hissi baskındır. Tahkiki iman geliştirirse, çok güçlü bir içsel merkez kurar. Derin bilgi ve manevî sezgi ile donanır.",
        "Bu hanedeki 8 rakamı aura problemini verir. Bu insanlar doyumu; otorite, güç ve maddi mutlulukla özdeşleştirme hatasına düşebilir. Sahip olmak, yönetmek, kazanç elde etmek ve konfor alanları yaratmak önceliklidir. Zaafı da budur. Bu durum, çevrenize karşı baskıcı ve zorlayıcı davranışlara yol açabilir. farkında olmadan insanları kırabilirsiniz.  Aura problemini çözerlerse girişimci ve fırsatları değerlendiren bir yapıya sahiptir. Ayet el kürsi önerilir. ",
        "Sürekli sınır ihlallerine açık olabilir (Anne müdahalesine dikkat). Anneyle ya da kadın figürlerle arasındaki sınır çizgileri bulanıktır. Ya aşırı teslim olur ya da tamamen uzaklaşır. Ruhsal sezgileri ve temiz kalbiyle gerçek maneviyatı deneyimlemeye açıktır. Şifacı potansiyeli güçlüdür.",
        #11
        "11/2 kişinin ilişkiler ve doyum konularında en büyük imtihanını simgeler. Bağ kurma yeteneği yüksek olsa da, sevgi ve ilgi açlığı kolayca bağımlılığa dönüşebilir. Anneyle güçlü ya da zayıf bağlar, yetişkinlikte tatminsizlik ve sürekli beslenme beklentisi yaratır. Dışarıya pek belli etmses de duygusal krizleri ve patlamaları ilişkilerde sağlıksız döngülere yol açabilir. Kişi bazen başkalarının duygularını anlamak yerine kendi kurgusuna göre tepki verebilir; bu durum hem özel hem iş yaşamında kriz ve baskıcı tavırlara neden olur. İçsel şükür ve tatmin gelişmediğinde sürekli boşluk hissi yaşar. Ailenin ve geçmişteki dişil figürlerin travmalarını anlamak ve şifa yöntemleriyle işlem yapmak ve sakral çakrayı iyileştirmek, bu döngüyü kırmada önemlidir."    
    ],
    [  # 8. hane - KAZANÇ VE BEREKET
        "Maddi alanda girişimcilik, liderlik ve etki yaratma enerjisini temsil eder. Doğal olarak inisiyatif alır, sesinizi duyurmak ve çevrenizdeki insanları harekete geçirmekten keyif alırsınız. İletişim ve yaratıcılığınızı kullanarak etrafınızdaki insanlara ilham verir, onlarla güçlü bir bağ kurabilirsiniz. Bağımsızlık arzunuz güçlüdür; kendi işinizi kurmak ve kendi yolunuzu çizmek için fırsatlar ararsınız, ancak bu bağımsızlık arzusu zaman zaman istikrarı sağlamakta zorluk yaratabilir. Kök çakranızın dengeli çalıştığında, otorite kurma ve liderlik yeteneklerinizi sağlıklı olur; geçmiş travmalar ve çocukluk deneyimleri üzerinde çalışmak, bu enerjiyi dengeli ve verimli kullanmanızı sağlar. Böylece hem maddi hem de sosyal alanda üretken ve etkili bir performans sergileyebilirsiniz.",
        "Başkalarına yardım etme, destek olma ve ilişkilerde denge yaratma enerjisini temsil eder. İnsanlara faydalı olabildiğinizde ve duygularınıza işinizde bir karşılık bulabildiğinizde kendinizi canlı ve motive hissedersiniz. Duygusal bağlar ve sevgi sizin için harekete geçme gücünün temel kaynaklarıdır; sevilmek ve takdir edilmek motivasyonunuzu artırır. Maddi alanda başarı ve üretkenlik çoğu zaman duygusal durumunuza bağlıdır; sevgi ve takdir aldığınızda yaratıcı ve etkili olursunuz, aksi takdirde geri çekilebilir ve motivasyonunuz düşebilir. Kendinizi ve auranızı sevgiyle beslemeyi öğrenmek, hem içsel tatmin hem de maddi verimlilik için önemlidir. Duygularınızı yansıtabileceğiniz işler, size hem memnuniyet hem de etkinlik hissi kazandırır.",
        "İletişim, ticaret ve üretkenlik enerjisini temsil eder. Karmaşık durumları hızla toparlayabilir, işleri planlayıp sonuçlandırabilirsiniz; üretmek ve iletişim sizin için motive edici bir güçtür. İnsanların yavaş hareket ettiği alanlarda devreye girer ve görevin tamamlanmasını sağlarsınız. Konuşmak, anlatmak doğal yeteneğinizdir; bu yeteneğinizi gelir elde edebileceğiniz işlere dönüştürebilirseniz, hayatınızı kelimeler ve iletişimle inşa edebilirsiniz. Kararsızlık ve dikkat dağınıklığı kazanç sürekliliğinizi etkileyebilir; Bu hanenin olumluluklarından faydalanabilmek için eğer varsa bastırılmışlık duygunuzu çözmeniz lazım. ",
        "Sabır, disiplin ve uzun vadeli planlama enerjisini temsil eder. Sabır en büyük sınavdır; aceleci davranmak parasal ve güç kayıplarına yol açabilir. Kazancınızı kalıcı kılmak için ciddi emek ve zaman yatırımı gerekir. Ticarette kolay güvenmemeli, özellikle ortaklıklarda dikkatli olmalısınız. Sıkı disiplinle hareket ederseniz, sabırla elde edilen kazancı sağlamlaştırabilirsiniz. İçsel olarak sabırlı olmayı öğrenmek, hem maddi hem de liderlik alanındaki başarınızı artırır ve uzun vadeli projelerde istikrar sağlar. Aynı zamanda mühendislik ve oluşturma enerjisi de verir.",
        "Sorun çözme becerisi, entelektüel merak, seyahat, yeni insanlarla tanışma ve özgürlük arzusunu simgeler. Sizi canlı tutan şey yeniliklerdir; farklı ortamlarda bulunmak, risk almak, yeni yollar keşfetmek ve çeşitlilik size enerji verir. Yurtdışı işlerde ve sanal alemde para kazanabilme ihtimaliniz vardır. Yenilikleri sever. Cesareti verir. Güzel bir iletişim ağına sahip olmanız, ihtiyacınız olduğunda size destek olabilecek insanları kolayca bulmanızı sağlar. Harika fikirlerinizi paylaşma isteğiniz, zaman zaman aceleyle konuşmanıza ve yanlış anlaşılmanıza yol açsa da, pratik zekânız ve hazır cevaplılığınız sizi bir çok durumda kurtarır. Gezgin ruhunuz, sizi bir yerde uzun süre tutmaz; yeni deneyimler size yaşam sevinci katar. Doğuştan iyi bir konuşmacı olmanız, sizi ikna edici ve eğlenceli bir kişilik yapar. İnsanları güldürme, coşturma ve motive etme gücünüz vardır. Kalabalıkların karşısına geçtiğinizde bile, ilk anda gergin olsanız da kısa sürede enerjinizi sahaya yayar ve herkesi peşinizden sürüklersiniz.",
        "Ticarette sezgileri iyi güçlüdür. Sezgilerinize güvendiğinizde hem kazanç hem de bereket alanınız güçlenir. Ancak aileden gelen hakedişler, özellikle baba kaynaklı sorunlar kazanç yolunu tıkayabilir. Babayla helalleşmesi gerekir. Bu durumları aşarsa Aile/Baba bereket kaynağıdır. Kendi kararlarını vermediği sürece sürekli başkalarının etkisinde kalabilir. Sezgilerine güvenip bireysel kararlar alırsa, bereket alanı genişler. Öğretmenlik enerjiniz güçlüdür. Sizin için en uygun alanlardan biri öğretmedir; bilgiyi estetik bir dille aktarma ve insanlara destek olma gücünüz vardır.",
        "İş hayatında titiz, çalışkan ve güvenilir bir yapınız vardır. Mükemmellik arayışınız nedeniyle sorumluluklarınızı en iyi şekilde yerine getirirsiniz. Sanata doğal bir yeteneğiniz bulunur; bu alan sizin için güçlü bir ifade aracıdır. Ayrıca spiritüel alandan gelir elde etme potansiyeliniz yüksektir. Maneviyatla uyumlu bir iş yaptığınızda kalıcı bereket yakalayabilirsiniz; ancak aurayı korumakta zorlandığınızda maddi kayıplar yaşayabilirsiniz. 7 sayısı, aynı zamanda 7. çakrayı yani sol beyni temsil eder. Tefekkür, derin düşünme, analitik bakış ve felsefi sorgulamalar size güç verir. Bu nedenle felsefe, matematik ve mühendislik gibi sol beyni besleyen alanlarda da başarılı olabilirsiniz",
        "Sorumluluk alma, ve işleri tamamlamaya yönelik güçlü bir motivasyon taşır. Doğuştan bolluk ve ticaret enerjisi ile donatılmışsınızdır; maddi gücünüzü doğru kullanırsanız hem bereketli hem de etkileyici bir figür olabilirsiniz. Kendi işinizi kurduğunuzda maddi olarak hızla büyüyebilir (özellikle 3 ü 1 ile açıyorsa), ancak 8 i 8 ile açmak zorlu bir açılımdır. Bu yolda yanlız yürümeniz gerekebilir. Nazara çok açıktır ve aura delikliği riski vardır. Bu yüzden helal haram noktasına (yeme, içme, ilişkiler yani bedeni ve ruhi helaller) çok dikkat etmeli. Arkadaşlıklarına ve ilişkilerine Rahmani sınırlar koymalı. Ruhunu bu şekilde korursa maddi, manevi zengin olur. Çokça Ayetel Kürsi ve koruma duaları okuması tavsiye edilmelidir.",
        "İyimserlik, isteği ile sizi harekete geçirir. Kazancınız çoğu zaman doktorluk hemşirelik gibi şifalandırıcı mesleklerden gelir, ancak önce kendi yaralarınızı sarmadan başkalarına fayda sağlayamazsınız. Auranız güçlüdür; korunmazsa başkalarının yüklerini taşımaya başlarsınız. Kendi iyileşme sürecinizi tamamladığınızda hem kendinize hem de başkalarına bolluk ve fayda sağlayabilirsiniz. İnsanlara yardım ve şifa içeren işler sizin için oldukça uygundur; sağlık ve koruma alanları, hem sizin hem de çevrenizdekilerin iyileşmesini destekler.",
        "Kazancınızın çoğu zaman şifalandırıcı  ve insanlara fayda sağlayan mesleklerden gelebileceğini gösterir, ancak önce kendi yaralarınızı sarmanız gerekir. Bazı sorumluluklar almak size iyi gelir. Aurası güçlüdür; korunmazsa başkalarının yüklerini taşımaya başlarsınız. Kendi iyileşme sürecinizi tamamladığınızda, başkalarına da bolluk ve destek aktarabilirsiniz. Çevrenizde bilgece sözlerinizle fark yaratır, insanlara güven ve ilham verirsiniz. İlginizi çeken konulara tutkuyla bağlı olursunuz, ama takıntı ve inatçılık zaman zaman sizi yorabilir. Pozitif ve sevgi dolu yaklaşımınız, çevrenizdeki herkesin size yönelmesini ve size destek olmasını sağlar.",
        #11
        "11/2 enerjisi, kişinin duygularını biriktirdiğinde ani ve güçlü patlamalar yaşayabilir; çevresindekiler bunu anlamayabilir ve yanlış yorumlayabilir. Bu durum, ikili ilişkilerde gereksiz gerilimlere yol açabilir. Maddi alanda bağımsızlık arzusu güçlüdür; kendi işini kurmak ve liderlik etmek ister, ancak bu bazen istikrarı bozabilir. Geçmiş travmalar ve çocukluk deneyimleri üzerinde çalışmak, enerjiyi dengeli kullanmayı sağlar. Yetenekleri arasında girişimcilik, iletişim ve yaratıcılığıyla insanlara ilham vermek vardır. Sevdiği ve hırslandığı işi bulduğunda büyük başarı ve parlamalar yaşayabilir ün potansiyeli vardır, ancak yıldız düşüklüğü ve zorlu dönüşümler de mümkündür. "
    ],
    [  # 9. hane - HAYAT AMACI
        "Liderlik ve yönlendirme enerjisini temsil eder. Bu hane, kişinin hem kendine hem de başkalarına rehberlik etme kapasitesini gösterir. Sağlam bir liderlik, insanların iyiliğini gözeterek adil ve dengeli kararlar almakla mümkündür; aşırı kontrol veya bencillik, ilişkilerde gerilime ve ego çatışmalarına yol açabilir. Öncelikle kişinin kendi iç dengesini ve olumsuz özelliklerini fark ederek onları dönüştürmesi önemlidir. Kök çakra ile sağlam temeller kurmak, bu liderlik enerjisinin kalıcı ve ilham verici olmasını sağlar. İnsanlara ışık tutmak ve onları desteklemek, varoluş amacınızı gerçekleştirmenin anahtarıdır. Güçlü bir öz-farkındalık ve doğru niyetle, bu hane hem kişisel hem de toplumsal alanda olumlu etkiler yaratabilir.",
        "koruma, destek ve şefkat enerjisini temsil eder. Bu hane, başkalarına yardım ederken aynı zamanda kendi sınırlarınızı korumanız gerektiğini hatırlatır. Hayat amacı sevgi ve şefkat üzerinden ilerler, ancak aşırı fedakârlık veya kendini tüketme, duygusal dengenizi bozabilir. İnsanları korumak ve onlara rehberlik etmek önemli olsa da, onların hatalarından öğrenmelerine izin vermek de gerekir; aksi takdirde bağımlılık ilişkileri ve aşırı kontrol sorunları oluşabilir. Sakral çakra ile uyumlu bir enerji, bu sevgiyi sağlıklı şekilde yaşamanızı ve çevrenize huzur taşımayı mümkün kılar. Dengeyi gözetmek ve duygusal sınırlarınızı korumak, hem sizin hem de çevrenizdekilerin büyümesini destekler.",
        "Üretme, düzen kurma, disiplin ve kararlılık enerjisini temsil eder. Bu hane, kaos içinde düzen oluşturmak ve zorluklar karşısında yılmadan ilerlemekle ilgilidir. Hayat amacınız, üretmek, aktarmak ve kendi yeteneklerinizi hem kendiniz hem toplum için değerli kılmaktır; bunu yaparken onay aramak yerine kendinizi gerçekleştirmek önemlidir. Disiplin ve organizasyon sırasında, bazen başkalarının kendilerini baskı altında hissetmeleri mümkündür; duygusallığınızı kontrol ederek ve öfkenizi yöneterek bu süreci daha uyumlu kılabilirsiniz. Kendinizi tanımak, olumsuz yönlerinizi dönüştürmek ve iletişimde incelikli davranmak, hem kişisel hem de toplumsal başarınızı destekler. Sorumluluklarınızı yerine getirirken öngörülü olmak ve planlı hareket etmek, bu hanenin amacını en verimli şekilde yaşamanızı sağlar",
        "Sabrı ve derin anlayış enerjisini temsil eder. Esneklik, olgunluk ve sabır, bu hanenin hayat boyu öğrenmesi gereken temel değerleridir. Kurallara ve kendine karşı katı olma eğilimi, ilerlemenizi zaman zaman zorlaştırabilir; bu nedenle kendinize karşı yumuşamayı öğrenmek önemlidir. Olgunluk ve sabırla birleştiğinde hem kendi yolunuzu hem de başkalarına rehberlik etme kapasitenizi güçlendirir. Bu hane, hem kendi hem de başkalarının yaşam yollarında işaretleri okuyabilme ve büyük resmi görebilme yeteneği verir. Araştırma ve keşif sırasında merakınızı dengede tutmak, başkalarının yaşamına aşırı müdahale etmeden yönlendirme yapmak gerekir. Hayat amacınız, öğrenme ve keşfetme sürecinde dengeyi koruyarak başkalarına farkındalık kazandırmak ve doğru yönlendirmeler sunmaktır. Maneviyatınızı güçlendirmek, dualar ve içsel farkındalıkla bu enerjiyi en verimli şekilde kullanmanızı sağlar.",
        "Yenilik, özgürlük ve devrim yaratma enerjisini temsil eder. Bu hane, sorunlara yaratıcı çözümler bulmayı, yenilikçi düşünmeyi ve gerektiğinde cesur adımlar atmayı teşvik eder. Hayat amacınız, konfor alanınızdan çıkarak yeni şeyler keşfetmek, deneyimlemek ve insanlara özgürlüğü öğretmektir. İnsanları etkileme ve bir araya getirme beceriniz, devrim niteliğinde değişimler başlatmanızı sağlar. Bununla birlikte, aşırı sivri dilli kontrolcü, veya asi olma eğiliminizi dengelemek, ilişkilerde ve yaşam yolunda daha başarılı olmanıza yardımcı olur. Özgürlüğün sınırlarını ve sorumluluklarını bilmek, hatalardan öğrenmek ve bağımlılıklardan arınmak, bu hanenin enerjisini dengeli ve verimli kullanmanızı sağlar.",
        "Denge, sezgiler ve sorumluluk enerjisini temsil eder. Hayat amacınız, hem kendi yaşamınızı hem de başkalarının yaşamlarını güzelleştirerek dengeli bir yol izlemektir. İnsanlara, hayatlarında dengeyi bulmaları ve zevkleri ölçülü şekilde deneyimlemeleri konusunda rehberlik edebilirsiniz. Sezgilerinizi fark etmeli ve onlara kulak vermelisiniz. Bu süreçte, aşırı ilgi veya zevke kapılmamak ve kıskançlık eğilimlerini kontrol altında tutmak önemlidir. Sorumluluklarınızı dengeli üstlenmeyi öğrenmek, kendinizi tüketmeden başkalarına katkı sağlamanızı mümkün kılar ve kurban psikolojisine girmenizi engeller. İçsel korkularınızı ve endişelerinizi fark etmek ve yönetmek, bu hanenin enerjisini bilinçli ve verimli kullanmanızı sağlar. Böylece hem toplumsal hem de kişisel yaşamınızda olumlu ve kalıcı etkiler yaratabilirsiniz.",        
        "Ruhsal derinlik, sezgi ve gizemli bilgi enerjisini temsil eder. Hayat yolunuzun ana teması, içsel tatmini ve gerçek huzuru içeride aramayı öğrenmek, inançlarınızı test ederek derin bir ruhsal olgunluğa ulaşmaktır. Evrenin sırlarını keşfetmek ve bunları sanat veya diğer yaratıcı yollarla başkalarına aktarmak sizin görevinizdir. Mahremiyetinize ve başkalarının sınırlarına saygı gösterirken, bireyselliği ve güveni öğretmek önemlidir. Bitmek bilmeyen arayışlar ve güvensizlikler, bu süreçte sizi zaman zaman geriye çekebilir; bunları fark edip dengelediğinizde, yaşam yolunuzda çok daha etkili ve zahmetsiz ilerlersiniz. Gerçekten ne istediğiniz anlamak ve farkındalığınızı artırmak  bu hanenin enerjisini dengeli ve etkili şekilde kullanmanızı sağlar.",
        "Maddi başarıyı ,sistem kurmayı ve otorite enerjisini ve aurayı temsil eder. Hayat amacınız, bu gücü bilinçli ve doğru bir şekilde yönetmektir. Bu enerji, liderlik yapmanızı, hedeflere ulaşmanızı ve çevrenizde sağlam yapılar kurmanızı sağlar. İnsanları bir araya getirme, sınırlar çizme ve sorumluluk alma beceriniz güçlüdür; ancak aşırı yüklenmek veya kontrolcü tutum geliştirmek sizi zorlayabilir. Kendinizi ve kaynaklarınızı dengede tutarak, hayır demeyi öğrenmek ve aşırı yüklerin altına girmemek ve aura alanınızı pozitifte tutmak yaşam yolunda daha verimli ve başarılı olmanızı sağlar. Otoritenizi ruhsal değerlerle birleştirdiğinizde ve aura alanınızı koruduğunuzda, güçlü bir vizyoner olabilirsiniz. Ama bu güç doğru niyetle yönlendirilmezse kontrolcü, aşırı hırslı ve doyumsuz bir kişiliğe dönüşebilirsiniz.",
        "Sınırları, öğrenme ve şifa enerjisini temsil eder. Hayat amacınız, sahip olduğunuz bilgeliği ve yetenekleri hem kendiniz hem de başkaları için faydalı şekilde kullanmaktır. İnsanlara güvenmeyi, hayallerinin peşinden gitmeyi ve kendi potansiyellerini keşfetmelerini öğretmek sizin görevleriniz arasındadır. Şifa potansiyeliniz yüksek olsa da, öncelikle kendi içsel yaralarınızı sarmayı ve kişisel sınırlarınızı korumayı öğrenmeniz önemlidir. Aşırı inatçılık ve sabit fikirli tutumlardan kaçınmak, enerjinizi verimli kullanmanızı sağlar. Kendi yaralarınızı iyileştirdiğinizde, hem kendinize hem de topluma ruhsal hizmet sunabilecek olgunluk ve bilgelik geliştirirsiniz. Maneviyatınızı güçlendirmek ve başkalarına yardım ederken dengeyi korumak, bu hanenin enerjisini en etkili şekilde yaşamanızı mümkün kılar.",
        #11 19 22 33
        "hanedeki 2 rakamı, koruma, destek ve şefkat enerjisini temsil eder. Ama bu hane, 11/2 olduğu için duyguları kontrol edebilmek daha zordur. Normal 2 lere göre daha inatçı ve hedef odaklı olduğunuz için Eğer duygularınızı kontrol edebilirseniz hedeflerinize hayallerinize ulaşabilirsiniz. Bu yüzden olumlu düşünüp harekete geçin. Bu hanedeki zorlukları dönüştürdüğünüzde ünlü olma potansiyeliniz vardır. Ama destek bekleyen bir yapıda olmanıza rağmen hayat amacı konusunu tek başınıza çözmeniz gerekir. Başkalarına yardım ederken aynı zamanda kendi sınırlarınızı korumanız gerektiğini hatırlatır. İnsanları korumak ve onlara rehberlik etmek önemli olsa da, onların hatalarından öğrenmelerine izin vermek de gerekir; aksi takdirde bağımlılık ilişkileri ve aşırı kontrol sorunları oluşabilir. Sakral çakranız açıksa bu haneyi hızlı açarsınız.  Dengeyi gözetmek ve duygusal sınırlarınızı korumak, hem sizin hem de çevrenizdekilerin büyümesini destekler.",
        "hanedeki 1 rakamı, liderlik ve yönlendirme enerjisini temsil eder. Bu hane, kişinin hem kendine hem de başkalarına rehberlik etme kapasitesini gösterir. Ama bu kişi 19 dan 1 ile dönüştüğü için bu kişilerin kibre düşme ihtimali vardır. Manevi eğitim için bu kişilerin zorlukları imtihanları normal 1 lere göre biraz daha fazla olabilir. Sağlam bir liderlik, insanların iyiliğini gözeterek adil ve dengeli kararlar almakla mümkündür; aşırı kontrol veya bencillik, ilişkilerde gerilime ve ego çatışmalarına yol açabilir. Öncelikle kişinin kendi iç dengesini ve olumsuz özelliklerini fark ederek onları dönüştürmesi önemlidir. Kök çakra ile sağlam temeller kurmak, bu liderlik enerjisinin kalıcı ve ilham verici olmasını sağlar. İnsanlara ışık tutmak ve onları desteklemek, varoluş amacınızı gerçekleştirmenin anahtarıdır. Güçlü bir öz-farkındalık ve doğru niyetle, bu hane hem kişisel hem de toplumsal alanda olumlu etkiler yaratabilir.",
        "hanedeki 22/4 rakamı, sabrı ve derin anlayış enerjisini temsil eder. Esneklik, olgunluk ve sabır, bu hanenin hayat boyu öğrenmesi gereken temel değerleridir. Kurallara ve kendine karşı katı olma eğilimi, ilerlemenizi zaman zaman zorlaştırabilir; bu nedenle kendinize karşı yumuşamayı öğrenmek önemlidir. Olgunluk ve sabırla birleştiğinde hem kendi yolunuzu hem de başkalarına rehberlik etme kapasitenizi güçlendirir. Bu hane, hem kendi hem de başkalarının yaşam yollarında işaretleri okuyabilme ve büyük resmi görebilme yeteneği verir. Araştırma ve keşif sırasında merakınızı dengede tutmak, başkalarının yaşamına aşırı müdahale etmeden yönlendirme yapmak gerekir. Açılımınız 22 sayısı ile olduğu için ciddi sıkıntılar yaşamış olma ihtimaliniz yüksektir. Bunlar elbette sizin kalp çakranızı açmak, imanınızı kuvvetlendirmek, maneviyatınızı arttırmak için başınıza gelmiştir. Maneviyatınızı güçlendirmek, dualar ve içsel farkındalıkla bu enerjiyi en verimli şekilde kullanmanızı sağlar.",
        "hanedeki 6 rakamı, denge, sezgiler ve sorumluluk enerjisini temsil eder. Hayat amacınız, hem kendi yaşamınızı hem de başkalarının yaşamlarını güzelleştirerek dengeli bir yol izlemektir. Ama 33 den 6 olduğunuz için normalden daha ağır sorumluluklara maruz kalmış olabilirsiniz. O yüzden sizin bu dengeyi kurmanız daha da önemlidir ve daha zordur.  Başarabilirseniz İnsanlara, hayatlarında dengeyi bulmaları ve zevkleri ölçülü şekilde deneyimlemeleri konusunda rehberlik edebilirsiniz. Sezgilerinizi fark etmeli ve onlara kulak vermelisiniz. Bu süreçte, aşırı ilgi veya zevke kapılmamak ve kıskançlık eğilimlerini kontrol altında tutmak önemlidir. Sorumluluklarınızı dengeli üstlenmeyi öğrenmek, kendinizi tüketmeden başkalarına katkı sağlamanızı mümkün kılar ve kurban psikolojisine girmenizi engeller. İçsel korkularınızı ve endişelerinizi fark etmek ve yönetmek, bu hanenin enerjisini bilinçli ve verimli kullanmanızı sağlar. Böylece hem toplumsal hem de kişisel yaşamınızda olumlu ve kalıcı etkiler yaratabilirsiniz. "
    ]
]

pin_kodu_yorumu_giris_cumlesi = [
    "KENDİNİ NASIL GÖRÜYOR. Bu hane, kişinin düşünce sistemini, karar alma mekanizmasını ve kendilik algısını temsil eder. Kişinin dış dünyayı nasıl algıladığı ve içsel diyaloğu burada belirginleşir. Ego, özgüven, zihinsel liderlik ve bireysel farkındalık bu alanın temel temalarıdır. Aynı zamanda hangi frekansta düşündüğü, zihinsel filtrelerinin nasıl çalıştığı da bu hanede görünür.",
    "DUYGULAR ve YAKIN İLİSKİLER. Bu hane, kişinin duygusal dünyasını, yakın ilişkilerinde sevgiyi nasıl algıladığını ve duygusal bağ kurma kapasitesini temsil eder. Sevme/sevilme ihtiyacı, duygusal bağımlılıklar, kırgınlıklar, özdeğer duygusu ve duygulara dair içgörü bu alanda belirginleşir. Aynı zamanda sakral çakrayla ilişkilidir; kişinin yaratım gücünü ve duygusal hareketliliğini gösterir.",
    "DÜNYAYA AÇILMA, HİTABET ve TİCARET. Bu hane kişinin: Kendini sözlü ya da yazılı olarak nasıl ifade ettiğini, İletişim becerilerini, Meslek seçimindeki eğilimlerini, Ve hayatla kurduğu ticari ya da duygusal alışveriş dengesini temsil eder.",
    "SEVGİ, OLGUNLUK ve HAYATIN ÖĞRETTİĞİ. Dördüncü hane sevgi, olgunluk ve kalbin sınavları ile doğrudan ilişkilidir. Bu hanede kişinin sevgi alma-verme biçimi, duygusal olgunluğu ve kalp merkezinden gelen tavırları ortaya çıkar. Disipline ve istikrarlı olduğumuz alanı ve sorunların üstesinden gelme yöntemimizi de verir.",
    "İMTİHAN, ZAAF ŞÜKÜRLE AŞMASI GEREKEN YER. Bu hane kişinin hayattan ne kadar tatmin olduğu, sahip olduklarıyla ne yaptığı ve içsel şükrü ne ölçüde deneyimlediğiyle ilgilidir. Bu hane, hayatınızda tekrar eden sorunların ardındaki davranış kalıplarını gösterir. Genellikle çocukluktan gelen şartlanmalarla karşılaştığınız sorunlar altındaki dinamiği ya da davranış kalıbını anlatır. Pin Kodu'nuzun yönetiminde kilit rol oynar.",
    "AİLE, BABA. Bu hane, kişinin aile yapısı, özellikle baba figürü ve eril otoriteyle kurduğu ilişkiyi temsil eder. Aynı zamanda sorumluluk alma becerisi, kontrol eğilimi ve aile içi rollerin nasıl deneyimlendiğini yansıtır. Sorunlar sadece babayla değil; aile içindeki dengeyle de ilgilidir.",
    "ANNE, İNANÇ. Bu hane, kişinin anneyle ilişkisini, iman boyutunu, içsel rehberlik kapasitesini ve sezgisel yönlerini yansıtır. Aynı zamanda duygusal kökler, teslimiyet, ruhsal olgunluk ve içsel bağlılık burada saklıdır. Geçmişten gelen dişil enerji aktarımı (özellikle anne ve kadın atalar) bu hanede iz bırakır.",
    "KAZANÇ ve BEREKET. Bu hane, kişinin maddi dünyayla ilişkisini, parayla kurduğu bağı, emanet ve değer üretme anlayışını, aynı zamanda aurasının ne kadar güçlü ya da sızdıran olduğunu gösterir.",
    "HAYAT AMACI. Bu hane, kişinin bu hayata ne için geldiğini, hangi tema üzerinden tamamlanacağını ve yaşam boyu yönelmesi gereken asıl amacı temsil eder. Ruhsal olarak buradaki sayı, kişinin olgunluk sınavlarını, kendisini gerçekleştirme biçimini ve kalıcı etkisini yansıtır."
]


cakra_yorumlari_text = [
    [#1
        """Kök Çakra – Tıkanık
•	Hayatın ilk 9 yılında yaşanan zorluklar, aile içi sınırlamalar ve duyguların bastırılmasıyla oluşur. Aidiyet eksikliği ve “sanki bu dünyada yok gibiyim” hissi belirgindir. Fanatiklik, eleştiriye gelememe, sabırsızlık ve geçmişte takılı kalma görülür.
•	Fiziksel belirtiler: halsizlik, yorgunluk, kansızlık, kemik ağrıları.
•	Psikolojik ve fizyolojik iyileşme için: geçmişi kabullenmek, affetmek, farkındalık geliştirmek, nefs tezkiyesi yapmak önemlidir.
 """,
        """Kök Çakra – Az Çalışan
•	Kök çakra kısmen açık olsa da kişi aidiyet hissetse bile ego ve hırsa bağlı davranır. Eleştiriyi kabul etmekte zorlanır, sürekli kendini haklı görme eğilimindedir.
•	Başarı için çok çalışmış, zorluklarla mücadele etmiş olabilir.
•	Gelişim için: başkalarının fikirlerine saygı göstermek, farklılıkları kabul etmek, kendi düşüncesini mutlak doğru saymamak gerekir.
 """,
        """Kök Çakra – İyi Çalışan
•	Duygularını rahat ifade eder, hayata sahip çıkar, liderlik ve yönetim yeteneklerini kullanır. Kendini ve başkalarını kabul etme bilinci yüksektir.
•	Çocukluk travmaları her zaman tamamen yok olmaz, bu yüzden çakra açık olsa da geliştirilmelidir.
•	Gelişim için: geçmişi iyileştirmek, affetmek, nefs tezkiyesi yapmak ve eleştiriye açık olmak önemlidir.
 """,
        """Kök Çakra – Çok Fazla Çalışan
•	Kendini güçlü ifade eder, fikirlerini rahatça söyler, hayatta sağlam basar. Ancak aşırı çalışması nedeniyle eleştiriye tahammülsüzlük, şikayet, kavgacı tavırlar görülebilir.
•	Hem olumlu hem olumsuz yönler aynı anda yaşanır.
•	Denge için: affetmek, farkındalık geliştirmek, şükür defteri tutmak ve nefs tezkiyesi yapmak gereklidir.
 """
    ],
    [#2
        """Sakral Çakra – Tıkanık
•	İkili ilişkilerde sıkıntı, duyguların bastırılması ve değer görmeme hissi hakimdir. Kısırlık, üreme problemleri veya psikolojik kapanıklık görülebilir. Aidiyet ve sevgi eksikliği, fedakarlık veya beklenti dengesizlikleri sorun yaratır.
•	Psikolojik durum: pısırıklık, duygularını ifade edememe, ilişki kuramama, sürekli olumsuz soru sorma ve kendini yalnız hissetme.
•	Fiziksel ve ruhsal belirtiler: kalp ve üreme sistemi ile bağlantılı problemler, ilişki kuramama, aura dengesizlikleri.
•	Dengeyi sağlamak için: duygularınızı fark etmek ve ifade etmek, gereksiz fedakarlıklardan kaçınmak, kendi değerinizi kendiniz vermek, ilişkilerde dengeyi korumak.
 """,
        """Sakral Çakra – Az Çalışan
•	Duygularını ifade edebilir ama yüzüne yansıtamadığından soğuk veya duygusuz görünebilir. İlişkilerde çekingen, kontrollü ve kırılgan olabilir.
•	Başkalarının duygularına yeterince açıklık göstermez, kendi egosunu koruma eğilimindedir.
•	Gelişim için: kendini gözlemleyerek iletişim ve empatiyi geliştirmek, duyguları bastırmamayı öğrenmek, ilişkilerde sağlıklı sınırlar oluşturmak gerekir.
 """,
        """Sakral Çakra – İyi Çalışan
•	Duygularını rahat ifade eder, empati kurar ve sağlıklı ikili ilişkiler geliştirir. Sevgi ve yakınlık verir ve alır, ilişkilerinde aranan kişi olur.
•	Çocuklukta bastırılmış duygular olsa bile, çakra aktif çalıştığında ilişkilerde dengeyi koruyabilir.
•	Korunması için: duygulara önem vermek, olaylarda hisleri fark etmek, gereksiz fedakarlıklardan kaçınmak ve kendi kendine iyi olmak gerekir.
 """,
        """Sakral Çakra – Çok Fazla Çalışan
•	İlişkilerde aşırı fedakar ve hassastır; alma-verme dengesi bozulmuştur. Sıklıkla kırılır ve duygusal olarak yıpranır.
•	Fazla çalışması nedeniyle ilişkilerde kendi değeri göz ardı edilir, bu da kırılganlık ve hassasiyeti artırır.
•	Dengeyi sağlamak için: kendini önceliklendirmek, sınırlar koymak, gereksiz fedakarlıklardan kaçınmak, duyguları ifade etmek ve kendi değerini bilmek önemlidir.
 """
    ],
    [#3
        """Solar Pleksus – Tıkanık
•	Çocuklukta bastırılmış duygular nedeniyle kişinin kendini ifade etmesi engellenmiştir. Bu kişiler içe kapanık, duygularını ifade edemeyen, kıskanç, sivri dilli olabilirler ve ilişkilerde paylaşım zorluğu yaşarlar.
•	Fiziksel etkiler: mide ağrıları, sindirim sistemi sorunları, pankreas ve karaciğer problemleri görülebilir.
•	Psikolojik etkiler: özgüvensizlik, sürekli savunma halinde olma, agresif veya geveze davranışlar, ilişkilerde kırılganlık ve daldan dala atma eğilimi.
•	İyileştirme için: çocukluk travmalarını sevgiyle kabullenmek, duyguları ve düşünceleri ifade etmek, sözleri özenle seçmek ve dozunda paylaşım yapmak önemlidir.
 """,
        """Solar Pleksus – Az Çalışan
•	Kısmen açık olan bu çakra, kişinin duygularını ifade etmesine izin verir ancak bazen geveze, sivri dilli veya kırıcı olabilir. İçe kapanma riski azalır ama hâlâ duygusal kontrol zorluğu yaşanabilir.
•	Gelişim için: üretken faaliyetler, hobiler ve duyguların düzenli olarak ifade edilmesi, öfke anında konuşmamaya dikkat etmek gerekir.
 """,
        """Solar Pleksus – İyi Çalışan
•	Kendi duygularını ve düşüncelerini güzel ifade eder, hitabeti güçlüdür. Üretken ve yaratıcıdır; kitap yazma veya projeler geliştirme kapasitesi yüksektir.
•	Çocuklukta yaşanan bastırılmışlıklar tamamen yok olmasa da çakra aktif çalıştığında kişi dengeli, kendine güvenli ve ilişkilerinde başarılıdır.
•	Korunması için: hobiler ve üretken aktivitelerle meşgul olmak, duygularını paylaşmak ve içe kapanmamak önemlidir.
 """,
        """Solar Pleksus – Çok Fazla Çalışan
•	Kendini çok iyi ifade edebilir fakat sivri dilli ve eleştirel olabilir, kırıcı sözler söyleme eğilimi vardır. Duygusal olarak aşırı hassas ve “daldan dala atlayan” bir yapısı olabilir.
•	Hem olumlu hem olumsuz özellikler aynı anda görülür; kendini savunma ve üretkenlik yüksek, ama ilişkilerde kırılganlık ve kıskançlık artabilir.
•	Denge için: sözleri özenle seçmek, dozunda paylaşmak, kıskançlık ve paylaşım sorunları üzerinde çalışmak ve üretkenliği olumlu şekilde yönlendirmek gerekir.
 """
    ],
    [#4
        """Kalp Çakrası – Tıkanık
•	Sevginin temel çakrasıdır; tıkanıklıkta kişi inatçı, öfkeli, aceleci ve başkalarının fikrine saygı göstermekte zorlanır. İlişkilerde güven ve sabır eksikliği yaşanır. Ani kararlar ve tedbirsiz davranışlar sık görülür.
•	Fiziksel etkiler: Timüs bezi ve bağışıklık sistemi ile ilgili sıkıntılar, kalp hastalıkları ve genel enerji dengesizliği ortaya çıkabilir.
•	Psikolojik etkiler: Öfke, sabırsızlık, dar görüşlülük, kincilik, empati eksikliği ve sürekli tekrar eden olumsuz deneyimler.
•	İyileştirme için: farkındalık geliştirmek, yaşanan imtihanları ders olarak görmek, sabırlı ve olgun davranmak, maneviyata yönelmek, yeşil alanlarda vakit geçirmek, namaz ve dua ile kalbi güçlendirmek, ani karar ve gereksiz fedakarlıktan kaçınmak.
""",
        """Kalp Çakrası – Az Çalışan / Geliştirilmeli
•	Kısmen açık olup kişi sabırlı, sakin ve maneviyatı güçlüdür. Ancak zaman zaman imtihanlar ve ani olaylar karşısında tepkilerde zorluk yaşayabilir.
•	Gelişim için: tedbirli ve temkinli olmak, ani karar vermemek, olumsuz yönleri fark edip olumluya çevirmek, sabır ve farkındalıkla hareket etmek.
 """,
        """Kalp Çakrası – İyi Çalışan
•	Sabırlı, sebatlı, sevgi dolu ve olgun bir kişilik vardır. Maneviyat güçlüdür ve yaptığı işleri sonuna kadar götürebilir. Kendini sever, olumlu düşünür ve ilişkilerde sağlıklıdır.
•	Kalp çakrasını korumak için: yeşil alanlarda vakit geçirmek, namaz ve dua ile manevi enerji sağlamak, ani karar ve gereksiz fedakarlıktan kaçınmak, bilinçli ve ölçülü güvenmek gerekir.
 """,
        """Kalp Çakrası – Çok Fazla Çalışan
•	Enerjisi yüksek ve aktif olup, aşırı çalışması inatçılık, öfke ve ani karar verme eğilimi yaratabilir. İnat ve sabrı dengede tutmak önemlidir.
•	Olumsuz yönleri fark edip sabır ve bilinçle yönetmek gerekir. Bu kişiler güçlü maneviyat ve sabır sayesinde enerjilerini olumlu yönde kullanabilir.
•	Aşırı çalışan: Nadirdir. İsmi Muhammet Mustafa olan kişilerde görülür. İnatçı olurlar. Peygamberimiz buna örnektir. İnadını azme çevirmiştir.
 """
    ],
    [#5
        """Tıkanık Boğaz Çakrası
•	Kişi dikkatsiz, odaklanma güçlüğü çeker, daldan dala atlar, depresyon ve kaygı yaşayabilir. Aşırı kontrol ve mükemmeliyetçilik görülür; olayları akışına bırakmakta zorlanır.
•	Bedensel etkiler: Tiroit sorunları ve metabolik dengesizlikler riski artar.
•	Psikolojik etkiler: Negatif enerjiye duyarlılık, kendini suçlama, depresyon ve kaygı eğilimi.
•	İyileştirme: Alfa dalgasına geçmek, dikkat geliştirme alıştırmaları, tek bir hobiye odaklanmak, negatif ortam ve kişilerden uzak durmak, gül yağı ile frekans yükseltmek, hatalardan ders alıp akışta kalmak.
 """,
        """Az Çalışan / Geliştirilmeli Boğaz Çakrası
•	Kısmen açık olup kişi yeniliklere ve keşiflere düşkündür, fakat konfor alanından çıkmakta zorlanabilir ve alışkanlıklarından vazgeçemez.
•	Gelişim için: Yeni deneyimler edinmek, negatif kişilerden uzak durmak, zihni sakinleştirmek ve alfa dalgasına yönelmek gerekir.
 """,
        """İyi Çalışan Boğaz Çakrası
•	Yenilikleri seven, kendini ifade edebilen, iradesi güçlü ve öğrenmeye açık kişilerdir. Monotonluğu sevmezler, hayatı aktif ve keşif odaklı yaşarlar.
•	Koruma yöntemleri: Dikkat geliştirme alıştırmaları yapmak, tek bir hobiye odaklanmak, frekansı düşüren ortam ve kişilerden uzak durmak, gül yağı ile enerji artırmak.
 """,
        """Çok Fazla Çalışan Boğaz Çakrası
•	Enerjisi yüksek fakat dikkati dağınık, maymun iştahlı, tiroit ve metabolik sorunlara yatkındır. Kendini sürekli sorgular, konfor alanına bağlıdır ve değişime dirençlidir.
•	Bu kişilerin ağzında sürekli “Canım sıkılıyor.” cümlesi dolanır. Zihinleri sürekli konuşur. Konsantre olamama ve dikkat eksikliği gibi problemler yaşarlar. 
•	Dengelemek için: Alfa dalgasına yükselmek, alışkanlıkları terk etmek, yenilikleri hayatına dahil etmek, dikkati toplamak ve frekansını yükseltmek gerekir.
 """
    ],
    [#6
        """Tıkanık Alın Çakrası
•	Evhamlı, korku ve vesvese eğilimi olan, mükemmeliyetçi ve endişeli kişilikler görülür. Baba veya aile ile sorunlar çakrayı bloke edebilir.
•	Bedensel etkiler: Florür ve paketli gıdalar çakra tıkanıklığını artırabilir; stres ve zihinsel yorgunluk ortaya çıkar.
•	Psikolojik etkiler: Öngörüsüzlük, karar alma güçlüğü, sürekli olumsuz senaryolar düşünme, korkularla yaşam.
•	Açma yöntemleri: Alın hacamatı, korku ve vesvese ile yüzleşmek, müzik veya sanatla ilgilenmek, florürsüz ürünler kullanmak.
 """,
        """Az Çalışan / Geliştirilmeli Alın Çakrası
•	Kısmen açık olup sezgisi az gelişmiş, B planı olmayan, ani kararlarla zorlanan kişiler.
•	Gelişim için: Sanat ve müzikle ilgilenmek, gözlem yeteneğini geliştirmek, sorumluluk alma pratikleri yapmak.
 """,
        """İyi Çalışan Alın Çakrası
•	Sezgisel, önünü gören, öngörüsü kuvvetli ve duygusal zekası yüksek kişilerdir. İyi ebeveyn olabilir ve çevresine yardım ederler.
•	Koruma yöntemleri: Alfa dalgasında sakin bir zihinle yaşamak, korkularla yüzleşmek, sanatsal faaliyetlere yönelmek, florürsüz ürün kullanmak.

 """,
        """İyi Çalışan Alın Çakrası
•	Sezgisel, önünü gören, öngörüsü kuvvetli ve duygusal zekası yüksek kişilerdir. İyi ebeveyn olabilir ve çevresine yardım ederler.
•	Koruma yöntemleri: Alfa dalgasında sakin bir zihinle yaşamak, korkularla yüzleşmek, sanatsal faaliyetlere yönelmek, florürsüz ürün kullanmak.

 """
    ],
    [#7
        """Tıkanık Taç Çakra
•	Karamsar, doyumsuz ve sürekli arayış içinde olma; eldekiyle yetinmeme, huzursuzluk ve boşluk hissi.
•	Bedensel/psikolojik etkiler: Zihinsel blokaj, stres, huzursuzluk, ruhsal tatminsizlik.
•	Nefsi ve maneviyat eksikliği, kanaatsizlik ve şükretmeme eğilimi.
•	Açma yöntemleri: İçsel farkındalık, namaz ve huşu, kitap okumak, felsefeyle uğraşmak, yeni dil öğrenmek, manevi arayış ve tefekkür.
 """,
        """Az Çalışan / Geliştirilmeli Taç Çakra
•	Kısmen açık olup analitik ve zekâ yeteneği mevcut; ancak kanaat edemez, zaman zaman karamsar ve arayış içindedir.
•	Gelişim için: Arayışları sorgulamak, manevi ve zihinsel farkındalık çalışmaları yapmak, elindekilerle yetinmeyi öğrenmek.
 """,
        """İyi Çalışan Taç Çakra
•	Zekâsına güvenen, analitik ve tefekkür yeteneği gelişmiş; manevi ve zihinsel dengesi yerindedir.
•	Bu kişiler huzurlu, kendine güvenli ve belirli bir alanda uzmanlaşabilirler; ertelememeyi ve sorumluluk almayı bilirler.
 """,
        """Çok Fazla Çalışan Taç Çakra
•	Aşırı çalışan kişiler nadirdir; yoğun arayış, doyumsuzluk ve manevi uğraşlar ortaya çıkar. Zeka ve yetenekleri yüksek olmasına rağmen tembellik ve erteleme eğilimi gösterebilirler.
•	Denge için: Arayışları sorgulamak, kanaat etmek, iman ve tefekkürle zihinsel enerjiyi yönlendirmek.
 """
    ],
    [#8
        """Tıkanık 8. Çakra
•	Parası ve ömrü bereketsiz, sürekli negatif enerji ve nazara açık, ilişkilerde ve sosyalleşmede zorluk çeker.
•	Aurada delikler oluşur, frekans düşer ve psikolojik sorunlar artar.
•	Gösterişe düşkün, açgözlü, israf eğilimli olabilir; sağlık ve yaşam kalitesi etkilenir.
•	Açma yöntemleri: Allah’a güven, helal-haram dengesine dikkat, evde sirke ve defne tütsüsü, Ayet’el Kursi ve Felak/Nas surelerini okumak, nefes farkındalığı.
 """,
        """Az Çalışan / Geliştirilmeli 8. Çakra
•	Kısmen açık, parası ve hayatı avantajlı; nazar ve negatif etkilerden korunmaya ihtiyaç duyar.
•	Koruma çalışmaları ile bereket ve enerji akışı artırılabilir.
 """,
        """İyi Çalışan 8. Çakra
•	Güçlü, asil ve otorite sahibi; parasal ve sosyal yaşamında istikrarlı ve bereketli.
•	Ticaret ve girişimlerde yetenekli, nazara karşı dirençli; aura dengeli ve sağlam.
 """,
        """Çok Fazla Çalışan 8. Çakra
•	Aşırı çalışanlarda güç, hırs ve bereket yoğun yaşanır; para ve prestij fazlasıyla elde edilir.
•	Yoğun enerji bazen ilişkilerde aşırı kontrol veya egoya dönüşebilir; denge için manevi ve ruhsal farkındalık önerilir.
 """
    ],
    [#9
        """Tıkanık 9. Çakra
•	Önünü göremez, ilhamı ve sezgisi zayıftır; saf, kolay aldanan, fanatik ya da kırılgan olabilir.
•	İlişkilerde sınır koyamaz, hayır diyemez; alma-verme dengesi bozulur.
•	Ticaret ve karar süreçlerinde yanlış seçimlere yatkın olabilir.
•	Şifacılık yönü kapalıdır; önce kendi iç dengesini ve sınırlarını iyileştirmesi gerekir.
 """,
        """Az Çalışan / Geliştirilmeli 9. Çakra
•	Sezgileri açıktır, insanlara yardım etmeyi ve bildiğini paylaşmayı sever.
•	İkili ilişkilerde sınır koymakta zorlanır; fedakârlık dengesini korumalıdır.
•	İlahi ilhamlara açıktır ancak kolay yönlendirilebilir, hayır demeyi öğrenmelidir.
•	Şifacılık potansiyeli vardır, gelişim için kendini iyileştirmesi önemlidir.
 """,
        """İyi Çalışan 9. Çakra
•	Sezgileri kuvvetli, ilahi ilhamı açık, empati ve merhameti güçlüdür.
•	İnsanlara yardım eder, şifacılık yeteneği vardır; iyileştirici etki bırakır.
•	Hizmet etmekten, bilgisini paylaşmaktan mutluluk duyar.
•	Alma-verme dengesini koruduğu sürece ilişkilerinde ve ruhsal yolculuğunda dengeyi sürdürür.
 """,
        """Çok Fazla Çalışan 9. Çakra
•	Şifacılığı güçlüdür, insanlara yardım etmeyi yoğun bir şekilde ister.
•	Aşırı verici olabilir, aldığında kendini değersiz hissedebilir; sınır koyamaz.
•	Fedakârlık nedeniyle alma-verme dengesi bozulur, bu durum 8. çakrayı da olumsuz etkileyebilir.
•	İlahi ilham açıktır fakat dengesiz çalıştığından hem güç hem de zayıflık aynı anda yaşanır.
 """
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
def ebced_toplama_asamali_sade(*args):
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
    print(k)
    # Değerleri şartlara göre güncelle
    for i in range(9):
        if int(k[i][0]) == (i + 1):
            k[i] += '!'
    
    # Pin kodu yorumlarını oluştur
    yorumlar = []
    for i in range(9):
        yorum = f"{i+1}. Hane: {pin_kodu_yorumu_giris_cumlesi[i]}<br><br>"
        # k[i] değerinin ilk karakterini al ve int'e çevir (örn: "4!" -> 4)
        base_index = int(k[i][0]) - 1  # 0-based index için -1
        index = base_index

        # Özel * durumları: 2* -> 10., 1* -> 11., 4* -> 12. eleman (varsa)
        if k[i].endswith('*') and (i != 5 and i != 8):
            uzunluk = len(pin_kodu_yorumu[i])
            if k[i] == '2*':
                yorum += f"11/2. ile açılmış: {pin_kodu_yorumu[i][9]}"
            elif k[i] == '1*':
                yorum += f"19/1. ile açılmış: {pin_kodu_yorumu[i][10]}"
            elif k[i] == '4*':
                yorum += f"22/4. ile açılmış: {pin_kodu_yorumu[i][11]}"
            elif k[i] == '6*':
                yorum += f"33/6. ile açılmış: {pin_kodu_yorumu[i][12]}"
            
        # İndeks kontrolü ekle
        elif 0 <= index < len(pin_kodu_yorumu[i]):
            yorum += f"{index+1}. ile açılmış: {pin_kodu_yorumu[i][index]}"
        else:
            yorum += f"Geçersiz sayı: {index+1} (Bu hane için 1-9 arası bir sayı olmalıdır)"
        
        
        yorumlar.append(yorum)
    
    return k, yorumlar

def tam_kulvar_bulma(isim_soyisim):
    #Bu fonksiyon, verilen isim soyisimin bütün harflerinin rakamsal karşılığını bulup toplar.
    total_sum = 0
    for char in isim_soyisim.upper():
        if char in chakra_values:
            total_sum += chakra_values[char]
    
    return ebced_toplama_asamali(total_sum)


def yasam_yolu_hesapla(birthdate):
    # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    total_sum = 0
    for char in birthdate:
        if char.isdigit():
            total_sum += int(char)
    
    return ebced_toplama_asamali_sade(total_sum)

def bereket_rakami_bulma(birthdate):
 # Doğum tarihi 'gg aa yyyy' formatında olmalıdır.
    gun, ay, _ = birthdate.split(' ')
    birthdate_without_year = gun + ay
    total_sum = 0
    for char in birthdate_without_year:
        if char.isdigit():
            total_sum += int(char)

    return ebced_toplama_asamali(total_sum)

def cakra_yorumlari(arti_sistemi):
    cakra_yorumlari = []
    for i in range(9):
        # Tüm sistemlerden (pin kodu + isim + ek isim) toplam artı sayısını hesapla
        toplam_arti = arti_sistemi[1][i]
        
        if toplam_arti == 0:
            cakra_yorumlari.append(cakra_yorumlari_text[i][0])
        elif toplam_arti == 1:
            cakra_yorumlari.append(cakra_yorumlari_text[i][1])
        elif 2<= toplam_arti <= 3:
            cakra_yorumlari.append(cakra_yorumlari_text[i][2])
        elif toplam_arti >= 4:
            cakra_yorumlari.append(cakra_yorumlari_text[i][3])

    return cakra_yorumlari

       
def donusum_yillari_bulma(dogum_tarihi):
    gun, ay, yil = dogum_tarihi.split(' ')

    dogum_yili = int(yil)
    yil = dogum_yili
    yas = 0

    result = ""

    from datetime import datetime
    current_year = datetime.now().year

    
    # Yıl, ay ve gün rakamlarını topla
    yil_rakam_toplami = sum(map(int, str(current_year)))
    ay_rakam_toplami = sum(map(int, str(ay)))
    gun_rakam_toplami = sum(map(int, str(gun)))
    
    donusum_rakami = ebced_toplama_asamali(yil_rakam_toplami+ ay_rakam_toplami+ gun_rakam_toplami)
    result += f"Bu yıl {int(ay)}.ayın {int(gun)}.günü sonrası dönüşüm rakamı {donusum_rakami}.(Doğum gününe kadarki dönüşüm rakamı: {ebced_toplama(ebced_toplama(current_year-1), ebced_toplama(gun), ebced_toplama(ay))}) \n\n"

    while yas <= 70:
        yil_rakam_toplami = sum(map(int, str(yil)))
        yeni_yil = yil + yil_rakam_toplami
        yas = yeni_yil - dogum_yili

        # Yeni yıl rakamlarını topla
        yeni_yil_rakam_toplami = sum(map(int, str(yeni_yil)))
        donusum_rakami = ebced_toplama_asamali(yeni_yil_rakam_toplami + ay_rakam_toplami + gun_rakam_toplami)
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
    
    # Rakam dizisini oluştur
    rakam_dizisi = [0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        rakam_dizisi[i] = int(k[i][0])

    # Her element için özellik hesaplama
    element_ozellikleri = {}
    
    # Hava elementi (1, 5) için
    hava_rakamlari = [r for r in rakam_dizisi if r in ozellikler['hava']]
    element_ozellikleri['hava'] = {
        'esnek': len([r for r in hava_rakamlari if r in ozellikler['esnek']]),
        'katı': len([r for r in hava_rakamlari if r in ozellikler['katı']]),
        'baskın': len([r for r in hava_rakamlari if r in ozellikler['Etken/Baskın']]),
        'edilgen': len([r for r in hava_rakamlari if r in ozellikler['edilgen']])
    }
    
    # Su elementi (2, 7) için
    su_rakamlari = [r for r in rakam_dizisi if r in ozellikler['su']]
    element_ozellikleri['su'] = {
        'esnek': len([r for r in su_rakamlari if r in ozellikler['esnek']]),
        'katı': len([r for r in su_rakamlari if r in ozellikler['katı']]),
        'baskın': len([r for r in su_rakamlari if r in ozellikler['Etken/Baskın']]),
        'edilgen': len([r for r in su_rakamlari if r in ozellikler['edilgen']])
    }
    
    # Toprak elementi (4, 8) için
    toprak_rakamlari = [r for r in rakam_dizisi if r in ozellikler['toprak']]
    element_ozellikleri['toprak'] = {
        'esnek': len([r for r in toprak_rakamlari if r in ozellikler['esnek']]),
        'katı': len([r for r in toprak_rakamlari if r in ozellikler['katı']]),
        'baskın': len([r for r in toprak_rakamlari if r in ozellikler['Etken/Baskın']]),
        'edilgen': len([r for r in toprak_rakamlari if r in ozellikler['edilgen']])
    }
    
    # Ateş elementi (3, 6) için
    ates_rakamlari = [r for r in rakam_dizisi if r in ozellikler['ateş']]
    element_ozellikleri['ates'] = {
        'esnek': len([r for r in ates_rakamlari if r in ozellikler['esnek']]),
        'katı': len([r for r in ates_rakamlari if r in ozellikler['katı']]),
        'baskın': len([r for r in ates_rakamlari if r in ozellikler['Etken/Baskın']]),
        'edilgen': len([r for r in ates_rakamlari if r in ozellikler['edilgen']])
    }

    return element_ozellikleri


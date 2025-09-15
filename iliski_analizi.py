k = [""] * 9

# Import necessary functions from ebced.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ebced import chakra_hesapla, yasam_yolu_hesapla, chakra_values


iliski_analizi_metinleri = [
    [#1
        "Bu ilişki bireysellik, liderlik çatışması ve ego mücadelesini gündeme getirir. İki güçlü kişinin birlikte var olma çabası vardır. Çocukluk deneyimlerinizden gelen kök çakra sorunları ilişkiye yansıyabilir. Bu yüzden geçmişinizi fark etmek, çocukluk travmalarınızı şifalandırmak önemlidir. Bilinçaltınızda taşıdığınız izleri konuşup, birbirinize destek olarak iyileşebilirsiniz. Sağlıklı sınırlar ve saygı ile bu ilişki güçlenir.",
        "Bu ilişkideki bireyler birbirlerini sever duygularını birbirleriyle paylaşırlar. Tarafların birbirine karşı güzel duyguları vardır. Bu ilişki karşılıklı şefkat ve anlayışı büyütür.  Fakat eğer bu sayı olumsuzdaysa (11den 2) ve bireylerin sakral çakraları tıkalıysa duygularını ifade edemeyecekleri için değersiz hissedebilirler. Ben değil biz olmayı öğrenirlerse aşarlar.",
        "İletişim, eğlence ve yaratıcılık bu ilişkinin merkezindedir. Birlikte konuşmak, üretmek ve paylaşmak önemlidir. Fakat taraflardan birinin 3. Çakrası sıkıntılıysa, bu durum baskınlık kurma, sivri dil ve kırıcı sözler olarak yansıyabilir. Güzel konuşmak, öfkeyi yönetmek ve saygıyı korumak ilişkiyi daha olgun hale getirir.",
        "Bu ilişkide güven çok önemlidir. Düzen ve sağlam bir temel bu ilişkinin amacıdır. Ortak yaşamın sınırlarını sağlıklı çizmek gerekir. Kalp çakrasındaki tıkanıklık varsa, öfke krizlerine sebep olabilir. Öfke yerine anlayış ve sınırlar koymak ilişkinizi dengeler. Düzenli, istikrarlı ve güvene dayalı bir bağ kurmanız hedeflenir.",
        "Tutku, hareket ve değişim bu ilişkinin dinamiğini oluşturur. Birlikte keşfetmek, yenilenmek ve hayatı deneyimlemek önemlidir. Ancak frekansınız düştüğünde ya da birbirinizi baskıladığınızda sorun yaşanabilir. Esnek olmak, enerjinizi yüksek tutmak, negatif olaylara takılıp kalmamak ilişkinizi ileriye taşır.",
        "Aile, sorumluluk ve bağlılık bu ilişkinin temelinde vardır. Sıcak bir yuva kurma arzusu yüksektir. Ama bu ilişkideki bireyler birbirine ebeveynlik yapmak için birbirini seçmiş ve kendi ailelerinin yüklerini almış bir ilişkidedir. Fakat çoğunlukla altıncı çakradaki tıkanıklık yüzünden taraflar birbirine fazla yüklenebilir ya da ebeveynlik rolüne kayabilir.  Sezgilerini kullanarak ve  sorumlulukları dengeleyerek hayata tutunmalı varsa korku vesvese evham bunları aşmalıdırlar.",
        "Bu ilişkideki bireyler birbirine karşı yetmeyebilirler, beklentili olabilirler. İçe dönüş ve anlamsal derinleşme bu ilişkinin özüdür. Manevi bağınız güçlüdür, fakat bireylerde taç çakra tıkanıklığı varsa beklenti, memnuniyetsizlik ve kusur aramaya neden olabilir. Karamsarlığa kapılmadan, olumlu düşünerek ve birbirinizi ruhsal olarak besleyerek bu bağı güçlendirmelisiniz. İlişkide çok yanlızlaşmamaya dikkat edin.",
        "Bu ilişkideki bireyler birbirlerine üstünlük sağlamak isteyebilirler veya birlikte hayata tutunmak için bir araya gelmiş olabilirler. Auralarını korumaları çok önemlidir Nazar negatif enerji olumsuz haller noktasında dikkat ederek güzel hallerini çevreyle paylaşmamalıdırlar.",
        "Bu ilişkinin amacı bağışlama, iyileştirme ve tamamlanmadır. Birbirinize iyi gelirsiniz fakat özgürlük isteği ve sınırsız davranışlar ilişkiyi zorlayabilir. Sorumluluk bilincini geliştirmek, geçmişten ders almak ve sağlıklı sınırlar koymak bu bağı olgunlaştırır. Şefkat, saygı ve kabul ile ilişki tamamlanma noktasına ulaşır.",
        #11
        "Bu ilişkideki bireyler birbirlerini sever duygularını birbirleriyle paylaşırlar. Tarafların birbirine karşı güzel duyguları vardır. Bu ilişki karşılıklı şefkat ve anlayışı büyütür.  Fakat eğer bu sayı olumsuzdaysa (11den 2) ve bireylerin sakral çakraları tıkalıysa duygularını ifade edemeyecekleri için değersiz hissedebilirler ve duygusal krizleri olabilir( bireysel analizlerinde de 11den 2ler varsa). Ben değil biz olmayı öğrenirlerse aşarlar."
    ],
    [#2
        "Bu ilişkide olan bireyler dışarıya güçlü bir izlenim verir. Bu güçlü izlenim daha gelişmesi kendi ayakları üzerinde durması için bilinçaltlarını kontrol etmeyi öğrenmelidir. ",
        "Bu ilişkideki bireyler uyumlu, sakin ve anlayışlı bir çift izlenimi verir. Bireysel analizlerinde sakral çakra düzgün çalıştığı sürece uyum vardır. ",
        "Bu ilişkideki bireyler enerjik, neşeli ve konuşkan bir çift olarak algılanır. ",
        "Bu ilişkideki bireyler istikrarlı ve ciddi bir ilişki yaşayan bir çift izlenimi verir.",
        "Bu ilişkide bireyler dışarıdan bakıldığında biraz eğlenceli, dengesiz veya özgürlükçü bir çift gibi durabilir.  ",
        "Bu ilişkide bireyler aile değerlerine önem veren geleneksel bir çift olarak görülürler.",
        "Bu ilişkide bireyler gizemli, entelektüel bir hava veriyor olabilir. Aynı zamanda mesafeli bir ilişkiyi gösterebilir.",
        "Bu çift güçlü, iddialı ve maddi anlamda iyi bir enerji yayıyor olabilir.",
        "Bu çift ruhsal yönü kuvvetli, fedakarlık yapan kimseye hayır diyemeyen kişiler olarak algılanıyor olabilir.",
        #11
        "Bu ilişkideki bireyler dışarıya karşı birbirine bağlı bir izlenim verir. Fakat içeride bir fırtına olabilir. Bunun en büyük sebebi birbirinize olan duygularını ifade etmemeleridir."
    ],
    [#3
        "İlişkide bağımsızlık arzusu ön plandadır. Ortak projeler geliştirebilirsiniz; ancak geçmişten gelen duygularınızı fark etmek ve bilinçaltınızı keşfetmek uyumunuzu güçlendirecektir.",
        "Ortak hedeflerde duygusal bağ ve uyum önemlidir. Hislerinizi paylaşmak ve birbirinize şeffaf davranmak, ilişkinin amaçlarının gerçekleşmesine yardımcı olur.",
        "Sosyal çevre ve yaratıcılık odaklı planlar ilişkiye enerji katar. Ancak birbirinizi eleştirirken kırıcı olmamaya özen göstermelisiniz.",
        "Uzun vadeli düzen ve işbirliği ilişki için değerlidir. Karşılıklı saygıyı koruduğunuzda hem işte hem de özel yaşamda sağlam bir temel kurabilirsiniz.",
        "Keşif, yenilik ve yolculuk isteği ilişkiyi ortak bir noktada buluşturur. Yine de enerjinizi dengede tutarak paylaştıklarınızı dikkatle seçmeniz faydalı olur. Frekansınızı korumalısınız.",
        "Aile kurma, sorumlulukları paylaşma ya da çocuk yetiştirme arzusu öne çıkar. Birlikte sanatsal faaliyetlerde bulunabilirsiniz. Uyum ve sevgi ilişki için temel yapı taşıdır.",
        "Ortak hedefiniz maneviyat ya da içsel yolculuk olabilir. Beklentilerinizi ölçülü tutmak, ilişkiye huzur katar.",
        "İş, para ya da kariyer odaklı hedefler ve ilerlemeler gündeme gelebilir. Ancak dışarıya her şeyinizi göstermek yerine bazı şeyleri muhafaza etmek ilişkiyi nazardan uzak tutar.",
        "Topluma hizmet etmek ve fayda sağlamak gibi idalleriniz amaçlarınız olabilir. Fakat önce kendi içsel dengenizi kurmanız, ilişkinin başkalarına ışık olmasını kolaylaştırır.",
        #11
        "Ortak hedeflerinizde duygusal uyum ve birliktelik ön plandadır. Birbirinize karşı duygularınızı ifade etmelisiniz."
    ],
    [#4
        "İlişkide fikirlerinize değer verilmesi ve karşılıklı destek, güveni ve köklenmeyi güçlendirir. Eğer geçmişten gelen aile bağları ya da çocukluk yaraları sizi zorluyorsa, bunları fark edip şefkatle kucaklamak ilişkinin temellerini sağlamlaştırır.",
        "Anlayışla dinlenmek ve duyguların kabul görmesi ilişkiye huzur katar. Çocuklukta deneyimlenen ilişkiler bugün yaşanan dinamikleri şekillendirebilir; bu yüzden geçmişteki izleri fark etmek ve dönüştürmek önemlidir.",
        "Bireylerin kendilerini özgürce ifade edilebileceği bir ortam ilişkiyi besler ve bastırılmışlıkları azaltır. Çocukluktan gelen bastırılmışlıklar iletişimi zorlaştırabilir; bu nedenle birbirinize alan tanımak ve güvenli bir ifade ortamı oluşturmak önemlidir.",
        "İlişkide planlı hareket etmek ve güven duygusu ilişkiyi destekler. İlişkinin belirli kuralları olmalı, taraflar birbirine saygı göstermeli ve hayatlarını birlikte düzenlemelidir. Kişiler, kendilerine veya çevrelerine sınır koymakta zorlanıyorlarsa sağlıklı sınırlar oluşturmayı öğrenmelidir.",
        "Baskıdan uzak, serbest bir alan ilişkiyi iyileştirir. Aileden gelen kısıtlamalar fark edilip dönüştürüldükçe, iletişim daha özgür ve akıcı hale gelir. Bu sayede ortak enerjiniz hayatınıza bilinçli bir yön verir ve boğaz çakranız açılmış olur.",
        "İlişkide sevgi, ilgi ve zor zamanlarda birbirine destek temel ihtiyaçtır ve ilişkiyi destekler. Ortak sorumlulukların farkına varmak ve birlikte sanatsal, yaratıcı faaliyetler geliştirmek bağınızı güçlendirir.",
        "Maneviyat ve içsel derinlik, bu hanede büyük önem taşır. Bazen sessizlik ya da bireysel alan tanımak ilişkiye iyi gelir. Ayrıca birlikte zihinsel gelişimi destekleyen çalışmalar faydalıdır (matematiksel ve dilsel zeka).",
        "Ortak hedefler belirlemek ve bu hedeflere ulaşırken birbirine destek olmak ilişkinin gücünü artırır. Birlikte toprakla ilgilenmek ya da iş hayatında ortak projeler geliştirmek de destekleyici olur.",
        "Başkalarına fayda sağlamak ve yardım etmek ilişkiye anlam katar. Bununla birlikte sağlıklı sınırlar çizmek ilişkiyi iyileştirir, karşılıklı saygıyı korumak ve duygusal yük yüklemeden anlayışla yaklaşmak önemlidir.",
        #11
        "Duyguları bastırmak ya da görmezden gelmek, zamanla içsel krizlere yol açabilir. İlişkide hisler fark edildiği anda ifade edilmeli; gereksiz duyguların kaynağına inilip çözümlenmesi dönüşüm sağlar."
    ],
    [#5
        "Kriz anlarında inatlaşma, ego savaşları ve kendi bildiğini uygulama eğilimi ortaya çıkabilir. Bu yüzden ilişkiye zarar vermemek için sağlıklı eşlerden biri ateşken diğeri su olmalı. Bazı çizgiler belirlenmelidir. Karşılıklı saygı krizleri hafifletir.",
        "Kriz anlarında duygular bastırılabilir. Bu yüzden sessizlik ve kopukluk yaşanabilir. Oysa duyguları açıkça ifade etmek, krizleri çözmenin en etkili yoludur.",
        "Kriz anlarında sözleriyle can yakabilirler. İlişkide ifadelerinizi kontrol altında tutmak önemlidir. Sertleşen tavırlar ya da aşırı savunmalar iki tarafı da yorar; bunun yerine yapıcı ve dengeli konuşmalar tercih edilmelidir.",
        "Kriz anlarında soğukluk, sert tavırlar ya da iletişimin kopması krizleri derinleştirebilir. Bu nedenle saygıyı her zaman korumak ilişkinin sürekliliği için değerlidir.",
        "Kriz anlarında Tartışmalar bir anda büyüyebilir, ani uzaklaşmalar yaşanabilir. Birbirinizi kontrol etme eğiliminden vazgeçip, partnerinizi olduğu gibi kabul etmek ilişkiyi rahatlatır.",
        "Kriz durumlarında aşırı fedakârlık ya da suçlamalar dengeyi bozabilir. Otorite çatışmaları yaşansa da sağduyulu davranmak ve sınırları netleştirmek çözüm getirir.",
        "Zor zamanlarda uzaklaşma, yalnız kalma ya da duygusal kopukluk görülebilir. İlişkide birbirinizde aradığınız desteği bulamadığınızı hissettiğinizde, kaygıyı beslemek yerine anlayışa yönelmek önemlidir.",
        "Kriz anlarında güç mücadeleleri veya kontrol savaşları kendini gösterebilir. Bu durum krizkeri tetikleyebilir de. Ayrıca ilişkinin nazara açık olması nedeniyle özel anlarınızı her zaman paylaşmamanız korunmanıza yardımcı olur. Nazar bereketinizi azaltabilir.",
        "Kriz anlarında bazen sessiz kabullenme, vazgeçme ya da ani bitişlerle sonuçlanabilir. Eğer taraflar “özgürüm, istediğimi yaparım” düşüncesine kapılıyorsa, bu algıdan vazgeçmek ilişkinin devamlılığı için şarttır.",
        #11
        "Kriz anlarında duygular bastırılabilir. Bu yüzden sessizlik ve kopukluk yaşanabilir. Oysa duyguları açıkça ifade etmek, krizleri çözmenin en etkili yoludur."
    ],
    [#6
        "Aşırı kontrol ya da benmerkezcilik ilişkiyi zorlayabilir. Partnerinizi değiştirmeye çalışmak yerine, birbirinizi olduğunuz gibi kabul etmek ve öncelikle kendi dönüşümünüze odaklanmak daha sağlıklıdır.",
        "Duygusal kırılganlık ve alınganlık sık sık sorun yaratabilir. Tasavvufi bir bakışla kırmaktan çok kırılmamak önemlidir. İlişkide duygusal merkezinde sorun yaşayan taraf, kendi içsel değişimine yönelmelidir.",
        "Dağınık iletişim, karşı tarafı bastırmaya çalışmak ya da düşünmeden söylenen sözler çatışma yaratabilir. Bu nedenle sözcüklerinizi özenle seçmek ilişkiye denge katar.",
        "Katılık ve değişime direnç, ilişkiyi yıpratır. Tarafların yalnızca kendi sınırlarını dayatması ilişkiyi yorar; bunun yerine ortak sınırlar belirlemek uyumu güçlendirir.",
        "Bağlanma korkusu ve düzensizlik ilişkide gerginlik yaratabilir. Ayrıca birbirinizi fazla kontrol etmeye çalışmak bağı zayıflatır.",
        "Taraflar ailelerinden aşırı sorumluluklar getirebilir ve bu yükler ilişkiyi ağırlaştırabilir. Öncelikle hangi sorumlulukların gerçekten size ait olduğunu fark etmek önemlidir. Sizin olmayan sorumlulukları üstlenmemelisiniz.",
        "Fazla mesafe koyma ya da aşırı içe dönüklük ilişkiyi zorlayabilir. Yüksek beklentiler, duyguları kapatma ve sürekli hata arama ise evlilikte yıpratıcı bir etki oluşturur. Bu eşler uzun süre birseysel kalmamalılar.",
        "Maddi konular üzerinden güç mücadelesi ya da kontrol oyunları ilişki dengesini bozar. Bu yüzden maddi alanlarda şeffaflık ve adalet esastır.",
        "“Kafama göre yaşarım” tavrı ilişkiyi çıkmaza sokabilir. Sınır koymakta zorlanmak ya da başkalarına aşırı verici davranmak da dengeyi bozar. Eğer taraflardan biri sınır koymayı başaramıyorsa, o kişinin bu alanda kendini geliştirmesi gerekir.",
        #11
        "Duygusal kırılganlık ve alınganlık sık sık sorun yaratabilir. Tasavvufi bir bakışla kırmaktan çok kırılmamak önemlidir. İlişkide duygusal merkezinde sorun yaşayan taraf, kendi içsel değişimine yönelmelidir.Duygusal kırılganlık ve alınganlık sık sık sorun yaratabilir. Tasavvufi bir bakışla kırmaktan çok kırılmamak önemlidir. İlişkide duygusal merkezinde sorun yaşayan taraf, kendi içsel değişimine yönelmelidir."
    ],
    [#7
        "Kendi alanını korumak kadar partnerin alanına saygı göstermek de gelişim için önemlidir. Aynı zamanda birbirinize ait olduğunuzu hissetmeli, çocukluk travmalarınızı fark edip şefkatle iyileştirmelisiniz.",
        "Duygusal hassasiyetleri anlamak ve empatiyle yaklaşmak ilişkinin büyümesine katkı sağlar. Bununla birlikte haz ve mutluluk alanında aşırılıklardan uzaklaşıp dengeyi korumak da gelişim için gereklidir.",
        "Ortak fikir alışverişi yapmak ve birlikte üretimde bulunmak ilişkiye canlılık katar ve geliştirir. Ortak üretim süreçleri ve iletişim, ilişkinin sürekli tazelenmesini sağlar.",
        "Sağlam bir temel ve düzen kurmak ilişkinin gelişimi için önemlidir. İnatlaşmadan, ortak kurallar çerçevesinde ilerlemek ilişkiye istikrar kazandırır.",
        "Değişime açık olmak ve esnek davranmak ilişkinizi geliştirir. Birbirinizle rahatlıkla konuşabilmek ve baskı kurmamak güveni artırır.",
        "Fedakârlık ile sağlıklı sınırlar arasında denge kurmak gerekir. Ayrıca her iki tarafın da babayla olan ilişkilerini fark etmesi önemlidir; çünkü bu dinamikler ilişkiye yansıyabilir. Sezgilerinizi dikkate alarak kabule geçmek gelişim sağlar.",
        "Güven ortamı oluşturarak duygularınızı paylaşmak, ilişkinin olgunlaşmasını destekler. Küsmek ya da aşırı beklentilere kapılmak yerine düşüncelerinizi açıkça ifade etmek önemlidir. Ayrıca her iki tarafın da annesiyle olan ilişkilerini fark etmesi önemlidir.",
        "Güç savaşları yerine ortak amaçlarda buluşmak gelişiminizi hızlandırır. Enerjinizi korumalı, özel güzelliklerinizi herkesle paylaşmamaya özen göstermelisiniz. Nazara karşı dikkatli olmak ilişkinizi daha sağlam kılar.",
        "Geçmişi affetmek ve ruhsal olgunlukla ilerlemek ilişkinizi derinleştirir. Öncelikle kendi sınırlarınızı netleştirmeli ve karşılıklı saygıyı temel değer olarak benimsemelisiniz.",
        #11
        "Duygusal krizleri ve duygusal hassasiyetleri anlamak ve empatiyle yaklaşmak ilişkinin büyümesine katkı sağlar. Bununla birlikte haz ve mutluluk alanında aşırılıklardan uzaklaşıp dengeyi korumak da gelişim için gereklidir."
    ],
    [#8
        "İlişkide liderlik potansiyeli güçlüdür; ortak projeler geliştirmek ve yön vermek için yüksek bir enerji bulunur.",
        "Birbirini tamamlayan ve destekleyen bir ortaklık kurarak uyum içinde üretim yapabilirsiniz.",
        "Yaratıcılık ve sosyal alanlarda ortak hayaller, ilişkinin enerjisini besler ve başarı getirebilir.",
        "Uzun vadeli, düzenli ve emekle büyüyen işler kurmak bu hanede desteklenir. İstikrar ilişkinin üretim gücünü ve bereketini  artırır.",
        "Yenilik arayışı ilişkiye dinamizm ve canlılık katar. Ancak aşırılığa kaçmadan değişimi yönetmek önemlidir.",
        "Aile, eğitim ya da bakım alanlarında birlikte üretim yapmak bağınızı güçlendirir, bereketinizi arttırır. Ortak sorumluluklar burada yaratıcı bir enerjiye dönüşür.",
        "Ruhsal ya da entelektüel alanlarda ortak çalışmalar, ilişkinin derinliğini artırır ve manevi tatmin sağlar.",
        "Ticari ve maddi girişimlerde güçlü bir iş ortaklığı oluşturabilirsiniz. Birlikte çalışmak finansal büyüme getirebilir. ",
        "Kolektif fayda için üretimde bulunmak, hayır işleri ya da topluma hizmet etmek ilişkinin bereketini arttırır.",
        #11
        "Birbirini tamamlayan ve destekleyen bir ortaklık kurarak uyum içinde üretim yapabilirsiniz."
    ],
    [#9
        "Bu ilişki, iki kişinin kendi benliğini bulması ve çocukluk izlerini fark etmesi için bir sahnedir. Çocuklukta yaşanan deneyimler bilinçaltını şekillendirir, bu nedenle geçmişinizi konuşmak ve şefkatle kabul etmek önemlidir. Birbirinizin hayat hikâyelerini dinlemek, şimdiye yansıyan tutumları anlamanızı sağlar. Duygular biriktiğinde sağlıklı boşaltmayı öğrenmeli ve tepkisel anlarda birbirinizi korumalısınız. Sevgiyle başlayan bağın saygıyla devam edeceğini unutmadan hareket edin. Ben demek yerine biz dediğinizde ilişki olgunlaşır ve gerçek bir yuvaya dönüşür.",
        "Bu ilişki, duyguları yönetmeyi ve sakral çakra yaralarını iyileştirmeyi öğretir. Çocukluktan taşınan etkiler fark edilip şefkatle kucaklandığında duygusal uyum güçlenir. Birlikte duygusal boşaltma ve sağlıklı ifade yöntemleri geliştirmek gerekir. Tepkisel anlarda birbirinizi suçlamadan destek olmanız önemlidir. Sevgi ve güvenin üzerine saygılı sınırlar eklediğinizde bağınız daha da sağlamlaşır. Bu şekilde ilişki, güven veren bir yuva hâline gelir.",
        "Bu bağ, kendini tanıma, üretme ve yeni fikirler geliştirme fırsatıdır. Nesillerden gelen bilinçaltı yüklerinizi fark ederek şimdiki davranışlarınızı çözümleyebilirsiniz. Geçmişinizi konuşmak ve şefkatle sahiplenmek, ilişkinin sağlıklı ilerlemesine katkı sağlar. Zaman zaman tepkisel ve sivri dilli davransanız da birbirinizi kollamanız gerekir. İlişkide hem bireysel gelişim hem de ortak üretim mümkündür. Beraber iş kurabilir, yeni fikirler üretebilirsiniz. Saygı ve sınır bilinci ile bu bağ, birlikte büyümenin temeli olur. ",
        "Bu ilişkinin amacı, sağlam bir düzen ve ortak temel kurmaktır. İnatlaşmadan adil ve sağlıklı sınırlar koymak gerekir. Çocukluktan gelen bilinçaltı kalıplar fark edilmezse öfke ve krizlere dönüşebilir. Bu yüzden geçmişi şefkatle kabul etmek ve duygularınızı sağlıklı boşaltmak önemlidir. Tepkisel anlarda birbirinizin arkasında durduğunuzda bağınız güçlenir. Saygı ve olgunlukla hareket ederek ilişkinizi güvenli bir yuvaya dönüştürebilirsiniz.",
        "Bu ilişki, hayatı keşfetmeyi, değişimi ve özgürlüğü beraber yaşamayı amaçlar. Değişime direnmemek ve esnek olmak ilişkinin gelişimini sağlar. Birbirinizi baskılamadan açık iletişim kurmanız gerekir. Çocukluktan gelen bilinçaltı izlerinizi fark ederek sağlıklı ifade yolları geliştirin. Tepkisel anlarda birbirinize sahip çıkmak, bağı korur. Saygı ve olgunlukla hareket ettiğinizde, bu ilişki sizi hem özgür hem de bağlı kılar.",
        "Bu ilişkinin temel amacı, sıcak ve güvenli bir yuva kurmaktır. Aile bağlarını güçlendirmek ve sorumlulukları dengeli paylaşmak önemlidir. Çocukluktan gelen yükleri fark edip onarmak ilişkiyi daha sağlıklı kılar. Duygularınızı bastırmak yerine boşaltmayı öğrenmelisiniz. Fazla sorumluluk almak ya da birbirinize karşı ebeveyn rolüne girmek ilişkide dengeyi bozabilir. Sezgilerinizi açmalı hissiyatınızı kuvvetlendirmelisiniz. ",
        "Bu bağın amacı maneviyatı güçlendirmektir. Karamsarlıktan çıkıp beklentilerin kökünü çocuklukta arayın. Çocukluktan gelen beklenti ve eksiklikler fark edilip iyileştirildiğinde bağ derinleşir. Birbirinize dair beklentileriniz ancak manevi farkındalıkla çözülebilir. Tepkisel duygular ortaya çıktığında birbirinizi korumanız önemlidir. Manevi bağınızı güçlendirdikçe ilişkiniz daha anlamlı olur ve derinleşir. Çift olarak kafa kafaya verince derinlemesine araştırmalar yaparsınız, anlamsal ve felsefi konularda derinlemesine bilgi sahibi olabilirsiniz. Saygılı sınırlarla bu birliktelik, ruhsal gelişiminiz için bir yol göstericiye dönüşür.",
        "Bu ilişkinin amacı, kontrol ve otorite savaşlarını bitirmektir. İki kişi gönüllü olarak hayatı paylaşmayı öğrenirse ortak üretim ve maddi düzen mümkün olur, güzel ticaret yapabilirler. Bireysel analizlerinde de auraları güçlüyse bu çift çok farkedilir, kendilerini çok güzel ortaya koyarlar. Yaptıkları işte veya girdikleri alanda hızlı büyür ve yayılırlar. Fakat auraları değikse ve cocukluktan gelen yaralar fark edilip iyileştirilmezse güç çatışmaları ilişkiyi zedeler. Tepkisel anlarda birbirinizi desteklemek bu süreci kolaylaştırır. Sağlıklı sınırlar korunduğunda bağınız güven ve dayanışma üzerine inşa olur.",
        "Bu ilişkinin temel amacı, birbirine yuva olmak, korumak ve iyileştirmektir. Fakat eğer kişiler aklına geleni yapıyor, kendi nefsine sınır koymakta zorlanıyor ise bu evliliği zorlar. Bu yüzden bu ilişkide sorumluluk bilincinin gelişmesi çok önemlidir. Çocuklukta yaşanan değersizlik duygusu yetişkinlikte aşırı vericilik ya da sorumsuzluk getirebilir. (Bunu anlamak için bireylerin bireysel analizlerine bakılmalıdır.) Bu yüzden geçmişi fark edip şefkatle kabul etmek gerekir. İlişkide birlikte iyileşme için birbirinizin hayat hikayelerini dinlemeli, yaşanmışlıkları birlikte değerlendirme yaparak şimdiye yansıyan tutumları çözümlemesiniz.  Yanlış seçimlerden korunmak için sınırlarınızı net koymalısınız. Olgunlukla birbirinizi kucakladığınızda, bu ilişki gerçek bir şifa, bilgelik ve tamamlanma alanına dönüşür. ",
        #11
        "Bu ilişki, duyguları yönetmeyi ve sakral çakra yaralarını iyileştirmeyi öğretir. Çocukluktan taşınan etkiler fark edilip şefkatle kucaklandığında duygusal uyum güçlenir. Birlikte duygusal boşaltma ve sağlıklı ifade yöntemleri geliştirmek gerekir. Tepkisel anlarda birbirinizi suçlamadan destek olmanız önemlidir. Sevgi ve güvenin üzerine saygılı sınırlar eklediğinizde bağınız daha da sağlamlaşır. Bu şekilde ilişki, güven veren bir yuva hâline gelir."
    ],
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


    
    # Sonuçları döndür
    # İlişki pin kodu yorumları: bireyseldeki mantıkla metin seçimi
    pin_kodu_yorumlari = []
    for i, deger in enumerate(k):
        try:
            if '2*' in deger:
                # 11 özel durumu, her bloktaki son metin
                idx = len(iliski_analizi_metinleri[i]) - 1
            else:
                sayi = int(deger[0]) if deger and deger[0].isdigit() else 0
                sayi = 1 if sayi < 1 else (9 if sayi > 9 else sayi)
                idx = sayi - 1
            pin_kodu_yorumlari.append(iliski_analizi_metinleri[i][idx])
        except Exception:
            pin_kodu_yorumlari.append("")

    return {
        'k': k,
        'pin_kodu_yorumlari': pin_kodu_yorumlari,
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
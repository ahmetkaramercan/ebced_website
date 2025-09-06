
def evlilik_ek_metin(ek_isim):
    ek_evlilik_metinleri = []
    giris_metni = "Ömür boyu kurduğumuz tüm ilişkiler bizim için çoğunlukla öğretici ilişkilerdir. Her ilişkide bize almamız gereken çeşitli mesajlar vardır ve evliliklerimiz en büyük öğretici ilişkilerimizdir. İşte ****** soy ismi de sizin için öğretici bir ilişki olmuş, öncelikle sizin kökeninizi size hatırlatarak, kökeninizi iyileştirmenizi istemiştir ve bunu size değersiz hissettirerek yapmıştır. Duygularınızı ifade etmediğiniz sürece aşırı derecede bağımlılıklar geliştirerek, duygu patlamaları yaşamış olabilirsiniz ve hayat böyle giderken olaylar karşısında ciddi anlamda sıkıntılı bir hayat yaşamış olabilirsiniz. Önemli olan kökendeki sıkıntılarımızı fark etmek, ilişkilerimizde bunu çözmeye çalışmaktır. Çünkü yarayı kökenden kurutmadıkça kabuğu her ilişkide kanayacaktır."
    giris_metni = giris_metni.replace("******", ek_isim)
    ek_evlilik_metinleri.append(giris_metni)    
    
    ek_isim_upper = ek_isim.upper()
    # B, T, K harflerini say
    asj_count = sum(1 for harf in ek_isim_upper if harf in ['A', 'S', 'Ş', 'J'])
    btk_count = sum(1 for harf in ek_isim_upper if harf in ['B', 'T', 'K'])
    ulc_count = sum(1 for harf in ek_isim_upper if harf in ['U', 'Ü', 'L', 'C', 'Ç'])
    dmv_count = sum(1 for harf in ek_isim_upper if harf in ['D', 'M', 'V'])
    en_count = sum(1 for harf in ek_isim_upper if harf in ['E', 'N',])
    fo_count = sum(1 for harf in ek_isim_upper if harf in ['F', 'O', 'Ö'])
    pyg_count = sum(1 for harf in ek_isim_upper if harf in ['P', 'Y', 'G', 'Ğ'])
    hz_count = sum(1 for harf in ek_isim_upper if harf in ['H', 'Z'])
    ir_count = sum(1 for harf in ek_isim_upper if harf in ['I', 'İ', 'R'])

    print(asj_count, btk_count, ulc_count, dmv_count,en_count, fo_count, pyg_count)

    if 1 <= dmv_count and 1 <= asj_count:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı ve 1. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. Bunun yanında olaylardan ötürü kendinizi ifade edemiyor iseniz bununla çalışmanızı sağlamıştır. Siz hayata bağlamış ve kök çakranızı iyileştirmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)
    
    elif 1 <= dmv_count and 1 <= ir_count:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı ve 9. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. 9.çakranızı geliştirerek de ilişkilerde sınır koymayı hayır demeyi öğretmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= dmv_count and 1 <= en_count:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı ve 5. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. Bunun yanında olaylardan ötürü kendinizi suçlama hatalardan ders çıkarmama gibi durumlara karşı sizin boğaz çakranıza çalışmanızı istemiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf) 

    
    elif 1 <= pyg_count and 1 <= dmv_count:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı ve 7. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. Bunun yanında ilişkilerinizde doyumsuzluk varsa bunların üstesinden gelmeniz için ve olayları derinlemesine düşünmeniz için taç çakranıza çalışmanızı istemiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)


    elif 1 <= dmv_count <= 3 and 4 <= ulc_count:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz. Bununla birlikte 3.çakranızı fazla çalıştırmış, bu ilişkide baskılanmış hissetmiş olabilirsiniz. Baskılanmadan ötürü kendimizi sürekli savunuyor halde bulabilirsiniz"
        ek_evlilik_metinleri.append(ek_paragraf) 

    elif 1 <= dmv_count <= 3 and 1 <= ulc_count <= 3:
        ek_paragraf = "Bu evlilik sizin kalp çakranızı ve 3. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi daha sabırlı sebatlı olgun bir karaktere büründürmüş hayatta ısrarla istediğiniz ve aşırı bağımlılıklarınız varsa onları kontrol etmeniz için sizi yönlendirmiştir. Bunun yanında olaylardan ötürü kendinizi ifade edemiyor iseniz bununla çalışmanızı sağlamıştır. Siz daha iyi konuşturmuş ve ifade ettirmiştir.Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)


    elif 1 <= asj_count and 1 <= ir_count:
        ek_paragraf = "Bu evlilik sizin kök çakranızı ve 9. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Böylelikle sizi, köklenmenizi, çocuklukta yaşanan travma vb. olayları anlamanızı sağlamış olabilir. Eğer olayların aslında olan mesajı almış iseniz artık daha özgüvenli ve daha sağlam adımlar atarsınız. Sizi 9.çakranıza çalıştırarak, size ilişkilerde sınır koymayı hayır demeyi öğretmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= asj_count and 1 <= pyg_count:
        ek_paragraf = "Bu evlilik sizin kök çakranızı ve 7. çakranızı geliştirmiştir. Her ilişki çocukken yaşadıklarımızın bir izdüşümüdür. Bu yüzden bu ilişki çocukken neye ait olamadığınızı babanıza annenize ailenize ait olamadığınızı kabullenilmediğinizi hatırlatmış olabilir. Her ne olduysa çocukken olduğu gibi kabul etmeyi öğrenmeli sevgiyle affa geçmelisiniz. Ayrıca İlişkilerinizde doyumsuzluk ait olamama varsa bunların üstesinden gelmeniz için ve olayları derinlemesine düşünmeniz için taç çakranıza çalışmanızı istemiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf) 

    elif 1 <= en_count and 1 <= asj_count :
        ek_paragraf = "Bu evlilik sizin 5. çakranızı ve kök çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Bunun yanında olaylardan ötürü kendinizi suçlama hatalardan ders çıkarmama gibi durumlara karşı sizin boğaz çakranıza çalışmanızı istemiştir. Her ilişki çocukken yaşadıklarımızın bir izdüşümüdür. Bu yüzden bu ilişki çocukken neye ait olamadığınızı babanıza annenize ailenize ait olamadığınızı kabullenilmediğinizi hatırlatmış olabilir. Her ne olduysa çocukken olduğu gibi kabul etmeyi öğrenmeli sevgiyle affa geçmelisiniz. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= en_count and 1 <= pyg_count:
        ek_paragraf = "Bu evlilik sizin 5. ve 7. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Bunun yanında olaylardan ötürü kendinizi suçlama hatalardan ders çıkarmama gibi durumlara karşı sizin boğaz çakranıza çalışmanızı istemiştir. Ayrıca İlişkilerinizde doyumsuzluk, ait olamama varsa bunların üstesinden gelmeniz için ve olayları derinlemesine düşünmeniz için taç çakranıza çalışmanızı istemiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= fo_count:
        ek_paragraf = "Bu evlilik sizin için ilk olarak sizde olan değersizlik hissini ortaya çıkararak onu iptal etmenizi, bunun için çaba göstermenizi sağlamıştır. Bu yüzden sizi fazlaca konuşturmuş kendi değerinizi anlatmanıza sebep olmuş olabilir. Fakat değersizlik hissi karşımızdaki kişiyle alakalı değil kendi kökenlerimizde yatan sorunlardan kaynaklanır. Kişi ilk olarak doğduğu evde değersiz hisseder ve sonra bunu ilişkilerinde yaşar. Bu yüzden kişiye değer verecek kişi yalnızca kendisidir. Kimseden değer beklememeyi öğrenmek elzemdir. Bu yüzden bu evlilik sizin sezgilerinizi arttırarak, derin düşünme kapasitesi vererek ve ilişkilerinizde sınır koymayı öğreterek sizin hayata tutunmanızı sağlamıştır."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= btk_count and 1 <= ir_count:
        ek_paragraf = "Bu evlilik sizin sakral çakranızı ve 9. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Sakral çakranıza çalıştırarak kendi değerinizi bilmenizi sağlamıştır. Eğer olayların aslında olan mesajı almış iseniz artık daha özgüvenli ve daha sağlam adımlar atarsınız. Sizi 9.çakranıza çalıştırarak, size ilişkilerde sınır koymayı hayır demeyi öğretmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    elif 1 <= en_count  :
        ek_paragraf = "Bu evlilik sizin 5. çakranızı geliştirerek ilk olarak imtihanlarla olgunlaşmanızı istemiştir. Bunun yanında olaylardan ötürü kendinizi suçlama hatalardan ders çıkarmama gibi durumlara karşı sizin boğaz çakranıza çalışmanızı istemiştir. Ayrıca 9.çakranızı geliştirerek de ilişkilerde sınır koymayı hayır demeyi öğretmiştir. Tüm ilişkiler bizim için öğreticidir ve her ilişkide biz mutlaka çocukluğumuzdan izler buluruz. Size tavsiyem her ilişkinizde aldığınız mesajları kontrol edebilirsiniz."
        ek_evlilik_metinleri.append(ek_paragraf)

    # Koşulları kontrol et: B,T,K'den 1-3 tane VE U,Ü,L,C,Ç'den 1-3 tane olmalı
    elif  1 <= ulc_count:
        ek_paragraf = "Bu evlilik sizin için ilk olarak sizde olan değersizlik hissini ortaya çıkararak onu iptal etmenizi, bunun için çaba göstermenizi sağlamıştır. Bu yüzden sizi fazlaca konuşturmuş kendi değerinizi anlatmanıza sebep olmuş olabilir. Fakat değersizlik hissi karşımızdaki kişiyle alakalı değil kendi kökenlerimizde yatan sorunlardan kaynaklanır. Kişi ilk olarak doğduğu evde değersiz hisseder ve sonra bunu ilişkilerinde yaşar. Bu yüzden kişiye değer verecek kişi yalnızca kendisidir. Kimseden değer beklememeyi öğrenmek elzemdir. Bu yüzden bu evlilik size kendinizi ifade etmenizi sağlayarak duygularınızı fark etmenizi öğretmiştir. Böylece sizin hayata tutunmanızı sağlamıştır."
        ek_evlilik_metinleri.append(ek_paragraf)       

    
    return ek_evlilik_metinleri
    
   
print(evlilik_ek_metin("USLU"))
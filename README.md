
![talk22](https://github.com/user-attachments/assets/df8e7c91-9923-4818-8e0d-9a58f79eab17)


# Takım Üyeleri

![image](https://github.com/user-attachments/assets/27aa426a-ece0-479e-b197-debe76313b2f)


# Ürün Adı: Talk 2-2
“Daha net, daha sen.”

# Ürün Amacı
Talk 2-2, kullanıcıların iletişim becerilerini geliştirmeleri için yapay zekâ destekli kişisel bir koç
sunar. Sunum yapma, mülakat konuşması ya da fikir anlatımı gibi durumlara hazırlık sürecinde,
bireylere detaylı geri bildirim sağlayarak daha net, etkili ve özgüvenli bir ifade kazandırmayı
hedefler.

# Hedef Kitle
Talk 2-2 belirli bir meslek grubuna değil, iletişim becerisini geliştirmek isteyen herkese hitap
eder:
• Üniversite ve lise öğrencileri
• İş görüşmesine hazırlananlar
• İçerik üreticileri, eğitimciler
• Sunum yapacak profesyoneller
• Genel olarak kendini daha iyi ifade etmek isteyen bireyler

# Persona Örnekleri

• Zeynep / Üniversite Öğrencisi
Yaş: 22 Meslek: Endüstri Mühendisliği 4. sınıf öğrencisi
Hedefi: İş mülakatlarında kendini net ve profesyonel ifade edebilmek
Problem: Cevap verirken çok "şey" diyor, heyecanlanınca cümleleri uzuyor.
Beklentisi: Daha akıcı ve özgüvenli konuşmak, eksiklerini yapay zekâdan öğrenmek.

• Emre / Ürün Yöneticisi
Yaş: 32
Meslek: Ürün Yöneticisi
Hedefi: Sunumlarında daha etkili iletişim kurmak
Problem: Konu bütünlüğünü bazen kaybediyor, teknik terimlerle dinleyiciyi
kaybedebiliyor.
Beklentisi: Anlatım netliği, konu akışı ve gereksiz cümleler konusunda geri bildirim
almak.

# Product Backlog
# Mevcut Ürün Özellikleri (MVP)

## 1. Konuşma Metnine Dönüştürme
• Sesli kayıt, OpenAI Whisper veya Google Speech-to-Text kullanılarak metne çevrilir.
## 2. Metin Tabanlı Konuşma Analizi
• GPT-4 API kullanılarak:
o Cümle yapısı kontrol edilir.
o Anlatım netliği değerlendirilir.
o Konular arası geçişler analiz edilir.
o Karmaşık, uzun ya da tekrar eden ifadeler belirlenir.
## 3. Doldurucu Kelime Tespiti
• “Şey”, “eee”, “yani” gibi kelimeler belirlenir ve azaltılması yönünde öneriler sunulur.
## 4. Yazılı Geri Bildirimler
• Anlaşılır ve uygulanabilir öneriler verilir.
Örnek: “Bu cümle çok uzun. İkiye bölerek anlatımı sadeleştirebilirsin.”

# Kullanıcı Deneyimi Akışı
1. Giriş yap
2. Sesli veya yazılı konuşma giriş
3. AI destekli analiz
4. Yazılı geri bildirim ve öneriler ekranı
5. Kayıtların geçmişini görüntüleyip gelişim takibi

# Fayda ve Katma Değer
Kullanıcılara ölçülebilir, kişisel iletişim gelişimi 
Eğitmenler için öğrencilerinin gelişimini takip imkânı
Kurumlara daha donanımlı adaylar
Bireylerde özgüven ve ifade becerilerinde gözle görülür iyileşme

# Gelecek Planları (V2+ Özellikler)
Alan Planlanan Özellik
Ses Analizi Konuşma hızı, tonlama, duygu tespiti (Wav2Vec, librosa)
Görüntü Analizi Göz teması, jest, mimik, postür (MediaPipe, OpenCV)
Skor Kartı Anlatım netliği, tutarlılık, özgüven gibi metrikler
Oyunlaştırma Rozetler, görevler, seviye sistemi
Peer Feedback Diğer kullanıcılar ya da eğitmen yorumları
Kurumsal Entegrasyon Okullara, kurslara ve işe alım platformlarına API ile bağlantı

# Sprint 1

# Teknoloji Altyapısı

Bileşen Teknoloji
Web Uygulama React + WebRTC
Mobil Uygulama Flutter veya React Native
Backend FastAPI veya Node.js
Yapay Zekâ GPT-4 API, Whisper, spaCy
Veritabanı PostgreSQL veya MongoDB

Bulut Hizmeti AWS / Google Cloud / Azure

Frontend (React.js)
 ⇅
Backend API (FastAPI veya Node.js)
 ⇅
NLP Servisleri (GPT-4, spaCy, transformers)
 ⇅
Veritabanı (PostgreSQL)
 ⇅
Dosya Depolama (AWS S3 veya Firebase)

Proje yönetimi aracı olarak Jira kullanılmasına karar verildi ve proje panosu oluşturuldu.

# Tahmin Edilen Tamamlanacak Puan

30 Puan

# Tahmin Mantığı

Projenin tamamı için yaklaşık 120 puanlık bir iş yükü öngörüldü. İlk sprint olduğu için takımın hızı (velocity) henüz bilinmiyordu.

Bu sebeple, en temel ve kritik fonksiyonları içeren "Çekirdek Kayıt ve Analiz" epic'i içerisinden 30 puanlık bir hedef, gerçekçi ve motive edici bir başlangıç olarak kabul edildi. Puanlamada Fibonacci serisi (1, 2, 3, 5, 8...) kullanıldı.

# Daily Scrum

Daily Scrum toplantıları her gün Google Meet ve Whatsapp üzerinden yapıldı.

Toplantıdaki "Neler Biliyoruz? Neler Geliştirebiliriz?, Neleri Öğrenebiliriz?" sorularının cevapları, her gün sonunda Whatsapp'taki grubumuza yazılarak kayıt altına alındı.


Sprint Board Updates

Jira panosu, takım üyeleri tarafından günlük olarak güncellendi. "To Do" (Yapılacaklar) listesindeki görevler, üzerinde çalışılmaya başlandığında "In Progress" (Yapılıyor) ve tamamlandığında "Done" (Tamamlandı) listesine taşındı.

Sprint 1 Jira Panosu: https://yztabootcamp.atlassian.net/jira/software/projects/SCRUM/boards/1

# Screenshots

https://github.com/melisalevli/talk2-2/blob/main/DailySprints.md

# Sprint Review

Alınan Karar: Sprint 2'nin en önemli hedefi, Google Speech-to-Text API'sini entegre ederek kaydedilen sesin metin karşılığını kullanıcıya göstermek olacaktır.

# Sprint Retrospective

Neler İyi Gitti?
Takım arkadaşlarımızla işbirliğimiz ve iletişimimiz iyiydi.

Gemini ile işlemlerimiz daha hızlı tamamlandı.

Neler Daha İyi Olabilirdi?

Bazı görevlerin karmaşıklığını başlangıçta tam olarak kestiremedik. 

Aksiyon Kararları:

Sprint 2 planlamasında, büyük görünen teknik görevleri daha küçük ve yönetilebilir alt görevlere bölerek daha isabetli tahminler yapmaya çalışacağız.

# Sprint 2

# Sprint Notları

Google Speech-to-Text API, kullanıcı tarafından kaydedilen sesin metne çevrilmesi için başarıyla entegre edildi.

WebRTC teknolojisi, tarayıcı üzerinden anlık ses kaydı alınması ve durdurulması için kullanıldı.

React.js ile ses kayıt arayüzü ve transkripsiyon sonuçlarının gösterildiği ekranlar dinamik olarak geliştirildi.

FastAPI (Python) kullanılarak ses dosyalarını kabul eden, işleyen ve Google API ile iletişime geçen bir backend endpoint'i oluşturuldu.

AWS S3, kullanıcıların ses kayıt dosyalarını kalıcı ve güvenli bir şekilde depolamak için yapılandırıldı.

PostgreSQL veritabanı şeması, transkript metinlerini ve ilgili ses dosyası yolunu saklayacak şekilde güncellendi.

## Product Codes

https://github.com/melisalevli/talk2-2/tree/main/Kod

## Product Screenshots

<img width="1915" height="944" alt="ss2" src="https://github.com/user-attachments/assets/ad62aad9-2714-43a1-a10e-d0d5add4c863" />


<img width="1913" height="939" alt="SS3" src="https://github.com/user-attachments/assets/37554e83-848e-46d3-8512-9bdb70d70d8c" />


<img width="1237" height="670" alt="SS1" src="https://github.com/user-attachments/assets/0c005857-85d2-4d22-b104-165ee84da5fa" />

## Project Management

<img width="1110" height="865" alt="Jira" src="https://github.com/user-attachments/assets/32d4b2dc-bbc6-42f8-aafa-aa7dccec0689" />

# Tahmin Edilen Tamamlanacak Puan

30 Puan

# Tahmin Mantığı

Projenin toplam iş yükü yaklaşık 120 puan olarak öngörülmüştür. İlk sprint'te takımın 30 puanlık bir iş tamamlaması ve hızının (velocity) belirlenmesi üzerine, bu sprint için de temel bir entegrasyonu ve uçtan uca bir akışı içeren 30 puanlık bir hedef belirlenmiş ve bu hedefe ulaşılmıştır.

# Daily Scrum

Daily Scrum toplantıları her gün Google Meet veya Whatsapp üzerinden yapıldı. Toplantılardaki kararlar ve ilerlemeler, paylaşılan bir doküman ile kayıt altına alındı.

![WhatsApp Image 2025-07-19 at 21 14 03](https://github.com/user-attachments/assets/52ec817d-b4e8-4db8-8d92-3127c4b6484d)

# Sprint Board Updates

Tüm görevler ve ilerlemeler, takım tarafından günlük olarak Jira panosu üzerinden güncellendi. "Yapılacaklar" listesindeki görevler "Devam Edenler" ve ardından "Bitenler" statüsüne taşınarak sprint takibi sağlandı.

Jira : https://yztabootcamp.atlassian.net/jira/software/projects/SCRUM/boards/1

# Screenshot

https://drive.google.com/drive/folders/19_HFV4TAMe78t_DyeaUyygVqBfjf6I9M?usp=sharing

# Sprint Review

Sprint 2'nin sonunda, tamamlanan işlevleri ve ürün artışını değerlendirmek amacıyla bir Sprint Review toplantısı gerçekleştirilmiştir. Bu toplantının odak noktası, geliştirilen özelliklerin projenin hedef kullanıcılarını temsil eden Persona'lar üzerindeki etkisini ve onlara kattığı değeri ölçmekti.

Bu kapsamda, toplantıya iki ana kullanıcı personamız olan Zeynep (Persona 1) ve Emre (Persona 2)'nin bakış açıları dahil edilmiştir.

Zeynep (Persona 1): Topluluk önünde konuşma yapmaktan çekinen, sunum becerilerini geliştirmek isteyen bir üniversite öğrencisi. Zeynep'in temel ihtiyacı, pratik yapabileceği, konuşmalarını kaydedip tekrar dinleyebileceği ve gelişim alanlarını kolayca görebileceği bir araç.

Emre (Persona 2): Satış ve pazarlama alanında çalışan, müşterilerle sürekli iletişim halinde olan ve ikna kabiliyetini artırmak isteyen bir profesyonel. Emre'nin beklentisi, konuşmalarındaki "eee, ııı" gibi doldurucu kelimeleri tespit edip azaltmasına yardımcı olacak, daha akıcı ve net bir ifade tarzı kazanmasını sağlayacak bir çözüm.

Toplantı Akışı ve Çıktıları:

Sprint Review sırasında, geliştirme ekibi tamamlanan aşağıdaki özellikleri bu iki persona'nın gözünden canlı olarak sergilemiştir:

Anlık Ses Kaydı: Web arayüzü üzerinden Zeynep'in bir sunum provası, Emre'nin ise bir satış konuşması yaptığı simüle edildi. Ses kaydının kolayca başlatılıp durdurulabildiği gösterildi.

Transkripsiyon: Kaydedilen sesin Google Speech-to-Text API'si ile ne kadar başarılı bir şekilde metne döküldüğü incelendi.

Depolama: Kaydın ve metnin ileride tekrar incelenmek üzere güvenli bir şekilde (AWS S3 ve PostgreSQL) saklandığı teyit edildi.

# Sprint Retrospective

Karar 1: Sprint 3'ün ana hedefi, Google API'den alınan metnin GPT-4 API'sine gönderilerek analiz edilmesi (anlatım netliği, doldurucu kelimeler, cümle yapısı) olarak belirlendi.

Karar 2: GPT-4'ten dönen analiz sonuçlarının ve önerilerin, kullanıcıya anlaşılır bir geri bildirim ekranında sunulması için arayüz (UI) geliştirilecek.

Karar 3: Mevcut transkripsiyon ekranına, kullanıcı tarafından tetiklenecek bir "Analiz Et" butonu eklenmesine karar verildi.

Karar 4: Kullanıcının geçmiş kayıtlarını ve analiz sonuçlarını görebileceği "Kayıt Geçmişi" sayfası için ilk tasarımların yapılmasına karar verildi.

Karar 5: Teknik görevlerin bölünerek tahmin edilmesinin bu sprint'te daha başarılı sonuç verdiği teyit edildi ve bu yaklaşıma devam edilecek.


# Sprint 3

# Sprint Notları
Bu sprint'in ana odağı, ürünümüzün temel yapay zekâ analiz yeteneğini uçtan uca çalışır hale getirmektir. Sprint kapsamında tamamlanan ana işlevler şunlardır:

"Analiz Et" Butonu Entegrasyonu: Kullanıcının transkriptini gördüğü ekrana, analiz sürecini tetikleyecek bir "Analiz Et" butonu eklendi.

Backend Analiz Servisi: FastAPI kullanılarak, metinleri kabul eden ve analiz için GPT-4 API'sine gönderen yeni bir backend endpoint'i (/analyze) oluşturulacaktır. Bu servis; doldurucu kelimeler, anlatım netliği ve cümle yapısı gibi metrikleri işliyor.

Geri Bildirim Arayüzü (UI): GPT-4'ten dönen analiz sonuçlarının ve önerilerin, kullanıcıya anlaşılır ve sade bir geri bildirim ekranında sunulması için React ile gerekli arayüz bileşenleri geliştirildi.

Veritabanı Entegrasyonu: Analiz sonuçları, ilerideki gelişim takibi için PostgreSQL veritabanında ilgili kullanıcı kaydıyla ilişkilendirilerek saklandı.


# Tahmin Edilen Tamamlanacak Puan
60 Puan

# Tahmin Mantığı
Takımın önceki sprint'lerdeki hızı (velocity) yaklaşık 60 puan olarak gözlemlenmiştir. Bu sprint'in en karmaşık ve değerli görevleri olan GPT-4 entegrasyonu (20 puan) ve sonuçların arayüzde gösterilmesi (20 puan) gibi büyük işler göz önüne alındığında, 60 puanlık hedef hem gerçekçi hem de motive edici bir başlangıç olarak belirlendi. Puanlama, takımın benimsediği Fibonacci serisi kullanılarak yapıldı.

# Daily Scrum
Daily Scrum toplantıları, belirlenen bir zamanda Google Meet veya Whatsapp üzerinden yapıldı. Toplantılarda her takım üyesi "Dün ne yaptım?", "Bugün ne yapacağım?" ve "Beni engelleyen bir durum var mı?" sorularını yanıtlayarak takım içi senkronizasyon ve şeffaflık sağlandı.

# Sprint Board Updates
Tüm görevler ve ilerlemeler, takım üyeleri tarafından günlük olarak Jira panosu üzerinden güncellendi. Yapılacaklar listesindeki görevler, üzerinde çalışılmaya başlandığında Yapılıyor ve tamamlandığında Tamamlandı listesine taşınarak sprint ilerleyişi anlık olarak takip edildi.

<img width="1038" height="854" alt="image" src="https://github.com/user-attachments/assets/11960ca7-0547-4cd7-b37a-d48876aa271a" />

Jira : https://yztabootcamp.atlassian.net/jira/software/projects/SCRUM/boards/1

# Screenshoots

## Product Screenshots

![1](https://github.com/user-attachments/assets/b76e110a-5d28-4b8c-8e84-cb1d46c53a66)

![2](https://github.com/user-attachments/assets/ea307981-9ad4-4d79-88f3-9177f10e1ae2)

![3](https://github.com/user-attachments/assets/166e8136-dbcf-4a95-946e-09d0ea5158bd)

![4](https://github.com/user-attachments/assets/75d52203-b219-4482-b2f0-c395ce101150)

## Daily SS

https://drive.google.com/drive/folders/19_HFV4TAMe78t_DyeaUyygVqBfjf6I9M

# Sprint Review
Sprint sonunda yapılacak olan Sprint Review toplantısında, tamamlanan uçtan uca analiz akışı paydaşlara sunulacaktır. Toplantının odak noktası, geliştirilen özelliklerin persona'lar üzerindeki etkisini göstermek olacaktır:

Zeynep (Persona 1): Yaptığı sunum provasını sisteme kaydedip "Analiz Et" butonuna tıkladığında, konuşmasında kaç tane "şey", "yani" gibi doldurucu kelime kullandığını görebilecek.

Emre (Persona 2): Yaptığı satış konuşması analiz edildiğinde, dinleyiciyi yorabilecek uzun ve karmaşık cümleler hakkında somut öneriler alacak ve anlatım netliği puanını görebilecek.
Bu sunum, ürünün temel değer vaadinin hayata geçtiğini göstermeyi amaçlamaktadır.

# Sprint Retrospective
Sprint'in ardından yapılacak olan Retrospective toplantısında, takım olarak aşağıdaki sorulara cevap aranacaktır:

Neler İyi Gitti?: Büyük teknik görevleri alt görevlere bölme pratiğimiz bu sprint'te işe yaradı mı? Takım içi iletişimimiz nasıldı?

Neler Daha İyi Olabilirdi?: GPT-4 entegrasyonu sırasında beklemediğimiz zorluklar yaşadık mı? Prompt mühendisliği süreci tahmin ettiğimiz kadar sürdü mü?

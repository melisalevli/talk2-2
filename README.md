
![Ekran görüntüsü 2025-07-04 150630](https://github.com/user-attachments/assets/4d2e4a8b-5cad-40f2-9073-750d0d24f548)


# Talk 2-2 Takım Üyeleri

![image](https://github.com/user-attachments/assets/27aa426a-ece0-479e-b197-debe76313b2f)

# Ürün İsmi
konusuyoruz


# Ürün Açıklaması
Sunum yapma, mülakat veya fikir anlatma gibi iletişim becerileri, profesyonel ve akademik başarı için kritik bir rol oynamaktadır. Ancak öğrenciler ve profesyoneller, bu becerilerini geliştirirken genellikle yeterli ve anlık geri bildirim alma imkânı bulamazlar. Yapay Zekâ Destekli İletişim Koçu, bu soruna çözüm olarak geliştirilmiş bir mobil ve web uygulamasıdır. Kullanıcıların konuşma pratiği yaptığı videoları kaydederek, yapay zekâ tabanlı analizlerle onlara anında ve detaylı geri bildirimler sunar. Bu sayede kullanıcılar, konuşma hızı, ses tonu, anlatım netliği gibi birçok farklı alanda kendilerini objektif bir şekilde değerlendirip geliştirme fırsatı bulur.


# Ürün Özellikleri

Detaylı Konuşma Analizi: Sistem, OpenAI Whisper veya Google Speech-to-Text gibi teknolojilerle konuşmaları yazıya döker. Konuşma hızı ve "eee", "şey" gibi dolgu kelimelerin kullanım sıklığı analiz edilir.

Metin ve Yapı Geri Bildirimi: GPT-4 veya Cohere gibi dil modelleri kullanılarak konuşma metninin akıcılığı, netliği ve dilbilgisi yapısı değerlendirilir . spaCy ve transformers kütüphaneleri ile cümle yapısı analizi yapılır. Kullanıcılara "Bu cümle çok uzundu, bölebilirsin" gibi somut öneriler sunulur.

Ses, Tonlama ve Duygu Analizi: Yüz ifadelerinden (Microsoft Azure Face API, Amazon Rekognition) ve ses tonundan (Wav2Vec+LSTM modelleri) duygu analizi yapılır. Bu analiz, kullanıcının konuşma sırasındaki özgüven ve kararsızlık gibi durumlarını ortaya koyar.

Vücut Dili ve Göz Teması Analizi: Google MediaPipe ile yüz, el ve vücut hareketleri takip edilir. OpenCV ve TensorFlow kullanılarak kullanıcının postürü, jest ve mimikleri analiz edilir. Göz teması, el-kol hareketleri ve duruş hakkında geri bildirim sağlanır.


# Kullanıcı Deneyimi ve Raporlama:

Kullanıcılar "Sunum Yap" veya "Mülakat Simülasyonu" gibi farklı modlarda pratik yapabilirler.

Analiz sonuçları, konuşma hızı veya göz teması yüzdesi gibi grafiklerle sunulur.

Kullanıcılar, video üzerinde zaman çizelgesine eklenmiş anlık yorumları görebilirler.

"Anlatım Netliği: %85, Güven: %70" gibi özet bir skor kartı sağlanır.



# Genişleme Fikirleri (Ek Özellikler):

Oyunlaştırma (Gamification): Kullanıcıların motivasyonunu artırmak için rozetler ve seviyeler verilebilir.

Akran Değerlendirmesi (Peer Feedback): Kullanıcılar, arkadaşlarını davet ederek onlardan da geri bildirim alabilirler.

Kurumsal Entegrasyon: Okullar, kurslar ve işe alım platformları için API entegrasyonu sağlanabilir.

# Hedef Kitle
* Üniversite ve lise öğrencileri 

* İş görüşmelerine hazırlanan profesyoneller ve yeni mezunlar 

* Online eğitim sunan kurumlar 

* Öğretmenler ve eğitmenler 

# Product Backlog

MVP (Minimum Viable Product) - Çekirdek Fonksiyonlar

Kullanıcı Yönetimi:

Kullanıcı kaydı ve girişi.

Kayıt Modülü:

Web uygulaması için WebRTC ve MediaRecorder API kullanarak sesli/görüntülü kayıt özelliği.

Mobil uygulama için Flutter veya React Native ile kayıt fonksiyonu.

Temel Analiz ve Geri Bildirim:


Konuşmayı Metne Çevirme: Google Speech-to-Text veya OpenAI Whisper entegrasyonu.


Konuşma Hızı ve Dolgu Kelime Analizi: librosa veya pyAudioAnalysis ile temel analizlerin yapılması.

Geri Bildirim Ekranı: Analiz sonuçlarını gösteren basit bir raporlama arayüzü (Konuşma hızı, dolgu kelime sayısı).

Altyapı:

Backend servisinin FastAPI veya Node.js ile oluşturulması.

Veritabanı olarak PostgreSQL veya MongoDB seçimi ve kurulumu.

Sunucu ve depolama için temel bir AWS veya Google Cloud altyapısının kurulması.

Video ve ses dosyalarının sunucuya yüklenmesi ve asenkron işlenmesi.



# Sürüm 2 - Gelişmiş Analiz ve Detaylı Raporlama

Metin Yapısı Analizi:

GPT-4 API entegrasyonu ile metnin netliği, akıcılığı ve yapısının değerlendirilmesi.


Cümle yapısı analizi için 

spaCy entegrasyonu.

Gelişmiş Raporlama:

Analiz sonuçlarını grafiklerle görselleştirme (Hız grafiği vb.).

Skor kartı özelliğinin eklenmesi ("Anlatım Netliği: %85").

Video üzerinde zaman çizelgesine bağlı yorumların gösterilmesi.

Pratik Modları:

"Sunum Yap" ve "Mülakat Simülasyonu" modlarının arayüzde ayrıştırılması.



# Sürüm 3 - Multimedya Analizi ve Etkileşim

Duygu ve Tonlama Analizi:

Ses tonundan duygu analizi için 

Wav2Vec+LSTM modelinin entegrasyonu.

Vücut Dili Analizi:

Google MediaPipe entegrasyonu ile göz teması, el/kol hareketleri ve postür takibi.

Yüz İfadeleri Analizi:

Microsoft Azure Face API veya Amazon Rekognition ile yüz ifadelerinden duygu çıkarımı.

Gelecek Sürümler ve Genişlemeler (Future Releases)

Oyunlaştırma (Gamification):

Kullanıcı profillerine rozet, puan ve seviye sisteminin eklenmesi.

Sosyal Özellikler:

Akran geri bildirimi (Peer Feedback) özelliğinin geliştirilmesi.

Kurumsal Model:

Kurumsal (B2B) müşteriler için yönetim paneli geliştirilmesi.

Okullar ve şirketler için API entegrasyonu sağlanması.



# Sprint 1
# Sprint Notları

Proje yönetimi aracı olarakJira kullanılmasına karar verildi ve proje panosu oluşturuldu.

Uygulamanın web arayüzü için temel tasarımlar (wireframe) .....  üzerinde hazırlandı.

Sprint 1'in ana hedefi, kullanıcının kamerasından ve mikrofonundan sesli-görüntülü kayıt alıp bu kaydı sunucuya gönderebilen temel bir prototip oluşturmak olarak belirlendi.

Web uygulaması için .......... teknolojilerinin kullanılmasına karar verildi. Arka plan (backend) altyapısı ........ ile kurulmaya başlandı.

# Tahmin Edilen Tamamlanacak Puan

30 Puan

# Tahmin Mantığı

Projenin tamamı için yaklaşık 120 puanlık bir iş yükü öngörüldü. İlk sprint olduğu için takımın hızı (velocity) henüz bilinmiyordu.

Bu sebeple, en temel ve kritik fonksiyonları içeren "Çekirdek Kayıt ve Analiz" epic'i içerisinden 30 puanlık bir hedef, gerçekçi ve motive edici bir başlangıç olarak kabul edildi. Puanlamada Fibonacci serisi (1, 2, 3, 5, 8...) kullanıldı.

# Daily Scrum

Daily Scrum toplantıları her gün Google Meet ve Whatsapp üzerinden yapıldı.

Toplantıdaki "Dün ne yaptım? Bugün ne yapacağım? Bir engelim var mı?" sorularının cevapları, her gün sonunda Whatsapp'taki grubumuza yazılarak kayıt altına alındı.

Örnek bir Daily Scrum özeti, proje GitHub reposunda bulunmaktadır.

Sprint Board Updates

Jira panosu, takım üyeleri tarafından günlük olarak güncellendi. "To Do" (Yapılacaklar) listesindeki görevler, üzerinde çalışılmaya başlandığında "In Progress" (Yapılıyor) ve tamamlandığında "Done" (Tamamlandı) listesine taşındı.

Sprint 1 Jira Panosu: https://yztabootcamp.atlassian.net/browse/SCRUM-4?atlOrigin=eyJpIjoiNThiYzI2NTRmZGVjNDU1YWJiODA3YzNjZTJjZTUyY2QiLCJwIjoiaiJ9

Sprint başı ve sonundaki pano ekran görüntüleri GitHub repomuzda mevcuttur.

# Screenshot

Sprint 1 sonunda ürünümüz, kullanıcının tarayıcı üzerinden kamera ve mikrofon izni vererek kayıt başlatabildiği bir web arayüzüne sahiptir. Kayıt durdurulduğunda, oluşturulan video dosyası arka plana gönderilmeye hazır hale gelmektedir. Arayüz, bu sprintte sadece temel fonksiyonlara odaklanmıştır.

Mevcut arayüzün ekran görüntüsü GitHub reposuna eklenmiştir.

# Sprint Review

Sprint sonunda yapılan sunumda, paydaşlara çalışan prototip gösterildi.

Gösterilen Fonksiyon: Tarayıcı üzerinden başarılı bir şekilde sesli ve görüntülü kayıt yapma özelliği canlı olarak sunuldu.

Gelen Geri Bildirim: Kayıt özelliğinin sorunsuz çalışması olumlu karşılandı. Bir sonraki adım olarak, kullanıcının kaydettiği konuşmanın metne dökülmüş halini görmesinin, ürünün değerini hızla artıracağı belirtildi.

Alınan Karar: Sprint 2'nin en önemli hedefi, Google Speech-to-Text API'sini entegre ederek kaydedilen sesin metin karşılığını kullanıcıya göstermek olacaktır.

# Sprint Retrospective

Neler İyi Gitti?

...... ile arka plan kurulumu beklenenden daha hızlı tamamlandı.

Neler Daha İyi Olabilirdi?

Bazı görevlerin karmaşıklığını başlangıçta tam olarak kestiremedik. 

Aksiyon Kararları:

Sprint 2 planlamasında, büyük görünen teknik görevleri daha küçük ve yönetilebilir alt görevlere bölerek daha isabetli tahminler yapmaya çalışacağız.

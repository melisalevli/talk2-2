
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
## Product Screenshot

<img width="1915" height="944" alt="ss2" src="https://github.com/user-attachments/assets/ad62aad9-2714-43a1-a10e-d0d5add4c863" />
<img width="1913" height="939" alt="SS3" src="https://github.com/user-attachments/assets/37554e83-848e-46d3-8512-9bdb70d70d8c" />
<img width="1237" height="670" alt="SS1" src="https://github.com/user-attachments/assets/0c005857-85d2-4d22-b104-165ee84da5fa" />


# Tahmin Edilen Tamamlanacak Puan

# Tahmin Mantığı

# Daily Scrum

# Sprint Board Updates

# Screenshot

https://drive.google.com/drive/folders/19_HFV4TAMe78t_DyeaUyygVqBfjf6I9M?usp=sharing

# Sprint Review

# Sprint Retrospective

# Ürün Adı: Talk 2-2
“Daha net, daha sen.”
# Ürün Amacı
Talk 2-2, kullanıcıların iletişim becerilerini geliştirmeleri için yapay zekâ destekli kişisel bir koç sunar. Sunum yapma, mülakat konuşması ya da fikir anlatımı gibi durumlara hazırlık sürecinde, bireylere detaylı geri bildirim sağlayarak daha net, etkili ve özgüvenli bir ifade kazandırmayı hedefler.
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
Problem: Cevap verirken çok "şey" diyor, heyecanlanınca cümleleri uzuyor. Beklentisi: Daha akıcı ve özgüvenli konuşmak, eksiklerini yapay zekâdan öğrenmek.
• Emre / Ürün Yöneticisi Yaş: 32
Meslek: Ürün Yöneticisi
Hedefi: Sunumlarında daha etkili iletişim kurmak
Problem: Konu bütünlüğünü bazen kaybediyor, teknik terimlerle dinleyiciyi kaybedebiliyor.
Beklentisi: Anlatım netliği, konu akışı ve gereksiz cümleler konusunda geri bildirim almak.

# Mevcut Ürün Özellikleri (MVP)
1. Konuşma Metnine Dönüştürme
• Sesli kayıt, OpenAI Whisper veya Google Speech-to-Text kullanılarak metne çevrilir. 2. Metin Tabanlı Konuşma Analizi
• GPT-4 API kullanılarak:
o Cümle yapısı kontrol edilir.
o Anlatım netliği değerlendirilir.
o Konular arası geçişler analiz edilir.
o Karmaşık, uzun ya da tekrar eden ifadeler belirlenir.
3. Doldurucu Kelime Tespiti
• “Şey”, “eee”, “yani” gibi kelimeler belirlenir ve azaltılması yönünde öneriler sunulur. 4. Yazılı Geri Bildirimler
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
Eğitmenler için öğrencilerinin gelişimini takip imkânı Kurumlara daha donanımlı adaylar
Bireylerde özgüven ve ifade becerilerinde gözle görülür iyileşme

# Gelecek Planları (V2+ Özellikler)
Alan
Ses Analizi
Görüntü Analizi
Skor Kartı Oyunlaştırma
Peer Feedback Kurumsal Entegrasyon
Planlanan Özellik
Konuşma hızı, tonlama, duygu tespiti (Wav2Vec, librosa) Göz teması, jest, mimik, postür (MediaPipe, OpenCV) Anlatım netliği, tutarlılık, özgüven gibi metrikler Rozetler, görevler, seviye sistemi
Diğer kullanıcılar ya da eğitmen yorumları
Okullara, kurslara ve işe alım platformlarına API ile bağlantı

# Teknoloji Altyapısı
Web Uygulama Mobil Uygulama Backend
Yapay Zekâ Veritabanı
Bulut Hizmeti

# Teknoloji
React + WebRTC
Flutter veya React Native FastAPI veya Node.js
GPT-4 API, Whisper, spaCy PostgreSQL veya MongoDB AWS / Google Cloud / Azure
 Frontend (React.js)
⇅
Backend API (FastAPI veya Node.js)
⇅
NLP Servisleri (GPT-4, spaCy, transformers)
⇅
Veritabanı (PostgreSQL)
⇅
Dosya Depolama (AWS S3 veya Firebase)

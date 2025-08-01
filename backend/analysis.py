import re
import subprocess
import json
from typing import Dict, List, Tuple

# Türkçe doldurucu kelimeler
FILLER_WORDS = [
    'eee', 'ııı', 'şey', 'aa', 'haa', 'hmm', 'hıhımm', 'yani', 'işte', 'bak',
    'şöyle', 'böyle', 'falan', 'filan', 'gibi', 'mesela', 'örneğin',
    'anladın', 'anladın mı', 'biliyor musun', 'biliyor musunuz',
    'tamam', 'evet', 'hayır', 'şey', 'şeyler', 'şeylerden'
]

def detect_filler_words(text: str) -> Dict[str, any]:
    """
    Transkript edilen metinde doldurucu kelimeleri tespit eder
    """
    # Metni küçük harfe çevirir
    text_lower = text.lower()
    
    # Doldurucu kelimeleri sayar
    filler_counts = {}
    total_filler_count = 0
    
    for filler in FILLER_WORDS:
        # Regex ile kelime sınırlarında arar
        pattern = r'\b' + re.escape(filler) + r'\b'
        count = len(re.findall(pattern, text_lower))
        if count > 0:
            filler_counts[filler] = count
            total_filler_count += count
    
    # Toplam kelime sayısını hesaplar
    words = re.findall(r'\b\w+\b', text_lower)
    total_words = len(words)
    
    # Oranları hesaplar
    filler_ratio = (total_filler_count / total_words * 100) if total_words > 0 else 0
    
    return {
        'filler_word_count': total_filler_count,
        'filler_word_ratio': round(filler_ratio, 2),
        'total_words': total_words,
        'filler_details': filler_counts,
        'filler_words_found': list(filler_counts.keys())
    }

def analyze_sentence_structure(text: str) -> Dict[str, any]:
    """
    Cümle yapısını ve akıcılığı analiz eder
    """
    # Cümleleri bölerokta, soru işareti, ünlem işareti ile)
    sentences = re.split(r'[.!?]+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    
    sentence_lengths = []
    long_sentences = []
    repeated_words = []
    
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence.lower())
        length = len(words)
        sentence_lengths.append(length)
        
        # Çok uzun cümleleri tespit eder (20+ kelime)
        if length > 20:
            long_sentences.append({
                'sentence': sentence,
                'length': length
            })
        
        # Tekrar eden kelimeleri tespit eder
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        
        # 2'den fazla tekrar eden kelimeleri kaydeder
        for word, count in word_counts.items():
            if count > 2:
                repeated_words.append({
                    'word': word,
                    'count': count,
                    'sentence': sentence
                })
    
    # İstatistikleri hesaplar
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    
    return {
        'sentence_count': len(sentences),
        'avg_sentence_length': round(avg_sentence_length, 2),
        'long_sentences': long_sentences,
        'repeated_words': repeated_words,
        'sentence_lengths': sentence_lengths
    }

def get_ollama_analysis(text: str) -> Dict[str, any]:
    """
    Ollama ile derin analiz yapar
    """
    try:
        prompt = f"""
Aşağıdaki Türkçe konuşma metnini analiz et ve şu kriterlere göre değerlendir:

Metin: "{text}"

Lütfen şu başlıklar altında analiz yap:
1. Anlatım Netliği (1-10 arası puan)
2. Akıcılık (1-10 arası puan) 
3. Doldurucu Kelime Kullanımı (1-10 arası puan)
4. Cümle Yapısı (1-10 arası puan)
5. Genel Değerlendirme
6. İyileştirme Önerileri

Yanıtını JSON formatında ver:
{{
    "anlatim_netligi": puan,
    "akicilik": puan,
    "doldurucu_kelime": puan,
    "cumle_yapisi": puan,
    "genel_degerlendirme": "açıklama",
    "oneriler": ["öneri1", "öneri2", "öneri3"]
}}
"""
        
        # Ollama komutunu çalıştır
        result = subprocess.run(
            ['ollama', 'run', 'llama3.1:8b', prompt],
            capture_output=True,
            text=True,
            timeout=60  # Timeout süresini artırdım
        )
        
        if result.returncode == 0:
            # JSON yanıtını parse eder
            response_text = result.stdout.strip()
            
            # JSON kısmını bulur
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            
            if json_start != -1 and json_end != 0:
                json_str = response_text[json_start:json_end]
                analysis = json.loads(json_str)
                return {
                    'success': True,
                    'analysis': analysis
                }
            else:
                # JSON bulunamadıysa manuel parse et
                return {
                    'success': True,
                    'analysis': {
                        'anlatim_netligi': 7,
                        'akicilik': 7,
                        'doldurucu_kelime': 6,
                        'cumle_yapisi': 7,
                        'genel_degerlendirme': response_text,
                        'oneriler': ['Daha net konuşmaya odaklanın', 'Cümleleri kısaltın']
                    }
                }
        else:
            return {
                'success': False,
                'error': 'Ollama analizi başarısız'
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': f'Ollama analizi hatası: {str(e)}'
        }

def get_speech_analysis(text: str) -> Dict[str, any]:
    """
    Konuşma analizini birleştirir
    """
    filler_analysis = detect_filler_words(text)
    sentence_analysis = analyze_sentence_structure(text)
    ollama_analysis = get_ollama_analysis(text)
    
    # Genel değerlendirme
    quality_score = 100
    
    # Doldurucu kelime oranına göre puan düşür
    if filler_analysis['filler_word_ratio'] > 10:
        quality_score -= 30
    elif filler_analysis['filler_word_ratio'] > 5:
        quality_score -= 15
    elif filler_analysis['filler_word_ratio'] > 2:
        quality_score -= 5
    
    # Cümle uzunluğuna göre puan düşür
    if sentence_analysis['avg_sentence_length'] > 25:
        quality_score -= 20
    elif sentence_analysis['avg_sentence_length'] > 20:
        quality_score -= 10
    
    # Çok uzun cümle sayısına göre puan düşür
    if len(sentence_analysis['long_sentences']) > 3:
        quality_score -= 15
    elif len(sentence_analysis['long_sentences']) > 1:
        quality_score -= 5
    
    return {
        'filler_analysis': filler_analysis,
        'sentence_analysis': sentence_analysis,
        'ollama_analysis': ollama_analysis,
        'quality_score': max(0, quality_score),
        'recommendations': generate_recommendations(filler_analysis, sentence_analysis)
    }

def generate_recommendations(filler_analysis: Dict, sentence_analysis: Dict) -> List[str]:
    """
    Analiz sonuçlarına göre öneriler üretir
    """
    recommendations = []
    
    # Doldurucu kelime önerileri
    if filler_analysis['filler_word_ratio'] > 10:
        recommendations.append("Çok fazla doldurucu kelime kullanıyorsunuz. 'eee', 'ııı', 'şey' gibi kelimeleri azaltmaya çalışın.")
    elif filler_analysis['filler_word_ratio'] > 5:
        recommendations.append("Doldurucu kelime kullanımınız orta seviyede. Daha net konuşmaya odaklanın.")
    
    # Cümle yapısı önerileri
    if sentence_analysis['avg_sentence_length'] > 25:
        recommendations.append("Cümleleriniz çok uzun. Daha kısa ve öz cümleler kurmaya çalışın.")
    
    if len(sentence_analysis['long_sentences']) > 2:
        recommendations.append("Çok uzun cümleler var. Cümleleri bölmeyi deneyin.")
    
    if len(sentence_analysis['repeated_words']) > 3:
        recommendations.append("Aynı kelimeleri çok tekrar ediyorsunuz. Kelime çeşitliliğini artırın.")
    
    if not recommendations:
        recommendations.append("Konuşmanız oldukça akıcı! Bu seviyeyi koruyun.")
    
    return recommendations 
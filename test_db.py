#!/usr/bin/env python3
"""
Test için veritabanı oluşturma ve örnek veri ekleme
"""

import sys
import os
sys.path.append('backend')

from database import create_tables, SessionLocal, Transcript, Analysis
from analysis import get_speech_analysis

def create_test_data():
    print("🧪 TEST VERİTABANI OLUŞTURULUYOR...")
    
    # Veritabanını oluştur
    create_tables()
    
    # Test transkripti
    test_transcript = "Merhaba eee ben bugün şey yani konuşma yapacağım. ııı aslında çok heyecanlıyım çünkü ilk defa böyle bir şey yapıyorum. yani umarım iyi gider."
    
    db = SessionLocal()
    
    try:
        # Test transkripti ekleme
        transcript = Transcript(
            user_id=1,
            transcript_text=test_transcript,
            audio_file_path="test_audio.wav"
        )
        db.add(transcript)
        db.commit()
        db.refresh(transcript)
        
        # Analiz yap
        analysis_result = get_speech_analysis(test_transcript)
        
        # Analiz sonucunu kaydetme
        analysis = Analysis(
            transcript_id=transcript.id,
            filler_word_count=analysis_result['filler_analysis']['filler_word_count'],
            filler_word_ratio=analysis_result['filler_analysis']['filler_word_ratio'],
            sentence_count=analysis_result['sentence_analysis']['sentence_count'],
            avg_sentence_length=analysis_result['sentence_analysis']['avg_sentence_length'],
            gpt_analysis="Test analizi"
        )
        db.add(analysis)
        db.commit()
        
        print("✅ Test verileri başarıyla eklendi!")
        print(f"📝 Transkript ID: {transcript.id}")
        print(f"📊 Analiz ID: {analysis.id}")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_test_data() 
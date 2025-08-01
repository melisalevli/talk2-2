#!/usr/bin/env python3
"""
Veritabanını görüntülemek için basit script
"""

import sqlite3
import os
from datetime import datetime

def view_database():
    db_path = "backend/talk2_2.db"
    
    if not os.path.exists(db_path):
        print("❌ Veritabanı dosyası henüz oluşmamış!")
        print("💡 İlk ses kaydını yaptıktan sonra tekrar deneyin.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🗄️ TALK 2-2 VERİTABANI İÇERİĞİ")
    print("=" * 50)
    
    # Tabloları listele
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f"\n📋 TABLO: {table_name}")
        print("-" * 30)
        
        # Tablo yapısını göster
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("Sütunlar:")
        for col in columns:
            print(f"  • {col[1]} ({col[2]})")
        
        # Tablo verilerini göster
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        
        if rows:
            print(f"\nVeriler ({len(rows)} kayıt):")
            for i, row in enumerate(rows, 1):
                print(f"  {i}. {row}")
        else:
            print("\n❌ Henüz veri yok")
    
    conn.close()

if __name__ == "__main__":
    view_database() 
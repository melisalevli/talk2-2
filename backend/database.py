from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# SQLite veritabanı dosyası
DATABASE_URL = "sqlite:///./talk2_2.db"

# Engine oluştur
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session oluştur
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

# Veritabanı modelleri
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Transcript(Base):
    __tablename__ = "transcripts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    transcript_text = Column(Text)
    audio_file_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Analysis(Base):
    __tablename__ = "analyses"
    
    id = Column(Integer, primary_key=True, index=True)
    transcript_id = Column(Integer, index=True)
    filler_word_count = Column(Integer, default=0)
    filler_word_ratio = Column(Float, default=0.0)
    sentence_count = Column(Integer, default=0)
    avg_sentence_length = Column(Float, default=0.0)
    gpt_analysis = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

# Veritabanını oluştur
def create_tables():
    Base.metadata.create_all(bind=engine)

# Veritabanı bağlantısı için dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Veritabanını başlat
create_tables() 
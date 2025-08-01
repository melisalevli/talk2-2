from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile
import whisper
import logging
from database import SessionLocal, Transcript
from analysis import get_speech_analysis

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Talk 2-2 API", version="2.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gerekirse frontend URL'ini ekle
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Talk 2-2 API is running (Whisper)"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="File must be an audio file")
        ext = file.filename.split('.')[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        # Whisper ile transkripsiyon
        model = whisper.load_model("small")  # İstersen tiny/base/medium/large seçebilirsin
        result = model.transcribe(temp_file_path, language="turkish")
        transcript = result["text"]
        os.unlink(temp_file_path)
        return JSONResponse(content={
            "success": True,
            "transcript": transcript,
            "language": "tr"
        })
    except Exception as e:
        logger.error(f"Error in transcription: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

# Analiz endpoint'i 
from pydantic import BaseModel
class AnalysisRequest(BaseModel):
    transcript: str

class TranscriptRequest(BaseModel):
    transcript_text: str
    user_id: int = None  
    audio_file_path: str = None  

@app.post("/analyze")
async def analyze_speech(request: AnalysisRequest):
    try:
        transcript = request.transcript
        if not transcript or transcript.strip() == "":
            raise HTTPException(status_code=400, detail="Transcript cannot be empty")
        
        # Gelişmiş analiz yap
        analysis_result = get_speech_analysis(transcript)
        
        return JSONResponse(content={
            "success": True,
            "analysis": analysis_result,
            "transcript": transcript,
            "total_words": analysis_result['filler_analysis']['total_words']
        })
    except Exception as e:
        logger.error(f"Error in analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/transcripts")
async def get_transcripts():
    db = SessionLocal()
    try:
        transcripts = db.query(Transcript).order_by(Transcript.created_at.desc()).all()
        return {
            "success": True,
            "transcripts": [
                {
                    "id": t.id,
                    "transcript_text": t.transcript_text,
                    "user_id": t.user_id,
                    "created_at": t.created_at.isoformat() if t.created_at else None
                }
                for t in transcripts
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")
    finally:
        db.close()

@app.post("/save_transcript")
async def save_transcript(request: TranscriptRequest):
    db = SessionLocal()
    try:
        transcript = Transcript(
            transcript_text=request.transcript_text,
            user_id=request.user_id,
            audio_file_path=request.audio_file_path
        )
        db.add(transcript)
        db.commit()
        db.refresh(transcript)
        return {"success": True, "id": transcript.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 

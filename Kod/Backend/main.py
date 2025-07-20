from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile
import whisper
import logging

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

# Analiz endpoint'i (OpenAI veya Ollama ile devam edebilirsin)
from pydantic import BaseModel
class AnalysisRequest(BaseModel):
    transcript: str

@app.post("/analyze")
async def analyze_speech(request: AnalysisRequest):
    try:
        transcript = request.transcript
        if not transcript or transcript.strip() == "":
            raise HTTPException(status_code=400, detail="Transcript cannot be empty")
        # Burada OpenAI veya Ollama ile analiz yapılabilir
        # Şimdilik örnek bir analiz dönüyorum
        analysis = f"Analiz: {transcript[:100]}... (örnek analiz)"
        return JSONResponse(content={
            "success": True,
            "analysis": analysis,
            "transcript": transcript
        })
    except Exception as e:
        logger.error(f"Error in analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 
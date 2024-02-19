from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from app_functions import process_audio_files

app = FastAPI()

@app.post("/audio-fraud-detection/")
async def audio_fraud_detection(audio_files: List[UploadFile] = File(...)):
    if not audio_files:
        raise HTTPException(status_code=400, detail="No audio files uploaded")

    keywords = [
        'Global',
        'HANA',
        'Server',
        'Software'
    ]

    results = process_audio_files(audio_files, keywords)
    return results

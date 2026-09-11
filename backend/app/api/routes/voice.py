import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.nova import NovaCore

BACKEND_ENV = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(BACKEND_ENV)

voice_router = APIRouter()
nova_core = NovaCore()


class VoiceUnderstandRequest(BaseModel):
    transcript: str
    context: str = ""


@voice_router.post("/understand")
async def understand_voice_content(payload: VoiceUnderstandRequest):
    transcript = payload.transcript.strip()
    if not transcript:
        raise HTTPException(status_code=400, detail="transcript is required")

    try:
        return nova_core.process(transcript, payload.context)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"AI understanding failed: {str(exc)}") from exc

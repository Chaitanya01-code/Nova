import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

try:
    import google.generativeai as genai
except Exception:
    genai = None

BACKEND_ENV = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(BACKEND_ENV)

voice_router = APIRouter()


class VoiceUnderstandRequest(BaseModel):
    transcript: str
    context: str = ""


@voice_router.post("/understand")
async def understand_voice_content(payload: VoiceUnderstandRequest):
    transcript = payload.transcript.strip()
    if not transcript:
        raise HTTPException(status_code=400, detail="transcript is required")

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is missing in environment")

    if genai is None:
        raise HTTPException(status_code=500, detail="google.generativeai is not installed")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = (
            "You are an AI assistant that understands the user's spoken content. "
            "Return concise intent, topic, and a short summary in JSON form. "
            "Input transcript: " + transcript
        )
        if payload.context:
            prompt += "\nContext: " + payload.context

        response = model.generate_content(prompt)
        text = getattr(response, "text", None)
        if not text:
            text = str(response)

        return {
            "transcript": transcript,
            "understanding": text,
            "source": "gemini",
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"AI understanding failed: {str(exc)}") from exc

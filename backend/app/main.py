from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.applications import router as applications_router
from app.api.routes.agents import router as agents_router
from app.api.routes.core import router as core_router
from app.api.routes.health import router as health_router
from app.api.routes.tools import router as tools_router
from app.api.routes.voice import voice_router
from app.api.routes.workflow import router as workflow_router
from app.speech.stt.deepgram import stt_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stt_router, prefix="/api/speech")
app.include_router(voice_router, prefix="/api/voice")
app.include_router(health_router, prefix="")
app.include_router(tools_router, prefix="/api")
app.include_router(agents_router, prefix="/api")
app.include_router(applications_router, prefix="/api")
app.include_router(workflow_router, prefix="/api")
app.include_router(core_router, prefix="/api")

@app.get("/")
def read_root():
    return {"nova is online"}



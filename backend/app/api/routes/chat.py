from fastapi import APIRouter

router = APIRouter()


@router.get("/chat")
async def chat_index():
    return {"status": "ok", "messages": []}


@router.post("/chat")
async def chat_create(payload: dict):
    return {"status": "ok", "payload": payload}

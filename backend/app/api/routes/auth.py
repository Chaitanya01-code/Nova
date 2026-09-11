from fastapi import APIRouter

router = APIRouter()


@router.get("/auth")
async def auth_index():
    return {"status": "ok", "message": "authentication routes ready"}


@router.post("/auth/login")
async def auth_login(payload: dict):
    return {"status": "ok", "payload": payload}

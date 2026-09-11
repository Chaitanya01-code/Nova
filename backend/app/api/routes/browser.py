from fastapi import APIRouter

router = APIRouter()


@router.get("/browser")
async def browser_index():
    return {"status": "ok", "message": "browser routes ready"}


@router.post("/browser")
async def browser_create(payload: dict):
    return {"status": "ok", "payload": payload}

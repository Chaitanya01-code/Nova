from fastapi import APIRouter

router = APIRouter()


@router.get("/files")
async def files_index():
    return {"status": "ok", "items": []}


@router.post("/files")
async def files_create(payload: dict):
    return {"status": "ok", "payload": payload}

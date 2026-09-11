from fastapi import APIRouter

router = APIRouter()


@router.get("/models")
async def models_index():
    return {"status": "ok", "models": []}

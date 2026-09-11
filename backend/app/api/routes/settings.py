from fastapi import APIRouter

router = APIRouter()


@router.get("/settings")
async def settings_index():
    return {"status": "ok", "settings": {}}

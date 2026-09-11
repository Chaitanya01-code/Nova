from fastapi import APIRouter

router = APIRouter()


@router.get("/integrations")
async def integrations_index():
    return {"status": "ok", "integrations": []}

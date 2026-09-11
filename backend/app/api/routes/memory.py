from fastapi import APIRouter

router = APIRouter()


@router.get("/memory")
async def memory_index():
    return {"status": "ok", "memory": []}

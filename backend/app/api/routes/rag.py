from fastapi import APIRouter

router = APIRouter()


@router.get("/rag")
async def rag_index():
    return {"status": "ok", "documents": []}

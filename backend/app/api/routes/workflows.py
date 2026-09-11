from fastapi import APIRouter

router = APIRouter()


@router.get("/workflows")
async def workflows_index():
    return {"status": "ok", "workflows": []}

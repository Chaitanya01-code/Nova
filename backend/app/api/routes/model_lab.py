from fastapi import APIRouter

router = APIRouter()


@router.get("/model-lab")
async def model_lab_index():
    return {"status": "ok", "experiments": []}

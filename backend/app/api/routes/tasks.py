from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def tasks_index():
    return {"status": "ok", "tasks": []}


@router.post("/tasks")
async def tasks_create(payload: dict):
    return {"status": "ok", "payload": payload}

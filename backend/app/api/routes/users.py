from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def users_index():
    return {"status": "ok", "users": []}

from fastapi import APIRouter

test_router = APIRouter()

@test_router.get("/test")
async def testing():

    return {"testing":"testing"}

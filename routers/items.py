from fastapi import APIRouter


router = APIRouter()


@router.get("/items/", tags=["items"])
async def getItems():
    return [{"ProductName": "A"}, {"ProductName": "B"}]

from fastapi import APIRouter

router = APIRouter()

# Placeholder endpoints
@router.get("/")
async def list_forms():
    return {"forms": []}

@router.post("/")
async def create_form():
    return {"message": "form created"}


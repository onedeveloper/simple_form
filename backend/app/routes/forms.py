from fastapi import APIRouter
from app.schemas.form import FormSchema
from app.db.mongo import db

router = APIRouter()

# Placeholder endpoints
@router.get("/")
async def list_forms():
    return {"forms": []}

@router.post("/")
async def create_form(form: FormSchema):
    result = await db.forms.insert_one(form.dict(exclude_none=True))
    return {"id": str(result.inserted_id)}


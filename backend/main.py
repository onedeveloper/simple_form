from fastapi import FastAPI
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.routes import forms

app = FastAPI(title="Simple Form Builder")

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(forms.router, prefix="/forms", tags=["forms"])



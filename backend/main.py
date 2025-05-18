from fastapi import FastAPI
from app.db.mongo import connect, close
from app.routes import forms

app = FastAPI(title="Simple Form Builder")

@app.on_event("startup")
async def startup_db_client():
    await connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close()

app.include_router(forms.router, prefix="/forms", tags=["forms"])



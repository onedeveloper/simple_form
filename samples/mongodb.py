# app/db/mongo.py

from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Optional: if using .env file for local dev

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_APPNAME = os.getenv("MONGO_APPNAME")

MONGO_URI = (
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/"
    f"?retryWrites=true&w=majority&appName={MONGO_APPNAME}"
)

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DBNAME]

# Optional: ping the DB at startup to test connection
async def verify_mongo_connection():
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("MongoDB connection failed:", e)

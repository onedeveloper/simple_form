# app/db/mongo.py

from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Optional: if using .env file for local dev

MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client["your_database_name"]  # replace with your actual DB name

# Optional: ping the DB at startup to test connection
async def verify_mongo_connection():
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("MongoDB connection failed:", e)

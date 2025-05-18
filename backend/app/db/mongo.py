import os
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

MONGO_USER = quote_plus(os.getenv("MONGO_USER"))
MONGO_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_APPNAME = os.getenv("MONGO_APPNAME")

MONGO_URI = (
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/"
    f"?retryWrites=true&w=majority&appName={MONGO_APPNAME}"
)

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DBNAME]

async def verify_mongo_connection():
    try:
        await client.admin.command("ping")
        print("MongoDB connection successful.")
    except Exception as e:
        print("MongoDB connection failed:", e)

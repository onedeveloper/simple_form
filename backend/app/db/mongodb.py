from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("MONGO_DB_NAME", "simple_form")

client: AsyncIOMotorClient | None = None

def get_client() -> AsyncIOMotorClient:
    assert client is not None, "Mongo client is not initialized"
    return client

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(MONGO_URI)

async def close_mongo_connection():
    client.close()

async def get_database():
    return get_client()[DATABASE_NAME]


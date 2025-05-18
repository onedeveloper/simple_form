from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os

MONGO_URI = os.environ.get("MONGO_URI")

client: Optional[AsyncIOMotorClient] = None

async def connect() -> None:
    """Initialize MongoDB connection."""
    global client
    client = AsyncIOMotorClient(MONGO_URI)

async def close() -> None:
    """Close MongoDB connection."""
    if client:
        client.close()

def get_client() -> AsyncIOMotorClient:
    assert client is not None, "Mongo client is not initialized"
    return client

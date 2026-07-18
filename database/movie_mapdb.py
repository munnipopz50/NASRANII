from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]

async def get_movie_map():
    data = await db.movie_map.find_one({"_id": "movie_map"})
    return data.get("data", {}) if data else {}

async def add_movie_map(wrong, correct):
    await db.movie_map.update_one(
        {"_id": "movie_map"},
        {"$set": {f"data.{wrong.lower()}": correct}},
        upsert=True
    )
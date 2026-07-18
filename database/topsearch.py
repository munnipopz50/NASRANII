from pymongo import MongoClient
from info import DATABASE_URI, DATABASE_NAME

client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]

searches = db["top_searches"]


async def save_search(movie):
    if not movie:
        return

    searches.update_one(
        {"movie": movie.lower().strip()},
        {"$inc": {"count": 1}},
        upsert=True
    )


async def get_top_searches(limit=10):
    return list(
        searches.find(
            {},
            {"_id": 0}
        ).sort(
            "count", -1
        ).limit(limit)
    )
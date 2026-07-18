
import logging
from struct import pack
import re
import base64
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER, MAX_B_TN, SECONDDB_URI
from utils import get_settings, save_group_settings
from sample_info import tempDict 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def has_malayalam(text):
    return bool(re.search(r'[\u0D00-\u0D7F]', text))
#some basic variables needed
saveMedia = None

#primary db
client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)
stats_col = db["stats"]

@instance.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)

    class Meta:
        indexes = ('$file_name', )
        collection_name = COLLECTION_NAME

#secondary db
client2 = AsyncIOMotorClient(SECONDDB_URI)
db2 = client2[DATABASE_NAME]
stats_col = db["stats"]
instance2 = Instance.from_db(db2)

@instance2.register
class Media2(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)

    class Meta:
        indexes = ('$file_name', )
        collection_name = COLLECTION_NAME

async def choose_mediaDB():
    """This Function chooses which database to use based on the value of indexDB key in the dict tempDict."""
    global saveMedia
    if tempDict['indexDB'] == DATABASE_URI:
        logger.info("Using first db (Media)")
        saveMedia = Media
    else:
        logger.info("Using second db (Media2)")
        saveMedia = Media2

async def save_file(media):
    """Save file in DB without extra count_documents check."""
    from database.ia_filterdb import choose_mediaDB, saveMedia, stats_col, ValidationError, DuplicateKeyError, unpack_new_file_id
    await choose_mediaDB()

    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))

    try:
        file = saveMedia(
            file_id=file_id,
            file_ref=file_ref,
            file_name=file_name,
            file_size=media.file_size,
            file_type=media.__class__.__name__.lower(),
            mime_type=getattr(media, "mime_type", None),
            caption=None,
        )

        await file.commit()
        return True, 1

    except DuplicateKeyError:
        await stats_col.update_one(
            {"_id": "duplicate_files"},
            {"$inc": {"count": 1}},
            upsert=True
        )
        return False, 0

    except ValidationError:
        return False, 2

    except Exception as e:
        logger.exception(e)
        return False, 2


async def is_file_exist(self, title):
    """ഫയലിന്റെ പേര് Media കളക്ഷനുകളിൽ ഉണ്ടോ എന്ന് നോക്കാനുള്ള ഫങ്ക്ഷൻ"""
    import re
    
    # 🌟 ഫിക്സ്: സിനിമയുടെ പേരിലെ സ്പേസുകൾ മാറ്റി അതിനിടയിൽ .* ഇട്ടു കൊടുക്കുന്നു.
    # കൂടാതെ പേരിന്റെ മുന്നിലും പിന്നിലും .* ഉള്ളതുകൊണ്ട് ഫയലിന്റെ ഏത് ഭാഗത്ത് ഈ പേര് വന്നാലും ബോട്ട് കണ്ടുപിടിക്കും.
    clean_title = title.strip().replace(' ', '.*')
    pattern = f".*{clean_title}.*"
    
    try:
        regex = re.compile(pattern, flags=re.IGNORECASE)
    except Exception:
        return False

    filter_query = {'file_name': regex}
        
    # COLLECTION_NAME ഗ്ലോബൽ ആണെന്ന് ഉറപ്പുവരുത്തുക, അല്ലെങ്കിൽ 'Media' എന്ന് നേരിട്ട് നൽകാം
    try:
        col_name = COLLECTION_NAME
    except NameError:
        col_name = "Media" # നിങ്ങളുടെ ഒറിജിനൽ കളക്ഷൻ പേര് ഇതാണെങ്കിൽ
        
    media_col = self.db[col_name]
    media_col2 = self.db2[col_name]
        
    count1 = await media_col.count_documents(filter_query)
    count2 = await media_col2.count_documents(filter_query)
        
    if (count1 + count2) > 0:
        return True
    return False



async def get_search_result(chat_id, query, file_type=None, max_results=10, offset=0, filter=False):
    """For given query return (results, next_offset)"""
    if chat_id is not None:
        settings = await get_settings(int(chat_id))
        try:
            if settings['max_btn']:
                max_results = 10
            else:
                max_results = int(MAX_B_TN)
        except KeyError:
            await save_group_settings(int(chat_id), 'max_btn', False)
            settings = await get_settings(int(chat_id))
            if settings['max_btn']:
                max_results = 10
            else:
                max_results = int(MAX_B_TN)
    query = query.strip()
    #if filter:
        #better ?
        #query = query.replace(' ', r'(\s|\.|\+|\-|_)')
        #raw_pattern = r'(\s|_|\-|\.|\+)' + query + r'(\s|_|\-|\.|\+)'
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_()]')
    
    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    if USE_CAPTION_FILTER:
        filter = {'$or': [{'file_name': regex}, {'caption': regex}]}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    total_results = ((await Media.count_documents(filter))+(await Media2.count_documents(filter)))

    #verifies max_results is an even number or not
    if max_results%2 != 0: #if max_results is an odd number, add 1 to make it an even number
        logger.info(f"Since max_results is an odd number ({max_results}), bot will use {max_results+1} as max_results to make it even.")
        max_results += 1

    cursor = Media.find(filter)
    cursor2 = Media2.find(filter)
    # Sort by recent
    cursor.sort('$natural', -1)
    cursor2.sort('$natural', -1)
    # Slice files according to offset and max results
    cursor2.skip(offset).limit(max_results)
    # Get list of files
    fileList2 = await cursor2.to_list(length=max_results)
    if len(fileList2)<max_results:
        next_offset = offset+len(fileList2)
        cursorSkipper = (next_offset-(await Media2.count_documents(filter)))
        cursor.skip(cursorSkipper if cursorSkipper>=0 else 0).limit(max_results-len(fileList2))
        fileList1 = await cursor.to_list(length=(max_results-len(fileList2)))
        files = fileList2+fileList1
        next_offset = next_offset + len(fileList1)
    else:
        files = fileList2
        next_offset = offset + max_results
    if next_offset >= total_results:
        next_offset = ''
    return files, next_offset, total_results





async def get_year_wise_count():
    pipeline = [
        {
            "$project": {
                "year": {
                    "$regexFind": {
                        "input": "$file_name",
                        "regex": "20[0-2][0-9]"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$ifNull": ["$year.match", "Others"]
                },
                "count": {
                    "$sum": 1
                }
            }
        }
    ]

    years = {}

    async for doc in Media.collection.aggregate(pipeline):
        years[doc["_id"]] = years.get(doc["_id"], 0) + doc["count"]

    async for doc in Media2.collection.aggregate(pipeline):
        years[doc["_id"]] = years.get(doc["_id"], 0) + doc["count"]

    return years











# --- get_search_results ---
async def get_search_results(chat_id, query, file_type=None, max_results=10, offset=0, filter=False):
    """Fast MongoDB text search with exact phrase matching."""

    query = query.strip()

    if not query:
        return [], '', 0

    await choose_mediaDB()

    # Multi-word query -> exact phrase search
    query_words = query.split()

    if len(query_words) >= 2:
        filter_query = {
            "$text": {
                "$search": f"\"{query}\""
            }
        }
    else:
        filter_query = {
            "$text": {
                "$search": query
            }
        }
#    if file_type:
#        filter_query = {
#            "title": {
#                "$regex": f"{query}.*{file_type}|{file_type}.*{query}|{file_type}",
#                "$options": "i"
#            }
#        }
#    else:
#        filter_query = {
#            "$text": {"$search": query}
#        }
        
        
        
        
    if file_type:
        filter_query["file_type"] = file_type

    total_results = await saveMedia.count_documents(filter_query)

    cursor = (
        saveMedia.find(filter_query)
        .skip(offset)
        .limit(max_results)
    )

    files = await cursor.to_list(length=max_results)

    next_offset = offset + len(files)

    print("OFFSET =", offset)
    print("FILES =", len(files))
    print("NEXT_OFFSET =", next_offset)
    print("TOTAL =", total_results)

    if next_offset >= total_results:
        next_offset = ''

    return files, next_offset, total_results










# --- get_search_results ---
async def get_search_resultss(chat_id, query, file_type=None, max_results=10, offset=0, filter=False):
    """Optimized for fast search using MongoDB Atlas text index with pagination."""
    if max_results % 2 != 0:
        max_results += 1

    query = query.strip()
    if not query:
        return [], '', 0

    if has_malayalam(query):
        regex = re.compile(re.escape(query), re.IGNORECASE)
        filter_query = {"file_name": regex}
    else:
        filter_query = {"$text": {"$search": query}}

    if file_type:
        filter_query['file_type'] = file_type

    await choose_mediaDB()

    total_results = await saveMedia.count_documents(filter_query)

    cursor = saveMedia.find(filter_query).skip(offset).limit(max_results)
    files = await cursor.to_list(length=max_results)

    next_offset = offset + len(files)

    if next_offset >= total_results:
        next_offset = ''

    return files, next_offset, total_results
    
    
    

async def get_file_details(query):
    filter = {'file_id': query}
    cursor = Media.find(filter)
    filedetails = await cursor.to_list(length=1)
    if not filedetails:
        cursor2 = Media2.find(filter)
        filedetails = await cursor2.to_list(length=1)
    return filedetails

def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")


def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")


def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref
    

    
async def get_last_files(limit=10):
    cursor = Media.find({}).sort("$natural", -1).limit(limit)
    files = await cursor.to_list(length=limit)

    if len(files) < limit:
        cursor2 = Media2.find({}).sort("$natural", -1).limit(limit - len(files))
        files.extend(
            await cursor2.to_list(length=limit - len(files))
        )

    return files
    




# =========================
# BATCH COLLECTION SYSTEM
# =========================

batch_col = db["batch_collections"]

async def save_batch_collection(name, creator_id, files):
    await batch_col.insert_one({
        "_id": name.lower(),
        "creator_id": creator_id,
        "files": files
    })

async def get_batch_collection(name):
    return await batch_col.find_one({
        "_id": name.lower()
    })

async def batch_exists(name):
    return await batch_col.find_one({
        "_id": name.lower()
    })  
    
    
    
    
async def get_all_batch_collections():
    cursor = batch_col.find({})
    return await cursor.to_list(length=None)    
    
    
async def get_last_files(limit=10):
    cursor = Media.find({}).sort("$natural", -1).limit(limit)
    files = await cursor.to_list(length=limit)

    if len(files) < limit:
        cursor2 = Media2.find({}).sort("$natural", -1).limit(limit - len(files))
        files.extend(
            await cursor2.to_list(length=limit - len(files))
        )

    return files
# https://github.com/odysseusmax/animated-lamp/blob/master/bot/database/database.py
import motor.motor_asyncio
from sample_info import tempDict
from info import DATABASE_NAME, DATABASE_URI, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF, SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT, AUTO_DELETE, MAX_BTN, AUTO_FFILTER, SHORTLINK_API, SHORTLINK_URL, MY_BUTTON, IS_SHORTLINK, SECONDDB_URI

from pymongo import MongoClient
from datetime import datetime, timedelta


class Database:
    
    
    def __init__(self, database_name):
    # primary db 
        self._client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
        self.db = self._client[database_name]

        self.col = self.db.users
        self.grp = self.db.groups
        self.stats = self.db.stats
        self.group_stats = self.db.group_stats

        self.requests = self.db.requests   # ✅ ADD HERE
        self.xp = self.db.xp # ✅ ADD HERE
        self.imdb_cache = self.db.imdb_cache
        # primary db
        self.channels = self.db.channels
    # secondary db
        self._client2 = motor.motor_asyncio.AsyncIOMotorClient(SECONDDB_URI)
        self.db2 = self._client2[database_name]

        self.col2 = self.db2.users
        self.grp2 = self.db2.groups

        self.requests2 = self.db2.requests  # (optional but good)
        self.xp2 = self.db2.xp         # (optional but good)
        self.channels2 = self.db2.channels

 
        
    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
        )

    def new_group(self, id, title):
        return dict(
            id = id,
            title = title,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ),
        )
        
        
    def new_channel(self, id, title, username=None):
        return dict(
            id=id,
            title=title,
            username=username,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ), 
        )
        
        
    def new_channel(self, id, title, username=None):
        return dict(
            id=id,
            title=title,
            username=username,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ),
        )    
        

    async def update_verification(self, id, date, time):
        status = {
            'date': str(date),
            'time': str(time)
        }
        user = await self.col.find_one({'id':int(id)})
        if not user:
            await self.col2.update_one({'id': int(id)}, {'$set': {'verification_status': status}})
        else:
            await self.col.update_one({'id': int(id)}, {'$set': {'verification_status': status}})

    async def get_verified(self, id):
        default = {
            'date': "1999-12-31",
            'time': "23:59:59"
        }
        user = await self.col.find_one({'id': int(id)})
        if user:
            return user.get("verification_status", default)
        else:
            user = await self.col2.find_one({'id': int(id)})
            if user:
                return user.get("verification_status", default)
        return default
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        if tempDict['indexDB'] == DATABASE_URI:
            await self.col.insert_one(user)
        else:
            await self.col2.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        if not user:
            user = await self.col2.find_one({'id':int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = ((await self.col.count_documents({}))+(await self.col2.count_documents({})))
        return count
    
    async def remove_ban(self, id):
        ban_status = dict(
            is_banned=False,
            ban_reason=''
        )
        user = await self.col.find_one({'id': int(id)})
        if not user:
            await self.col2.update_one({'id': id}, {'$set': {'ban_status': ban_status}})
        else:
            await self.col.update_one({'id': id}, {'$set': {'ban_status': ban_status}})
    
    async def ban_user(self, user_id, ban_reason="No Reason"):
        ban_status = dict(
            is_banned=True,
            ban_reason=ban_reason
        )
        user = await self.col.find_one({'id': int(user_id)})
        if not user:
            await self.col2.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}})
        else:
            await self.col.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}})

    async def get_ban_status(self, id):
        default = dict(
            is_banned=False,
            ban_reason=''
        )
        user = await self.col.find_one({'id':int(id)})
        if not user:
            user = await self.col2.find_one({'id':int(id)})
            if not user:
                return default
        return user.get('ban_status', default)

    async def get_all_users(self):
        users_list = (await (self.col.find({})).to_list(length=None))+(await (self.col2.find({})).to_list(length=None))
        return users_list
    

    async def delete_user(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        if user:
            await self.col.delete_many({'id': int(user_id)})
        else:
            await self.col2.delete_many({'id': int(user_id)})


    async def get_banned(self):
        users = self.col.find({'ban_status.is_banned': True})
        chats = self.grp.find({'chat_status.is_disabled': True})
        b_chats = [chat['id'] async for chat in chats]
        b_users = [user['id'] async for user in users]
        users = self.col2.find({'ban_status.is_banned': True})
        chats = self.grp2.find({'chat_status.is_disabled': True})
        b_chats += [chat['id'] async for chat in chats]
        b_users += [user['id'] async for user in users]
        return b_users, b_chats
    
### ❌❌❌




    async def increase_group_activity(self, chat_id, title):
        await self.group_stats.update_one(
            {"_id": chat_id},
            {
                "$inc": {"count": 1},
                "$set": {"title": title}
            },
            upsert=True
        )

    async def get_top_groups(self, limit=3):
        groups = await self.group_stats.find().sort("count", -1).limit(limit).to_list(length=limit)
        return groups


    async def increase_movie_request(self):
        await self.stats.update_one(
            {"_id": "movie_requests"},
            {"$inc": {"count": 1}},
            upsert=True
        )

    async def increase_noresult_request(self):
        await self.stats.update_one(
            {"_id": "noresult_requests"},
            {"$inc": {"count": 1}},
            upsert=True
        )

    async def increase_group_activity(self, chat_id, title):
        await self.group_stats.update_one(
            {"_id": chat_id},
            {
                "$inc": {"count": 1},
                "$set": {"title": title}
            },
            upsert=True
        )

    async def get_top_groups(self, limit=3):
        groups = await self.group_stats.find().sort("count", -1).limit(limit).to_list(length=limit)
        return groups


    async def get_movie_request_count(self):
        data = await self.stats.find_one({"_id": "movie_requests"})
        return data.get("count", 0) if data else 0

    async def get_noresult_request_count(self):
        data = await self.stats.find_one({"_id": "noresult_requests"})
        return data.get("count", 0) if data else 0


    async def add_chat(self, chat, title):
        chat = self.new_group(chat, title)
        print(f"tempDict: {tempDict['indexDB']}\n\nDATABASE_URI: {DATABASE_URI}")
        if tempDict['indexDB'] == DATABASE_URI:
            await self.grp.insert_one(chat)
        else:
            await self.grp2.insert_one(chat)
            
            
    async def add_channel(self, channel_id, title, username=None):
        channel = self.new_channel(
            channel_id,
            title,
            username
        )
 
        if tempDict['indexDB'] == DATABASE_URI:
            await self.channels.insert_one(channel)
        else:
            await self.channels2.insert_one(channel)       
            
    

    async def get_chat(self, id):
        chat = await self.grp.find_one({'id':int(id)})
        if not chat:
            chat = await self.grp2.find_one({'id':int(id)})
        return False if not chat else chat.get('chat_status')
    

    async def re_enable_chat(self, id):
        chat_status=dict(
            is_disabled=False,
            reason="",
            )
        chat = await self.grp.find_one({'id':int(id)})
        if chat:
            await self.grp.update_one({'id': int(id)}, {'$set': {'chat_status': chat_status}})
        else:
            await self.grp2.update_one({'id': int(id)}, {'$set': {'chat_status': chat_status}})
        
    async def update_settings(self, id, settings):
        chat = await self.grp.find_one({'id':int(id)})
        if chat:
            await self.grp.update_one({'id': int(id)}, {'$set': {'settings': settings}})
        else:
            await self.grp2.update_one({'id': int(id)}, {'$set': {'settings': settings}})
        
    
    async def get_settings(self, id):
        default = {            
            'button': SINGLE_BUTTON,
            'mybutton': MY_BUTTON,
            'botpm': P_TTI_SHOW_OFF,
            'file_secure': PROTECT_CONTENT,
            'imdb': IMDB,
            'spell_check': SPELL_CHECK_REPLY,
            'welcome': MELCOW_NEW_USERS,
            'auto_delete': AUTO_DELETE,
            'auto_ffilter': AUTO_FFILTER,
            'max_btn': MAX_BTN,
            'template': IMDB_TEMPLATE,
            'shortlink': SHORTLINK_URL,
            'shortlink_api': SHORTLINK_API,
            'is_shortlink': IS_SHORTLINK
        }
        chat = await self.grp.find_one({'id':int(id)})
        if chat:
            return chat.get('settings', default)
        else:
            chat = await self.grp2.find_one({'id':int(id)})
            if chat:
                return chat.get('settings', default)
        return default
    

    async def disable_chat(self, chat, reason="No Reason"):
        chat_status=dict(
            is_disabled=True,
            reason=reason,
            )
        chat = await self.grp.find_one({'id':int(chat)})
        if chat:
            await self.grp.update_one({'id': int(chat)}, {'$set': {'chat_status': chat_status}})
        else:
            await self.grp2.update_one({'id': int(chat)}, {'$set': {'chat_status': chat_status}})
    

    async def total_chat_count(self):
        count = (await self.grp.count_documents({}))+(await self.grp2.count_documents({}))
        return count
    

    async def get_all_chats(self):
        return ((await (self.grp.find({})).to_list(length=None))+(await (self.grp2.find({})).to_list(length=None)))

# imdb cache 



    async def save_cached_imdb(self, key, data):
        await self.imdb_cache.update_one(
            {"_id": key},
            {
                "$set": {
                    "data": data,
                    "updated_at": datetime.utcnow()
                }
            },
            upsert=True
        )
    
    async def get_cached_imdb(self, key):
        data = await self.imdb_cache.find_one({"_id": key})

        if not data:
            return None

        updated = data.get("updated_at")

        if not updated:
            return None

        if datetime.utcnow() - updated > timedelta(days=30):
            return None

        return data
# imdb cache

    async def get_channel(self, id):
        channel = await self.channels.find_one(
            {'id': int(id)}
        )

        if not channel:
            channel = await self.channels2.find_one(
                {'id': int(id)}
            )

        return channel
        
    async def total_channel_count(self):
        count = (
            (await self.channels.count_documents({}))
            +
            (await self.channels2.count_documents({}))
        )
        return count   
        
    async def get_all_channels(self):
        return (
            (await self.channels.find({}).to_list(length=None))
            +
            (await self.channels2.find({}).to_list(length=None))
        )
        
    async def delete_channel(self, channel_id):
        channel = await self.channels.find_one(
            {'id': int(channel_id)}
        )

        if channel:
            await self.channels.delete_many(
                {'id': int(channel_id)}
            )
        else:
            await self.channels2.delete_many(
                {'id': int(channel_id)}
            ) 
            
            
    async def delete_chat(self, chat_id):
        chat = await self.grp.find_one({'id': int(chat_id)})

        if chat:
            await self.grp.delete_many({'id': int(chat_id)})
        else:
            await self.grp2.delete_many({'id': int(chat_id)})


db = Database(DATABASE_NAME)




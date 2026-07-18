# TELEGRAPH FILTER
from html_telegraph_poster import TelegraphPoster
from database.users_chats_db import db
requestdb = db.xp

from plugins.rules import MALAYALAM_RULES # നിങ്ങളുടെ ഫയലിന്റെ പേര്
import aiohttp
# എന്നിട്ട് ഫങ്ക്ഷനിൽ rules = MALAYALAM_RULES എന്ന് കൊടുത്താൽ മതി.

# LAST_FILES
from database.ia_filterdb import get_year_wise_count
from database.topsearch import save_search
from io import BytesIO

# MALAYALAM SPELLCHECK
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from difflib import get_close_matches
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from difflib import SequenceMatcher


from urllib.parse import quote
from info import *
from difflib import SequenceMatcher
import requests
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatPermissions

#spellcheck 
from PIL import ImageDraw, Image, ImageFont, ImageChops
from logging import getLogger
LOGGER = getLogger(__name__)
from plugins.p_ttishow import spellcheck, WelDatabase, circle
wlcm = WelDatabase()
# Google spellcheck
from traceback import format_exc
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackSearch
from search_engine_parser.core.exceptions import NoResultsFound, NoResultsOrTrafficError
# from plugins.modules.SearchGoogle import ikb
# gsearch = GoogleSearch()
# stsearch = StackSearch()

# sticker
import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters, enums



# Kanged From @TroJanZheX
import asyncio
import re
import ast
import math
import random
import pyrogram
lock = asyncio.Lock()

import pytz
from datetime import datetime, timedelta, date, time
lock = asyncio.Lock()


from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, SUPPORT_CHAT_ID, CUSTOM_FILE_CAPTION, MSG_ALRT, PICS, GRP_LNK, CHNL_LNK, NOR_IMG, LOG_CHANNEL, SPELL_IMG, MAX_B_TN, \
    NO_RESULTS_MSG, IS_VERIFY, HOW_TO_VERIFY, IMDB, SEASONS, GRP_LNK, CHNL_LNK, FILE_CHANNEL, FILE_FORWARD, ADMIN, SP
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from pyrogram import Client, filters, enums
from pyrogram.errors import UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, is_subscribe, get_poster, temp, get_settings, save_group_settings, get_shortlink, send_all, check_verification, get_token, get_cap, send_all_files, search_gagala
from database.users_chats_db import db as userdb
from database.connections_mdb import mycol, mycol2
from database.ia_filterdb import stats_col, get_last_files
from database.movie_mapdb import get_movie_map, add_movie_map

# from database.ia_filterdb import Media, Media2, get_file_details, get_search_results, get_bad_files, db as clientDB, db2 as clientDB2 
from database.ia_filterdb import Media, Media2, get_file_details, get_search_results, db as clientDB, db2 as clientDB2
# from database.ia_filterdb import *
from database.ia_filterdb import Media, Media2, db as filterdb, db2 as filterdb2
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
from database.gfilters_mdb import (
    find_gfilter,
    get_gfilters,
    del_allg
)
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

from urllib.parse import quote_plus

AUTH_CHANNELS = [-1001335744963, -1001203428484, -1001371670080] 
BUTTONS = {}
SPELL_CHECK = {}

BUTTON = {}
FRESH = {}
BUTTONS0 = {}
BUTTONS1 = {}
BUTTONS2 = {}
SPELL_CHECK = {}
REQUEST_USERS = {}

RUN_STRINGS = (
    "🍬",
    "🎨",
    "🍿",
    "☘",
    "🍭",
    "🍁",
    "📀",
    "🍃",
    "🎭",    
)



MOVIE_MAP = {

    # Aparichithan
    "aparijithan": "aparichithan",
    "aparichitan": "aparichithan",
    "aparichitan": "aparichithan",

    # Minnal Murali
    "minnalmurali": "minnal murali",
    "minnalmurali": "minnal murali",
    "minnal murali": "minnal murali",

    # Drishyam
    "drshyam": "drishyam",
    "drisyam": "drishyam",
    "drishyam2": "drishyam 2",

    # Premalu
    "premaloo": "premalu",
    "premallu": "premalu",
    "premaluu": "premalu",

    # Hridayam
    "hridaym": "hridayam",
    "hrudayam": "hridayam",

    # Romancham
    "romanjam": "romancham",
    "romanjam": "romancham",

    # Aavesham
    "avesham": "aavesham",
    "aveshamm": "aavesham",

    # Manjummel Boys
    "manjummal boys": "manjummel boys",
    "manjumel boys": "manjummel boys",
    "manjummelboys": "manjummel boys",

    # Lucifer
    "lucifer movie": "lucifer",
    "lusifer": "lucifer",

    # Empuraan
    "empuran": "empuraan",
    "l2 empuran": "empuraan",

    # Kishkindha Kaandam
    "kishkinda kandam": "kishkindha kaandam",
    "kishkindakandam": "kishkindha kaandam",

    # ARM
    "ajayante randam moshanam": "arm",
    "a r m": "arm",

    # Thudarum
    "thudaram": "thudarum",

    # Marco
    "marko": "marco",

    # Officer on Duty
    "officer duty": "officer on duty",

    # Sookshmadarshini
    "sookshma darshini": "sookshmadarshini",
    "sukshmadarshini": "sookshmadarshini",

    # Guruvayoor Ambalanadayil
    "guruvayoor ambalanadayil": "guruvayoorambalanadayil",
    "guruvayur ambalanadayil": "guruvayoorambalanadayil",
}

# ENABLE_SHORTLINK = ""

telegraph = TelegraphPoster(use_api=True)
telegraph.create_api_token("AutoFilter Bot")

GENERAT = "-1001203428484"
UPLOAD_CHANNEL = "batchfiles_store"
BATCH_LINK = "-1001203428484"

REACTIONS = ["🔥", "❤️", "😍", "⚡"]

RUN_STRINGS = (
    "🍬",
    "🎨",
    "🍿",
    "☘",
    "🍭",
    "🍁",
    "📀",
    "🍃",
    "🎭",    
)

MARKED_FILES = {}

MARK_MODE_USERS = []
#1
#2
MARK_MODE = {}
MARKED_FILES = {}




from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from plugins.helpers.config import Telegram
from info import *



# മെയിൻ ഫയലിന്റെ ഏറ്റവും മുകളിൽ ചേർക്കേണ്ടത്:
from database.connections_mdb import vote_db


import asyncio

async def choose_mediaDB():
    global saveMedia
    if tempDict['indexDB'] == DATABASE_URI:
        saveMedia = Media
    else:
        saveMedia = Media2



# Progress simulation function
async def show_progress(message, search, steps=5, delay=0.5):
    progress_symbols = ['▏','▎','▍','▌','▋','▊','▉','█']
    for i in range(steps):
        bar = ''.join(progress_symbols[:i+1]).ljust(8, ' ')
        await message.edit_text(f"🔎 Searching for '{search}'\n[{bar}]")
        await asyncio.sleep(delay)


async def get_file_votes(file_id):
    """ഫയലിന്റെ നിലവിലുള്ള വോട്ട് വിവരങ്ങൾ ഡാറ്റാബേസിൽ നിന്ന് എടുക്കുന്നു"""
    # ഇവിടെ നമ്മൾ 'global vote_db' എന്നത് പൂർണ്ണമായും ഒഴിവാക്കി.
    # പകരം നേരിട്ട് തന്നെ vote_db ഉപയോഗിക്കാം.
    vote_data = vote_db.find_one({"file_id": file_id})

    if not vote_data:
        vote_data = {
            "file_id": file_id,
            "like": 0,
            "dislike": 0,
            "smile": 0,
            "users": []
        }
        vote_db.insert_one(vote_data)
    return vote_data

async def update_file_vote(file_id, user_id, action):

    vote_data = await get_file_votes(file_id)

    if vote_data and str(user_id) in vote_data.get("users", []):
        return False, "നിങ്ങൾ ഇതിനകം വോട്ട് ചെയ്തതാണ്!"

    vote_db.update_one(
        {"file_id": file_id},
        {
            "$inc": {action: 1},
            "$push": {"users": str(user_id)}
        },
        upsert=True
    )

    return True, "വോട്ട് രേഖപ്പെടുത്തി!"

async def reaction(sp):
    try:
       await sp.react(choice(Telegram.EMOJIS))
    except (
        MessageIdInvalid,
        EmoticonInvalid,
        ChatAdminRequired,
        ReactionInvalid
    ):
        pass
    return True, "Success"
# unwanted_words = ['pm', 'dm', 'pm me', 'hi', 'hlo', 'message', 'Me', 'Link', 'Message', 'Hii', 'Helo', 'Pm', 'Dm', 'ayyk', 'Ayyk', 'nook', 'Nook', 'bro', 'Bro', 'file', 'File', 'illa', 'ille', 'veno', 'Veno', 'Vend', 'vend', 'venm', 'Venm', 'Myre', 'Myre', 'link', 'msg', 'Msg', 'Mssge mee', 'kityo', 'kittyo', '🔞']

# @Client.on_message(filters.group)
# async def delete_message(client, message):
#     for word in unwanted_words:
#         if word in message.text.lower():
#             await message.delete()
#
CUSTOM_THUMB = {}

async def get_top_requesterss():
    users = await requestdb.find().sort("requests", -1).to_list(length=3)

    top = []

    for user in users:
        if user.get("username"):
            top.append(f"@{user['username']}")
        else:
            top.append(user.get("name", "Unknown"))

    while len(top) < 3:
        top.append("No User")

    return top

async def get_top_requesters():
    users = await requestdb.find().sort("requests", -1).to_list(length=3)

    top = []

    for user in users:
        # 🟢 യൂസറുടെ ടോട്ടൽ റിക്വസ്റ്റ് കൗണ്ട് എടുക്കുന്നു (ഇല്ലെങ്കിൽ 0)
        count = user.get("requests", 0) 
        
        if user.get("username"):
            top.append(f"@{user['username']} - {count}")
        else:
            top.append(f"{user.get('name', 'Unknown')} - {count}")

    while len(top) < 3:
        top.append("No User")

    return top


@Client.on_message(filters.command("addmap"))
async def adddname_cmd(client, message):
    print("ADDMAP COMMAND HIT")
    await message.reply_text("Command received")

@Client.on_message(filters.command("addname") & filters.user(ADMINS))
async def addname_ccmd(client, message):
    try:
        _, wrong, correct = message.text.split(" ", 2)
    except:
        return await message.reply_text(
            "Usage:\n/addname aparijithan aparichithan"
        )

    await add_movie_map(wrong, correct)
    print("ADDMAP COMMAND HIT")
    await message.reply_text(
        f"✅ Saved\n{wrong} ➜ {correct}"
    )

from database.movie_mapdb import get_movie_map, add_movie_map, db


@Client.on_message(filters.command("delmap") & filters.user(ADMINS))
async def delmap_cmd(client, message):

    try:
        _, wrong = message.text.split(maxsplit=1)
    except:
        return await message.reply_text(
            "Usage:\n/delmap aparijithan"
        )

    await db.movie_map.update_one(
        {"_id": "movie_map"},
        {"$unset": {f"data.{wrong.lower()}": ""}}
    )

    await message.reply_text("✅ Deleted")



@Client.on_message(filters.command("totaldelete_map") & filters.user(ADMINS))
async def totaldelete_map_cmd(client, message):

    data = await get_movie_map()
    total = len(data)

    await db.movie_map.update_one(
        {"_id": "movie_map"},
        {"$set": {"data": {}}},
        upsert=True
    )

    await message.reply_text(
        f"✅ Deleted {total} movie mappings."
    )


@Client.on_message(filters.command("searchmap") & filters.user(ADMINS))
async def searchmap_cmd(client, message):

    try:
        _, keyword = message.text.split(maxsplit=1)
    except:
        return await message.reply_text(
            "Usage:\n/searchmap keyword"
        )

    mappings = await get_movie_map()

    if not mappings:
        return await message.reply_text("❌ No mappings found")

    keyword = keyword.lower()

    results = []

    for wrong, correct in mappings.items():
        if keyword in wrong.lower() or keyword in correct.lower():
            results.append(f"{wrong} ➜ {correct}")

    if not results:
        return await message.reply_text(
            f"❌ No mapping found for: {keyword}"
        )

    await message.reply_text(
        "🔍 Results:\n\n" + "\n".join(results[:100])
    )



@Client.on_message(filters.command("listmap") & filters.user(ADMINS))
async def listmap_cmd(client, message):

    mappings = await get_movie_map()

    if not mappings:
        return await message.reply_text("❌ No mappings found")

    content = "📋 Saved Movie Mappings\n"
    content += "="*40 + "\n"
    content += f"📊 Total: {len(mappings)}\n\n"

    for wrong, correct in sorted(
        mappings.items(),
        key=lambda x: x[0].lower()
    ):
        content += f"{wrong} -> {correct}\n"

    file = BytesIO(content.encode("utf-8"))
    file.name = "movie_mappings.txt"

    await message.reply_document(
        file,
        caption=f"📋 Total Mappings: {len(mappings)}"
    )





from database.ia_filterdb import get_batch_collection

async def batch_filter(client, message):

    search = message.text.lower().strip()

    data = await get_batch_collection(search)

    if not data:
        return False

    btn = []

    for i, file in enumerate(data["files"]):

        btn.append([
            InlineKeyboardButton(
                text=file["file_name"][:60],
                callback_data=f"packfile#{search}#{i}"
            )
        ])

    await message.reply_text(
        f"📦 {len(data['files'])} Files Found",
        reply_markup=InlineKeyboardMarkup(btn)
    )

    return True



@Client.on_message(
    (filters.group | filters.private) &
    (filters.text | filters.photo | filters.video | filters.document)
)
async def give_filter(client, message):

    # 🚫 Delete forwarded messages
    if (
        message.forward_date
        or message.forward_from
        or message.forward_from_chat
        or message.forward_sender_name
    ):
        try:
            await message.delete()
        except:
            pass
        return

    # 🚫 Delete links / usernames
    if message.text:
        if re.search(
            r"(https?://|t\.me/|telegram\.me/|telegram\.dog/|www\.|@\w+)",
            message.text,
            re.IGNORECASE
        ):
            try:
                await message.delete()
            except:
                pass
            return

    # 👉 PRIVATE CHAT
    if message.chat.type == enums.ChatType.PRIVATE:
        settings = await get_settings(message.from_user.id)

        # ⚙️ PRIVATE CHAT-ലും SPELL CHECK ഓൺ ആണെങ്കിൽ ആദ്യം ബട്ടൺ കാണിക്കാൻ
        if settings.get("botpm", False):
            # ✅ spell_check മാറ്റി spellcheck ആക്കി, ഫംഗ്ഷൻ പേരും മാറ്റി
            if settings.get("spellcheck", False) and message.text and not message.text.startswith("/"):
                return await advantage_spellcheck(client, message)
            else:
                await auto_filter(client, message)
        return

    # 👉 GROUP CHAT
    if message.chat.id != SUPPORT_CHAT_ID:

        if not await userdb.get_chat(message.chat.id):
            if message.text != "/start":
                return await message.reply_text(
                    "⚠️ 𝐓𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐢𝐬 𝐧𝐨𝐭 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝.\n\n"
                    "𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 /𝐬𝐭𝐚𝐫𝐭 𝐨𝐧𝐜𝐞 𝐢ൻ 𝐭𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐭𝐨 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭.\n\n\n"
                    "നിങ്ങൾക്ക് മൂവീസ് വേണമെങ്കിൽ ആദ്യം /𝘴𝘵𝘢𝘳𝘵 എന്ന് അയച്ചതിനു ശേഷം ഗ്രൂപ്പിൽ മൂവിയുടെ പേര് അയക്കുക."
                )

        content = message.text

        # 🔒 Force Subscribe
        if AUTH_CHANNEL and not await is_subscribed(client, message):
            try:
                invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
            except ChatAdminRequired:
                logger.error("Make sure Bot is admin in Forcesub channel")
                return

            buttons = [
                [InlineKeyboardButton("📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📢", url=invite_link.invite_link)],
                [InlineKeyboardButton("🔁 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐀𝐠𝐚и 🔁", callback_data="grp_checksub")]
            ]

            reply_markup = InlineKeyboardMarkup(buttons)

            try:
                await client.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    ChatPermissions(),
                    datetime.now() + timedelta(minutes=1)
                )
            except:
                pass

            k = await message.reply_photo(
                photo=random.choice(SP),
                caption=f"👋 𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention},\n\n{content} 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞..!!\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢н 𝐌𝐲 '𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥' 𝐀𝐧𝐝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐀𝐠𝐚𝐢𝐧. 😇",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )

            await asyncio.sleep(300)
            await k.delete()
            return
            
        settings = await get_settings(message.chat.id)

        if settings.get("gfilter", True):
#            batch = await batch_filter(client, message)
#            if batch:
#                return
            await batch_filter(client, message) # ഇവിടെ return നീക്കം ചെയ്തു                
        # 🌐 Filters
        glob = await global_filters(client, message)

        if glob is False:
            manual = await manual_filters(client, message)

            if manual is False:
                try:
                    # ✅ ഇവിടെ spellcheck ലോജിക്കും ഫംഗ്ഷൻ പേരും അപ്ഡേറ്റ് ചെയ്തു
                    if settings.get('spellcheck', False) and message.text and not message.text.startswith("/"):
                        return await advantage_spellcheck(client, message)
                        
                    elif settings['auto_ffilter']:
                        await auto_filter(client, message)

                except KeyError:
                    grpid = await active_connection(str(message.from_user.id))
                    await save_group_settings(grpid, 'auto_ffilter', True)

                    settings = await get_settings(message.chat.id)
                    
                    # ✅ ഇവിടെയും അപ്ഡേറ്റ് ചെയ്തു
                    if settings.get('spellcheck', False) and message.text and not message.text.startswith("/"):
                        return await advantage_spellcheck(client, message)
                    elif settings['auto_ffilter']:
                        await auto_filter(client, message)

    # 👉 SUPPORT GROUP
    else:
        search = message.text
        temp_files, temp_offset, total_results = await get_search_results(
            chat_id=message.chat.id,
            query=search.lower(),
            offset=0,
            filter=True
        )

        if total_results == 0:
            return
        else:
            return await message.reply_text(
                text=f"<b>Hᴇʏ {message.from_user.mention}, {str(total_results)} ʀᴇsᴜʟᴛs ᴀʀᴇ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {search}. Kɪɴᴅʟʏ ᴜsᴇ ɪɴʟɪɴᴇ sᴇᴀʀᴄʜ ᴏʀ ᴍᴀᴋᴇ ᴀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ᴍᴏᴠɪᴇ ғɪʟᴇs. Tʜɪs ɪs ᴀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ sᴏ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ғɪʟᴇs ғʀᴏᴍ ʜᴇʀᴇ...\n\nFᴏʀ Mᴏᴠɪᴇs, Jᴏɪɴ @free_movies_all_languages</b>",
                parse_mode=enums.ParseMode.HTML
            )
            
            
            
            
            
#######  
@Client.on_callback_query(filters.regex("^packfile#"))
async def send_pack_file(client, query):

    _, pack_name, index = query.data.split("#")

    data = await get_batch_collection(pack_name)

    if not data:
        return await query.answer(
            "Pack deleted",
            show_alert=True
        )

    file_data = data["files"][int(index)]

    try:

        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_data["file_id"],
            caption=file_data["file_name"]
        )

        await query.answer(
            "File sent to PM",
            show_alert=True
        )

    except Exception:

        await query.answer(
            "Start bot in PM first",
            show_alert=True
        )




#    ident, req, key, offset = query.data.rsplit("_", 3)


@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    print("CALLBACK DATA =", query.data)	
    ident, req, key, offset = query.data.split("_")
    curr_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()

    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(
            script.ALRT_TXT.format(query.from_user.first_name),
            show_alert=True
        )

    try:
        offset = int(offset)
    except:
        offset = 0
    if offset < 0:
        offset = 0

    search = BUTTONS.get(key) or FRESH.get(key)

    if not search:
        await query.answer(
            script.OLD_ALRT_TXT.format(query.from_user.first_name),
            show_alert=True
        )
        return

    settings = await get_settings(query.message.chat.id)

    # --- Newmod അനുസരിച്ച് ഇവിടെ PAGE_SIZE സെറ്റ് ചെയ്യുന്നു ---
    if settings.get("newmod", False):
        PAGE_SIZE = 40 if settings.get("max_btn") else 20
    else:
        PAGE_SIZE = 10 if settings.get("max_btn", True) else int(MAX_B_TN)

    # ⚡ ⚡ ⚡ [PAGINATION & LOCKING FIX] ⚡ ⚡ ⚡
    # സെർച്ച് ക്വറിയിൽ ക്വാളിറ്റിയോ ഭാഷയോ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു
    filter_keywords = ["720p", "1080p", "480p", "hevc", "bluray", "malayalam", "tamil", "hindi", "telugu", "english", "kannada"]
    has_filter = any(x in search.lower() for x in filter_keywords)

    if has_filter:
        # സ്പെൽചെക്ക് ഫിൽട്ടർ ഉള്ളതാണെങ്കിൽ മൂവി നെയിം മാത്രം വേർതിരിക്കുന്നു
        clean_movie = search
        detected_tag = ""
        for word in filter_keywords:
            if word in search.lower():
                detected_tag = word
                clean_movie = re.sub(r"\b" + re.escape(word) + r"\b", "", clean_movie, flags=re.IGNORECASE).strip()
        
        clean_movie = re.sub(r"[:\-\.\(\)]", " ", clean_movie)
        clean_movie = re.sub(r"\s+", " ", clean_movie).strip()

        # വലിയ ലിമിറ്റിൽ (100) ഡാറ്റാബേസിൽ നിന്ന് എടുത്ത് ഇൻ-മെമ്മറി ആയി ഫിൽട്ടർ ചെയ്യുന്നു (6 ഫയൽ ലിമിറ്റ് ബൈപാസ്സ് ചെയ്യാൻ)
        all_files, _, _ = await get_search_results(
            query.message.chat.id,
            clean_movie,
            offset=0,
            max_results=100,
            filter=False
        )
        
        filtered_files = []
        if all_files:
            for file in all_files:
                f_name = file.file_name if hasattr(file, 'file_name') else getattr(file, 'name', str(file))
                if detected_tag.lower() in f_name.lower():
                    filtered_files.append(file)
        
        total = len(filtered_files)
        files = filtered_files[offset:offset + PAGE_SIZE]
        n_offset = offset + len(files)
        if n_offset >= total:
            n_offset = ""
    else:
        # സാധാരണ മൂവി സെർച്ചുകൾക്ക് നിങ്ങളുടെ പഴയ ഒറിജിനൽ സിസ്റ്റം തന്നെ പ്രവർത്തിക്കും
        files, n_offset, total = await get_search_results(
            query.message.chat.id,
            search,
            offset=offset,
            max_results=PAGE_SIZE,
            filter=True
        )
    
    total_results = total

    print("OFFSET =", offset)
    print("FILES =", len(files))
    print("NEXT_OFFSET =", n_offset)
    print("TOTAL =", total_results)

    if not files:
        await query.answer("No more files found!", show_alert=True)
        return

    temp.GETALL[key] = files
    temp.SHORT[query.from_user.id] = query.message.chat.id
    pre = 'filep' if settings.get('file_secure') else 'file'

    btn = []
    mark_enabled = query.from_user.id in MARK_MODE_USERS

    if settings.get("button", True):

        if settings.get("telegraph", False):

            btn.append([
                InlineKeyboardButton(
                    "📄𝐓e𝐥e𝐠𝐫𝐚𝐩𝐡📄",
                    callback_data=f"telegraph#{key}"
                )
            ])

            if mark_enabled:
                btn.append([
                    InlineKeyboardButton(
                        "❌ 𝐔𝐧𝐦𝐚𝐫𝐤 ❌",
                        callback_data="markmode"
                    ),
                    InlineKeyboardButton(
                        "📦𝐒𝐞𝐧𝐝 𝐌𝐚𝐫𝐤📦",
                        callback_data="sendmarked"
                    )
                ])
            else:
                btn.append([
                    InlineKeyboardButton(
                        "⭐𝐌𝐚𝐫𝐤𝐦𝐨𝐝⭐",
                        callback_data="markmode"
                    ),
                    InlineKeyboardButton(
                        "📂𝐋𝐞𝐭𝐞𝐬𝐭 𝐅𝐢𝐥𝐞𝐬📂",
                        callback_data=f"topsearch#{key}"
                    )
                ])

        else:

            if mark_enabled:
                btn.append([
                    InlineKeyboardButton(
                        "❌ 𝐔𝐧𝐦𝐚𝐫𝐤 ❌",
                        callback_data="markmode"
                    ),
                    InlineKeyboardButton(
                        "📦𝐒𝐞𝐧𝐝 𝐌𝐚𝐫𝐤📦",
                        callback_data="sendmarked"
                    )
                ])
            else:
                btn.append([
                    InlineKeyboardButton(
                        "⭐𝐌𝐚𝐫𝐤𝐦𝐨𝐝⭐",
                        callback_data="markmode"
                    ),
                    InlineKeyboardButton(
                        "📂𝐋𝐞𝐭𝐞𝐬𝐭 𝐅𝐢𝐥𝐞𝐬📂",
                        callback_data=f"topsearch#{key}"
                    )
                ])

    else:

        if settings.get("telegraph", False):
            btn.append([
                InlineKeyboardButton(
                    "📄𝐓e𝐥e𝐠𝐫𝐚𝐩𝐡📄",
                    callback_data=f"telegraph#{key}"
                )
            ])

    # ✅ FILE BUTTONS GENERATION
    if settings.get('button', True):
        processed_file_buttons = []

        for file in files:
            file_name = ' '.join(
                filter(lambda x: not x.startswith('[')
                       and not x.startswith('@')
                       and not x.startswith('www.'),
                       file.file_name.split())
            )
            file_size = get_size(file.file_size)

            if mark_enabled:
                marked = (query.from_user.id in MARKED_FILES and file.file_id in MARKED_FILES[query.from_user.id])
                icon = "✅" if marked else "❌"
                
                button_text = f"{icon} {file_size}" if settings.get("newmod", False) else f"{icon} [{file_size}] {file_name}"
                callback_data_value = f"mark#{file.file_id}"
            else:
                EMOJI = random.choice(RUN_STRINGS)
                button_text = f"📂 {file_size}" if settings.get("newmod", False) else f"{EMOJI}[{file_size}] {file_name}"
                callback_data_value = f"{pre}#{file.file_id}"

            processed_file_buttons.append(
                InlineKeyboardButton(text=button_text, callback_data=callback_data_value)
            )

        # --- Newmod അനുസരിച്ച് വരിയിൽ 4 എണ്ണം വീതം പുഷ് ചെയ്യുന്നു ---
        if settings.get("newmod", False):
            row = []
            buttons_per_row = 4 
            for b in processed_file_buttons:
                row.append(b)
                if len(row) == buttons_per_row:
                    btn.append(row)
                    row = []
            if row: 
                btn.append(row)
        else:
            for b in processed_file_buttons:
                btn.append([b])

    # ✅ PAGINATION SYSTEM FIXED (BACK / NEXT BUTTONS)
    try:
        max_btn_setting = settings.get('max_btn', True)
        
        if 0 < offset <= PAGE_SIZE:
            off_set = 0
        elif offset == 0:
            off_set = None
        else:
            off_set = offset - PAGE_SIZE
            
        # 🔄 ഇവിടെ മാറ്റുക:
        current_page = 1 if offset == 0 else (int(offset) // PAGE_SIZE) + 1
        total_pages = math.ceil(total/PAGE_SIZE) if total > 0 else 1

        if n_offset == 0 or n_offset == "":
            if off_set is None:
                btn.append([
                    InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"),
                    InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                    InlineKeyboardButton("🛑 𝐄𝐍𝐃", callback_data="pages")
                ])
            else:
                btn.append([
                    InlineKeyboardButton("⌫ 𝐁𝐀𝐂𝐊", callback_data=f"next_{req}_{key}_{off_set}"), 
                    InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                    InlineKeyboardButton("🛑 𝐄𝐍𝐃", callback_data="pages")
                ])
        elif off_set is None:
            btn.append([
                InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"), 
                InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"), 
                InlineKeyboardButton("𝐍𝐄𝐗𝐓 ➪", callback_data=f"next_{req}_{key}_{n_offset}")
            ])
        else:
            btn.append([
                InlineKeyboardButton("⌫ 𝐁𝐀𝐂𝐊", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                InlineKeyboardButton("𝐍𝐄𝐗𝐓 ➪", callback_data=f"next_{req}_{key}_{n_offset}")
            ])
            
    except KeyError:
        await save_group_settings(query.message.chat.id, 'max_btn', True)
        if 0 < offset <= PAGE_SIZE:
            off_set = 0
        elif offset == 0:
            off_set = None
        else:
            off_set = offset - PAGE_SIZE
            
        # 🔄 ഇവിടെയും മാറ്റുക:
        current_page = 1 if offset == 0 else (int(offset) // PAGE_SIZE) + 1
        total_pages = math.ceil(total/PAGE_SIZE) if total > 0 else 1
        
        if n_offset == 0 or n_offset == "":
            if off_set is None:
                btn.append([
                    InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"),
                    InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                    InlineKeyboardButton("🛑 𝐄𝐍𝐃", callback_data="pages")
                ])
            else:
                btn.append([
                    InlineKeyboardButton("⌫ <b>𝐁𝐀𝐂𝐊</b>", callback_data=f"next_{req}_{key}_{off_set}"), 
                    InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                    InlineKeyboardButton("🛑 𝐄𝐍𝐃", callback_data="pages")
                ])
        elif off_set is None:
            btn.append([
                InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"), 
                InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"), 
                InlineKeyboardButton("<b>𝐍𝐄𝐗𝐓 ➪</b>", callback_data=f"next_{req}_{key}_{n_offset}")
            ])
        else:
            btn.append([
                InlineKeyboardButton("⌫ <b>𝐁𝐀𝐂𝐊</b>", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="pages"),
                InlineKeyboardButton("<b>𝐍𝐄𝐗𝐓 ➪</b>", callback_data=f"next_{req}_{key}_{n_offset}")
            ])
            
    temp.BACK_BUTTONS[key] = btn
    
    if not settings.get("button", True):
        cur_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        time_difference = timedelta(hours=cur_time.hour, minutes=cur_time.minute, seconds=(cur_time.second+(cur_time.microsecond/1000000))) - timedelta(hours=curr_time.hour, minutes=curr_time.minute, seconds=(curr_time.second+(curr_time.microsecond/1000000)))
        remaining_seconds = "{:.2f}".format(time_difference.total_seconds())
        cap = await get_cap(settings, remaining_seconds, files, query, total, search)
        try:
            await query.message.edit_text(text=cap, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
        except MessageNotModified:
            pass
    else:
        try:
            await query.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(btn)
            )
        except MessageNotModified:
            pass
    await query.answer() 





            #languages
            
    


    




# =====================================================================
# 3. ROTATE ബട്ടൺ ക്ലിക്ക് ഹാൻഡ്ലർ (Callback Query Handler)
# =====================================================================
# ⚠️ ശ്രദ്ധിക്കുക: ഈ ഫങ്ക്ഷൻ നിങ്ങളുടെ ബോട്ടിലെ inline.py അല്ലെങ്കിൽ callback ഹാൻഡ്ലറുകൾ ഉള്ള ഫയലിലേക്ക് മാറ്റുന്നതാണ് ഏറ്റവും സുരക്ഷിതം.
@Client.on_callback_query(filters.regex(r"^rotatesp#"))
async def handle_rotate_spelling(client, query):
    # കോൾബാക്കിൽ നിന്ന് ഡാറ്റ കൃത്യമായി വേർതിരിക്കുന്നു
    data_parts = query.data.split("#")
    user_id = data_parts[1]
    current_search = data_parts[2].replace("-", " ")
    
    # 🔄 ബാക്കിയുള്ള സ്പെല്ലിംഗ് ലിസ്റ്റ് എടുക്കുന്നു
    spelling_list = data_parts[3].split(",") if len(data_parts) > 3 else [current_search]
    
    if int(user_id) != query.from_user.id:
        await query.answer("ഇത് നിങ്ങളുടെ സെർച്ച് റിസൾട്ട് അല്ല!", show_alert=True)
        return

    await query.answer("🔄 പുതിയ സ്പെല്ലിംഗിൽ സെർച്ച് ചെയ്യുന്നു...")
    print(f"📢 [ROTATE CLICK LOG] സെർച്ച് ചെയ്യുന്നു: {current_search}")

    from database.ia_filterdb import get_search_results
    chat_id = query.message.chat.id
    files, _, _ = await get_search_results(chat_id, current_search, offset=0, max_results=10)
    
    if files:
        btn = []
        for f in files:
            clean_name = f.file_name
            clean_name = re.sub(r'\[.*?\]|\(.*?\)|@\w+|www\.\S+', '', clean_name)
            clean_name = clean_name.split('.')[0]
            unwanted_tags = r"\b(malayalam|tamil|hindi|telugu|english|torrents|torrent|mp4|mkv|avi|1080p|720p|480p|2160p|4k|hevc|x264|x265|bluray|brrip|hdrip|webrip|web-dl|dvdrip|camrip|hdtv|esub|sub|subtitle|subtitles|dual|audio)\b"
            clean_name = re.sub(unwanted_tags, " ", clean_name, flags=re.IGNORECASE)
            clean_name = re.sub(r'[^a-zA-Z0-9\s]', ' ', clean_name).strip()
            clean_name = re.sub(r'\s+', ' ', clean_name)

            btn.append([InlineKeyboardButton(text=clean_name.strip(), callback_data=f"files#{f.file_id}")])

        # 🎯 ഫയൽ ലഭിച്ചാൽ മെസ്സേജ് ഡിലീറ്റ് ചെയ്യാതെ എഡിറ്റ് ചെയ്ത് റിസൾട്ട് കാണിക്കുന്നു
        await query.message.edit_text(
            text=f"✅ **{current_search.upper()}** എന്ന സ്പെല്ലിംഗിൽ ലഭിച്ച റിസൾട്ടുകൾ:",
            reply_markup=InlineKeyboardMarkup(btn)
        )
    else:
        # 🔄 [INFINITE LOOP LOGIC] ഇപ്പോൾ തിരഞ്ഞ വാക്ക് ലിസ്റ്റിൽ നിന്ന് താൽക്കാലികമായി മാറ്റുന്നു
        if current_search in spelling_list:
            spelling_list.remove(current_search)
            
        # ലിസ്റ്റിൽ ഇനിയും വാക്കുകൾ ഉണ്ടെങ്കിൽ അത് എടുക്കുന്നു, ഇല്ലെങ്കിൽ പഴയ മുഴുവൻ ലിസ്റ്റും റീ-ലോഡ് ചെയ്ത് ലൂപ്പ് തിരിക്കുന്നു!
        if not spelling_list or len(spelling_list) == 0:
            # 🔄 വീണ്ടും മെയിൻ ഫങ്ക്ഷനിൽ നിന്ന് ലിസ്റ്റ് ജനറേറ്റ് ചെയ്യാൻ advantage_spell_chok വഴി നിർമ്മിച്ച ലിസ്റ്റ് ആവശ്യമാണ്.
            # തൽക്കാലം ലൂപ്പ് മുറിയാതിരിക്കാൻ ഈ വാക്ക് തന്നെ വീണ്ടും ലിസ്റ്റിലേക്ക് ഇട്ട് റൊട്ടേഷൻ ഇൻഫിനിറ്റ് ആക്കുന്നു.
            spelling_list = [current_search]
            
        next_spelling = spelling_list[0]
        safe_next_spelling = next_spelling.replace(" ", "-")
        remaining_spells = ",".join(spelling_list)

        buttons = [[
            InlineKeyboardButton(
                text=f"🔄 Rotate Check: {next_spelling.upper()}", 
                callback_data=f"rotatesp#{user_id}#{safe_next_spelling}#{remaining_spells}"
            )
        ]]
        
        # 🎯 എറർ മെസ്സേജ് അയക്കില്ല, മെസ്സേജ് ഡിലീറ്റ് ചെയ്യില്ല, പകരം അതേ മെസ്സേജിൽ ബട്ടൺ അപ്ഡേറ്റ് ചെയ്ത് കൊണ്ടേ ഇരിക്കും!
        await query.message.edit_text(
            text=f"⚠️ '{current_search.upper()}' ലഭ്യമായില്ല. അടുത്ത കോമ്പിനേഷൻ ശ്രമിക്കൂ 👇",
            reply_markup=InlineKeyboardMarkup(buttons)
        )






    
    






@Client.on_callback_query(filters.regex("^toggle_botpm$"))
async def toggle_botpm(client, query):

    user_id = query.from_user.id

    settings = await get_settings(user_id)

    current = settings.get("botpm", False)

    await save_group_settings(
        user_id,
        "botpm",
        not current
    )

    new_status = not current

    btn = query.message.reply_markup.inline_keyboard

    for row in btn:
        for button in row:
            if button.callback_data == "toggle_botpm":
                button.text = (
                    "Bot PM ✅"
                    if new_status else
                    "Bot PM ❌"
                )

    await query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(btn)
    )

    await query.answer(
        f"Bot PM {'Enabled' if new_status else 'Disabled'}",
        show_alert=False
    )









@Client.on_callback_query(filters.regex(r"^(vlike_|vdis_|vsmi_)"))
async def handle_database_votes(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data
    
    # callback_data-ൽ നിന്ന് ആക്ഷനും ഫയൽ ഐഡിയും വേർതിരിക്കുന്നു
    raw_action, file_id = data.split("_", 1)
    
    # ഡാറ്റാബേസിലേക്ക് അയക്കാൻ ആക്ഷൻ പേര് മാറ്റുന്നു
    action_map = {"vlike": "like", "vdis": "dislike", "vsmi": "smile"}
    action = action_map[raw_action]
    
    # ഡാറ്റാബേസ് അപ്ഡേറ്റ് ചെയ്യുന്നു
    success, message = await update_file_vote(file_id, user_id, action)
    
    if not success:
        # യൂസർ മുൻപ് വോട്ട് ചെയ്തിട്ടുണ്ടെങ്കിൽ അലേർട്ട് കാണിക്കും
        await callback_query.answer(message, show_alert=True)
        return

    # വോട്ട് വിജയകരമാണെങ്കിൽ ഡാറ്റാബേസിൽ നിന്ന് പുതിയ കൗണ്ടുകൾ എടുക്കുന്നു
    updated_vote_data = await get_file_votes(file_id)
    like_count = updated_vote_data.get("like", 0)
    dislike_count = updated_vote_data.get("dislike", 0)
    smile_count = updated_vote_data.get("smile", 0)
    
    # നിലവിലെ മെസ്സേജിലെ ബട്ടണുകൾ എടുത്ത് പുതുക്കുന്നു
    current_markup = callback_query.message.reply_markup
    buttons = current_markup.inline_keyboard
    
    updated_markup = InlineKeyboardMarkup(
        [
            [buttons[0][0]], # Save File Id Button
            [buttons[1][0]], # Download Button
            [
                InlineKeyboardButton(f"👍 {like_count}", callback_data=f"vlike_{file_id}"),
                InlineKeyboardButton(f"👎 {dislike_count}", callback_data=f"vdis_{file_id}"),
                InlineKeyboardButton(f"😊 {smile_count}", callback_data=f"vsmi_{file_id}")
            ]
        ]
    )
    
    # ചാനലിലെ വോട്ട് ബട്ടൺ ലൈവ് ആയി അപ്ഡേറ്റ് ചെയ്യുന്നു
    await callback_query.message.edit_reply_markup(reply_markup=updated_markup)
    await callback_query.answer(message)
    
    
    
    
@Client.on_callback_query(filters.regex("^backtele#"))
async def backtele_callback(client, query):
    back_key = query.data.split("#", 1)[1]
    data = temp.BACK_DATA.get(back_key)
    key = query.data.split("#")[1]

    buttons = temp.BACK_BUTTONS.get(key)

    if not buttons:
        return await query.answer("Expired", show_alert=True)

    await query.message.edit_reply_markup(
        InlineKeyboardMarkup(buttons)
    )

    await query.answer()

@Client.on_callback_query(filters.regex("^telegraph#"))
async def telegraph_callback(client, query):
	
    key = f"{query.message.chat.id}-{query.message.reply_to_message.id}"

    if REQUEST_USERS.get(key) != query.from_user.id:
        return await query.answer(
            "❌ This is not for you",
            show_alert=True
        )	

    username = (
        f"@{query.from_user.username}"
        if query.from_user and query.from_user.username
        else query.from_user.mention
    )

    key = query.data.split("#")[1]
    settings = await get_settings(query.message.chat.id)

    if not settings.get("telegraph", False):
        return await query.answer(
            "❌ Telegraph is disabled.",
            show_alert=True
        )

    search = FRESH.get(key)
    files = temp.GETALL.get(key)

    if not search or not files:
        return await query.answer(
            "Expired Result",
            show_alert=True
        )

    url = await create_telegraph_page(
        username,
        search,
        files,
        settings
    )

    await query.message.edit_reply_markup(
        InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🗂️𝐎𝐩𝐞𝐧🗂️",
                    url=url
                )
            ],
            [
                InlineKeyboardButton(
                    "◀️𝐁𝐚𝐜𝐤▶️",
                    callback_data=f"backtele#{key}"
                )
            ]
        ])
    )

    await query.answer()
    
    

@Client.on_callback_query(filters.regex("^telegraphp#"))
async def telegraph_callbacck(client, query):

    key = query.data.split("#")[1]
    settings = await get_settings(query.message.chat.id)
    if not settings.get("telegraph", False):
        return await query.answer(
            "❌Telegraph is disabled.❌",
            show_alert=True
        )

    # ബാക്കി code...
    search = FRESH.get(key)
    files = temp.GETALL.get(key)

    if not search or not files:
        return await query.answer(
            "Expired Result",
            show_alert=True
        )

    url = await create_telegraph_page(
        search,
        files,
        settings 
    )

    await query.answer()

    await query.message.reply_text(
        "📄𝐎𝐩𝐞𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐏𝐚𝐠𝐞📄",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🗂️𝐎𝐩𝐞𝐧🗂️",
                    url=url
                )
            ]]
        )
    )

@Client.on_callback_query(filters.regex("^back_top#"))
async def back_top(client, query):
    back_key = query.data.split("#", 1)[1]

    data = temp.BACK_DATA.get(back_key)
    buttons = data.get("buttons", [])
    if not data:
        return await query.answer("Expired", show_alert=True)

    await query.message.edit_reply_markup(
        InlineKeyboardMarkup(buttons)
    )

    await query.answer()



@Client.on_callback_query(filters.regex(r"^spol"))
async def advantage_spoll_choker(bot, query):
    data = query.data.split('#')
    
    # ക്ലോസ് ബട്ടൺ
    if len(data) > 2 and data[2] == "close_spellcheck":
        return await query.message.delete()
        
    _, user, msg_id, movie_index = data[:4]
    user = int(user)
    msg_id = int(msg_id)
    movie_index = int(movie_index)
    
    action = data[4] if len(data) > 4 else "main"
    value = data[5] if len(data) > 5 else None
    page = int(data[6]) if len(data) > 6 else 1 # പേജിനേഷൻ പേജ് നമ്പർ

    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)

    movies = SPELL_CHECK.get(msg_id)
    if not movies:
        return await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name), show_alert=True)

    # IMDb ഒറിജിനൽ പേര് എടുത്ത് ക്ലീൻ ചെയ്യുന്നു
    org_movie = movies[movie_index]
    movie = re.sub(r"[:\-\.]", " ", org_movie)
    movie = re.sub(r"\s+", " ", movie).strip()

    # 1️⃣ മെയിൻ കാറ്റഗറി ബട്ടണുകൾ
    if action == "main":
        await query.answer("Select Category")
        buttons = [
            [
                InlineKeyboardButton("🌐 Language", callback_data=f"spol#{user}#{msg_id}#{movie_index}#lang"),
                InlineKeyboardButton("🎞️ Quality", callback_data=f"spol#{user}#{msg_id}#{movie_index}#qual#1#1")
            ],
            [
                InlineKeyboardButton("📺 Season", callback_data=f"spol#{user}#{msg_id}#{movie_index}#season"),
                InlineKeyboardButton("🧩 Episode", callback_data=f"spol#{user}#{msg_id}#{movie_index}#episode#1#1")
            ],
            [InlineKeyboardButton("🔍 Direct Search", callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#all")],
            [InlineKeyboardButton("❌ Close", callback_data=f"spol#{user}#0#close_spellcheck")]
        ]
        return await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    # 2️⃣ എല്ലാ Languages ബട്ടണുകൾ
    elif action == "lang":
        await query.answer("Select Language")
        languages = ["Malayalam", "English", "Hindi", "Tamil", "Telugu", "Kannada", "Korea", "Dubbed", "Bengali", "Marathi", "Bhojpuri", "Punjabi", "Gujarati", "Spanish", "French", "Japanese", "Chinese"]
        buttons = []
        for i in range(0, len(languages), 2):
            row = [InlineKeyboardButton(languages[i], callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{languages[i].lower()}")]
            if i+1 < len(languages):
                row.append(InlineKeyboardButton(languages[i+1], callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{languages[i+1].lower()}"))
            buttons.append(row)
        buttons.append([InlineKeyboardButton("🔙 Back", callback_data=f"spol#{user}#{msg_id}#{movie_index}#main")])
        return await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    # 3️⃣ ക്വാളിറ്റി ബട്ടണുകൾ (144p മുതൽ 2160p വരെയും ബാക്കി ടാഗുകളും - 2 പേജുകൾ)
    elif action == "qual":
        await query.answer("Select Quality")
        qual_list = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "4k", "8k", "hdrip", "brrip", "dvdrip", "webrip", "webdl", "bluray", "uhd", "fullhd", "sd", "hd", "cam", "dvdscr"]
        
        # പേജ് തിരിക്കുന്നു (ഒരു പേജിൽ 12 എണ്ണം വീതം)
        per_page = 12
        start = (page - 1) * per_page
        end = start + per_page
        current_quals = qual_list[start:end]
        
        buttons = []
        for i in range(0, len(current_quals), 2):
            row = [InlineKeyboardButton(current_quals[i].upper(), callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{current_quals[i]}")]
            if i+1 < len(current_quals):
                row.append(InlineKeyboardButton(current_quals[i+1].upper(), callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{current_quals[i+1]}"))
            buttons.append(row)
            
        # പേജിനേഷൻ കൺട്രോൾസ് (Next/Prev)
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton("⬅️ Prev", callback_data=f"spol#{user}#{msg_id}#{movie_index}#qual#1#{page-1}"))
        if end < len(qual_list):
            nav_row.append(InlineKeyboardButton("Next ➡️", callback_data=f"spol#{user}#{msg_id}#{movie_index}#qual#1#{page+1}"))
        if nav_row:
            buttons.append(nav_row)
            
        buttons.append([InlineKeyboardButton("🔙 Back", callback_data=f"spol#{user}#{msg_id}#{movie_index}#main")])
        return await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    # 4️⃣ സീസൺ ബട്ടണുകൾ (S01 മുതൽ S12 വരെ)
    elif action == "season":
        await query.answer("Select Season")
        buttons = []
        for s in range(1, 13):
            s_text = f"S{s:02d}" # S01, S02...
            if s % 2 != 0:
                row = [InlineKeyboardButton(s_text, callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{s_text.lower()}")]
            else:
                row.append(InlineKeyboardButton(s_text, callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{s_text.lower()}"))
                buttons.append(row)
        buttons.append([InlineKeyboardButton("🔙 Back", callback_data=f"spol#{user}#{msg_id}#{movie_index}#main")])
        return await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    # 5️⃣ എപ്പിസോഡ് ബട്ടണുകൾ (E01 മുതൽ E24 വരെ - 2 പേജുകൾ)
    elif action == "episode":
        await query.answer("Select Episode")
        ep_list = [f"E{e:02d}" for e in range(1, 25)] # E01 മുതൽ E24 വരെ
        
        per_page = 12
        start = (page - 1) * per_page
        end = start + per_page
        current_eps = ep_list[start:end]
        
        buttons = []
        for i in range(0, len(current_eps), 3): # ഒരു വരിയിൽ 3 എണ്ണം വീതം
            row = [InlineKeyboardButton(current_eps[i], callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{current_eps[i].lower()}")]
            if i+1 < len(current_eps):
                row.append(InlineKeyboardButton(current_eps[i+1], callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{current_eps[i+1].lower()}"))
            if i+2 < len(current_eps):
                row.append(InlineKeyboardButton(current_eps[i+2], callback_data=f"spol#{user}#{msg_id}#{movie_index}#search#{current_eps[i+2].lower()}"))
            buttons.append(row)
            
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton("⬅️ Prev", callback_data=f"spol#{user}#{msg_id}#{movie_index}#episode#1#{page-1}"))
        if end < len(ep_list):
            nav_row.append(InlineKeyboardButton("Next ➡️", callback_data=f"spol#{user}#{msg_id}#{movie_index}#episode#1#{page+1}"))
        if nav_row:
            buttons.append(nav_row)
            
        buttons.append([InlineKeyboardButton("🔙 Back", callback_data=f"spol#{user}#{msg_id}#{movie_index}#main")])
        return await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

# 6️⃣ ഫൈനൽ ഫയൽ സെർച്ചിങ് ഘട്ടം (സ്പീഡും കൃത്യതയും കൂട്ടിയ ലോജിക്)
# 6️⃣ ഫൈനൽ ഫയൽ സെർച്ചിങ് ഘട്ടം (Autofilter ലോക്കിങ് പൂർണ്ണമായി ബൈപാസ്സ് ചെയ്തത്)
    elif action == "search":
        await query.answer("Filtering files...", show_alert=False)
        
        clean_movie_name = re.sub(r"\(\d{4}\)", "", movie).strip()
        clean_movie_name = re.sub(r"[:\-\.\(\)]", " ", clean_movie_name)
        clean_movie_name = re.sub(r"\s+", " ", clean_movie_name).strip()

        settings = await get_settings(query.message.chat.id)
        if settings.get("newmod", False):
            max_results = 40 if settings.get("max_btn") else 20
        else:
            max_results = 10 if settings.get("max_btn") else int(MAX_B_TN)

        # ഡാറ്റാബേസിൽ നിന്ന് 100 ഫയലുകൾ എടുക്കുന്നു (filter=False ആയതിനാൽ എല്ലാ ഫയലും വരും)
        all_files, offset, total_results = await get_search_results(
            query.message.chat.id,
            clean_movie_name,
            offset=0,
            max_results=100, 
            filter=False     
        )

        files = []
        if all_files:
            if value and value != "all":
                filtered_files = []
                for file in all_files:
                    file_name = file.file_name if hasattr(file, 'file_name') else getattr(file, 'name', str(file))
                    file_name_lower = file_name.lower()
                    
                    if value.lower() in file_name_lower:
                        filtered_files.append(file)
                
                files = filtered_files[:max_results]
                total_results = len(filtered_files)
            else:
                files = all_files[:max_results]
                total_results = len(all_files)

        if files:
            display_query = f"{clean_movie_name} {value}" if value and value != "all" else clean_movie_name
            
            # 🎯 ഇവിടെയാണ് മാജിക്: നമ്മൾ ഫിൽട്ടർ ചെയ്ത ഫയലുകൾ (files) നേരിട്ട് auto_filter-ലേക്ക് വിടുന്നു
            k = (display_query, files, 0, total_results)
            await auto_filter(bot, query, k)
        else:
            display_query = f"{clean_movie_name} {value}" if value and value != "all" else clean_movie_name
            
            LOCAL_LANG_MAP = {
                "ml": "Malayalam 🎥",
                "ta": "Tamil 🍿",
                "hi": "Hindi 🪙",
                "te": "Telugu ⚡",
                "en": "English 🌐",
                "kn": "Kannada 🏔️"
            }
            
            lang = "N/A"
            release_status = "N/A"
            ott_status = "OTT❌ waiting...⏳"
            today = datetime.now(pytz.timezone('Asia/Kolkata')).date()
            
            try:
                search_url = f"https://api.themoviedb.org/3/search/movie?api_key=229c6b13681d95ffc03362a0c53904e7&query={clean_movie_name.strip()}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(search_url, timeout=10) as response:
                        if response.status == 200:
                            res = await response.json()
                            results = res.get("results", [])
                            
                            if results:
                                tmdb_movie = results[0]
                                movie_id = tmdb_movie.get("id")
                                
                                # 🌐 [LANGUAGE]
                                lang_code = tmdb_movie.get("original_language", "en")
                                lang = LOCAL_LANG_MAP.get(lang_code.lower(), lang_code.upper())
                                
                                # 📅 [THEATER RELEASE DATE & STATUS]
                                date_str = tmdb_movie.get("release_date", "")
                                if date_str:
                                    try:
                                        release_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                                        # 💡 ഇവിടെ മാറ്റം വരുത്തി: 'July 10, 2026' എന്ന ഫോർമാറ്റിലേക്ക് മാറ്റി
                                        formatted_date = release_date.strftime("%B %d, %Y")
                                        if release_date <= today:
                                            release_status = f"{formatted_date} (Released ✅)"
                                        else:
                                            release_status = f"Releasing on: {formatted_date} ⏳"
                                    except:
                                        release_status = date_str
                                
                                # 🟢 [STRICT OTT VERIFICATION LOGIC]
# 🟢 [STRICT OTT VERIFICATION LOGIC]
                                is_digital_released = False
                                if movie_id:
                                    release_url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates?api_key=229c6b13681d95ffc03362a0c53904e7"
                                    async with session.get(release_url, timeout=5) as rel_res:
                                        if rel_res.status == 200:
                                            rel_data = await rel_res.json()
                                            for country in rel_data.get("results", []):
                                                if country.get("iso_3166_1") in ["IN", "US"]:
                                                    for r_info in country.get("release_dates", []):
                                                        if r_info.get("type") == 4:
                                                            try:
                                                                digi_date = datetime.strptime(r_info.get("release_date")[:10], "%Y-%m-%d").date()
                                                                if digi_date <= today:
                                                                    is_digital_released = True
                                                            except:
                                                                is_digital_released = True

                                    watch_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key=229c6b13681d95ffc03362a0c53904e7"
# ... (മുകളിലെ കോഡ് എല്ലാം ശരിയാണെന്ന് ഉറപ്പുവരുത്തുക)
                                    async with session.get(watch_url, timeout=5) as watch_res:
                                        if watch_res.status == 200:
                                            try:
                                                w_data = await watch_res.json()
                                                providers = w_data.get("results", {})
                                                in_provider = providers.get("IN") or providers.get("US") or {}
                                                ott_list = in_provider.get("flatrate") or in_provider.get("free")
                                                
                                                if ott_list:
                                                    platforms = list(set([p.get("provider_name") for p in ott_list if p.get("provider_name")]))
                                                    platform_str = ", ".join(platforms)
                                                    ott_status = f"OTT✅ ({platform_str})"
                                                else:
                                                    ott_status = "OTT❌ Coming Soon...⏳"
                                            except:
                                                pass
            except Exception as tmdb_err:
                print(f"TMDB Search Error: {tmdb_err}")
            # 🟢 [USER INFO]
            try:
                req_user = await bot.get_users(user)
                user_name = req_user.mention if req_user else f"User ID: {user}"
            except:
                user_name = f"User ID: {user}"

            # 🟢 [GROUP LINK/USERNAME FIX]
            chat = query.message.chat
            group_name = chat.title if chat.title else "Private PM"
            contentt = query.message.reply_to_message.text

            print("STEP 2")

            imdb = await get_poster(contentt) if IMDB else None
            
            if chat.username:
                group_info = f"<a href='https://t.me/{chat.username}'>{group_name}</a> (@{chat.username})"
            else:
                try:
                    invite_link = await bot.create_chat_invite_link(chat.id)
                    group_info = f"<a href='{invite_link.invite_link}'>{group_name}</a> (Private Link)"
                except:
                    group_info = f"<b>{group_name}</b> (Invite Link Missing/Bot not Admin)"

            # 🟢 [ADMIN ALERT TEXT - WITH PROPER SPACES]
            admin_alert_text = (
                "🚨 <b><u>Movie Not Found Request</u></b>\n\n"
                f"👤 <b>User Name:</b> {user_name} (<code>{user}</code>)\n\n"
                f"👥 <b>Group Name:</b> {group_info}\n\n"
                f"🎬 <b>Movie Name:</b> <code>{display_query.upper()}</code>\n\n"
                f"📅 <b>Release Date:</b> {release_status}\n\n"
                f"🌐 <b>Language:</b> {lang}\n\n"
                f"💿 <b>OTT Status:</b> {ott_status}"
            )

            # 🟢 [SEND TO ADMINS PM]
# 🟢 [SEND TO ADMINS PM]
            if ADMINS:
                poster = imdb.get('poster') if imdb else None # പോസ്റ്റർ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു
                
                for admin_id in ADMINS:
                    try:
                        if poster and poster != "N/A":
                            # പോസ്റ്റർ ഉണ്ടെങ്കിൽ ഫോട്ടോ അയക്കുക
                            await bot.send_photo(
                                photo=poster,
                                chat_id=int(admin_id),
                                caption=admin_alert_text,
                                parse_mode=enums.ParseMode.HTML
                            )
                        else:
                            # പോസ്റ്റർ ഇല്ലെങ്കിൽ ടെക്സ്റ്റ് മാത്രം അയക്കുക
                            await bot.send_message(
                                chat_id=int(admin_id),
                                text=admin_alert_text,
                                parse_mode=enums.ParseMode.HTML,
                                disable_web_page_preview=True
                            )
                    except Exception as pm_err:
                        print(f"Could not send PM to admin {admin_id}: {pm_err}")
            # യൂസർക്ക് ഗ്രൂപ്പിൽ സാധാരണ കാണിക്കുന്ന നോട്ട് ഫൗണ്ട് മെസ്സേജ്
            await query.message.edit_text(
                f"<code>{display_query.upper()}</code> ᴍᴏᴠɪᴇ/ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴ ɪɴ ᴅᴀᴛᴀʙᴀ宣e...",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"spol#{user}#{msg_id}#{movie_index}#main")]]),
                parse_mode=enums.ParseMode.HTML
            )










# --- CALLBACK FUNCTION ---
# --- CALLBACK FUNCTION ---
@Client.on_callback_query(filters.regex(r"^spoll"))
async def advantage_spoll_chokerr(bot, query):
    data = query.data.split('#')
    
    if data[2] == "close_spellcheck":
        return await query.message.delete()
        
    _, user, msg_id, movie_index = data
    user = int(user)
    msg_id = int(msg_id)

    movies = SPELL_CHECK.get(msg_id)
    if not movies:
        return await query.answer(
            script.OLD_ALRT_TXT.format(query.from_user.first_name),
            show_alert=True
        )

    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(
            script.ALRT_TXT.format(query.from_user.first_name),
            show_alert=True
        )

    # IMDb-യിൽ നിന്നുള്ള ഒറിജിനൽ പേര് എടുക്കുന്നു (ഉദാ: K.G.F: Chapter 1)
    movie = movies[int(movie_index)]
    
    # 🎯 ഇവിടെയാണ് മാജിക്! 
    # 1. ഡോട്ടുകളും (.), കോളനുകളും (:), ഹൈഫനുകളും (-) മാറ്റി അവിടെ സ്പെയ്സ് ഇട്ടുകൊടുക്കുന്നു.
    movie = re.sub(r"[:\-\.]", " ", movie)
    
    # 2. അനാവശ്യമായി ഒന്നിൽ കൂടുതൽ വന്നിട്ടുള്ള സ്പെയ്സുകൾ കളഞ്ഞ് സിംഗിൾ സ്പെയ്സ് ആക്കുന്നു.
    movie = re.sub(r"\s+", " ", movie).strip()
    
    # ഇപ്പോൾ 'K.G.F: Chapter 1' എന്നത് കൃത്യമായി 'K G F Chapter 1' എന്ന് മാറി കഴിഞ്ഞു.

    await query.answer(script.TOP_ALRT_MSG)

    gl = await global_filters(bot, query.message, text=movie)

    if gl is False:
        k = await manual_filters(bot, query.message, text=movie)

        if k is False:
            settings = await get_settings(query.message.chat.id)
            
            if settings.get("newmod", False):
                max_results = 40 if settings.get("max_btn") else 20
            else:
                max_results = 10 if settings.get("max_btn") else int(MAX_B_TN)

            # 🔎 ഇവിടെ നമ്മൾ ക്ലീൻ ചെയ്ത 'K G F Chapter 1' വെച്ചാണ് സെർച്ച് ചെയ്യുന്നത്!
            files, offset, total_results = await get_search_results(
                query.message.chat.id,
                movie,
                offset=0,
                max_results=max_results,
                filter=True
            )

            if files:
                k = (movie, files, offset, total_results)
                await auto_filter(bot, query, k)

            else:
                # ഫയൽ കണ്ടെത്താത്ത പക്ഷം ഉള്ള ബാക്കി കോഡ്...
                try:
                    conten = query.message.reply_to_message.text
                except:
                    conten = movie

                imdb = await get_poster(conten) if IMDB else None
                poster = imdb.get("poster") if imdb else None

                if not poster or poster == "N/A":
                    poster = "https://graph.org/file/3d0f0f0f0f0f0f0f0f0f.jpg"

                reqstr1 = query.from_user.id if query.from_user else 0
                reqstr = await bot.get_users(reqstr1)

                if NO_RESULTS_MSG:
                    await bot.send_message(
                        chat_id=LOG_CHANNEL,
                        text=script.NORSLTS.format(reqstr.id, reqstr.mention, movie)
                    )

                buttons = [[
                    InlineKeyboardButton(
                        "🔁 𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲 🔁",
                        callback_data=f"show_option#{user}#{query.message.chat.id}#{query.message.id}#{movie}"
                    )
                ]]

                reply_markup = InlineKeyboardMarkup(buttons)

                try:
                    mention_user = query.message.reply_to_message.from_user.mention
                except:
                    mention_user = query.from_user.mention

                k = await query.message.edit(
                    f"{mention_user}\n"
                    f"<code>{conten}</code> ᴍᴏᴠɪᴇ ɴᴏᴛ 👑 ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱе...",
                    reply_markup=reply_markup,
                    parse_mode=enums.ParseMode.HTML
                )
                
                # (ബാക്കി അഡ്മിൻ നോട്ടിഫിക്കേഷൻ കോഡുകൾ താഴേക്ക് വരും...)
        
        
        

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "gfiltersdeleteallconfirm":
        await del_allg(query.message, 'gfilters')
        await query.answer("Dᴏɴᴇ !")
        return
    elif query.data == "gfiltersdeleteallcancel": 
        await query.message.reply_to_message.delete()
        await query.message.delete()
        await query.answer("Pʀᴏᴄᴇss Cᴀɴᴄᴇʟʟᴇᴅ !")
        return
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == enums.ChatType.PRIVATE:
            grpid = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Mᴀᴋᴇ sᴜʀᴇ I'ᴍ ᴘʀᴇsᴇɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!!", quote=True)
                    return await query.answer(MSG_ALRT)
            else:
                await query.message.edit_text(
                    "I'ᴍ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘs!\nCʜᴇᴄᴋ /connections ᴏʀ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘs",
                    quote=True
                )
                return await query.answer(MSG_ALRT)

        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return await query.answer(MSG_ALRT)

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʙᴇ Gʀᴏᴜᴘ Oᴡɴᴇʀ ᴏʀ ᴀɴ Aᴜᴛʜ Usᴇʀ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == enums.ChatType.PRIVATE:
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Tʜᴀᴛ's ɴᴏᴛ ғᴏʀ ʏᴏᴜ!!", show_alert=True)
    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        act = query.data.split(":")[2]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}"),
             InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Gʀᴏᴜᴘ Nᴀᴍᴇ : **{title}**\nGʀᴏᴜᴘ ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return await query.answer(MSG_ALRT)
    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title

        user_id = query.from_user.id

        mkact = await make_active(user_id, int(group_id))

        if mkact:
            await query.message.edit_text(
                f"Cᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ **{title}**",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await query.message.edit_text('Sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ!!', parse_mode=enums.ParseMode.MARKDOWN)
        return await query.answer(MSG_ALRT)
    elif "disconnect" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title
        user_id = query.from_user.id

        mkinact = await make_inactive(user_id)

        if mkinact:
            await query.message.edit_text(
                f"Dɪsᴄᴏɴɴᴇᴄᴛᴇᴅ ғʀᴏᴍ **{title}**",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await query.message.edit_text(
                f"Sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ!!",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        return await query.answer(MSG_ALRT)
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(user_id, int(group_id))

        if delcon:
            await query.message.edit_text(
                "Sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ !"
            )
        else:
            await query.message.edit_text(
                f"Sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ!!",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        return await query.answer(MSG_ALRT)
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(userid)
        if groupids is None:
            await query.message.edit_text(
                "Tʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴀᴄᴛɪᴠᴇ ᴄᴏɴɴᴇᴄᴛɪᴏɴs!! Cᴏɴɴᴇᴄᴛ ᴛᴏ sᴏᴍᴇ ɢʀᴏᴜᴘs ғɪʀsᴛ.",
            )
            return await query.answer(MSG_ALRT)
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = active = await if_active(userid, groupid)
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Yᴏᴜʀ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟs ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
    elif "gfilteralert" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_gfilter('gfilters', keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert, show_alert=True)
    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert, show_alert=True)
    if query.data.startswith("file"):
        
        clicked = query.from_user.id
        try:
            typed = query.message.reply_to_message.from_user.id
        except:
            typed = query.from_user.id
        ident, file_id = query.data.split("#")
        
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('Nᴏ sᴜᴄʜ ғɪʟᴇ ᴇxɪsᴛ.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = files.caption
        username = query.message.from_user.first_name
        settings = await get_settings(query.message.chat.id)
        
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
            f_caption = f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"

        try:
            print("CURRENT BOTPM =", settings["botpm"])
            print("CLICKED =", clicked)
            print("TYPED =", typed)

            if AUTH_CHANNEL and not await is_subscribed(client, query):
                if clicked == typed:
                    await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start={ident}_{file_id}")
                    
                    return
                else:
                    await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
            elif settings.get("mod_mode", False):

                if clicked != typed:
                    return await query.answer(
                        "This is not your request",
                        show_alert=True
                    )

                buttons = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🤖 BOT PM",
                                callback_data=f"modpm#{ident}#{file_id}"
                            ),
                            InlineKeyboardButton(
                                "📢 CHANNEL",
                                callback_data=f"modch#{ident}#{file_id}"
                            )
                        ]
                    ]
                )

                return await query.message.reply_text(
                    "Select Download Mode",
                    reply_markup=buttons
                )
                                                
            elif settings['botpm'] and settings['is_shortlink'] and clicked not in PREMIUM_USER:
                if clicked == typed:
                    temp.SHORT[clicked] = query.message.chat.id
                    await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=short_{file_id}")
                    await query.answer('Check PM, I have sent files in pm',show_alert = True)
                    return
                else:
                    await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
                    
            elif settings['is_shortlink'] and not settings['botpm'] and clicked not in PREMIUM_USER:
                print("ENTERED SHORTLINK BLOCK")

                if clicked == typed:
                    temp.SHORT[clicked] = query.message.chat.id
                    await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=short_{file_id}")

                    await query.answer('Check PM, I have sent files in pm', show_alert=True)
                    return
                else:
                	
                    await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
                    print("CURRENT BOTPM =", settings["botpm"])
                    print("PREMIUM =", clicked in PREMIUM_USER)
                    print("CURRENT BOTPM =", settings["botpm"])
                    print("PREMIUM CHECK =", clicked in PREMIUM_USER)
                    print("CLICKED =", clicked)
#            elif settings['botpm'] or clicked in PREMIUM_USER:
            elif settings['botpm']:
                print("ENTERED BOTPM BLOCK")

                if clicked == typed:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=f"{ident}_{file_id}",
                        caption=f_caption
                    )
                    await query.answer('Check PM, I have sent files in pm',show_alert = True)
                    return
                else:
                    await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
                                
            else:
                print("ENTERED FILE_CHANNEL BLOCK")
                print("FILE_CHANNEL =", FILE_CHANNEL)

                if clicked == typed:
                    print("STEP 1")

                    content = query.message.reply_to_message.text

                    print("STEP 2")
#                    import urllib.parse
                    imdb = await get_poster(content) if IMDB else None
                    
#                    poster_encoded = urllib.parse.quote(poster)
                    JRMA_URL = "https://nasranibot-c53.e.jrnm.app"
                    stream_link = f"{JRMA_URL}/watch/{file_id}"

                    print("STEP 3")

                    try:
                        vote_data = await get_file_votes(file_id)
                        print("VOTE DATA =", vote_data)
                    except Exception as e:
                        print("VOTE ERROR =", e)
                        vote_data = {}

                    print("STEP 4")

                    like_count = vote_data.get("like", 0)
                    dislike_count = vote_data.get("dislike", 0)
                    smile_count = vote_data.get("smile", 0)

                    print("STEP 5")
#😔                    
                    print("SENDING TO FILE_CHANNEL")

                    file_send = await client.send_cached_media(
                        chat_id=FILE_CHANNEL,
                        file_id=file_id,
                        caption=script.CHANNEL_CAP.format(
                            query.from_user.mention,
                            title,
                            query.message.chat.title
                        ),
                        protect_content=True if ident == "filep" else False,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        f"👍 {like_count}",
                                        callback_data=f"vlike_{file_id}"
                                    )
                                ],                                
                                [
                                    InlineKeyboardButton(
                                        "📩𝐒𝐚𝐯𝐞 𝐅𝐢𝐥𝐞 𝐈𝐝📩",
                                        url=f"https://t.me/share/url?url={file_id}"
                                    )
                                ],                                
                                [                                
                                    InlineKeyboardButton(
                                        "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝💻",
                                        url="https://t.me/batchfiles_store"
                                    )
                                ]
                            ]
                        )
                    )

                    print("FILE SENT SUCCESS")
                    print("FILE ID =", file_send.id)
                    print("FILE LINK =", file_send.link)

                    
                                          
                    Joel_tgx = await query.message.reply_photo(
                        photo=imdb.get('poster'),
                        caption=script.FILE_MSG.format(query.from_user.mention, title, size),
                        parse_mode=enums.ParseMode.HTML,
                        reply_markup=InlineKeyboardMarkup(
                            [
                             [
                              InlineKeyboardButton('📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 📥 ', url = file_send.link)
                           ],[
                              InlineKeyboardButton("⚠️ 𝐂𝐚𝐧'𝐭 𝐀𝐜𝐜𝐞𝐬𝐬 ❓ 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 ⚠️", url=(FILE_FORWARD))
                           ],[
                              InlineKeyboardButton("📺 Watch Online / Stream 📺", url=stream_link)
                             ]
                            ]
                        )
                    )
                    if settings['auto_delete']:
                        await asyncio.sleep(90)
                        await Joel_tgx.delete()
                        await file_send.delete()
                    

                    s = await client.send_message(
                        chat_id=FILE_CHANNEL,                        
                        text=script.DONE_MSG.format(query.from_user.mention, title, size),
                        parse_mode=enums.ParseMode.HTML,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                     InlineKeyboardButton(f"📩𝐒𝐚𝐯𝐞 𝐅𝐢𝐥𝐞 𝐈??📩", url=f"https://t.me/share/url?url={ident}_{file_id}")
                                 ],
                                 [
                                 InlineKeyboardButton(f"💻𝐒𝐞𝐧𝐝 𝐅??𝐥𝐞 𝐈𝐃💻", url=f"https://t.me/share/url?url={file_id}")
                                 
                                 ]                            
                            ]
                        )
                    )
#                    return 
                    name_format = f"okda"
                    image = await Joel_tgx.download(file_name=f"{name_format}.jpg")
                    
                    im = Image.open(image).convert("RGB")
                    im.save(f"{name_format}.webp", "webp")
                    sticker = f"{name_format}.webp"
                    buttons = [[
                     #   InlineKeyboardButton(f"📥{imdb.get('title')} {imdb.get('year')}📥", url=f"https://telegram.me/{temp.U_NAME}?start={ident}_{file_id}")
                        InlineKeyboardButton(f"📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 📥", url= s.link)
                    
                    ], [
                        InlineKeyboardButton(f"⚠️𝐃𝐞??𝐞𝐭𝐞 𝐍𝐨𝐰⚠️", callback_data="dl")
                
                    ]]
                    reply_markup = InlineKeyboardMarkup(buttons)
           
                    sp = await client.send_sticker(
                    chat_id=AUTH_CHANNEL,
                    sticker=sticker,            
                    reply_markup=reply_markup,                       
                    )
                    await sp.react(emoji=random.choice(REACTIONS))
                    os.remove(sticker)
                    os.remove(image)
#                   await asyncio.sleep(300)
#                   await sp.delete()
#                            return await query.answer('Cʜᴇᴄᴋ PM, I ʜᴀᴠᴇ sᴇɴᴛ ғɪʟᴇs ɪɴ PM', show_alert=True)
                else:
                    return await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
        except UserIsBlocked:
            await query.answer('Uɴʙʟᴏᴄᴋ ᴛʜᴇ ʙᴏᴛ ᴍᴀʜɴ !', show_alert=True)
        except PeerIdInvalid:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
        except Exception as e:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")

    # 🛑 ഇവിടെയാണ് നിങ്ങളുടെ പുതിയ SENDMARKED ബട്ടൺ വരേണ്ടത് (കറക്റ്റ് ഇൻഡന്റേഷനിൽ)


    elif query.data.startswith("sendfiles"):
        clicked = query.from_user.id
        ident, key = query.data.split("#")
        settings = await get_settings(query.message.chat.id)
        try:
            if settings['is_shortlink'] and clicked not in PREMIUM_USER:
                await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=sendfiles1_{key}")
                return
            else:
                await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=allfiles_{key}")
                return
        except UserIsBlocked:
            await query.answer('Uɴʙʟᴏᴄᴋ ᴛʜᴇ ʙᴏᴛ ᴍᴀʜɴ !', show_alert=True)
        except PeerIdInvalid:
            await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=sendfiles3_{key}")
        except Exception as e:
            logger.exception(e)
            await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=sendfiles4_{key}")


    
    elif query.data.startswith("send_fsall"):
        temp_var, ident, key, offset = query.data.split("#")
        search = BUTTON0.get(key)
        if not search:
            await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
            return
        files, n_offset, total = await get_search_results(query.message.chat.id, search, offset=int(offset), filter=True)
        await send_all(client, query.from_user.id, files, ident, query.message.chat.id, query.from_user.first_name, query)
        search = BUTTONS1.get(key)
        files, n_offset, total = await get_search_results(query.message.chat.id, search, offset=int(offset), filter=True)
        await send_all(client, query.from_user.id, files, ident, query.message.chat.id, query.from_user.first_name, query)
        search = BUTTONS2.get(key)
        files, n_offset, total = await get_search_results(query.message.chat.id, search, offset=int(offset), filter=True)
        await send_all(client, query.from_user.id, files, ident, query.message.chat.id, query.from_user.first_name, query)
        await query.answer(f"Hey {query.from_user.first_name}, All files on this page has been sent successfully to your PM !", show_alert=True)
        
    
    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("Jᴏɪɴ ᴏᴜʀ Bᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒", show_alert=True)
            return
        ident, kk, file_id = query.data.split("#")
        await query.answer(url=f"https://t.me/{temp.U_NAME}?start={kk}_{file_id}")
        
    elif query.data.startswith("del"):
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('Nᴏ sᴜᴄʜ ғɪʟᴇ ᴇxɪsᴛ.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        f_caption = files.caption
        settings = await get_settings(query.message.chat.id)
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
            f_caption = f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"
        await query.answer(url=f"https://telegram.me/{temp.U_NAME}?start=file_{file_id}")
    
    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("Jᴏɪɴ ᴏᴜʀ Bᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒", show_alert=True)
            return
        ident, kk, file_id = query.data.split("#")
        await query.answer(url=f"https://t.me/{temp.U_NAME}?start={kk}_{file_id}")
        
    elif query.data == "pages":
        await query.answer()

    elif query.data.startswith("grp_checksub"):
        userid = query.message.reply_to_message.from_user.id
        if int(userid) not in [query.from_user.id, 0]:
            return await query.answer("This Is Not For You!", show_alert=True)
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("Please join first my Updates Channel", show_alert=True)
            return
        await client.unban_chat_member(query.message.chat.id, query.from_user.id)
        await query.answer("Can You Request Now!", show_alert=True)
        permissions = ChatPermissions(can_send_messages=True)
        await query.message.chat.restrict_member(userid, permissions)
        await query.message.delete()
        await query.message.reply_to_message.delete()



    
    elif query.data.startswith("allsend"):
        temp_var, ident, offset, userid = query.data.split("#")
        if int(userid) not in [query.from_user.id, 0]:
            return await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)
        files = temp.SEND_ALL_TEMP.get(query.from_user.id)
        is_over = await send_all_files(client, query.from_user.id, files, ident)
        if is_over == 'done':
            return await query.answer(f"Hᴇʏ {query.from_user.first_name}, Aʟʟ ғɪʟᴇs ᴏɴ ᴛʜɪs ᴘᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ʏᴏᴜʀ PM !", show_alert=True)
        elif is_over == 'fsub':
            return await query.answer("Hᴇʏ, Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ɪɴ ᴍʏ ʙᴀᴄᴋ ᴜᴘ ᴄʜᴀɴɴᴇʟ. Cʜᴇᴄᴋ ᴍʏ PM ᴛᴏ ᴊᴏɪɴ ᴀɴᴅ ɢᴇᴛ ғɪʟᴇs !", show_alert=True)
        elif is_over == 'verify':
            return await query.answer("Hᴇʏ, Yᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ. Yᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴠᴇʀɪғʏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ. Cʜᴇᴄᴋ ᴍʏ PM ᴛᴏ ᴠᴇʀɪғʏ ᴀɴᴅ ɢᴇᴛ ғɪʟᴇs !", show_alert=True)
        else:
            return await query.answer(f"Eʀʀᴏʀ: {is_over}", show_alert=True)

    


    elif query.data.startswith("send_fall"):
        temp_var, ident, key, offset = query.data.split("#")
        if BUTTONS.get(key)!=None:
            search = BUTTONS.get(key)
        else:
            search = FRESH.get(key)
        if not search:
            await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
            return
        files, n_offset, total = await get_search_results(query.message.chat.id, search, offset=int(offset), filter=True)
        await send_all(client, query.from_user.id, files, ident, query.message.chat.id, query.from_user.first_name, query)
        await query.answer(f"Hey {query.from_user.first_name}, All files on this page has been sent successfully to your PM !", show_alert=True)
        
    elif query.data.startswith("killfilesdq"):
        ident, keyword = query.data.split("#")
        await query.message.edit_text(f"<b>Fᴇᴛᴄʜɪɴɢ Fɪʟᴇs ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {keyword} ᴏɴ DB... Pʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
        files, total = await get_bad_files(keyword)
        await query.message.edit_text(f"<b>Fᴏᴜɴᴅ {total} Fɪʟᴇs ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {keyword} !\n\nFɪʟᴇ ᴅᴇʟᴇᴛɪᴏɴ ᴘʀᴏᴄᴇss ᴡɪʟʟ sᴛᴀʀᴛ ɪɴ 5 sᴇᴄᴏɴᴅs!</b>")
        await asyncio.sleep(5)
        deleted = 0
        async with lock:
            try:
                for file in files:
                    file_ids = file.file_id
                    file_name = file.file_name
                    result = await Media.collection.delete_one({
                        '_id': file_ids,
                    })
                    if not result.deleted_count:
                        result = await Media2.collection.delete_one({
                            '_id': file_ids,
                        })
                    if result.deleted_count:
                        logger.info(f'Fɪʟᴇ Fᴏᴜɴᴅ ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {keyword}! Sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ {file_name} ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ.')
                        deleted += 1
                        if deleted % 20 == 0:
                            await query.message.edit_text(f"<b>Pʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ ғᴏʀ ᴅᴇʟᴇᴛɪɴɢ ғɪʟᴇs ғʀᴏᴍ DB. Sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ {str(deleted)} ғɪʟᴇs ғʀᴏᴍ DB ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {keyword} !\n\nPʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
            except Exception as e:
                logger.exception(e)
                await query.message.edit_text(f'Eʀʀᴏʀ: {e}')
            else:
                await query.message.edit_text(f"<b>Pʀᴏᴄᴇss Cᴏᴍᴘʟᴇᴛᴇᴅ ғᴏʀ ғɪʟᴇ ᴅᴇʟᴇᴛɪᴏɴ !\n\nSᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ {str(deleted)} ғɪʟᴇs ғʀᴏᴍ DB ғᴏʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀʏ {keyword}.</b>")




    elif query.data.startswith("setgs#gfiltersss#"):
        try:
            # split callback_data: setgs#gfilter#True#grp_id
            _, set_type, value, grp_id = query.data.split("#")
        except ValueError:
            await query.answer("Invalid callback data!", show_alert=True)
            return

        grp_id = int(grp_id)
        value = True if value == "True" else False
        new_value = not value

        # Save updated setting in DB
        await save_group_settings(grp_id, set_type, new_value)

            # Update local settings dict
        settings = await get_settings(grp_id)
        settings[set_type] = new_value

        # Rebuild buttons (only gfilter shown; add others as needed)
        buttons = [
            [
                InlineKeyboardButton(
                    'FILTER✅' if settings["gfilter"] else 'FILTER❌',
                    callback_data=f'setgs#gfilter#{settings["gfilter"]}#{grp_id}'
                )
            ],
        ]

        await query.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
        await query.answer(f"FILTER {'Enabled' if new_value else 'Disabled'}", show_alert=True)

    elif query.data.startswith("setgs#gfilters#"):
#    print("SET_TYPE =", set_type)
#    elif set_type == 'gfilters':
        current = settings['gfilter']
        new_value = not current
        await save_group_settings(grp_id, 'gfilter', new_value)

    # update settings dict
        settings['gfilter'] = new_value

    # create updated button layout
        buttons = [
            [
                InlineKeyboardButton('FILTER✅' if settings["gfilter"] else 'FILTER❌',
                    callback_data=f'setgs#gfilter#{settings["gfilter"]}#{str(grp_id)}')
            ],
        # add other buttons as needed
        ]

        await query.message.edit_reply_markup(
            InlineKeyboardMarkup(buttons)
        )

        await query.answer(f"FILTER {'Enabled' if new_value else 'Disabled'}", show_alert=True)

    elif query.data.startswith("get_afiles|"):

        keyword = query.data.split("|",1)[1]  # split only once

        col = mydb["global_filters"]

        data = col.find_one({"text": keyword})

        if not data or "files" not in data:
            await query.answer("No files found!", show_alert=True)
            return

        for f in data["files"]:
            await client.send_cached_media(
                query.from_user.id,
                f["file_id"],
                caption=f["file_name"]
            )

        await query.answer("Files sent to your PM!")  




    elif query.data.startswith("opnsetgrp"):
        ident, grp_id = query.data.split("#")
        grp_id = int(grp_id)
        userid = query.from_user.id if query.from_user else None
        st = await client.get_chat_member(grp_id, userid)
        if (
                st.status != enums.ChatMemberStatus.ADMINISTRATOR
                and st.status != enums.ChatMemberStatus.OWNER
                and int(userid) not in ADMINS
        ):
            await query.answer("Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Tʜᴇ Rɪɢʜᴛs Tᴏ Dᴏ Tʜɪs !", show_alert=True)
            return
        title = query.message.chat.title 
        print("OPEN grp_id =", grp_id)
        print("ACTIVE grp_id =", await active_connection(int(query.from_user.id)))
        settings = await get_settings(int(grp_id))
#        settings = await get_settings(grp_id)
        print("OPEN SETTINGS =", settings)
        print("CACHE SETTINGS =", temp.SETTINGS.get(grp_id))
        print("OPEN SETTINGS BOTPM =", settings["botpm"])
        print("TYPE grp_id =", type(grp_id))
        print("VALUE grp_id =", grp_id)
        if settings is not None:
            buttons = [
                [
                    InlineKeyboardButton('𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫✅' if settings["auto_ffilter"] else '𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["button"] else '𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐃𝐞𝐥𝐞𝐭𝐞✅' if settings["auto_delete"] else '𝐃𝐞𝐥𝐞𝐭𝐞❌',
                                         callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝✅' if settings["botpm"] else '𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝❌',
                                         callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐭𝐞𝐫✅' if settings["gfilter"] else '𝐅𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#gfilter#{settings["gfilter"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐈𝐦𝐝𝐛✅' if settings["imdb"] else '𝐈𝐦𝐝𝐛❌',
                                         callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ✅' if settings["landscape_mode"] else '𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ❌',
                                         callback_data=f'setgs#landscape_mode#{settings["landscape_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬✅' if settings["max_btn"] else '𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬❌',
                                         callback_data=f'setgs#max_btn#{settings["max_btn"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["newmod"] else '𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#newmod#{settings["newmod"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐌??𝐝✅' if settings["spellcheck"] else '𝐏𝐫𝐨 𝐌𝐨𝐝❌',
                                         callback_data=f'setgs#spellcheck#{settings["spellcheck"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧✅' if settings["file_secure"] else '𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧❌',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭✅' if settings["mod_mode"] else '𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭❌',
                                         callback_data=f'setgs#mod_mode#{settings["mod_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤✅' if settings["is_shortlink"] else '𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤❌',
                                         callback_data=f'setgs#is_shortlink#{settings["is_shortlink"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤✅' if settings["spell_check"] else '𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤❌',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡✅' if settings["telegraph"] else '𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡❌',
                                         callback_data=f'setgs#telegraph#{settings["telegraph"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐖𝐞𝐥𝐜𝐨𝐦𝐞✅' if settings["welcome"] else '𝐖𝐞𝐥𝐜𝐨𝐦𝐞❌',
                                         callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML
            )
            await query.message.edit_reply_markup(reply_markup)
        
    elif query.data.startswith("opnsetpm"):
        ident, grp_id = query.data.split("#")
        userid = query.from_user.id if query.from_user else None
        st = await client.get_chat_member(grp_id, userid)
        if (
                st.status != enums.ChatMemberStatus.ADMINISTRATOR
                and st.status != enums.ChatMemberStatus.OWNER
                and int(userid) not in ADMINS
        ):
            await query.answer("Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Tʜᴇ Rɪɢʜᴛs Tᴏ Dᴏ Tʜɪs !", show_alert=True)
            return
        title = query.message.chat.title
        settings = await get_settings(grp_id)
        btn2 = [[
                 InlineKeyboardButton("Cʜᴇᴄᴋ PM", url=f"t.me/{temp.U_NAME}")
               ]]
        reply_markup = InlineKeyboardMarkup(btn2)
        await query.message.edit_text(f"<b>Yᴏᴜʀ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ ғᴏʀ {title} ʜᴀs ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʏᴏᴜʀ PM</b>")
        await query.message.edit_reply_markup(reply_markup)
        if settings is not None:
            buttons = [
                [
                    InlineKeyboardButton('𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫✅' if settings["auto_ffilter"] else '𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["button"] else '𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐃𝐞𝐥𝐞𝐭𝐞✅' if settings["auto_delete"] else '𝐃𝐞𝐥𝐞𝐭𝐞❌',
                                         callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝✅' if settings["botpm"] else '𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝❌',
                                         callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐭𝐞𝐫✅' if settings["gfilter"] else '𝐅𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#gfilter#{settings["gfilter"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐈𝐦𝐝𝐛✅' if settings["imdb"] else '𝐈𝐦𝐝𝐛❌',
                                         callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ✅' if settings["landscape_mode"] else '𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ❌',
                                         callback_data=f'setgs#landscape_mode#{settings["landscape_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬✅' if settings["max_btn"] else '𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬❌',
                                         callback_data=f'setgs#max_btn#{settings["max_btn"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["newmod"] else '𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#newmod#{settings["newmod"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐌𝐨𝐝✅' if settings["spellcheck"] else '𝐏𝐫𝐨 𝐌𝐨𝐝❌',
                                         callback_data=f'setgs#spellcheck#{settings["spellcheck"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧✅' if settings["file_secure"] else '𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧❌',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭✅' if settings["mod_mode"] else '𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭❌',
                                         callback_data=f'setgs#mod_mode#{settings["mod_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤✅' if settings["is_shortlink"] else '𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤❌',
                                         callback_data=f'setgs#is_shortlink#{settings["is_shortlink"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤✅' if settings["spell_check"] else '𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤❌',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡✅' if settings["telegraph"] else '𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡❌',
                                         callback_data=f'setgs#telegraph#{settings["telegraph"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐖𝐞𝐥𝐜𝐨𝐦𝐞✅' if settings["welcome"] else '𝐖𝐞𝐥𝐜𝐨𝐦𝐞❌',
                                         callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await client.send_message(
                chat_id=userid,
                text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML,
                reply_to_message_id=query.message.id
            )

    elif query.data.startswith("setting"):
        userid = query.from_user.id if query.from_user else None
        if not userid:
            return await message.reply(f"Yᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. Usᴇ /connect {query.message.chat.id} ɪɴ PM")
        chat_type = query.message.chat.type

        if chat_type == enums.ChatType.PRIVATE:
            grpid = await active_connection(int(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = query.message.chat.title
                except:
                    await query.message.reply_text("Mᴀᴋᴇ sᴜʀᴇ I'ᴍ ᴘʀᴇsᴇɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ !", quote=True)
                    return
            else:
                await query.message.reply_text("I'ᴍ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘs !", quote=True)
                return

        elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return


        st = await client.get_chat_member(grp_id, userid)
        if (
                st.status != enums.ChatMemberStatus.ADMINISTRATOR
                and st.status != enums.ChatMemberStatus.OWNER
                and str(userid) not in ADMINS
        ):
            return
    
        settings = await get_settings(grp_id)

        try:
            if settings['max_btn']:
                settings = await get_settings(grp_id)
        except KeyError:
            await save_group_settings(grp_id, 'max_btn', False)
            settings = await get_settings(grp_id)
        if 'is_shortlink' not in settings.keys():
            await save_group_settings(grp_id, 'is_shortlink', False)
        else:
            pass
        if settings is not None:
            buttons = [
                [
                    InlineKeyboardButton('𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫✅' if settings["auto_ffilter"] else '𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["button"] else '𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐃𝐞𝐥𝐞𝐭𝐞✅' if settings["auto_delete"] else '𝐃𝐞𝐥𝐞𝐭𝐞❌',
                                         callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝✅' if settings["botpm"] else '𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝❌',
                                         callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐅𝐢𝐥𝐭𝐞𝐫✅' if settings["gfilter"] else '𝐅𝐢𝐥𝐭𝐞𝐫❌',
                                         callback_data=f'setgs#gfilter#{settings["gfilter"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐈𝐦𝐝𝐛✅' if settings["imdb"] else '𝐈𝐦𝐝𝐛❌',
                                         callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ✅' if settings["landscape_mode"] else '𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ❌',
                                         callback_data=f'setgs#landscape_mode#{settings["landscape_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬✅' if settings["max_btn"] else '𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬❌',
                                         callback_data=f'setgs#max_btn#{settings["max_btn"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["newmod"] else '𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                         callback_data=f'setgs#newmod#{settings["newmod"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨 𝐌𝐨𝐝✅' if settings["spellcheck"] else '𝐏𝐫𝐨 𝐌𝐨𝐝❌',
                                         callback_data=f'setgs#spellcheck#{settings["spellcheck"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧✅' if settings["file_secure"] else '𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧❌',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭✅' if settings["mod_mode"] else '𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭❌',
                                         callback_data=f'setgs#mod_mode#{settings["mod_mode"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤✅' if settings["is_shortlink"] else '𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤❌',
                                         callback_data=f'setgs#is_shortlink#{settings["is_shortlink"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤✅' if settings["spell_check"] else '𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤❌',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                    InlineKeyboardButton('𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡✅' if settings["telegraph"] else '𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡❌',
                                         callback_data=f'setgs#telegraph#{settings["telegraph"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('𝐖𝐞𝐥𝐜𝐨𝐦𝐞✅' if settings["welcome"] else '𝐖𝐞𝐥𝐜𝐨𝐦𝐞❌',
                                         callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
                ]
            ]

            reply_markup = InlineKeyboardMarkup(buttons)
            if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                m=await query.message.reply_text(
                    text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
                    reply_markup=reply_markup,
                    disable_web_page_preview=True,
                    parse_mode=enums.ParseMode.HTML,
                )
                await asyncio.sleep(60)
                await m.delete()


    elif query.data.startswith("show_option"):
        _, from_user, group_id, message_id, movie = query.data.split("#", 4)
        if query.from_user.id not in ADMINS:
            return await query.answer(
                "Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜɪs !",
                show_alert=True
            )
        buttons = [
            [
                InlineKeyboardButton(
                    "Uᴘʟᴏᴀᴅᴇᴅ",
                    callback_data=f"uploaded#{from_user}#{group_id}#{message_id}#{movie}"                
                )
            ]
        ]
        await query.message.edit_reply_markup(
            InlineKeyboardMarkup(buttons)
        )
        await query.answer("Hᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴏᴘᴛɪᴏɴs !")
           
    elif query.data.startswith("uploaded"):
        _, from_user, group_id, movie = query.data.split("#", 3)
        if query.from_user.id not in ADMINS:
            return await query.answer(
                "Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs!",
                show_alert=True
            )
        request_user = await client.get_users(int(from_user))
        imdb = await get_poster(movie) if IMDB else None
        text = movie
        poster = None
        if imdb:
            poster = imdb.get("poster")
        m = query.message
        if poster and poster != "N/A":
            try:
                m = await client.edit_message_media(
                    chat_id=query.message.chat.id,
                    message_id=query.message.id,
                    media=InputMediaPhoto(media=poster)
                )
            except Exception as e:
                print("POSTER ERROR :", e)
                m = query.message
        buttons = [[
            InlineKeyboardButton(
                "✅ Uᴘʟᴏᴀᴅᴇᴅ ✅",
                url="https://t.me/nasrani_update"
            )
        ],[
            InlineKeyboardButton(
                "⚠️ Close ⚠️",
                callback_data="close_data"
            )
        ]]
        await query.message.edit_text(
            text=(
                f"<b>Hello {request_user.mention}\n\n"
                f"🎬 <code>{text}</code>\n\n"
                f"Movie Uploaded Successfully ✅</b>"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )
        k = await query.message.reply_text(
            text=(
                f"<b>Hello {request_user.mention}\n\n"
                f"🎬 <code>{text}</code>\n\n"
                f"Movie Uploaded Successfully ✅</b>"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML
        )
        if getattr(m, "photo", None):
            try:
                name_format = "okda"
                image = await m.download(
                    file_name=f"{name_format}.jpg"
                )
                im = Image.open(image).convert("RGB")
                im.save(f"{name_format}.webp", "webp")
                sticker = f"{name_format}.webp"
                sticker_btn = [[
                    InlineKeyboardButton(
                        "✅ Uᴘʟᴏᴀᴅᴇᴅ ✅",
                        url="https://t.me/nasrani_update"
                    )
                ],[
                    InlineKeyboardButton(
                        "⚠️ Delete Now ⚠️",
                        callback_data="dl"
                    )
                ]]
                await client.send_sticker(
                    chat_id=UPLOAD_CHANNEL,
                    sticker=sticker,
                    reply_markup=InlineKeyboardMarkup(sticker_btn)
                )
            except Exception as e:
                print("STICKER ERROR :", e)
        try:
            await asyncio.sleep(60)
            await m.delete()
        except:
            pass
        try:
            await asyncio.sleep(60)
            await k.delete()
        except:
            pass
    

    elif query.data.startswith("alalert"):
        ident, from_user = query.data.split("#")
        if int(query.from_user.id) == int(from_user):
            user = await client.get_users(from_user)
            await query.answer(f"Hᴇʏ {user.first_name}, Yᴏᴜʀ Rᴇᴏ̨ᴜᴇsᴛ ɪs Aʟʀᴇᴀᴅʏ Aᴠᴀɪʟᴀʙʟᴇ !", show_alert=True)
        else:
            await query.answer("Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴀɴᴛ ʀɪɢᴛs ᴛᴏ ᴅᴏ ᴛʜɪs !", show_alert=True)

    elif query.data.startswith("upalert"):
        ident, from_user = query.data.split("#")
        if int(query.from_user.id) == int(from_user):
            user = await client.get_users(from_user)
            await query.answer(f"Hᴇʏ {user.first_name}, Yᴏᴜʀ Rᴇᴏ̨ᴜᴇsᴛ ɪs Uᴘʟᴏᴀᴅᴇᴅ !", show_alert=True)
        else:
            await query.answer("Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴀɴᴛ ʀɪɢᴛs ᴛᴏ ᴅᴏ ᴛʜɪs !", show_alert=True)
        
    elif query.data.startswith("unalert"):
        ident, from_user = query.data.split("#")
        if int(query.from_user.id) == int(from_user):
            user = await client.get_users(from_user)
            await query.answer(f"Hᴇʏ {user.first_name}, Yᴏᴜʀ Rᴇᴏ̨ᴜᴇsᴛ ɪs Uɴᴀᴠᴀɪʟᴀʙʟᴇ !", show_alert=True)
        else:
            await query.answer("Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴀɴᴛ ʀɪɢᴛs ᴛᴏ ᴅᴏ ᴛʜɪs !", show_alert=True)



    elif query.data.startswith("get_afiles|"):

        keyword = unquote(query.data.split("|", 1)[1])

        col = mydb["global_filters"]
        data = col.find_one({"text": keyword})
        if not data or not data.get("files"):
            await query.answer("❌ No files found!", show_alert=True)
            return

    # Send PM files...

        # Check if PM started
        try:
                await client.send_message(
                        query.from_user.id,
                        f"📥 Sending files for: {keyword}"
                )
        except Exception:
                await query.answer("⚠️ Start the bot in PM first!", show_alert=True)
                return

        sent = 0
        for f in data["files"]:
                try:
                        print("FILE ID =", f["file_id"])
                        # First try cached media
                        msg = await client.send_cached_media(
                                chat_id=query.from_user.id,
                                file_id=f["file_id"],
                                caption=f.get("file_name", "")
                        )
                        print("SENT OK =", msg.id)
                        sent += 1
                        await asyncio.sleep(0.5)

                except Exception as e:
                        print("CACHED MEDIA FAILED, TRYING send_document:", repr(e))
                        try:
                                # Fallback to send_document
                                msg = await client.send_document(
                                        chat_id=query.from_user.id,
                                        document=f["file_id"],
                                        caption=f.get("file_name", "")
                                )
                                print("SENT OK (document) =", msg.id)
                                sent += 1
                                await asyncio.sleep(0.5)
                        except Exception as e2:
                                print("SEND FAILED:", repr(e2))

        await query.answer(f"✅ {sent} files sent to PM!", show_alert=True)


    elif query.data == "done":
#        search = query.message.text
#        imdb = await get_poster(search) if IMDB else None
#        await query.answer(f"🏷 𝐓𝐢𝐭𝐥𝐞 : {search} \n 📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {imdb.get('year')} \n 📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {imdb.get('runtime')} \n ☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {imdb.get('languages')} \n\n 🍿{query.message.chat.title}??", show_alert=True)

        if query.from_user.id in ADMINS:
            buttons = [[
                InlineKeyboardButton('✅ 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 ✅', url="https://t.me/nasrani_update")                            
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            k=await query.message.edit_text(
                text=f"✅ 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
            await query.answer(MSG_ALRT)



       
    elif query.data == "source":
        await query.answer(script.SOURCE, show_alert=True)    
    
    elif query.data == "reqinfo":
        await query.answer(text=script.REQINFO, show_alert=True)

    elif query.data == "minfo":
        await query.answer(text=script.MINFO, show_alert=True)

    elif query.data == "sinfo":
        await query.answer(text=script.SINFO, show_alert=True)
      

    elif query.data == "eng":
        reporter = str(query.message.from_user.id)
        mv_rqst = query.message.reply_to_message.text
        buttons = [[
#            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐒𝐞𝐚𝐫𝐜𝐡 𝐆𝐨𝐨𝐠𝐥𝐞{random.choice(RUN_STRINGS)}', url=f"https://www.google.com/search?q={mv_rqst}")
#        ],[
            InlineKeyboardButton("🔁 𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲 🔁", callback_data=f'show_option#{reporter}')
        ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        k=await query.message.edit_text(
            text=script.ENG.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
        await asyncio.sleep(60)
        await k.delete()

    elif query.data == "mal":
        reporter = str(query.message.from_user.id)
        mv_rqst = query.message.reply_to_message.text
        buttons = [[
#            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐒𝐞𝐚𝐫𝐜𝐡 𝐆𝐨𝐨𝐠𝐥𝐞{random.choice(RUN_STRINGS)}', url=f"https://www.google.com/search?q={mv_rqst}")
#        ],[
            InlineKeyboardButton("🔁 𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲 🔁", callback_data=f'show_option#{reporter}')            
        ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        k=await query.message.edit_text(
            text=script.MAL.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
        await asyncio.sleep(60)
        await k.delete()
       
    elif query.data == "hin":
        reporter = str(query.message.from_user.id)
        mv_rqst = query.message.reply_to_message.text
        buttons = [[
#            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐒𝐞𝐚𝐫𝐜𝐡 𝐆𝐨𝐨𝐠𝐥𝐞{random.choice(RUN_STRINGS)}', url=f"https://www.google.com/search?q={mv_rqst}")
#        ],[
            InlineKeyboardButton("🔁 𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲 🔁", callback_data=f'show_option#{reporter}')            
        ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        k=await query.message.edit_text(
            text=script.HIN.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
        await asyncio.sleep(60)
        await k.delete()

    elif query.data == "tam":
        reporter = str(query.message.from_user.id)
        mv_rqst = query.message.reply_to_message.text
        buttons = [[
#            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐒𝐞𝐚𝐫𝐜𝐡 𝐆𝐨𝐨𝐠𝐥𝐞{random.choice(RUN_STRINGS)}', url=f"https://www.google.com/search?q={mv_rqst}")
#        ],[
            InlineKeyboardButton("🔁 𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲 🔁", callback_data=f'show_option#{reporter}')            
        ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        k=await query.message.edit_text(
            text=script.TAM.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
        await asyncio.sleep(60)
        await k.delete()

    
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩{random.choice(RUN_STRINGS)}', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ], [                    
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐇𝐞𝐥𝐩{random.choice(RUN_STRINGS)}', callback_data='help'),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬{random.choice(RUN_STRINGS)}', callback_data='helps')     
        ], [
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐋𝐞𝐭??𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 {random.choice(RUN_STRINGS)}', callback_data="topsearch")
        ], [      
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐈𝐧𝐥𝐢𝐧𝐞{random.choice(RUN_STRINGS)}', switch_inline_query_current_chat=''),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐛𝐨𝐮𝐭{random.choice(RUN_STRINGS)}', callback_data='about')                      
        ], [
            InlineKeyboardButton('𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ✅' if (await get_settings(query.message.from_user.id)).get("botpm", False) else '𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ❌', callback_data="toggle_botpm")      
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer(MSG_ALRT)
    
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Sᴛᴀᴛᴜs', callback_data='stats')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=GRP_LNK),
            InlineKeyboardButton('Sᴏᴜʀᴄᴇ Cᴏᴅᴇ', callback_data='source')
        ],[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close_data')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='filters'),
            InlineKeyboardButton('Bᴜᴛᴛᴏɴs', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='manuelfilter')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='filters')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='help')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('Aᴅᴍɪɴ', callback_data='admin')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
        
        
        


  
    elif query.data == "store_file":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='help')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FILE_STORE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='extra')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "year_stats":

        year_data = await get_year_wise_count()

        text = "<b>📅 Year Wise Files\n\n"

        for year in sorted(
            [y for y in year_data.keys() if y != "Others"],
            reverse=True
        ):
            text += f"★ {year} = <code>{year_data[year]}</code>\n"

        if "Others" in year_data:
            text += f"\n★ Others = <code>{year_data['Others']}</code>"
#        text += "</b>"

        buttons = [[
            InlineKeyboardButton("🔙 Back", callback_data="stats")
        ]]

        await query.message.edit_text(
            text,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )        
    elif query.data == "stats":
        buttons = [[
                InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='help'),
                InlineKeyboardButton('⟲ Rᴇғʀᴇsʜ', callback_data='rfrsh')
                ], [
                InlineKeyboardButton('📅 Year Wise Files', callback_data='year_stats')
        ]]
        await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)

        # Primary & Secondary DB files count
        totalp = await Media.count_documents({})
        totalsec = await Media2.count_documents({})

        duplicate_doc = await stats_col.find_one({"_id": "duplicate_files"})
        duplicate_count = duplicate_doc.get("count", 0) if duplicate_doc else 0

        total_index_files = totalp + totalsec + duplicate_count
        # Connected groups count
        connected_groups = 0
        if "mycol" in globals():
                for doc in mycol.find({}, {"group_details": 1}):
                        connected_groups += len(doc.get("group_details", []))

        # Users & chats
        users = await userdb.total_users_count()
        chats = await userdb.total_chat_count()

        # Primary DB stats
        stats = await clientDB.command('dbStats')
        used_dbSize = (stats['dataSize'] / (1024*1024)) + (stats['indexSize'] / (1024*1024))
        free_dbSize = 512 - used_dbSize

        # Secondary DB stats
        stats2 = await clientDB2.command('dbStats')
        used_dbSize2 = (stats2['dataSize'] / (1024*1024)) + (stats2['indexSize'] / (1024*1024))
        free_dbSize2 = 512 - used_dbSize2

        # Minnal Murali stats
        movie_requests = await userdb.get_movie_request_count()
        noresult_requests = await userdb.get_noresult_request_count()
        top_groups = await userdb.get_top_groups()
        year_data = await get_year_wise_count()

        year_text = ""

        for year in sorted(
            [y for y in year_data.keys() if y != "Others"],
            reverse=True
        ):
            year_text += f"{year} = {year_data[year]} files\n"

        if "Others" in year_data:
            year_text += f"Others = {year_data['Others']} files"

        # Top groups text
        if top_groups:
                group_text = "\n".join(
                        f"{i}. {grp.get('title', 'Unknown')}"
                        for i, grp in enumerate(top_groups, start=1)
                )
        else:
                group_text = "No groups found"

        # Edit message with stats
        await query.message.edit_text(
                script.STATUS_TXT.format(
                        totalp + totalsec,          # Total files from both DBs
                        connected_groups,           # Connected groups
                        users,                      # Total users
                        chats,                      # Total chats
                        totalp,                     # Primary files
                        round(used_dbSize, 2),      # Primary used storage
                        round(free_dbSize, 2),      # Primary free storage
                        totalsec,                   # Secondary files
                        round(used_dbSize2, 2),     # Secondary used storage
                        round(free_dbSize2, 2),     # Secondary free storage
                        total_index_files,          # Total indexed files including duplicates
                        movie_requests,             # Movie requests
                        noresult_requests,          # Failed requests
                        group_text                # Top active groups
#                        year_text
                ),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "rfrsh":
        await query.answer("Fetching MongoDB DataBase")

        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('⟲ Rᴇғʀᴇsʜ', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)

        # Primary & Secondary DB files count
        totalp = await Media.count_documents({})
        totalsec = await Media2.count_documents({})

        duplicate_doc = await stats_col.find_one({"_id": "duplicate_files"})
        duplicate_count = duplicate_doc.get("count", 0) if duplicate_doc else 0

        total_index_files = totalp + totalsec + duplicate_count
        # Connected groups count
        connected_groups = 0
        if "mycol" in globals():
            for doc in mycol.find({}, {"group_details": 1}):
                connected_groups += len(doc.get("group_details", []))

        # Users & chats
        users = await userdb.total_users_count()
        chats = await userdb.total_chat_count()

        # Primary DB stats
        stats = await clientDB.command('dbStats')
        used_dbSize = (stats['dataSize'] / (1024*1024)) + (stats['indexSize'] / (1024*1024))
        free_dbSize = 512 - used_dbSize

        # Secondary DB stats
        stats2 = await clientDB2.command('dbStats')
        used_dbSize2 = (stats2['dataSize'] / (1024*1024)) + (stats2['indexSize'] / (1024*1024))
        free_dbSize2 = 512 - used_dbSize2

        # Minnal Murali stats
        movie_requests = await userdb.get_movie_request_count()
        noresult_requests = await userdb.get_noresult_request_count()
        top_groups = await userdb.get_top_groups()
        year_data = await get_year_wise_count()

        year_text = ""

        for year in sorted(
            [y for y in year_data.keys() if y != "Others"],
            reverse=True
        ):
            year_text += f"{year} = {year_data[year]} files\n"

        if "Others" in year_data:
            year_text += f"Others = {year_data['Others']} files"

        # Top groups text
        if top_groups:
            group_text = "\n".join(
                f"{i}. {grp.get('title', 'Unknown')}"
                for i, grp in enumerate(top_groups, start=1)
            )
        else:
            group_text = "No groups found"

        # Edit message with stats
        try:
            await query.message.edit_text(
                script.STATUS_TXT.format(
                    totalp + totalsec,          # Total files from both DBs
                    connected_groups,           # Connected groups
                    users,                      # Total users
                    chats,                      # Total chats
                    totalp,                     # Primary files
                    round(used_dbSize, 2),      # Primary used storage
                    round(free_dbSize, 2),      # Primary free storage
                    totalsec,                   # Secondary files
                    round(used_dbSize2, 2),     # Secondary used storage
                    round(free_dbSize2, 2),     # Secondary free storage
                    total_index_files,          # Total indexed files including duplicates
                    movie_requests,             # Movie requests
                    noresult_requests,          # Failed requests
                    group_text
#                    year_text               # Top active groups
                ),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
        except MessageNotModified:
            pass
            
            
            
    elif query.data == "owner_info":
            btn = [[
                    InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data="start"),
                    InlineKeyboardButton("Cᴏɴᴛᴀᴄᴛ", url="t.me/creatorbeatz")
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=(script.OWNER_INFO),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
                
    elif query.data.startswith("modpm#"):

        _, ident, file_id = query.data.split("#", 2)

        files_ = await get_file_details(file_id)

        if not files_:
            return await query.answer(
                "File not found",
                show_alert=True
            )

        files = files_[0]

        f_caption = files.caption
        title = files.file_name
        size = get_size(files.file_size)

        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(
                    file_name='' if title is None else title,
                    file_size='' if size is None else size,
                    file_caption='' if f_caption is None else f_caption
                )
            except Exception:
                pass

        if f_caption is None:
            f_caption = f"{files.file_name}"

        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption
        )

        return await query.answer(
            "Check PM, I have sent files in PM",
            show_alert=True
        ) 


    elif query.data.startswith("modch#"):

        _, ident, file_id = query.data.split("#", 2)

        files_ = await get_file_details(file_id)

        if not files_:
            return await query.answer(
                "File not found",
                show_alert=True
            )

        files = files_[0]

        title = files.file_name
        size = get_size(files.file_size)

        content = ""

        if query.message.reply_to_message:
            content = query.message.reply_to_message.text or ""
#        content = query.message.reply_to_message.text

        print("STEP 2")

#        imdb = await get_poster(content) if IMDB else None
        imdb = await get_poster(content) if IMDB and content else None
        poster = imdb.get("poster") if imdb else random.choice(PICS)

        try:
            vote_data = await get_file_votes(file_id)
        except:
            vote_data = {}

        like_count = vote_data.get("like", 0)

        # 🟢 ചാനലിലേക്ക് ഫയൽ സെൻഡ് ചെയ്യുന്നു
        file_send = await client.send_cached_media(
            chat_id=FILE_CHANNEL,
            file_id=file_id,
            caption=script.CHANNEL_CAP.format(
                query.from_user.mention,
                title,
                query.message.chat.title
            ),
            protect_content=True if ident == "filep" else False
        )

        # 📺 [JUSTRUNMY.APP STREAM LOGIC]
        # നിങ്ങളുടെ JRMA ഡൊമെയ്ൻ വെച്ച് സ്ട്രീം ലിങ്ക് ജനറേറ്റ് ചെയ്യുന്നു
        import urllib.parse
        poster_encoded = urllib.parse.quote(poster)
        JRMA_URL = "https://nasranibot-c53.e.jrnm.app"
        stream_link = f"{JRMA_URL}/watch/{file_id}"

        # 📝 [CUSTOM CAPTION - WITH SPACES]
        # യൂസർ നെയിം കഴിഞ്ഞൊരു സ്പേസും താഴെ ഫയൽ വിവരങ്ങളും നൽകുന്നു
        custom_caption = (
            f"👤 <b>User Name:</b> {query.from_user.mention}\n\n"
            f"📂 <b>File Name:</b> <code>{title}</code>\n"
            f"⚖️ <b>File Size:</b> {size}\n\n"
            f"✨ <i>Enjoy your movie!</i>"
        )

        # 🚀 യൂസർക്ക് പോസ്റ്ററും ബട്ടണുകളും അയക്കുന്നു
        await query.message.reply_text(
#            photo=poster,
            text=custom_caption, # 💡 നമ്മൾ മുകളിൽ സെറ്റ് ചെയ്ത പുതിയ ക്യാപ്ഷൻ
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        # 1. സ്ട്രീം ബട്ടൺ (ആദ്യം കാണാൻ)
                        InlineKeyboardButton(
                            "📺 Watch Online / Stream 📺",
                            url=stream_link
                        )
                    ],
                    [
                        # 2. ഡൗൺലോഡ് ബട്ടൺ (തൊട്ടുതാഴെ)
                        InlineKeyboardButton(
                            "📥 Fast Download Link 📥",
                            url=file_send.link
                        )
                    ],
                    [
                        # 3. ഹെൽപ്പ് ബട്ടൺ
                        InlineKeyboardButton(
                            "⚠️ 𝐂𝐚𝐧't 𝐀𝐜𝐜𝐞𝐬𝐬 ❓ 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 ⚠️",
                            url=FILE_FORWARD
                        )
                    ]
                ]
            )
        )

        return await query.answer()


    elif query.data == "sendmarked":
        user_id = query.from_user.id
        files = MARKED_FILES.get(user_id, [])

        if not files:
            return await query.answer("❌ No marked files selected!", show_alert=True)

        await query.answer("Processing your marked files...", show_alert=False)
        bot_username = (await client.get_me()).username
        
        try:
            share_link = f"https://t.me/{bot_username}?start=M3-{user_id}"
            
            message_text = (
                f"✨ **Hᴇʏ {query.from_user.mention}, Yᴏᴜʀ Mᴀʀᴋᴇᴅ Fɪʟᴇs Aʀᴇ Rᴇᴀᴅʏ!**\n\n"
                f"📦 **Total Files:** `{len(files)}`\n\n"
                f"👇 **Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Gᴇᴛ Fɪʟᴇs**"
            )
            
            btn_message = await query.message.reply_text(
                text=message_text,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📥 GᴇT Mᴀʀᴋᴇᴅ Fɪʟᴇs 📥", url=share_link)]
                ]),
                disable_web_page_preview=True
            )
            
            async def auto_delete_btn(msg):
                await asyncio.sleep(180)
                try: await msg.delete()
                except: pass
            asyncio.create_task(auto_delete_btn(btn_message))

            # ഗ്രൂപ്പിലെ ബട്ടണുകൾ മാത്രം ❌ ആക്കുന്നു
            current_buttons = query.message.reply_markup.inline_keyboard
            reset_buttons = []
            for row in current_buttons:
                new_row = []
                for btn in row:
                    if btn.text.startswith("✅"):
                        new_text = btn.text.replace("✅", "❌")
                        new_row.append(InlineKeyboardButton(text=new_text, callback_data=btn.callback_data))
                    else:
                        new_row.append(btn)
                reset_buttons.append(new_row)
            
            try:
                await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(reset_buttons))
            except:
                pass

            return
            
        except Exception as e:
            print(f"Error: {e}")
            return
 

     
    elif query.data == "sendmarkedd":

        user_id = query.from_user.id

        files = MARKED_FILES.get(user_id, [])

        if not files:
            return await query.answer(
                "❌ No marked files",
                show_alert=True
            )

        sent = 0

        for file_id in files:

            try:
                files_ = await get_file_details(file_id)

                if not files_:
                    continue

                file = files_[0]

                title = file.file_name
                size = get_size(file.file_size)
                f_caption = file.caption

                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption = CUSTOM_FILE_CAPTION.format(
                            file_name='' if title is None else title,
                            file_size='' if size is None else size,
                            file_caption='' if f_caption is None else f_caption
                        )
                    except Exception as e:
                        logger.exception(e)

                if f_caption is None:
                    f_caption = file.file_name

                await client.send_cached_media(
                    chat_id=user_id,
                    file_id=file.file_id,
                    caption=f_caption
                )

                sent += 1

            except Exception as e:
                print(e)

        MARKED_FILES[user_id] = []

        await query.answer(
            f"✅ Sent {sent} files",
            show_alert=True
        )
        
        



        
        
    elif query.data == "markmode":
        key = f"{query.message.chat.id}-{query.message.reply_to_message.id}"

        if REQUEST_USERS.get(key) != query.from_user.id:
            return await query.answer(
                "❌ This is not for you",
                show_alert=True
            )     

        user_id = query.from_user.id
        buttons = query.message.reply_markup.inline_keyboard
        new_buttons = []
        file_buttons = []
        control_buttons = []
        telegraph_row = None 

        enabled = user_id in MARK_MODE_USERS

        if enabled:
            MARK_MODE_USERS.remove(user_id)
        else:
            MARK_MODE_USERS.append(user_id)

        settings = await get_settings(query.message.chat.id)
        is_newmod = settings.get("newmod", False) # New Mod ഓൺ ആണോ എന്ന് നോക്കുന്നു

        for row in buttons:
            is_control_row = False
            for btn in row:
                if b_data := btn.callback_data:
                    if b_data.startswith("telegraph#"):
                        telegraph_row = row
                        is_control_row = True
                        break
                    
                    if any(x in b_data for x in ["markmode", "sendmarked", "topsearch", "next", "pages"]):
                        is_control_row = True
                        break
            
            if is_control_row:
                if row not in control_buttons:
                    control_buttons.append(row)
            else:
                for btn in row:
                    if btn.callback_data and not any(x in btn.callback_data for x in ["markmode", "sendmarked", "topsearch", "telegraph", "next", "pages"]):
                        file_buttons.append(btn)

        # 1️⃣ [TOP MENU]
        if telegraph_row:
            new_buttons.append(telegraph_row)

        # 2️⃣ [SECOND MENU]
        if enabled:
            new_buttons.append([
                InlineKeyboardButton("⭐𝐌𝐚𝐫𝐤𝐦𝐨𝐝⭐", callback_data="markmode"),
                InlineKeyboardButton("📂𝐋𝐞𝐭𝐞𝐬𝐭 𝐅𝐢𝐥𝐞𝐬📂", callback_data=f"topsearch#{key}")
            ])
        else:
            new_buttons.append([
                InlineKeyboardButton("❌𝐔𝐧𝐦𝐚𝐫𝐤❌", callback_data="markmode"),
                InlineKeyboardButton("📦𝐒𝐞𝐧𝐝 𝐌𝐚𝐫𝐤📦", callback_data="sendmarked")
            ])

        # 3️⃣ [FILE BUTTONS]
        processed_file_buttons = []
        for btn in file_buttons:
            file_id = btn.callback_data.split("#")[-1] if "#" in btn.callback_data else btn.callback_data.split("_")[-1]
            
            # പഴയ ടെക്സ്റ്റിൽ നിന്ന് ചിഹ്നങ്ങളും ഇമോജികളും ക്ലിയർ ചെയ്ത് ഫ്രഷ് ആക്കുന്നു
            text = btn.text.replace("❌ ", "").replace("✅ ", "")
            for emo in RUN_STRINGS:
                text = text.replace(emo, "")
            text = text.strip()

            if enabled:
                # 🟢 [FIX] New Mod ആണെങ്കിൽ ഇമോജി ഒഴിവാക്കും, Normal Mode ആണെങ്കിൽ മാത്രം ഇമോജി വെക്കും!
                if is_newmod:
                    btn_text = text
                else:
                    EMOJI = random.choice(RUN_STRINGS)
                    btn_text = f"{EMOJI}{text}"

                processed_file_buttons.append(
                    InlineKeyboardButton(
                        text=btn_text,
                        callback_data=f"file#{file_id}"
                    )
                )
            else:
                # Mark Mode ഓൺ ചെയ്യുമ്പോൾ ഉള്ള ലോജിക്
                marked = (user_id in MARKED_FILES and file_id in MARKED_FILES[user_id])
                icon = "✅" if marked else "❌"
                processed_file_buttons.append(
                    InlineKeyboardButton(
                        text=f"{icon} {text}",
                        callback_data=f"mark#{file_id}"
                    )
                )

        if is_newmod:
            row = []
            for b in processed_file_buttons:
                row.append(b)
                if len(row) == 4: 
                    new_buttons.append(row)
                    row = []
            if row:
                new_buttons.append(row)
        else:
            for b in processed_file_buttons:
                new_buttons.append([b])

        # 4️⃣ [BOTTOM MENU]
        for row in control_buttons:
            if any(b.callback_data in ["markmode", "sendmarked"] or (b.callback_data and b.callback_data.startswith("topsearch")) or (b.callback_data and b.callback_data.startswith("telegraph")) for b in row):
                continue
            new_buttons.append(row)

        back_key = None
        for row in new_buttons:
            for b in row:
                if b.callback_data and b.callback_data.startswith("telegraph#"):
                    back_key = b.callback_data.split("#", 1)[1]
                    break
            if back_key:
                break

        if back_key:
            temp.BACK_BUTTONS[back_key] = new_buttons

        await query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(new_buttons)
        )

        if enabled:
            await query.answer("❌ Mark Mode Disabled")
        else:
            await query.answer("✅ Mark Mode Enabled")








    elif query.data.startswith("mark#"):
        key = f"{query.message.chat.id}-{query.message.reply_to_message.id}"

        if REQUEST_USERS.get(key) != query.from_user.id:
            return await query.answer(
                "❌ This is not for you",
                show_alert=True
            )

        await query.answer("✅ Updated", show_alert=False)

        _, file_id = query.data.split("#")
        user_id = query.from_user.id

        if user_id not in MARKED_FILES:
            MARKED_FILES[user_id] = []

        buttons = query.message.reply_markup.inline_keyboard
        changed = False

        # ഇതിൽ ബട്ടൺ ലേഔട്ട് മാറില്ല, വെറും ഐക്കൺ (✅/❌) മാത്രം മാറും
        for row in buttons:
            for btn in row:
                if btn.callback_data == f"mark#{file_id}":
                    if file_id in MARKED_FILES[user_id]:
                        MARKED_FILES[user_id].remove(file_id)
                        if "✅" in btn.text:
                            btn.text = btn.text.replace("✅", "❌", 1)
                    else:
                        MARKED_FILES[user_id].append(file_id)
                        if "❌" in btn.text:
                            btn.text = btn.text.replace("❌", "✅", 1)

                    changed = True
                    break
            if changed:
                break

        if changed:
            try:
                await query.message.edit_reply_markup(
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                
                back_key = None
                for row in buttons:
                    for b in row:
                        if b.callback_data and b.callback_data.startswith("telegraph#"):
                            back_key = b.callback_data.split("#", 1)[1]
                            break
                    if back_key:
                        break

                if back_key:
                    temp.BACK_BUTTONS[back_key] = buttons                

            except MessageNotModified:
                pass
            except Exception:
                pass
        
        
    elif query.data.startswith("normalmode#"):

        _, key = query.data.split("#")

        buttons = []

        for file in files:

            file_name = ' '.join(
                filter(
                    lambda x: not x.startswith('[')
                    and not x.startswith('@')
                    and not x.startswith('www.'),
                    file.file_name.split()
                )
            )

            buttons.append([
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file_name}",
                    callback_data=f"{pre}#{file.file_id}"
                )
            ])

        buttons.insert(0, [
            InlineKeyboardButton("⭐𝐌𝐚𝐫𝐤𝐦𝐨𝐝⭐", callback_data=f"markmode#{key}"),
            InlineKeyboardButton("📥𝐒𝐞𝐧𝐝 𝐌𝐚𝐫𝐤📥", callback_data=f"sendmarked#{key}")
        ])

        await query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )


    elif query.data.startswith("topsearch#"):

        key = f"{query.message.chat.id}-{query.message.reply_to_message.id}"

        if REQUEST_USERS.get(key) != query.from_user.id:
            return await query.answer(
                "❌ This is not for you",
                show_alert=True
            )    	

    	
        msg = query.message

#        key = query.data.split("#", 1)[1]

#        allowed_user = None

#        if query.message.chat.type in ["group", "supergroup"]:
        	
#            allowed_user = REQUEST_USERS.get(key)

#        if allowed_user and allowed_user != query.from_user.id:

#            return await query.answer(
#                "❌ This is not for you",
#                show_alert=True
#            )

        # Force Subscribe
        if AUTH_CHANNEL and not await is_subscribe(client, query.from_user.id):
            try:
                invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
            except:
                return await query.answer("Channel error", show_alert=True)

            btn = [
                [InlineKeyboardButton("❆ 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ❆", url=invite_link.invite_link)],
                [InlineKeyboardButton("🔄 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧", callback_data="topsearch")]
            ]

            return await query.message.edit_text(
                f"👋 Hello {query.from_user.mention}\n\n"
                f"You must join our channel to view last indexed files.",
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.HTML
            )

        files = await get_last_files(100)

        if not files:
            return await query.answer("No files found", show_alert=True)

        username = (
            f"@{query.from_user.username}"
            if query.from_user and query.from_user.username
            else query.from_user.mention
        )

        page_url = await create_telegraph_page(
            username=username,
            search="Last Indexed Files",
            files=files,
            settings={"imdb": False}
        )

        back_key = f"top_{msg.chat.id}_{query.from_user.id}"

        temp.BACK_DATA[back_key] = {
            "photo": msg.photo.file_id if msg.photo else None,
            "caption": msg.caption,
            "buttons": msg.reply_markup.inline_keyboard if msg.reply_markup else None
        }
        await query.message.edit_reply_markup(
            InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🗂️𝐎𝐩𝐞𝐧🗂️",
                        url=page_url
                    )
                ],
                [
                    InlineKeyboardButton(
                        "◀️𝐁𝐚𝐜𝐤▶️",
                        callback_data=f"back_top#{back_key}"
                    )
                ]
            ])
        )


#pm
    elif query.data == "topsearch":
    # PM /start logic
    	
        msg = query.message

        "topsearch".split("#", 1)
        # Force Subscribe
        if AUTH_CHANNEL and not await is_subscribe(client, query.from_user.id):
            try:
                invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
            except:
                return await query.answer("Channel error", show_alert=True)

            btn = [
                [InlineKeyboardButton("❆ Join Channel ❆", url=invite_link.invite_link)],
                [InlineKeyboardButton("🔄 Try Again", callback_data="topsearch")]
            ]

            return await query.message.edit_text(
                f"👋 Hello {query.from_user.mention}\n\n"
                f"You must join our channel to view last indexed files.",
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.HTML
            )

        files = await get_last_files(100)

        if not files:
            return await query.answer("No files found", show_alert=True)

        username = (
            f"@{query.from_user.username}"
            if query.from_user and query.from_user.username
            else query.from_user.mention
        )

        page_url = await create_telegraph_page(
            username=username,
            search="Last Indexed Files",
            files=files,
            settings={"imdb": False}
        )

        back_key = f"top_{msg.chat.id}_{query.from_user.id}"

        temp.BACK_DATA[back_key] = {
            "photo": msg.photo.file_id if msg.photo else None,
            "caption": msg.caption,
            "buttons": msg.reply_markup.inline_keyboard if msg.reply_markup else None
        }

        await query.message.edit_reply_markup(
            InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🗂️𝐎𝐩𝐞𝐧🗂️",
                        url=page_url
                    )
                ],
                [
                    InlineKeyboardButton(
                        "◀️𝐁𝐚𝐜𝐤▶️",
                        callback_data=f"back_top#{back_key}"
                    )
                ]
            ])
        )
# pm




    elif query.data == "topsearchh":

    # 🔒 Force Subscribe Check
        if AUTH_CHANNEL and not await is_subscribe(client, query.from_user.id):
            try:
                invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
            except:
                return await query.answer("Channel error", show_alert=True)

            btn = [
                [InlineKeyboardButton("❆ Join Channel ❆", url=invite_link.invite_link)],
                [InlineKeyboardButton("🔄 Try Again", callback_data="topsearch")]
            ]

            return await query.message.edit_text(
                f"👋 𝐇𝐞𝐥𝐥𝐨 {query.from_user.mention},\n\n"
                f"You must join our channel to view last indexed files.",
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.HTML
            )

        # 📌 Save user → chat mapping unconditionally
        temp.SHORT[query.from_user.id] = query.message.chat.id

        # 📂 Fetch files
        files = await get_last_files(100)

        if not files:
            return await query.answer("No files found", show_alert=True)

        # 🌐 Telegraph Page create
        page_url = await create_telegraph_page(
            search="Last Indexed Files",
            files=files,
            settings={"imdb": False}
        )

        await query.message.edit_text(
            f"<b>📂 Last Indexed Files</b>\n\n"
            f"?? <a href='{page_url}'>Click here to open Telegraph Page</a>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=False
        )

        # ✅ Optional: PM user a direct link if botpm is enabled
        settings = await get_settings(query.from_user.id)
        if settings.get("botpm", False):
            try:
                await client.send_message(
                    query.from_user.id,
                    f"📂 Here is your last indexed files link:\n{page_url}"
                )
            except Exception:
                pass


    elif query.data == "topsearchs":

        # check subscriptions
        missing_channel = None
        for ch in AUTH_CHANNELS:
            if not await is_subscribe(client, query.from_user.id, ch):
                missing_channel = ch
                break

        if missing_channel:
            invite_link = await client.create_chat_invite_link(int(missing_channel))
            buttons = [
                [InlineKeyboardButton("📢 Join Channel 📢", url=invite_link.invite_link)],
                [InlineKeyboardButton("🔁 Request Again 🔁", callback_data="topsearch")]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                f"👋 𝐇𝐞𝐥𝐥𝐨 {query.from_user.mention},\n\nPlease join the channel to continue.",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
            await query.answer()
            return

        # proceed with last files if subscribed
        files = await get_last_files(10)

        if not files:
            return await query.answer("No files found", show_alert=True)

        text = "<b>📂 Last Indexed Files</b>\n\n"

        for i, file in enumerate(files, start=1):
            file_name = file.file_name[:40]  # max 40 chars
            size = get_size(file.file_size)
            text += (
                f"{i}. {file_name}\n"
                f"💾 <a href='https://telegram.me/{temp.U_NAME}?start=file_{file.file_id}'>{size}</a>\n\n"
            )

        await query.message.edit_text(
            text,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )

    elif query.data.startswith("setgs#landscape_modes"):
        _, _, current, chat_id = query.data.split("#")
        new_status = not (current == "True")
        await save_group_settings(int(chat_id), "landscape_mode", new_status)
        await query.answer(f"Landscape mode {'Enabled' if new_status else 'Disabled'}", show_alert=True)

    # Optional: Update button in-place
    # Edit message reply_markup to show updated ✅/❌


    elif query.data.startswith("setgs"):

        ident, set_type, status, grp_id = query.data.split("#")

        grp_id = int(grp_id)
        display_names = {
            "auto_ffilter": "𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫",
            "button": "𝐁𝐮𝐭𝐭𝐨𝐧",
            "auto_delete": "𝐃𝐞𝐥𝐞𝐭𝐞",
            "botpm": "𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝",
            "gfilter": "𝐅𝐢𝐥𝐞𝐫",
            "imdb": "𝐈𝐦𝐝𝐛",
            "landscape_mode": "𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞",
            "max_btn": "𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬",
            "newmod": "𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧",
            "spellcheck": "𝐏𝐫𝐨 𝐌𝐨𝐝",
            "file_secure": "𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧",
            "mod_mode": "𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭",
            "is_shortlink": "𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤",
            "spell_check": "𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤",
            "telegraph": "𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩ʜ",
            "welcome": "𝐖𝐞𝐥𝐜𝐨𝐦𝐞"
        }
        print(f"CALLBACK RECEIVED: {query.data}")
        print("SETTING:", set_type)
        print("OLD STATUS:", status)
        print("GROUP ID:", grp_id)

        if set_type == "is_shortlink" and query.from_user.id not in ADMINS:

                return await query.answer(
                        "Only admins can change shortlink settings",
                        show_alert=True
                )

        new_status = False if status == "True" else True

        await save_group_settings(
                grp_id,
                set_type,
                new_status
        )

        settings = await get_settings(grp_id)
        setting_name = display_names.get(set_type, set_type)
        status_icon = "✅" if new_status else "❌"

        print("UPDATED SETTINGS:", settings)
            
        buttons = [
            [
                InlineKeyboardButton('𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫✅' if settings["auto_ffilter"] else '𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐭𝐞𝐫❌',
                                     callback_data=f'setgs#auto_ffilter#{settings["auto_ffilter"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["button"] else '𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                     callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                InlineKeyboardButton('𝐃𝐞𝐥𝐞𝐭𝐞✅' if settings["auto_delete"] else '𝐃𝐞𝐥𝐞𝐭𝐞❌',
                                     callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝✅' if settings["botpm"] else '𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝❌',
                                     callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐅𝐢𝐥𝐭𝐞𝐫✅' if settings["gfilter"] else '𝐅𝐢𝐥𝐭𝐞𝐫❌',
                                     callback_data=f'setgs#gfilter#{settings["gfilter"]}#{str(grp_id)}'),
                InlineKeyboardButton('𝐈𝐦𝐝𝐛✅' if settings["imdb"] else '𝐈𝐦𝐝𝐛❌',
                                     callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ✅' if settings["landscape_mode"] else '𝐋𝐚𝐧𝐝𝐬𝐜𝐚𝐩𝐞 ❌',
                                     callback_data=f'setgs#landscape_mode#{settings["landscape_mode"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬✅' if settings["max_btn"] else '𝐌𝐚𝐱 𝐁𝐮𝐭𝐭𝐨𝐧𝐬❌',
                                     callback_data=f'setgs#max_btn#{settings["max_btn"]}#{str(grp_id)}'),
                InlineKeyboardButton('𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧✅' if settings["newmod"] else '𝐏𝐫𝐨 𝐁𝐮𝐭𝐭𝐨𝐧❌',
                                     callback_data=f'setgs#newmod#{settings["newmod"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐏𝐫𝐨 𝐌𝐨𝐝✅' if settings["spellcheck"] else '𝐏𝐫𝐨 𝐌𝐨𝐝❌',
                                     callback_data=f'setgs#spellcheck#{settings["spellcheck"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧✅' if settings["file_secure"] else '𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧❌',
                                     callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭✅' if settings["mod_mode"] else '𝐒𝐡𝐨𝐫𝐭𝐜𝐮𝐭❌',
                                     callback_data=f'setgs#mod_mode#{settings["mod_mode"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤✅' if settings["is_shortlink"] else '𝐒𝐡𝐨𝐫𝐭𝐥𝐢𝐧𝐤❌',
                                     callback_data=f'setgs#is_shortlink#{settings["is_shortlink"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤✅' if settings["spell_check"] else '𝐒𝐩𝐞𝐥𝐥𝐜𝐡𝐞𝐜𝐤❌',
                                     callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                InlineKeyboardButton('𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡✅' if settings["telegraph"] else '𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡❌',
                                     callback_data=f'setgs#telegraph#{settings["telegraph"]}#{str(grp_id)}')
            ],
            [
                InlineKeyboardButton('𝐖𝐞𝐥𝐜𝐨𝐦𝐞✅' if settings["welcome"] else '𝐖𝐞𝐥𝐜𝐨𝐦𝐞❌',
                                     callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
            ]
        ]
        await query.edit_message_text(
            text=f"<b>{setting_name}{status_icon} ᴀs ʙᴇᴇɴ sᴇᴛ ᴛᴏ {new_status}</b>\n\n<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs ⚙</b>",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )

        await query.answer("Setting Updated")
#    await query.answer(MSG_ALRT)


    
async def create_telegraph_page(username, search, files, settings):
    content = "" 
#    username = message.from_user.mention
    imdb = await get_poster(search) if settings.get("imdb", False) else None
    if settings.get("imdb", False):
    	imdb = await get_poster(search)

    if imdb:
        content += script.IMDB_TEMPLATE_TXT.format(
            query=search,
            username=username,
            title=imdb.get('title', 'N/A'),
            genres=imdb.get('genres', 'N/A'),
            year=imdb.get('year', 'N/A'),
            runtime=imdb.get('runtime', 'N/A'),
            rating=imdb.get('rating', 'N/A')
        )

        poster = imdb.get("poster")

        if poster:
            content = f'<img src="{poster}"><br>' + content

    content += "<br><br><b>📂 Available Files</b><br><br>"

    for file in files:
        file_name = file.file_name or "Unknown File"

        link = (
            f"https://telegram.me/"
            f"{temp.U_NAME}?start=files_{file.file_id}"
        )

        content += f'📄 <a href="{link}">{file_name}</a><br>'

    page = telegraph.post(
        title=search[:150],
        author="AutoFilter Bot",
        text=content
    )

    return page["url"]

async def create_telegraph_pages(search, files):
	

    content = f"<h3>{search}</h3>"

    for file in files:
        file_name = file.file_name or "Unknown File"

        link = (
            f"https://telegram.me/"
            f"{temp.U_NAME}?start=files_{file.file_id}"
        )

        content += (
            f'<p><a href="{link}">{file_name}</a></p>'
        )

    page = telegraph.post(
        title=search[:150],
        author="AutoFilter Bot",
        text=content
    )

    return page["url"]


# --- auto_filter ---
async def auto_filter(client, msg, spoll=False):
    curr_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
    reqstr1 = msg.from_user.id if msg.from_user else 0
    reqstr = await client.get_users(reqstr1)
    
    if not spoll:
        message = msg
        if message.text.startswith("/"): 
            return  # ignore commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if len(message.text) < 100:
            search = message.text
            m = await message.reply_text(f"<b><i> s𝖾𝖺𝗋𝖼𝗂̣ng f𝗈𝗋 '{search}' 🔎</i></b>")
            search = search.lower()
            find = search.split(" ")
            search = ""
            removes = ["in", "upload", "series", "full", "horror", "thriller", "mystery", "print", "file"]
            for x in find:
                if x in removes:
                    continue
                else:
                    search = search + x + " "
            search = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|bro|bruh|broh|helo|that|find|dubbed|link|venum|iruka|pannunga|pannungga|anuppunga|anupunga|anuppungga|anupungga|film|undo|kitti|kitty|tharu|kittumo|kittum|movie|any(one)|with\ssubtitle(s)?)", "", search, flags=re.IGNORECASE)
            search = re.sub(r"\s+", " ", search).strip()
            search = search.replace("-", " ")
            search = search.replace(":", "")
            if search:
                await save_search(search)
                print("DB =", userdb)
                print("TYPE =", type(userdb))
                await userdb.increase_movie_request()
                await userdb.increase_group_activity(
                    message.chat.id,
                    message.chat.title or "Private"
                )

            settings = await get_settings(message.chat.id)
            
            if settings.get("newmod", False):
                max_results = 40 if settings.get("max_btn") else 20
            else:
                max_results = 10 if settings.get("max_btn") else int(MAX_B_TN)
                
            files, offset, total_results = await get_search_results(
                message.chat.id,
                search,
                offset=0,
                max_results=max_results,
                filter=True
            )
            print("SEARCH =", search)
            print("TOTAL =", total_results)
            if not files:
                await userdb.increase_noresult_request()

                if settings["spell_check"]:
                    try: 
                        await m.delete()
                    except: 
                        pass
                    return await advantage_spell_chok(client, msg)

                try: 
                    await m.delete()
                except: 
                    pass
                return
        else:
            return
    else:
        message = msg.message.reply_to_message  
        search, files, offset, total_results = spoll
        m = await message.reply_text(f"<b><i> 𝖲𝖾𝖺𝗋𝖼hfng fᴏʀ '{search}' 🔎</i></b>")
        settings = await get_settings(message.chat.id)
        await msg.message.delete()

        if settings.get("newmod", False):
            max_results = 40 if settings.get("max_btn") else 20
        else:
            max_results = 10 if settings.get("max_btn") else int(MAX_B_TN)

        if not files:
            files, offset, total_results = await get_search_results(
                message.chat.id,
                search,
                offset=0,
                max_results=max_results,
                filter=True
            )
        
    pre = 'filep' if settings['file_secure'] else 'file'
    key = f"{message.chat.id}-{message.id}"
    REQUEST_USERS[key] = message.from_user.id
    FRESH[key] = search
    temp.GETALL[key] = files    
    temp.SHORT[message.from_user.id] = message.chat.id
    result_msg = m

    btn = []

    # 1. Telegraph ബട്ടൺ
    if settings.get("telegraph", False):
        try:
            username = f"@{message.from_user.username}" if message.from_user and message.from_user.username else message.from_user.mention
            telegraph_url = await create_telegraph_page(username, search, files, settings)
            btn.append([InlineKeyboardButton("📄𝐓e𝐥𝐞𝐠𝐫𝐚𝐩𝐡📄", callback_data=f"telegraph#{key}")])
        except Exception as e:
            logger.exception(e)

    # 2. ഫയൽ ബട്ടണുകൾ (Button Mode ഓൺ ആണെങ്കിൽ മാത്രം)
    if settings["button"]:
        btn.append([
            InlineKeyboardButton("⭐𝐌𝐚𝐫𝐤𝐦𝐨𝐝⭐", callback_data="markmode"),
            InlineKeyboardButton("📂𝐋𝐞𝐭𝐞𝐬𝐭 𝐅𝐢𝐥𝐞𝐬📂", callback_data=f"topsearch#{key}")
        ])

        if settings.get("newmod", False):
            row = []
            btn_limit = 40 if settings.get("max_btn") else 20
            buttons_per_row = 4
            
            for file in files[:btn_limit]:
                file_size = get_size(file.file_size)
                row.append(InlineKeyboardButton(text=f"📂 {file_size}", callback_data=f"{pre}#{file.file_id}"))
                if len(row) == buttons_per_row:
                    btn.append(row)
                    row = []
            if row: 
                btn.append(row)
        else:
            for file in files:
                EMOJI = random.choice(RUN_STRINGS)
                file_name = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))
                if message.from_user.id in MARK_MODE_USERS:
                    mark_icon = "✅" if (message.from_user.id in MARKED_FILES and file.file_id in MARKED_FILES[message.from_user.id]) else "❌"
                    btn.append([InlineKeyboardButton(text=f"{mark_icon} [{get_size(file.file_size)}] {file_name}", callback_data=f"mark#{file.file_id}")])
                else:
                    btn.append([InlineKeyboardButton(text=f"{EMOJI}[{get_size(file.file_size)}] {file_name}", callback_data=f"{pre}#{file.file_id}")])

    # 3. Pagination System (Next Button)
    if offset != "":
        req = message.from_user.id if message.from_user else 0
        try:
            div_val = 40 if settings.get("newmod", False) and settings.get("max_btn") else (20 if settings.get("newmod", False) else (10 if settings.get("max_btn") else int(MAX_B_TN)))
            
            try: 
                off_num = int(offset)
            except: 
                off_num = 0

            if off_num == 0 or off_num == div_val:
                current_pg = 1
                next_offset = div_val
            else:
                current_pg = (off_num // div_val) + 1
                next_offset = off_num + div_val

            total_pgs = math.ceil(int(total_results)/div_val) if int(total_results) > 0 else 1
            if current_pg > total_pgs: 
                current_pg = 1 

            btn.append([
                InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"), 
                InlineKeyboardButton(text=f"{current_pg}/{total_pgs}", callback_data="pages"), 
                InlineKeyboardButton(text="𝐍𝐄𝐗𝐓 ➪", callback_data=f"next_{req}_{key}_{next_offset}")
            ])
        except Exception:
            await save_group_settings(message.chat.id, 'max_btn', True)
            div_val = 40 if settings.get("newmod", False) and settings.get("max_btn") else (20 if settings.get("newmod", False) else (10 if settings.get("max_btn") else int(MAX_B_TN)))
            
            try: 
                off_num = int(offset)
            except: 
                off_num = 0

            if off_num == 0 or off_num == div_val:
                current_pg = 1
                next_offset = div_val
            else:
                current_pg = (off_num // div_val) + 1
                next_offset = off_num + div_val

            total_pgs = math.ceil(int(total_results)/div_val) if int(total_results) > 0 else 1
            if current_pg > total_pgs: 
                current_pg = 1

            btn.append([
                InlineKeyboardButton("📄 𝐏𝐀𝐆𝐄", callback_data="pages"), 
                InlineKeyboardButton(text=f"{current_pg}/{total_pgs}", callback_data="pages"), 
                InlineKeyboardButton(text="𝐍𝐄𝐗𝐓 ➪", callback_data=f"next_{req}_{key}_{next_offset}")
            ])
    else:
        btn.append([InlineKeyboardButton(text="𝐍𝐎 𝐌𝐎𝐑𝐄 𝐏𝐀𝐆𝐄𝐒 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄", callback_data="pages")])

    temp.BACK_BUTTONS[key] = btn
    
    await requestdb.update_one(
        {"user_id": message.from_user.id},
        {"$inc": {"requests": 1}, "$set": {"name": message.from_user.first_name, "username": message.from_user.username}},
        upsert=True
    )
    
    imdb = await get_poster(search, file=(files[0]).file_name, landscape_mode=settings.get("landscape_mode", False))
    
    cur_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
    time_difference = timedelta(hours=cur_time.hour, minutes=cur_time.minute, seconds=(cur_time.second+(cur_time.microsecond/1000000))) - timedelta(hours=curr_time.hour, minutes=curr_time.minute, seconds=(curr_time.second+(curr_time.microsecond/1000000)))
    remaining_seconds = "{:.2f}".format(time_difference.total_seconds())
    username = f"@{message.from_user.username}" if message.from_user and message.from_user.username else message.from_user.mention
    
    if imdb:
        f_title = imdb.get("title", search)
        f_genres = imdb.get("genres", "N/A")
        f_year = imdb.get("year", "N/A")
        f_runtime = imdb.get("runtime", "N/A")
        f_rating = imdb.get("rating", "N/A")
    else:
        f_title = search
        f_genres = "N/A"
        f_year = getattr(files[0], 'year', "N/A") if files else "N/A"
        f_runtime = "N/A"
        f_rating = "N/A"

    cap = (
        f"<b>𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention}: 𝐘𝐨𝐮𝐫 {search} 𝐑𝐞𝐚𝐝𝐲..\n\n"
        f"🏷 𝐓𝐢𝐭𝐥𝐞 : {f_title}\n\n"
        f"🎭 𝐆𝐞𝐧𝐫𝐞𝐬 : {f_genres}\n\n"
        f"📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {f_year}\n\n"
        f"📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {f_runtime}\n\n"
        f"🌟 𝐑𝐚𝐭𝐢𝐧𝐠 :  {f_rating} / 10\n\n</b>"
    )
        
    temp.IMDB_CAP[message.from_user.id] = cap
    
    if not settings["button"]:
        cap += "<b>\n<u>📚 Requested Files 👇</u></b>\n\n"
        for file in files:
            EMOJI = random.choice(RUN_STRINGS)
            file_clean_name = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))
            cap += f"<b>{EMOJI} <a href='https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}'>[{get_size(file.file_size)}] {file_clean_name}\n\n</a></b>"
            
    top = await get_top_requesters()
    cap += f"\n<b>𝐓𝐨𝐩 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐫𝐬</b>\n1. {top[0]}\n2. {top[1]}\n3. {top[2]}"
    
    poster = imdb.get("poster") if (imdb and settings.get("imdb", False)) else None
    if poster == "N/A": 
        poster = None
        
    if poster:
        try:
            hehe = await message.reply_photo(photo=poster, caption=cap, reply_markup=InlineKeyboardMarkup(btn) if btn else None)
            await m.delete()
            if settings['auto_delete']:
                await asyncio.sleep(300)
                await hehe.delete()
                await message.delete()
        except Exception as e:
            logger.exception(e)
            fek = await message.reply_text(text=cap, reply_markup=InlineKeyboardMarkup(btn) if btn else None)
            await m.delete()
            if settings['auto_delete']:
                await asyncio.sleep(300)
                await fek.delete()
                await message.delete()
    else:
        fuk = await message.reply_text(text=cap, reply_markup=InlineKeyboardMarkup(btn) if btn else None, disable_web_page_preview=True)
        await m.delete()
        if settings['auto_delete']:
            await asyncio.sleep(300)
            await fuk.delete()
            await message.delete() 




# SPELL CHECK RE-EDITED BY GOUTHAMSER (Fully corrected & debugged)
from plugins.rules import MALAYALAM_RULES

def ml_to_eng_sound(text):
    # 1. ആദ്യം rules.py-ലെ വലിയ കൂട്ടക്ഷരങ്ങൾ (നീളം 2-ൽ കൂടുതൽ ഉള്ളവ) മാത്രം മാറ്റുന്നു
    sorted_rules = sorted(MALAYALAM_RULES.items(), key=lambda item: len(item[0]), reverse=True)
    for ml_char, eng_char in sorted_rules:
        if len(ml_char) > 1:
            text = text.replace(ml_char, eng_char)

    # 2. 🎯 [PERFECT FIX] വള്ളിപുള്ളി ഇല്ലാത്ത ഒറ്റ വ്യഞ്ജനാക്ഷരങ്ങൾക്ക് 'a' ചേർക്കുന്നു
    pure_malayalam_consonants = "കഖഗഘങചഛജഝഞടഠഡഢണതഥദധനപഫബഭമയരലവശഷസഹളഴററ്റ"
    vowels_and_signs = ['്', 'ാ', 'ി', 'ീ', 'ു', 'ൂ', 'ൃ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൗ', 'ം', 'ഃ']
    
    result = []
    text_len = len(text)
    
    for i, char in enumerate(text):
        result.append(char)
        # അക്ഷരം ഒരു വ്യഞ്ജനാക്ഷരമാണെങ്കിൽ ചെക്ക് ചെയ്യുന്നു
        if char in pure_malayalam_consonants:
            # തൊട്ടടുത്ത അക്ഷരം ഒരു വള്ളിപുള്ളിയോ അല്ലെങ്കിൽ ചന്ദ്രക്കലയോ ആണോ എന്ന് നോക്കുന്നു
            if i + 1 < text_len:
                next_char = text[i+1]
                if next_char not in vowels_and_signs:
                    # അടുത്ത അക്ഷരം വള്ളിപുള്ളി അല്ലങ്കിൽ ഇവിടെ ഒരു 'a' ശബ്ദം നിർബന്ധമാണ്
                    result.append('ാ') # തൽക്കാലം 'ാ' ചേർക്കുന്നു (അടുത്ത സ്റ്റെപ്പിൽ ഇത് 'a' ആയി മാറും)
            else:
                # വാക്കിന്റെ അവസാനത്തെ അക്ഷരമാണെങ്കിൽ
                result.append('ാ')
                
    modified_text = "".join(result)

    # 3. ഇനി ബാക്കിയുള്ള സിംഗിൾ അക്ഷരങ്ങളെയും വള്ളിപുള്ളികളെയും rules.py വെച്ച് മാറ്റുന്നു
    for ml_char, eng_char in sorted_rules:
        modified_text = modified_text.replace(ml_char, eng_char)

    # 4. ഫൈനൽ ക്ലീനിംഗ് (ചന്ദ്രക്കലയും ചിഹ്നങ്ങളും കളയുന്നു)
    modified_text = modified_text.replace('്', '')
    modified_text = re.sub(r'[^a-zA-Z0-9\s]', '', modified_text)
    
    # രണ്ട് 'aa' ഒരുമിച്ച് വന്നാൽ അതിനെ സിംഗിൾ 'a' ആക്കുന്നു (ഉദാ: naarasimham -> narasimham)
    modified_text = re.sub(r'aa+', 'a', modified_text) 
    
    return re.sub(r'\s+', ' ', modified_text).strip().lower()


async def advantage_spellcheck(client, msg):
    mv_id = msg.id
    mv_rqst = msg.text.strip()
    reqstr1 = msg.from_user.id if msg.from_user else 0
    reqstr = await client.get_users(reqstr1)
    settings = await get_settings(msg.chat.id)
    
    # 🟢 [FIXED REGEX ORDER] - 'a' കട്ടാകാത്ത സുരക്ഷിതമായ ഫിൽട്ടർ ഉപയോഗിക്കുന്നു
    stop_words = r"\b(please|pls|plz|send|snd|give|gib|movie|movies|new|latest|bro|bruh|hello|halo|malayalam|tamil|file|files|find|und|full\smovie|with\ssubtitle|with\ssubtitles)\b"
    query = re.sub(stop_words, "", msg.text, flags=re.IGNORECASE)
    query = re.sub(r'\s+', ' ', query).strip()
    
    if not query:
        query = mv_rqst

    # 🟢 [MALAYALAM SOUND CONVERSION]
    if re.search(r'[\u0D00-\u0D7F]', query):
        print(f"📌 [DEBUG] മലയാളം കണ്ടെത്തി: {query}")
        converted_query = ml_to_eng_sound(query)
        print(f"✅ [DEBUG] കൺവേർട്ട് ചെയ്ത രൂപം: {converted_query}")
        query = converted_query
        mv_rqst = converted_query

    movielist = []

    # 🟢 [LOCAL DATABASE SEARCH]
    try:
        from database.ia_filterdb import get_search_results  
        print(f"🔍 [DB SEARCH] ഫൈനൽ സെർച്ച് വാക്ക്: {query}")
        
        files, _, _ = await get_search_results(msg.chat.id, query, offset=0, max_results=15)
        
        if files:
            temp_list = []
            
            for file in files:
                clean_name = file.file_name
                
                # 1. അനാവശ്യമായ ബ്രാക്കറ്റുകളും ലിങ്കുകളും നീക്കം ചെയ്യുന്നു
                clean_name = re.sub(r'\[.*?\]|\(.*?\)|@\w+|www\.\S+', ' ', clean_name)
                
                # 2. അനാവശ്യ വാക്കുകൾ (സൈസ്, ഫോർമാറ്റ്, മറ്റ് വാക്കുകൾ) നീക്കം ചെയ്യുന്നു
                clean_name = re.sub(r'(?i)(mkv|mp4|avi|malayalam|mal|srt|hdrip|bluray|webrip|\d+mb|\d+gb|x264|x265|hevc|hindi|english|tamil|telugu|720p|1080p|aac|hq|hd|web-dl|mm|bo|cemovies|mntgx|teaser|trailer|back|aikido|astray|a\b)', ' ', clean_name)
                
                # 3. വർഷം കണ്ടെത്തുന്നു (4 അക്കങ്ങളുള്ള നമ്പർ)
                year_match = re.search(r'\b(19|20)\d{2}\b', clean_name)
                year = year_match.group(0) if year_match else ""
                
                # 4. ഫയൽ പേര് ക്ലീൻ ചെയ്യുന്നു
                clean_name = os.path.splitext(clean_name)[0]
                clean_name = re.sub(r'[^a-zA-Z\s]', ' ', clean_name) # അക്ഷരങ്ങളും സ്പേസും മാത്രം
                clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                
                # 5. വർഷം മാറ്റി പേര് മാത്രം എടുക്കുന്നു
                base_name = re.sub(r'\b(19|20)\d{2}\b', '', clean_name).strip()
                base_name = re.sub(r'\s+', ' ', base_name).strip()
                
                # 6. [LIST APPENDING]
                if base_name:
                    # വെറും പേര് ആഡ് ചെയ്യുന്നു
                    if base_name not in temp_list:
                        temp_list.append(base_name)
                    
                    # വർഷം ഉണ്ടെങ്കിൽ മാത്രം പേര് + വർഷം ആഡ് ചെയ്യുന്നു
                    if year:
                        full_name = f"{base_name} {year}".strip()
                        if full_name not in temp_list:
                            temp_list.append(full_name)
            
            # 7. SORTING - കൃത്യമായ പേര് മുകളിൽ വരാൻ
            temp_list.sort(key=lambda x: (query.lower() not in x.lower(), len(x), x))
            
            # 10 റിസൾട്ട് മാത്രം
            movielist = temp_list[:10]
    except Exception as e:
        print(f"❌ [DB ERROR]: {e}")

    # 🔵 DB-യിൽ ഇല്ലെങ്കിൽ മാത്രം IMDb
    if not movielist:
        try:
            movies = await get_poster(query, bulk=True)
            if movies:
                for movie in movies:
                    if movie.get('Title'):
                        movielist.append(movie.get('Title'))
                    if movie.get('Title') and movie.get('Year'):
                        movielist.append(f"{movie.get('Title')} {movie.get('Year')}")
        except Exception as e:
            logger.exception(e)

    # 🔴 ഒന്നും കിട്ടിയില്ലെങ്കിൽ ഗൂഗിൾ ബട്ടൺ
    if not movielist:
        reqst_gle = query.replace(" ", "+")
        button = [[InlineKeyboardButton("GᴏᴏɢʟＥ", url=f"https://www.google.com/search?q={reqst_gle}")]]
        if NO_RESULTS_MSG:
            await client.send_message(chat_id=LOG_CHANNEL, text=(script.NORSLTS.format(reqstr.id, reqstr.mention, query)))
        k = await msg.reply_photo(photo=SPELL_IMG, caption=script.I_CUDNT.format(query), reply_markup=InlineKeyboardMarkup(button))
        await asyncio.sleep(30)
        await k.delete()
        return  

    display_name = msg.from_user.username if msg.from_user.username else msg.from_user.first_name     
    try:
        user_obj = await client.get_users(msg.from_user.id)
        pic = await client.download_media(user_obj.photo.big_file_id, file_name=f"downloads/{msg.from_user.id}.png") if user_obj.photo else "plugins/helpers/spell.png"
    except Exception:
        pic = "plugins/helpers/spell.png"

    spell_img_path = spellcheck(pic, display_name, query, msg.from_user.first_name, msg.chat.title, msg.from_user.id, msg.from_user.username)

    SPELL_CHECK[mv_id] = movielist
    
    btn = [
        [InlineKeyboardButton(text=movie_name.strip(), callback_data=f"spol#{reqstr1}#{mv_id}#{idx}")]
        for idx, movie_name in enumerate(movielist[:10])
    ]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spol#{reqstr1}#close_spellcheck')])
    
    try:
        await msg.reply_photo(
            photo=open(spell_img_path, "rb"),
            caption=script.CUDNT_FND.format(reqstr.mention),
            has_spoiler=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except Exception as e:
        import traceback
        traceback.print_exc()








async def manual_filters(client, message, text=False):
    settings = await get_settings(message.chat.id)
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            joelkb = await client.send_message(
                                group_id, 
                                reply_text, 
                                disable_web_page_preview=True,
                                protect_content=True if settings["file_secure"] else False,
                                reply_to_message_id=reply_id
                            )
                            try:
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)
                                    try:
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                else:
                                    try:
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_ffilter', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)

                        else:
                            button = eval(btn)
                            joelkb = await client.send_message(
                                group_id,
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                protect_content=True if settings["file_secure"] else False,
                                reply_to_message_id=reply_id
                            )
                            try:
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)
                                    try:
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                else:
                                    try:
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_ffilter', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)

                    elif btn == "[]":
                        joelkb = await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            protect_content=True if settings["file_secure"] else False,
                            reply_to_message_id=reply_id
                        )
                        try:
                            if settings['auto_ffilter']:
                                await auto_filter(client, message)
                                try:
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                            else:
                                try:
                                    if settings['auto_delete']:
                                        await asyncio.sleep(600)
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await asyncio.sleep(600)
                                        await joelkb.delete()
                        except KeyError:
                            grpid = await active_connection(str(message.from_user.id))
                            await save_group_settings(grpid, 'auto_ffilter', True)
                            settings = await get_settings(message.chat.id)
                            if settings['auto_ffilter']:
                                await auto_filter(client, message)

                    else:
                        button = eval(btn)
                        joelkb = await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id=reply_id
                        )
                        try:
                            if settings['auto_ffilter']:
                                await auto_filter(client, message)
                                try:
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                            else:
                                try:
                                    if settings['auto_delete']:
                                        await asyncio.sleep(600)
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await asyncio.sleep(600)
                                        await joelkb.delete()
                        except KeyError:
                            grpid = await active_connection(str(message.from_user.id))
                            await save_group_settings(grpid, 'auto_ffilter', True)
                            settings = await get_settings(message.chat.id)
                            if settings['auto_ffilter']:
                                await auto_filter(client, message)

                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False

async def global_filters(client, message, text=False):
    settings = await get_settings(message.chat.id)
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    keywords = await get_gfilters('gfilters')
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_gfilter('gfilters', keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            joelkb = await client.send_message(
                                group_id, 
                                reply_text, 
                                disable_web_page_preview=True,
                                reply_to_message_id=reply_id
                            )
                            manual = await manual_filters(client, message)
                            if manual == False:
                                settings = await get_settings(message.chat.id)
                                try:
                                    if settings['auto_ffilter']:
                                        await auto_filter(client, message)
                                        try:
                                            if settings['auto_delete']:
                                                await joelkb.delete()
                                        except KeyError:
                                            grpid = await active_connection(str(message.from_user.id))
                                            await save_group_settings(grpid, 'auto_delete', True)
                                            settings = await get_settings(message.chat.id)
                                            if settings['auto_delete']:
                                                await joelkb.delete()
                                    else:
                                        try:
                                            if settings['auto_delete']:
                                                await asyncio.sleep(600)
                                                await joelkb.delete()
                                        except KeyError:
                                            grpid = await active_connection(str(message.from_user.id))
                                            await save_group_settings(grpid, 'auto_delete', True)
                                            settings = await get_settings(message.chat.id)
                                            if settings['auto_delete']:
                                                await asyncio.sleep(600)
                                                await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_ffilter', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_ffilter']:
                                        await auto_filter(client, message) 
                            else:
                                try:
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                            
                        else:
                            button = eval(btn)
                            joelkb = await client.send_message(
                                group_id,
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id=reply_id
                            )
                            manual = await manual_filters(client, message)
                            if manual == False:
                                settings = await get_settings(message.chat.id)
                                try:
                                    if settings['auto_ffilter']:
                                        await auto_filter(client, message)
                                        try:
                                            if settings['auto_delete']:
                                                await joelkb.delete()
                                        except KeyError:
                                            grpid = await active_connection(str(message.from_user.id))
                                            await save_group_settings(grpid, 'auto_delete', True)
                                            settings = await get_settings(message.chat.id)
                                            if settings['auto_delete']:
                                                await joelkb.delete()
                                    else:
                                        try:
                                            if settings['auto_delete']:
                                                await asyncio.sleep(600)
                                                await joelkb.delete()
                                        except KeyError:
                                            grpid = await active_connection(str(message.from_user.id))
                                            await save_group_settings(grpid, 'auto_delete', True)
                                            settings = await get_settings(message.chat.id)
                                            if settings['auto_delete']:
                                                await asyncio.sleep(600)
                                                await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_ffilter', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_ffilter']:
                                        await auto_filter(client, message) 
                            else:
                                try:
                                    if settings['auto_delete']:
                                        await joelkb.delete()
                                except KeyError:
                                    grpid = await active_connection(str(message.from_user.id))
                                    await save_group_settings(grpid, 'auto_delete', True)
                                    settings = await get_settings(message.chat.id)
                                    if settings['auto_delete']:
                                        await joelkb.delete()

                    elif btn == "[]":
                        joelkb = await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id=reply_id
                        )
                        manual = await manual_filters(client, message)
                        if manual == False:
                            settings = await get_settings(message.chat.id)
                            try:
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)
                                    try:
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                else:
                                    try:
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_ffilter', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message) 
                        else:
                            try:
                                if settings['auto_delete']:
                                    await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_delete', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_delete']:
                                    await joelkb.delete()

                    else:
                        button = eval(btn)
                        joelkb = await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id=reply_id
                        )
                        manual = await manual_filters(client, message)
                        if manual == False:
                            settings = await get_settings(message.chat.id)
                            try:
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message)
                                    try:
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await joelkb.delete()
                                else:
                                    try:
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                                    except KeyError:
                                        grpid = await active_connection(str(message.from_user.id))
                                        await save_group_settings(grpid, 'auto_delete', True)
                                        settings = await get_settings(message.chat.id)
                                        if settings['auto_delete']:
                                            await asyncio.sleep(600)
                                            await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_ffilter', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_ffilter']:
                                    await auto_filter(client, message) 
                        else:
                            try:
                                if settings['auto_delete']:
                                    await joelkb.delete()
                            except KeyError:
                                grpid = await active_connection(str(message.from_user.id))
                                await save_group_settings(grpid, 'auto_delete', True)
                                settings = await get_settings(message.chat.id)
                                if settings['auto_delete']:
                                    await joelkb.delete()

                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False









async def advantage_spell_chok(client, msg):
    mv_id = msg.id
    mv_rqst = msg.text
    reqstr1 = msg.from_user.id if msg.from_user else 0
    reqstr = await client.get_users(reqstr1)
    settings = await get_settings(msg.chat.id)
    
    # ക്വറി ക്ലീൻ ചെയ്യുന്നു
    cleaned_text = re.sub(r"^[=\d\s#\-\+\.]+", "", msg.text).strip()

    query = re.sub(
        r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)",
        "", cleaned_text, flags=re.IGNORECASE)  
    query = query.strip()
    
    if not query:
        query = cleaned_text if cleaned_text else mv_rqst

    # 🎯 ACCURACY കൂട്ടാൻ: ഒറ്റയൊറ്റ അക്ഷരങ്ങൾക്കിടയിലെ സ്പേസ് മാറ്റുന്നു (ഉദാ: k g f -> kgf)
    if re.search(r"\b\w\s+\w\b", query):
        # വാക്കുകൾക്കിടയിലെ സ്പേസ് പൂർണ്ണമായി കളയുന്നു
        query_fixed = re.sub(r"\s+", "", query)
        # ഒറിജിനൽ ക്വറിയും ഫിക്സ് ചെയ്ത ക്വറിയും വെച്ച് സെർച്ച് ചെയ്യാൻ ഒന്നിലധികം ശ്രമങ്ങൾ നടത്താം
    else:
        query_fixed = query

    movies = None
    try:
        print("ORIGINAL =", msg.text)
        print("FILTERED QUERY FOR IMDb =", query_fixed)
        movies = await get_poster(query_fixed, bulk=True)
        
        # ഫിക്സ് ചെയ്ത പേരിൽ കിട്ടിയില്ലെങ്കിൽ ഒറിജിനൽ പേര് വെച്ച് ഒരിക്കൽ കൂടി നോക്കും
        if not movies and query_fixed != query:
            movies = await get_poster(query, bulk=True)
    except Exception as e:
        logger.exception(e)

    if not movies:
        reqst_gle = query_fixed.replace(" ", "+")
        button = [[
                   InlineKeyboardButton("Gᴏᴏɢʟᴇ", url=f"https://www.google.com/search?q={reqst_gle}")
        ]]
        if NO_RESULTS_MSG:
            await client.send_message(chat_id=LOG_CHANNEL, text=(script.NORSLTS.format(reqstr.id, reqstr.mention, query_fixed)))
        k = await msg.reply_photo(
            photo=SPELL_IMG, 
            caption=script.I_CUDNT.format(query_fixed),
            reply_markup=InlineKeyboardMarkup(button)
        )
        await asyncio.sleep(30)
        await k.delete()
        return  

    movielist = []
    imdb_poster = None

    for movie in movies:
        title = movie.get('Title')
        if title:
            movielist.append(title.strip())
        if not imdb_poster and movie.get('poster'):
            imdb_poster = movie.get('poster')

    if 'dfxp' in globals():
        movielist = list(dfxp(movielist))
    else:
        seen = set()
        movielist = [x for x in movielist if not (x in seen or seen.add(x))]
    
    if not movielist:
        return 
        
    SPELL_CHECK[mv_id] = movielist
    
    btn = []
    for k, movie_name in enumerate(movielist):
        btn.append([
            InlineKeyboardButton(
                text=movie_name,
                callback_data=f"spol#{reqstr1}#{mv_id}#{k}",
            )
        ])
        
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spol#{reqstr1}#0#close_spellcheck')])
    
    if not imdb_poster or imdb_poster == "N/A":
        imdb_poster = "https://graph.org/file/3d0f0f0f0f0f0f0f0f0f.jpg"

    try:
        spell_check_del = await msg.reply_photo(
            photo=imdb_poster,  
            caption=(script.CUDNT_FND.format(reqstr.mention)),
            has_spoiler=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except Exception as e:
        print("Reply Photo Error, sending text instead:", e)
        spell_check_del = await msg.reply_text(
            text=(script.CUDNT_FND.format(reqstr.mention)),
            reply_markup=InlineKeyboardMarkup(btn)
        )
    
    try:
        if settings['auto_delete']:
            await asyncio.sleep(600)
            await spell_check_del.delete()
    except KeyError:
        grpid = await active_connection(str(msg.from_user.id))
        await save_group_settings(grpid, 'auto_delete', True)
        settings = await get_settings(msg.chat.id)
        if settings['auto_delete']:
            await asyncio.sleep(600)
            await spell_check_del.delete()
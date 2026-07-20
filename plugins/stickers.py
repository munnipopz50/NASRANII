print("=== STICKER IMPORTED ===")
from pyrogram import Client, filters
from pyrogram.types import Message
# ടെലിഗ്രാമിന്റെ raw ഫങ്ക്ഷനുകൾ ഇംപോർട്ട് ചെയ്യുന്നു
from pyrogram.raw import functions
from pyrogram.raw.types import ReactionEmoji


from info import *

import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, Media2, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from database.users_chats_db import db as userdb
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT, CHNL_LNK, GRP_LNK, REQST_CHANNEL, SUPPORT_CHAT_ID, MAX_B_TN, IS_VERIFY, VERIFY, HOW_TO_VERIFY
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp, verify_user, check_token, check_verification, get_token, send_all, get_shortlink, get_tutorial
from database.connections_mdb import add_connection, active_connection
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)

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


BATCH_FILES = {}

from pyrogram import Client, filters
print("✅ STICKERS PLUGIN LOADED")

@Client.on_message(filters.command("s"))
async def stikcker(client, message):
    await message.reply_text("Working")
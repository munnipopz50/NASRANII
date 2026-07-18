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


@Client.on_message(filters.command("telegraph") & filters.group)
async def telegraph_settings(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/telegraph on\n/telegraph off"
        )

    value = message.command[1].lower()

    if value == "on":
        await save_group_settings(
            message.chat.id,
            "telegraph",
            True
        )
        await message.reply_text("✅ Telegraph Enabled")

    elif value == "off":
        await save_group_settings(
            message.chat.id,
            "telegraph",
            False
        )
        await message.reply_text("❌ Telegraph Disabled")




@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩{random.choice(RUN_STRINGS)}', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ], [                    
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐇𝐞𝐥𝐩{random.choice(RUN_STRINGS)}', callback_data='help'),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬{random.choice(RUN_STRINGS)}', callback_data='helps')     
        ], [
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐋𝐞𝐭𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 {random.choice(RUN_STRINGS)}', callback_data="topsearch")
        ], [      
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐈𝐧𝐥𝐢𝐧𝐞{random.choice(RUN_STRINGS)}', switch_inline_query_current_chat=''),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐛𝐨𝐮𝐭{random.choice(RUN_STRINGS)}', callback_data='about')                      
        ], [
            InlineKeyboardButton('𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ✅' if (await get_settings(message.from_user.id)).get("botpm", False) else '𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ❌', callback_data="toggle_botpm")      
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await userdb.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩{random.choice(RUN_STRINGS)}', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ], [                    
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐇𝐞𝐥𝐩{random.choice(RUN_STRINGS)}', callback_data='help'),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬{random.choice(RUN_STRINGS)}', callback_data='helps')     
        ], [
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐋𝐞𝐭𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 {random.choice(RUN_STRINGS)}', callback_data="topsearch")
        ], [      
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐈𝐧𝐥𝐢𝐧𝐞{random.choice(RUN_STRINGS)}', switch_inline_query_current_chat=''),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐛𝐨𝐮𝐭{random.choice(RUN_STRINGS)}', callback_data='about')                      
        ], [
            InlineKeyboardButton('𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ✅' if (await get_settings(message.from_user.id)).get("botpm", False) else '𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ❌', callback_data="toggle_botpm")      
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "❆ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            try:
                kk, file_id = message.command[1].split("_", 1)
                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", callback_data=f"checksub#{kk}#{file_id}")])
            except (IndexError, ValueError):
                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{temp.U_NAME}?start={message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**You are not in our channel given below so you don't get the movie file...\n\nIf you want the movie file, click on the '🍿ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ🍿' button below and join our back-up channel, then click on the '🔄 Try Again' button below...\n\nThen you will get the movie files...**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩{random.choice(RUN_STRINGS)}', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ], [                    
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐇𝐞𝐥𝐩{random.choice(RUN_STRINGS)}', callback_data='help'),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬{random.choice(RUN_STRINGS)}', callback_data='helps')     
        ], [
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐋𝐞𝐭𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 {random.choice(RUN_STRINGS)}', callback_data="topsearch")
        ], [      
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐈𝐧𝐥𝐢𝐧𝐞{random.choice(RUN_STRINGS)}', switch_inline_query_current_chat=''),
            InlineKeyboardButton(f'{random.choice(RUN_STRINGS)}𝐀𝐛𝐨𝐮𝐭{random.choice(RUN_STRINGS)}', callback_data='about')                      
        ], [
            InlineKeyboardButton('𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ✅' if (await get_settings(message.from_user.id)).get("botpm", False) else '𝐏𝐦 𝐒𝐞𝐚𝐫𝐜𝐡 ❌', callback_data="toggle_botpm")      
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
# ------------------ COMMANDS.PY FINAL FIX WITH DEBUG PRINTS ------------------
    data = message.command[1]
    print(f"[DEBUG] 📥 Start command received with data: '{data}'")
    
    # കമാൻഡ് സ്പ്ലിറ്റ് ചെയ്യുന്നു
    try:
        pre, file_id = data.split('_', 1)
        print(f"[DEBUG] 🔍 Split Success -> pre: '{pre}', file_id: '{file_id}'")
    except Exception as split_err:
        file_id = data
        pre = ""
        print(f"[DEBUG] ⚠️ Split Failed (Single word data) -> pre: '{pre}', file_id: '{file_id}'. Error: {split_err}")

    # 🟢 1. HYPERLINK / SINGLE FILE ലോജിക്
    if pre == "files" or data.startswith("files_"):
        print(f"[DEBUG] 🚀 Entered 'files' block! Processing file_id: {file_id}")
        user = message.from_user.id
        
        try:
#            from utils import get_shortlink, get_tutorial, active_connection, get_settings
#            from info import PREMIUM_USER, VERIFY, CUSTOM_FILE_CAPTION, SUPPORT_CHAT, CHNL_LNK
            print("[DEBUG] ✅ Imports inside 'files' block successful.")
        except Exception as imp_err:
            print(f"[DEBUG] ❌ Import Error inside 'files' block: {imp_err}")
            return await message.reply(f"<b>❌ Import Error: {imp_err}</b>")
            
        try:
            chat_id = temp.SHORT.get(user)
            if chat_id is None:
                chat_id = await active_connection(int(user))
            if chat_id is None:
                chat_id = 0
            print(f"[DEBUG] 🌐 Active Connection Chat ID: {chat_id}")
                

            settings = await get_settings(chat_id) if chat_id else {'is_shortlink': False, 'botpm': True}

# തൊട്ടുതാഴെ ഈ 2 വരി കൂടി ചേർക്കുക:
#            if not settings.get('botpm', True):
#                return await message.reply("<b>❌ സെറ്റിങ്സ് അനുസരിച്ച് ഫയലുകൾ PM-ൽ ലഭ്യമായിരിക്കില്ല. ചാനൽ വഴി ഡൗൺലോഡ് ചെയ്യുക.</b>")
#            print(f"[DEBUG] ⚙️ Shortlink Setting for chat {chat_id}: {settings.get('is_shortlink', False)}")
            
            # Shortlink ഓൺ ആണെങ്കിൽ
            if settings.get('is_shortlink', False) and user not in PREMIUM_USER:
                print(f"[DEBUG] 🔗 Shortlink is Active for user {user}. Fetching details...")
                files_ = await get_file_details(file_id)
                if not files_:
                    print(f"[DEBUG] ❌ File NOT found in DB for ID: {file_id}")
                    return await message.reply('<b>❌ No such file exist in database.</b>')
                
                files = files_[0]
                JRMA_URL = "https://nasranibot-c53.e.jrnm.app"
                g = f"{JRMA_URL}/watch/{file_id}"
#                g = await get_shortlink(chat_id, f"https://telegram.me/{temp.U_NAME}?start=file_{file_id}")
                print(f"[DEBUG] 🔗 Generated Shortlink: {g}")
                
                k = await client.send_message(chat_id=message.from_user.id, text=f"<b>📕Nᴀᴍᴇ ➠ : <code>{files.file_name}</code> \n\n🔗Sɪᴢᴇ ➠ : {get_size(files.file_size)}\n\n📂FɪʟЕ ʟɪɴᴋ ➠ : {g}\n\n<i>Note: This message is deleted in 20 mins to avoid copyrights. Save the link to Somewhere else</i></b>", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton('📂 😁Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)],
                     [InlineKeyboardButton(' Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ', url=await get_tutorial(chat_id))]]
                ))
                await asyncio.sleep(1200)
                await k.edit("<b>Your message is successfully deleted!!!</b>")
                return

            # Shortlink ഓഫ് ആണെങ്കിൽ നേരിട്ട് ഫയൽ അയക്കുന്നു
            print(f"[DEBUG] 📁 Shortlink is OFF or Premium User. Fetching file details directly...")
            files_ = await get_file_details(file_id)
            if not files_:
                print(f"[DEBUG] ❌ Direct File NOT found in DB for ID: {file_id}")
                return await message.reply('<b>❌ No such file exist.</b>')
                
            files = files_[0]
            title = '@NASRANI_SUPPORT ' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files.file_name.split()))
            size = get_size(files.file_size)
            f_caption = files.caption
            
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    print(f"[DEBUG] ⚠️ Caption formatting error: {e}")
                    
            if f_caption is None:
                f_caption = f"@NASRANI_SUPPORT {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files.file_name.split()))}"
                
            if not await check_verification(client, message.from_user.id) and VERIFY == True:
                print(f"[DEBUG] 🔒 User {user} is not verified. Sending verification link.")
                btn = [[InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{temp.U_NAME}?start="))]]
                return await message.reply_text(text="<b>You are not verified !\nKindly verify to continue !</b>", protect_content=True, reply_markup=InlineKeyboardMarkup(btn))
                
            print(f"[DEBUG] 📤 Sending cached media to user {user}...")
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                caption=f_caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'), InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇﻠ', url=CHNL_LNK)],
                    [InlineKeyboardButton("MᴏᴠɪＥ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")]
                ])
            )
            print("[DEBUG] ✅ Cached media sent successfully!")
            
            btn = [[InlineKeyboardButton("Get File Again", callback_data=f'delfile#{file_id}')]]
            k = await msg.reply("<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie File/Video will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this File/Video to your Saved Messages and Start Download there</i></b>", quote=True)
            await asyncio.sleep(600)
            await msg.delete()
            await k.edit_text("<b>Your File/Video is successfully deleted!!!\n\nClick below button to get your deleted file 👇</b>", reply_markup=InlineKeyboardMarkup(btn))
            return
        except Exception as main_err:
            print(f"[DEBUG] ❌ CRITICAL ERROR inside 'files' block: {main_err}")
            return await message.reply(f"<b>❌ Error inside files block: {main_err}</b>")

    # 🟢 2. MARKED FILES (M3-) ലോജിക്
    elif data.startswith("M3-") or pre == "M3":
        print(f"[DEBUG] 🚀 Detected M3- Mark Mod Link! Full data: '{data}'")
        sts = await message.reply("<b>Please wait... Fetching your marked files...</b>")
        
        try:
            target_user_id = int(data.split("-", 1)[1])
            from plugins.pmfilter import MARKED_FILES
            
            files = MARKED_FILES.get(target_user_id, [])
            print(f"[DEBUG] 📋 Marked files found for user {target_user_id}: {len(files)} files.")
            if not files:
                return await sts.edit("<b>❌ No files found! വീണ്ടും ഫയലുകൾ മാർക്ക് ചെയ്യുക.</b>")
                
            success = 0
            sent_files_list = []
            
            for index, file_id in enumerate(files, 1):
                try:
                    files_ = await get_file_details(file_id)
                    if files_:
                        file_info = files_[0]
                        title = '@NASRANI_SUPPORT ' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), file_info.file_name.split()))
                        size = get_size(file_info.file_size)
                        f_caption = f"<code>{title}</code>"
                    else:
                        title = "Marked File"
                        size = "Unknown"
                        f_caption = f"<code>{title}</code>"

                    sent_media = await client.send_cached_media(chat_id=message.from_user.id, file_id=file_id, caption=f_caption)
                    sent_files_list.append(sent_media)
                    success += 1
                    await asyncio.sleep(0.5)
                    
                except Exception as file_err:
                    print(f"[DEBUG] ❌ Error sending marked file at index {index}: {file_err}")
                    continue
                    
            await sts.edit(f"<b>✅ Successfully Sent {success} Files!\n\n⚠️ ഈ ഫയലുകൾ 3 മിനിറ്റിനുള്ളിൽ ഡിലീറ്റ് ചെയ്യപ്പെടും.</b>")
            MARKED_FILES[target_user_id] = []
            
            if sent_files_list:
                async def auto_delete_files(media_messages):
                    await asyncio.sleep(180)
                    for msg in media_messages:
                        try: await msg.delete()
                        except: pass
                asyncio.create_task(auto_delete_files(sent_files_list))
            return
            
        except Exception as err:
            print(f"[DEBUG] ❌ CRITICAL ERROR inside M3 block: {err}")
            return await sts.edit("<b>❌ Something went wrong while fetching files!</b>")

    # 🟢 3. പഴയ മറ്റ് ലോജിക്കുകൾ (BATCH, DSTORE) ഉള്ള ഭാഗം തുടരുന്നു...
    print(f"[DEBUG] ℹ️ Data passed down to older handlers (BATCH/DSTORE). Current pre: '{pre}'")
    if data.split("-", 1)[0] == "BATCH":
        # ... (നിങ്ങളുടെ BATCH ഫയൽ അയക്കുന്ന പഴയ കോഡ് ഇവിടെ തുടരും)
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if BATCH_FILE_CAPTION:
                try:
                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            try:
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),
                          InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                       ],[
                          InlineKeyboardButton("Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")
                         ]
                        ]
                    )
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),
                          InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                       ],[
                          InlineKeyboardButton("Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")
                         ]
                        ]
                    )
                )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
            await asyncio.sleep(1) 
        await sts.delete()
        return
    
    elif data.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("<b>Please wait...</b>")
        b_string = data.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        try:
            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)
        except:
            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
            protect = "/pbatch" if PROTECT_CONTENT else "batch"
        diff = int(l_msg_id) - int(f_msg_id)
        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):
            if msg.media:
                media = getattr(msg, msg.media.value)
                if BATCH_FILE_CAPTION:
                    try:
                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))
                    except Exception as e:
                        logger.exception(e)
                        f_caption = getattr(msg, 'caption', '')
                else:
                    media = getattr(msg, msg.media.value)
                    file_name = getattr(media, 'file_name', '')
                    f_caption = getattr(msg, 'caption', file_name)
                try:
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            elif msg.empty:
                continue
            else:
                try:
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            await asyncio.sleep(1) 
        return await sts.delete()

    elif data.split("-", 1)[0] == "verify":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(message.from_user.id) != int(userid):
            return await message.reply_text(
                text="<b>Invalid link or Expired link !</b>",
                protect_content=True
            )
        is_valid = await check_token(client, userid, token)
        if is_valid == True:
            await message.reply_text(
                text=f"<b>Hey {message.from_user.mention}, You are successfully verified !\nNow you have unlimited access for all movies till today midnight.</b>",
                protect_content=True
            )
            await verify_user(client, userid, token)
        else:
            return await message.reply_text(
                text="<b>Invalid link or Expired link !</b>",
                protect_content=True
            )

    if data.startswith("sendfiles"):
        chat_id = int("-" + file_id.split("-")[1])
        userid = message.from_user.id if message.from_user else None
        JRMA_URL = "https://nasranii.onrender.com"
        g = f"{JRMA_URL}/watch/{file_id}"
#        g = await get_shortlink(chat_id, f"https://telegram.me/{temp.U_NAME}?start=allfiles_{file_id}")
        k = await client.send_message(chat_id=message.from_user.id,text=f"<b>Get All Files in a Single Click!!!\n\n<i>Note: This message is deleted in 5 mins to avoid copyrights. Save the link to Somewhere else</i></b>", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📂 🥰 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
                    ], [
                        InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=await get_tutorial(chat_id))
                    ]
                ]
            )
        )
        await asyncio.sleep(300)
        await k.edit("<b>Your message is successfully deleted!!!</b>")
        return
        
    
    elif data.startswith("short"):
        user = message.from_user.id
        chat_id = temp.SHORT.get(user)
        files_ = await get_file_details(file_id)
        files = files_[0]
#        g = await get_shortlink(chat_id, f"https://telegram.me/{temp.U_NAME}?start=file_{file_id}")
        JRMA_URL = "https://nasranii.onrender.com"
        g = f"{JRMA_URL}/watch/{file_id}"
        k = await client.send_message(chat_id=user,text=f"<b>📕Nᴀᴍᴇ ➠ : <code>{files.file_name}</code> \n\n🔗Sɪᴢᴇ ➠ : {get_size(files.file_size)}\n\n<i>Note: This message is deleted in 20 mins to avoid copyrights. Save the link to Somewhere else</i></b>", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📂 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
                    ], [
                        InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=await get_tutorial(chat_id))
                    ]
                ]
            )
        )
        await asyncio.sleep(1200)
        await k.edit("<b>Your message is successfully deleted!!!</b>")
        return
        
    elif data.startswith("all"):
        files = temp.GETALL.get(file_id)
        if not files:
            return await message.reply('<b><i>No such file exist.</b></i>')
        filesarr = []
        for file in files:
            file_id = file.file_id
            files_ = await get_file_details(file_id)
            files1 = files_[0]
            title = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files1.file_name.split()))
            size=get_size(files1.file_size)
            f_caption=files1.caption
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files1.file_name.split()))}"
            if not await check_verification(client, message.from_user.id) and VERIFY == True:
                btn = [[
                    InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{temp.U_NAME}?start="))
                ]]
                await message.reply_text(
                    text="<b>You are not verified !\nKindly verify to continue !</b>",
                    protect_content=True,
                    reply_markup=InlineKeyboardMarkup(btn)
                )
                return
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                caption=f_caption,
                protect_content=True if pre == 'filep' else False,
                reply_markup=InlineKeyboardMarkup(
                    [
                     [
                      InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),
                      InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                   ],[
                      InlineKeyboardButton("Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")
                     ]
                    ]
                )
            )
            filesarr.append(msg)
        k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie Files/Videos will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this ALL Files/Videos to your Saved Messages and Start Download there</i></b>")
        await asyncio.sleep(600)
        for x in filesarr:
            await x.delete()
        await k.edit_text("<b>Your All Files/Videos is successfully deleted!!!</b>")
        return    
        
    elif data.startswith("filesssssss"):
        user = message.from_user.id

        chat_id = temp.SHORT.get(user)

        if chat_id is None:
            chat_id = await active_connection(int(user))

        if chat_id is None:
            chat_id = 0
        settings = await get_settings(chat_id)
        if settings['is_shortlink'] and user not in PREMIUM_USER:
            files_ = await get_file_details(file_id)
            files = files_[0]
            g = await get_shortlink(chat_id, f"https://telegram.me/{temp.U_NAME}?start=file_{file_id}")
            k = await client.send_message(chat_id=message.from_user.id,text=f"<b>📕Nᴀᴍᴇ ➠ : <code>{files.file_name}</code> \n\n🔗Sɪᴢᴇ ➠ : {get_size(files.file_size)}\n\n\n<i>Note: This message is deleted in 20 mins to avoid copyrights. Save the link to Somewhere else</i></b>", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('🤣📂 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
                        ], [
                            InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=await get_tutorial(chat_id))
                        ]
                    ]
                )
            )
            await asyncio.sleep(1200)
            await k.edit("<b>Your message is successfully deleted!!!</b>")
            return
    user = message.from_user.id
    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            if not await check_verification(client, message.from_user.id) and VERIFY == True:
                btn = [[
                    InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{temp.U_NAME}?start="))
                ]]
                await message.reply_text(
                    text="<b>You are not verified !\nKindly verify to continue !</b>",
                    protect_content=True,
                    reply_markup=InlineKeyboardMarkup(btn)
                )
                return
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=True if pre == 'filep' else False,
                reply_markup=InlineKeyboardMarkup(
                    [
                     [
                      InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),
                      InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                   ],[
                      InlineKeyboardButton("Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")
                     ]
                    ]
                )
            )
            filetype = msg.media
            file = getattr(msg, filetype.value)
            title = '@NASRANI_SUPPORT ' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), file.file_name.split()))
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(f_caption)
            btn = [[
                InlineKeyboardButton("Get File Again", callback_data=f'delfile#{file_id}')
            ]]
            k = await msg.reply("<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie File/Video will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this File/Video to your Saved Messages and Start Download there</i></b>",quote=True)
            await asyncio.sleep(600)
            await msg.delete()
            await k.edit_text("<b>Your File/Video is successfully deleted!!!\n\nClick below button to get your deleted file 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
            return
        except:
            pass
        return await message.reply('No such file exist.')
    files = files_[0]
    title = '@NASRANI_SUPPORT ' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files.file_name.split()))
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"@NASRANI_SUPPORT {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files.file_name.split()))}"
    if not await check_verification(client, message.from_user.id) and VERIFY == True:
        btn = [[
            InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{temp.U_NAME}?start="))
        ]]
        await message.reply_text(
            text="<b>You are not verified !\nKindly verify to continue !</b>",
            protect_content=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return
    msg = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=True if pre == 'filep' else False,
        reply_markup=InlineKeyboardMarkup(
            [
             [
              InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),
              InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
           ],[
              InlineKeyboardButton("Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Gʀᴏᴜᴘ", url="https://t.me/nasrani_update")
             ]
            ]
        )
    )
    btn = [[
        InlineKeyboardButton("Get File Again", callback_data=f'delfile#{file_id}')
    ]]
    k = await msg.reply("<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie File/Video will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this File/Video to your Saved Messages and Start Download there</i></b>",quote=True)
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>Your File/Video is successfully deleted!!!\n\nClick below button to get your deleted file 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
    return                  

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Uɴᴇxᴘᴇᴄᴛᴇᴅ ᴛʏᴘᴇ ᴏғ CHANNELS")

    text = '📑 **Iɴᴅᴇxᴇᴅ ᴄʜᴀɴɴᴇʟs/ɢʀᴏᴜᴘs**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('Logs.txt')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Pʀᴏᴄᴇssɪɴɢ...⏳", quote=True)
    else:
        await message.reply('Rᴇᴘʟʏ ᴛᴏ ғɪʟᴇ ᴡɪᴛʜ /delete ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('Tʜɪs ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ ғɪʟᴇ ғᴏʀᴍᴀᴛ')
        return
    
    file_id, file_ref = unpack_new_file_id(media.file_id)
    if await Media.count_documents({'file_id': file_id}):
        result = await Media.collection.delete_one({
            '_id': file_id,
        })
    else:
        result = await Media2.collection.delete_one({
            '_id': file_id,
        })
    if result.deleted_count:
        await msg.edit('Fɪʟᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_many({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            await msg.edit('Fɪʟᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ')
        else:
            result = await Media2.collection.delete_many({
                'file_name': file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                await msg.edit('Fɪʟᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ')
            else:
                # files indexed before https://github.com/EvamariaTG/EvaMaria/commit/f3d2a1bcb155faf44178e5d7a685a1b533e714bf#diff-86b613edf1748372103e94cacff3b578b36b698ef9c16817bb98fe9ef22fb669R39 
                # have original file name.
                result = await Media.collection.delete_many({
                    'file_name': media.file_name,
                    'file_size': media.file_size,
                    'mime_type': media.mime_type
                })
                if result.deleted_count:
                    await msg.edit('Fɪʟᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ')
                else:
                    result = await Media2.collection.delete_many({
                        'file_name': media.file_name,
                        'file_size': media.file_size,
                        'mime_type': media.mime_type
                    })
                    if result.deleted_count:
                        await msg.edit('Fɪʟᴇ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ')
                    else:
                        await msg.edit('Fɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ')

@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'Tʜɪs ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɪɴᴅᴇxᴇᴅ ғɪʟᴇs.\nDᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ?',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Yᴇs", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Cᴀɴᴄᴇʟ", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await Media2.collection.drop()
    await message.answer("Eᴠᴇʀʏᴛʜɪɴɢ's Gᴏɴᴇ")
    await message.message.edit('Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ Aʟʟ Tʜᴇ Iɴᴅᴇxᴇᴅ Fɪʟᴇs.')

@Client.on_message(filters.command('settings'))
async def settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"Yᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. Usᴇ /connect {message.chat.id} ɪɴ PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Mᴀᴋᴇ sᴜʀᴇ I'ᴍ ᴘʀᴇsᴇɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ !", quote=True)
                return
        else:
            await message.reply_text("I'ᴍ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘs !", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

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
    # Default values for missing settings
    defaults = {
        "button": False,
        "botpm": False,
        "file_secure": False,
        "imdb": True,
        "spell_check": True,
        "welcome": False,
        "auto_delete": False,
        "auto_ffilter": True,
        "max_btn": False,
        "is_shortlink": False,
        "template": False,
        "telegraph": False,
        "mod_mode": False,
        "landscape_mode": False,
        "gfilter": True,
        "newmod": False,
        "spellcheck": False,
        "tmdb": False,
    }

    for key, value in defaults.items():
        settings.setdefault(key, value)

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
    if 'mod_mode' not in settings.keys():
        await save_group_settings(grp_id, 'mod_mode', False)

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

        btn = [[
                InlineKeyboardButton("Oᴘᴇɴ Hᴇʀᴇ ↓", callback_data=f"opnsetgrp#{grp_id}"),
                InlineKeyboardButton("Oᴘᴇɴ Iɴ PM ⇲", callback_data=f"opnsetpm#{grp_id}")
              ]]

        reply_markup = InlineKeyboardMarkup(buttons)
        if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await message.reply_text(
                text="<b>Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏᴘᴇɴ sᴇᴛᴛɪɴɢs ʜᴇʀᴇ ?</b>",
                reply_markup=InlineKeyboardMarkup(btn),
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML,
                reply_to_message_id=message.id
            )
        else:
            await message.reply_text(
                text=f"<b>Cʜᴀɴɢᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs Fᴏʀ {title} As Yᴏᴜʀ Wɪsʜ ⚙</b>",
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML,
                reply_to_message_id=message.id
            )



@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    sts = await message.reply("Cʜᴇᴄᴋɪɴɢ ᴛᴇᴍᴘʟᴀᴛᴇ...")
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"Yᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. Usᴇ /connect {message.chat.id} ɪɴ PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Mᴀᴋᴇ sᴜʀᴇ I'ᴍ ᴘʀᴇsᴇɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!!", quote=True)
                return
        else:
            await message.reply_text("I'ᴍ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘs!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != enums.ChatMemberStatus.ADMINISTRATOR
            and st.status != enums.ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return

    if len(message.command) < 2:
        return await sts.edit("Nᴏ Iɴᴘᴜᴛ!!")
    template = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'template', template)
    await sts.edit(f"Sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ {title} ᴛᴏ:\n\n{template}")


@Client.on_message((filters.command(["request", "Request"]) | filters.regex("#request") | filters.regex("#Request")) & filters.group)
async def requests(bot, message):
    if REQST_CHANNEL is None or SUPPORT_CHAT_ID is None: return # Must add REQST_CHANNEL and SUPPORT_CHAT_ID to use this feature
    if message.reply_to_message and SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.reply_to_message.text
        try:
            if REQST_CHANNEL is not None:
                btn = [[
                        InlineKeyboardButton('Vɪᴇᴡ Rᴇᴏ̨ᴜᴇsᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('Sʜᴏᴡ Oᴘᴛɪᴏɴs', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})\n\n𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {content}</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('Vɪᴇᴡ Rᴇᴏ̨ᴜᴇsᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('Sʜᴏᴡ Oᴘᴛɪᴏɴs', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})\n\n𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {content}</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>Yᴏᴜ ᴍᴜsᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇᴏ̨ᴜᴇsᴛ [Mɪɴɪᴍᴜᴍ 3 Cʜᴀʀᴀᴄᴛᴇʀs]. Rᴇᴏ̨ᴜᴇsᴛs ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
        
    elif SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.text
        keywords = ["#request", "/request", "#Request", "/Request"]
        for keyword in keywords:
            if keyword in content:
                content = content.replace(keyword, "")
        try:
            if REQST_CHANNEL is not None and len(content) >= 3:
                btn = [[
                        InlineKeyboardButton('Vɪᴇᴡ Rᴇᴏ̨ᴜᴇsᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('Sʜᴏᴡ Oᴘᴛɪᴏɴs', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})\n\n𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {content}</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('Vɪᴇᴡ Rᴇᴏ̨ᴜᴇsᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('Sʜᴏᴡ Oᴘᴛɪᴏɴs', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})\n\n𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {content}</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>Yᴏᴜ ᴍᴜsᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇᴏ̨ᴜᴇsᴛ [Mɪɴɪᴍᴜᴍ 3 Cʜᴀʀᴀᴄᴛᴇʀs]. Rᴇᴏ̨ᴜᴇsᴛs ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Eʀʀᴏʀ: {e}")
            pass

    else:
        success = False
    
    if success:
        btn = [[
                InlineKeyboardButton('Vɪᴇᴡ Rᴇᴏ̨ᴜᴇsᴛ', url=f"{reported_post.link}")
              ]]
        await message.reply_text("<b>Yᴏᴜʀ ʀᴇᴏ̨ᴜᴇsᴛ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ! Pʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ sᴏᴍᴇ ᴛɪᴍᴇ.</b>", reply_markup=InlineKeyboardMarkup(btn))

        
@Client.on_message(filters.command("send") & filters.user(ADMINS))
async def send_msg(bot, message):
    if message.reply_to_message:
        target_id = message.text.split(" ", 1)[1]
        out = "Usᴇʀs Sᴀᴠᴇᴅ Iɴ DB Aʀᴇ:\n\n"
        success = False
        try:
            user = await bot.get_users(target_id)
            users = await db.get_all_users()
            async for usr in users:
                out += f"{usr['id']}"
                out += '\n'
            if str(user.id) in str(out):
                await message.reply_to_message.copy(int(user.id))
                success = True
            else:
                success = False
            if success:
                await message.reply_text(f"<b>Yᴏᴜʀ ᴍᴇssᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇɴᴅ ᴛᴏ {user.mention}.</b>")
            else:
                await message.reply_text("<b>Tʜɪs ᴜsᴇʀ ᴅɪᴅɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ʏᴇᴛ!</b>")
        except Exception as e:
            await message.reply_text(f"<b>Eʀʀᴏʀ: {e}</b>")
    else:
        await message.reply_text("<b>Usᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ɪᴅ. Fᴏʀ ᴇɢ: /send ᴜsᴇʀɪᴅ</b>")

@Client.on_message(filters.command("deletefiles") & filters.user(ADMINS))
async def deletemultiplefiles(bot, message):
    chat_type = message.chat.type
    if chat_type != enums.ChatType.PRIVATE:
        return await message.reply_text(f"<b>Hᴇʏ {message.from_user.mention}, Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏɴ'ᴛ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘs. Iᴛ ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ ᴍʏ PM!</b>")
    else:
        pass
    try:
        keyword = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text(f"<b>Hᴇʏ {message.from_user.mention}, Gɪᴠᴇ ᴍᴇ ᴀ ᴋᴇʏᴡᴏʀᴅ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ғɪʟᴇs.</b>")
    btn = [[
       InlineKeyboardButton("Yᴇs, Cᴏɴᴛɪɴᴜᴇ !", callback_data=f"killfilesdq#{keyword}")
       ],[
       InlineKeyboardButton("Nᴏ, Aʙᴏʀᴛ ᴏᴘᴇʀᴀᴛɪᴏɴ !", callback_data="close_data")
    ]]
    await message.reply_text(
        text="<b>Aʀᴇ ʏᴏᴜ sᴜʀᴇ? Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ?\n\nNᴏᴛᴇ:- Tʜɪs ᴄᴏᴜʟᴅ ʙᴇ ᴀ ᴅᴇsᴛʀᴜᴄᴛɪᴠᴇ ᴀᴄᴛɪᴏɴ!</b>",
        reply_markup=InlineKeyboardMarkup(btn),
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("shortlink") & filters.user(ADMINS))
async def shortlink(bot, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        return await message.reply_text(f"<b>Hᴇʏ {message.from_user.mention}, Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘs !</b>")
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grpid = message.chat.id
        title = message.chat.title
    else:
        return
    data = message.text
    userid = message.from_user.id
    user = await bot.get_chat_member(grpid, userid)
    if user.status != enums.ChatMemberStatus.ADMINISTRATOR and user.status != enums.ChatMemberStatus.OWNER and str(userid) not in ADMINS:
        return await message.reply_text("<b>Yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ !</b>")
    else:
        pass
    try:
        command, shortlink_url, api = data.split(" ")
    except:
        return await message.reply_text("<b>Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ :(\n\nGɪᴠᴇ ᴍᴇ ᴀ sʜᴏʀᴛʟɪɴᴋ ᴀɴᴅ ᴀᴘɪ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ !\n\nFᴏʀᴍᴀᴛ: <code>/shortlink shorturllink.in 95a8195c40d31e0c3b6baa68813fcecb1239f2e9</code></b>")
    reply = await message.reply_text("<b>Pʟᴇᴀsᴇ Wᴀɪᴛ...</b>")
    await save_group_settings(grpid, 'shortlink', shortlink_url)
    await save_group_settings(grpid, 'shortlink_api', api)
    await save_group_settings(grpid, 'is_shortlink', True)
    await reply.edit_text(f"<b>Sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ sʜᴏʀᴛʟɪɴᴋ API ғᴏʀ {title}.\n\nCᴜʀʀᴇɴᴛ Sʜᴏʀᴛʟɪɴᴋ Wᴇʙsɪᴛᴇ: <code>{shortlink_url}</code>\nCᴜʀʀᴇɴᴛ API: <code>{api}</code></b>")


@Client.on_message(filters.command("connect_chat") & filters.group)
async def connect_group(client, message):
    user_id = message.from_user.id
    grp_id = message.chat.id
    await save_group_settings(user_id, "active_connection", grp_id)
    await message.reply_text("✅ Group connected successfully!")
    
 
@Client.on_message(filters.command("connected") & filters.private)
async def connect_group_pm(client, message):
    # User must provide group id to connect
    try:
        text = message.text.split()
        if len(text) < 2:
            return await message.reply_text("Usage: /connect <group_id>")

        group_id = int(text[1])
        user_id = message.from_user.id

        success = await add_connection(group_id, user_id)
        if success:
            await message.reply_text(f"✅ Connected to group {group_id} successfully!")
        else:
            await message.reply_text(f"⚠ Already connected to group {group_id}")

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")   
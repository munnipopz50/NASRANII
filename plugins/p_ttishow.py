from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS, MELCOW_VID, CHNL_LNK, GRP_LNK
from database.users_chats_db import db
from database.users_chats_db import db as userdb
from database.ia_filterdb import Media, Media2,  db as clientDB, db2 as clientDB2
from database.ia_filterdb import stats_col, get_last_files

from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired
import asyncio 
from database.ia_filterdb import get_year_wise_count

"""-----------------------------------------https://t.me/GetTGLink/4179 --------------------------------------"""

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import mycol, mycol2
from database.connections_mdb import all_connections

import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from pyrogram import filters, Client, enums
from info import *
import asyncio
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp
    


def circles(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):

    background = Image.open("plugins/helpers/dil.png").convert("RGBA")

    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)

    # profile size
    pfp = pfp.resize((440, 440))

    # profile position
    pfp_position = (160, 136)

    # paste profile
    background.paste(pfp, pfp_position, pfp)

    draw = ImageDraw.Draw(background)

    # font
    font = ImageFont.truetype("plugins/helpers/font.ttf", 40)

    # text positions
    draw.text((700, 255), f"NAME : {user}", fill="white", font=font)

    draw.text((700, 325), f"ID : {id}", fill="white", font=font)

    draw.text((700, 395), f"USERNAME : @{uname}", fill="white", font=font)

    output = f"{id}.png"

    background.save(output)

    return output




def spellcheck(pic, display_name, mv_rqst, user, chatname, id, uname):
    print("pic =", pic)
    print("display_name =", display_name)
    name = f"@{uname}" if uname else user
    background = Image.open("plugins/helpers/dil.png").convert("RGBA")

    try:
        pfp = Image.open(pic).convert("RGBA")
    except Exception as e:
        print(f"DP Error: {e}")
        pfp = Image.open("plugins/helpers/spell.png").convert("RGBA")

    pfp = circle(pfp)

    # profile size
    pfp = pfp.resize((440, 440))

    # profile position
    pfp_position = (160, 136)

    # paste profile
    background.paste(pfp, pfp_position, pfp)

    draw = ImageDraw.Draw(background)

    # font
    font = ImageFont.truetype("plugins/helpers/font.ttf", 40)

    # text positions
    draw.text((700, 255), f"𝐍𝐚𝐦𝐞 : {name}", fill="white", font=font)

    draw.text((700, 325), f"𝐈𝐝 : {id}", fill="white", font=font)

    draw.text((700, 395), f"𝐒𝐞𝐚𝐫𝐜𝐡 : {mv_rqst}", fill="white", font=font)

    output = f"{id}.png"

    background.save(output)

    return output






import os  # ഫയൽ ഡിലീറ്റ് ചെയ്യാൻ ആവശ്യമാണ് (കോഡിന്റെ ഏറ്റവും മുകളിൽ ഉണ്ടെങ്കിൽ വീണ്ടും കൊടുക്കേണ്ടതില്ല)

@Client.on_message(filters.new_chat_members & filters.group)
async def welcome(client, message):

    for user in message.new_chat_members:

        me = await client.get_me()

        if user.id == me.id:
            if not await userdb.get_chat(message.chat.id):
                await user.add_chat(message.chat.id, message.chat.title)

        try:
            pic = await client.download_media(
                user.photo.big_file_id,
                file_name=f"{user.id}.png"
            )
        except:
            pic = "plugins/helpers/dil.png"

        # 1. വെൽക്കം ഇമേജ് താൽക്കാലികമായി ഉണ്ടാക്കുന്നു
        welcomeimg = welcomepic(
            pic,
            user.first_name,
            message.chat.title,
            user.id,
            user.username if user.username else "No Username"
        )

        try:
            # 2. ആദ്യം ഇമേജ് LOG_CHANNEL-ലേക്ക് അപ്‌ലോഡ് ചെയ്യുന്നു
            # (ശ്രദ്ധിക്കുക: നിങ്ങളുടെ info.py ഫയലിൽ LOG_CHANNEL ഡിഫൈൻ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക)
            from info import LOG_CHANNEL
            log_msg = await client.send_photo(
                chat_id=LOG_CHANNEL,
                photo=welcomeimg,
                caption=f"#WelcomeImage\nUser: {user.mention}\nGroup: {message.chat.title}"
            )
            
            # LOG_CHANNEL-ൽ അപ്‌ലോഡ് ആയ ഫയലിന്റെ ടെലഗ്രാം file_id എടുക്കുന്നു
            telegram_file_id = log_msg.photo.file_id
        except Exception as log_err:
            print(f"Error uploading to LOG_CHANNEL: {log_err}")
            # ഒരുപക്ഷേ LOG_CHANNEL വർക്ക് ആയില്ലെങ്കിൽ നേരിട്ട് ഫയൽ അയക്കാൻ വേണ്ടിയുള്ള ബാക്കപ്പ്
            telegram_file_id = welcomeimg

        # 3. ഗ്രൂപ്പിലേക്ക് ഇമേജ് അയക്കുന്നു (ഇപ്പോൾ സെർവറിൽ നിന്നല്ല, ടെലഗ്രാം സെർവറിൽ നിന്നാണ് നേരിട്ട് പോകുന്നത്)
        await client.send_photo(
            chat_id=message.chat.id,
            photo=telegram_file_id,
            caption=f"""
Welcome {user.mention}

ID : {user.id}
Username : @{user.username}
"""
        )
        
        # 4. 🧹 ഹോസ്റ്റിലെ (സെർവർ) സ്റ്റോറേജ് ഫ്രീ ആക്കാൻ താൽക്കാലിക ഫയലുകൾ അപ്പോൾത്തന്നെ ഡിലീറ്റ് ചെയ്യുന്നു
        try:
            if os.path.exists(welcomeimg) and welcomeimg != "plugins/helpers/dil.png":
                os.remove(welcomeimg)
            if os.path.exists(pic) and pic != "plugins/helpers/dil.png":
                os.remove(pic)
            print(f"[CLEANUP] Successfully removed temporary images for user {user.id}")
        except Exception as clean_err:
            print(f"Error during file cleanup: {clean_err}")
    
    
@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    count = await bot.get_chat_members_count(message.chat.id)
    settings = await get_settings(message.chat.id)
    if settings["welcome"]:    
        k = await bot.send_message(chat_id=message.chat.id, text=f"𝐇𝐞𝐥𝐥𝐨: {message.from_user.mention}\n {message.chat.title} \n𝐘𝐨𝐮𝐫 𝐈𝐝: {message.from_user.id} \n𝐓𝐨𝐭𝐚𝐥 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {count}")
        await message.delete()     
        await asyncio.sleep(60)
        await k.delete()
       


                    
               

@Client.on_message(filters.left_chat_member)
async def end(bot, message):
    count = await bot.get_chat_members_count(message.chat.id)
    settings = await get_settings(message.chat.id)
    if settings["welcome"]:    
        k = await bot.send_message(chat_id=message.chat.id, text=f"𝐇𝐞𝐥𝐥𝐨: {message.from_user.mention}😞 \n 𝐁𝐲 𝐁𝐲... {message.chat.title} \n𝐘𝐨𝐮𝐫 𝐈𝐝: {message.from_user.id} \n𝐓𝐨𝐭𝐚𝐥 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {count}")
        await message.delete()     
        await asyncio.sleep(30)
        await k.delete()

@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hello Friends, \nMy admin has told me to leave from group so i go! If you wanna add me again contact my support group.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat Not Found In DB")
    if cha_t['is_disabled']:
        return await message.reply(f"This chat is already disabled:\nReason-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Chat Successfully Disabled')
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Hello Friends, \nMy admin has told me to leave from group so i go! If you wanna add me again contact my support group.</b> \nReason : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat Not Found In DB !")
    if not sts.get('is_disabled'):
        return await message.reply('This chat is not yet disabled.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat Successfully re-enabled")
    
    
    
@Client.on_message(filters.command('stats') & filters.incoming)
async def get_stats(bot, message):
    # ബോട്ട് ഓണർമാർക്ക്/അഡ്മിൻമാർക്ക് മാത്രം കാണാൻ (ആവശ്യമെങ്കിൽ)
    # if message.from_user.id not in ADMINS: return

    rju = await message.reply('Fetching stats.. ⏳')
    
    # Movie Requests
    movie_requests = await db.get_movie_request_count()
    noresult_requests = await db.get_noresult_request_count()
    top_groups = await db.get_top_groups()
    
    # Files Count
    totalp = await Media.count_documents({})
    totalsec = await Media2.count_documents({})

    # Users and chats
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()

    # Duplicate Files Count
    duplicate_doc = await stats_col.find_one({"_id": "duplicate_files"})
    duplicate_count = duplicate_doc.get("count", 0) if duplicate_doc else 0

    total_index_files = totalp + totalsec + duplicate_count
    
    # DB 1 Size
    stats = await clientDB.command('dbStats')
    used_dbSize = (stats['dataSize'] / (1024*1024)) + (stats['indexSize'] / (1024*1024))
    free_dbSize = 512 - used_dbSize

    # DB 2 Size
    stats2 = await clientDB2.command('dbStats')
    used_dbSize2 = (stats2['dataSize'] / (1024*1024)) + (stats2['indexSize'] / (1024*1024))
    free_dbSize2 = 512 - used_dbSize2
    
    # Connected groups count (ശരിയാക്കിയ ഭാഗം - async for ഉപയോഗിച്ചു)
    connected_groups = 0
    for doc in mycol.find({}, {"group_details": 1}):
        connected_groups += len(doc.get("group_details", []))
        
    group_text = "\n".join(
        f"{i}. {grp.get('title', 'Unknown')}"
        for i, grp in enumerate(top_groups, start=1)
    )
    
    # Year wise data
    year_data = await get_year_wise_count()
    year_text = ""

    for year in sorted(
        [y for y in year_data.keys() if y != "Others"],
        reverse=True
    ):
        year_text += f"{year} = {year_data[year]} files\n"

    if "Others" in year_data:
        year_text += f"Others = {year_data['Others']} files"

    # Edit message with all stats
    await rju.edit(
        script.STATUS_TXT.format(
            (totalp + totalsec),       # Total files
            connected_groups,          # Connected groups
            total_users,               # Total users
            totl_chats,                # Total chats
            totalp,                    # Primary files (filesp-ക്ക് പകരം totalp നൽകി)
            round(used_dbSize, 2),     # Primary used storage
            round(free_dbSize, 2),     # Primary free storage
            totalsec,                  # Secondary files
            round(used_dbSize2, 2),    # Secondary used storage
            round(free_dbSize2, 2),    # Secondary free storage
            total_index_files,
            movie_requests,
            noresult_requests,
            group_text,
            year_text
        )
    )    
    
    
    
    
    


@Client.on_message(filters.command('statss') & filters.incoming)
async def get_statss(bot, message):
    rju = await message.reply('Fetching stats..')
    # minnal murali 
    movie_requests = await db.get_movie_request_count()
    noresult_requests = await db.get_noresult_request_count()
    top_groups = await db.get_top_groups()
    totalp = await Media.count_documents({})
    totalsec = await Media2.count_documents({})


    # Users and chats
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()

    # Files count
    filesp = await Media.count_documents()       # Primary DB
    totalsec = await Media2.count_documents()
    duplicate_doc = await stats_col.find_one({"_id": "duplicate_files"})
    duplicate_count = duplicate_doc.get("count", 0) if duplicate_doc else 0
# Secondary DB

    total_index_files = totalp + totalsec + duplicate_count
    

    # DB size
    stats = await clientDB.command('dbStats')
    used_dbSize = (stats['dataSize'] / (1024*1024)) + (stats['indexSize'] / (1024*1024))
    free_dbSize = 512 - used_dbSize

    stats2 = await clientDB2.command('dbStats')
    used_dbSize2 = (stats2['dataSize'] / (1024*1024)) + (stats2['indexSize'] / (1024*1024))
    free_dbSize2 = 512 - used_dbSize2
    
   
    # Connected groups count
    connected_groups = 0
    for doc in mycol.find({}, {"group_details": 1}):
        connected_groups += len(doc.get("group_details", []))
        
        
    group_text = "\n".join(
        f"{i}. {grp.get('title', 'Unknown')}"
        for i, grp in enumerate(top_groups, start=1)
    )
    year_data = await get_year_wise_count()

    year_text = ""

    for year in sorted(
        [y for y in year_data.keys() if y != "Others"],
        reverse=True
    ):
        year_text += f"{year} = {year_data[year]} files\n"

    if "Others" in year_data:
        year_text += f"Others = {year_data['Others']} files"
    print(year_text)
        

    # Edit message with all stats
    await rju.edit(
        script.STATUS_TXT.format(
            (filesp + totalsec),       # Total files
            connected_groups,          # Connected groups
            total_users,               # Total users
            totl_chats,                # Total chats
            filesp,                    # Primary files
            round(used_dbSize, 2),     # Primary used storage
            round(free_dbSize, 2),     # Primary free storage
            totalsec,                  # Secondary files
            round(used_dbSize2, 2),    # Secondary used storage
            round(free_dbSize2, 2),     # Secondary free storage
            total_index_files,
            movie_requests,
            noresult_requests,
#            totalp + totalsec,          # Total files from both DBs
#            top_groups,
            group_text,
            year_text
            
            
        )
    )
    
    

@Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Invite Link Generation Failed, Iam Not Having Sufficient Rights")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is already banned\nReason: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Successfully banned {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("Thismight be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Successfully unbanned {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Getting List Of chats')
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Disabled Chat )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")

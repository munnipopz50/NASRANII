import pyrogram
import sys

print("Pyrogram:", pyrogram.__version__)
print("Python:", sys.version)

from pyrogram import Client, filters

import pyrogram
print(pyrogram.__version__)
import re
import os
import json
import asyncio  # 👈 ഈ വരി ഫയലിന്റെ ഏറ്റവും മുകളിൽ ചേർക്കുക
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import *
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>➲ First Name:</b> {first}\n<b>➲ Last Name:</b> {last}\n<b>➲ Username:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += (
            "<b>➲ Chat ID</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>➲ Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➲First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➲Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>➲Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➲User Name:</b> @{username}\n"
    message_out_str += f"<b>➲User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in ((enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL)):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = (
                chat_member_p.joined_date or datetime.now()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
    await status_message.delete()

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# നിങ്ങളുടെ ഫയലിലെ imdb_search ഫങ്ക്ഷൻ മാറ്റി താഴെയുള്ളത് നൽകുക:
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# പ്രൊജക്റ്റിലെ മറ്റ് ആവശ്യമായ എററുകൾ ഇവിടെ ഇമ്പോർട്ട് ചെയ്യുക (ഉദാഹരണത്തിന്: MediaEmpty...)

@Client.on_message(filters.command("imdb") & filters.incoming)
async def imdb_search(client, message):
    if len(message.command) < 2:
        return await message.reply_text("ഉപയോഗിക്കേണ്ട രീതി: /imdb movie_name")
        
    query = message.text.split(None, 1)[1]
    msg = await message.reply_text("തിരയുന്നു... ⏳")

    try:
        movies_res = await get_poster(query, bulk=True)

        if not movies_res:
            return await msg.edit("ക്ഷമിക്കണം, അങ്ങനെയൊരു മൂവി കണ്ടെത്താൻ കഴിഞ്ഞില്ല! ❌")

        if isinstance(movies_res, dict):
            movies_res = [movies_res]

        btn = []

        for movie in movies_res:
            if isinstance(movie, dict):
                # get_poster രീതിയും OMDB രീതിയും മാറി വന്നാലും വർക്കാവാൻ വേണ്ടി:
                title = movie.get('title') or movie.get('Title') or "Unknown"
                year = movie.get('year') or movie.get('Year') or "N/A"
                imdb_id = movie.get('imdb_id') or movie.get('imdbID') or "none"
                callback_value = f"imdb#{imdb_id}"
            else:
                title = str(movie)
                year = "N/A"
                callback_value = "imdb#none"

            btn.append([
                InlineKeyboardButton(text=f"{title} - {year}", callback_data=callback_value)
            ])

        if btn:
            await msg.edit(
                text=f"**'{query}'** എന്നതിനായി കണ്ടെത്തിയ ഫലങ്ങൾ 👇",
                reply_markup=InlineKeyboardMarkup(btn)
            )
        else:
            await msg.edit("ഫലങ്ങളൊന്നും ലഭ്യമായില്ല! ❌")

    except Exception as e:
        await msg.edit(f"ഒരു എറർ സംഭവിച്ചു: `{str(e)}`")


@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(client, quer_y):
    i, movie_id = quer_y.data.split('#')
    
    if movie_id == "none":
        return await quer_y.answer("ID ലഭ്യമല്ല! ❌", show_alert=True)

    await quer_y.answer("വിവരങ്ങൾ ശേഖരിക്കുന്നു... ⏳")

    try:
        api_base = globals().get('IMDB_API_BASE') or "http://www.omdbapi.com/"
        api_key = globals().get('OMDB_API_KEY')
        details_url = f"{api_base}?apikey={api_key}&i={movie_id}"
        
        movie = await asyncio.to_thread(lambda: requests.get(details_url).json())
        
        if movie.get("Response") == "False":
            return await quer_y.message.edit("വിവരങ്ങൾ ലഭ്യമായില്ല! ❌")

        plot = movie.get("Plot") or ""
        if plot and len(plot) > 800:
            plot = plot[:800] + "..."

        imdb = {
            'title': movie.get('Title'),
            'votes': movie.get('imdbVotes', 'N/A'),
            "aka": "N/A",
            "seasons": movie.get('totalSeasons', 'N/A'),
            "box_office": movie.get('BoxOffice', 'N/A'),
            'localized_title': movie.get('Title'),
            'kind': movie.get("Type", "movie"),
            "imdb_id": movie.get('imdbID'),
            "cast": movie.get("Actors", "N/A"),
            "runtime": movie.get("Runtime", "N/A"),
            "countries": movie.get("Country", "N/A"),
            "certificates": movie.get("Rated", "N/A"),
            "languages": movie.get("Language", "N/A"),
            "director": movie.get("Director", "N/A"),
            "writer": movie.get("Writer", "N/A"),
            'release_date': movie.get("Released") or movie.get("Year") or "N/A",
            'year': movie.get('Year'),
            'genres': movie.get("Genre", "N/A"),
            'poster': movie.get('Poster'),
            'plot': plot,
            'rating': str(movie.get("imdbRating", "N/A")),
            'url': f"https://www.imdb.com/title/{movie_id}"
        }

    except Exception as e:
        return await quer_y.message.edit(f"ഒരു എറർ സംഭവിച്ചു: {e}")

    user = quer_y.from_user
    username = f"@{user.username}" if user.username else user.mention
    first_name = user.first_name
    user_id = user.id

    query = imdb['title']
    title = imdb['title']
    votes = imdb['votes']
    aka = imdb["aka"]
    seasons = imdb["seasons"]
    box_office = imdb['box_office']
    localized_title = imdb['localized_title']
    kind = imdb['kind']
    imdb_id = imdb["imdb_id"]
    cast = imdb["cast"]
    runtime = imdb["runtime"]
    countries = imdb["countries"]
    certificates = imdb["certificates"]
    languages = imdb["languages"]
    director = imdb["director"]
    writer = imdb["writer"]
    producer = "N/A"
    composer = "N/A"
    cinematographer = "N/A"
    music_team = "N/A"
    distributors = "N/A"
    release_date = imdb['release_date']
    year = imdb['year']
    genres = imdb['genres']
    poster = imdb['poster']
    plot = imdb['plot']
    rating = imdb['rating']
    url = imdb['url']

    caption = IMDB_TEMPLATE.format(**locals())

    # ✅ പുതിയ ബട്ടണുകൾ: IMDb ലിങ്കും ഒപ്പം സ്റ്റിക്കർ പാക്ക് ക്രിയേറ്റ് ചെയ്യാനുള്ള ബട്ടണും
    btn = [
        [InlineKeyboardButton(text=f"{imdb['title']}", url=imdb['url'])],
        [InlineKeyboardButton(text="Create Sticker Pack 🎭", callback_data=f"mks_stk#{movie_id}")]
    ]
    
    if imdb.get('poster') and imdb['poster'] != "N/A":
        try:
            await quer_y.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
            await quer_y.message.delete()
        except Exception:
            await quer_y.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
    else:
        await quer_y.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)


# --- CREATE STICKER PACK CALLBACK ---
import json
import os
import re
import requests
import asyncio
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import os
import re
import requests
import asyncio
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# --- STEP 1: SEND STICKER WITH TINY CALLBACK DATA ---
import json
import os
import re
import requests
import asyncio
from io import BytesIO
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ബ്രൗസർ ആണെന്ന് സെർവറിനെ വിശ്വസിപ്പിക്കാനുള്ള ഹെഡ്ഡർ
import json
import os
import re
import requests
import asyncio
from io import BytesIO
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ബ്രൗസർ ആണെന്ന് സെർവറിനെ വിശ്വസിപ്പിക്കാനുള്ള ഹെഡ്ഡർ
HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# --- STEP 1: SEND GENUINE STICKER WITH INTEGRATED BUTTON ---
@Client.on_callback_query(filters.regex('^mks_stk'))
async def make_sticker_callback(client, quer_y):
    _, movie_id = quer_y.data.split('#')
    user_id = quer_y.from_user.id
    
    await quer_y.answer("ഫോട്ടോ സ്റ്റിക്കർ ആക്കുന്നു... ⏳", show_alert=False)
    prog_msg = await quer_y.message.reply_text("ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുന്നു... 📥")

    try:
        # 1. OMDB-യിൽ നിന്ന് പോസ്റ്റർ ലിങ്ക് എടുക്കുന്നു
        api_base = globals().get('IMDB_API_BASE') or "http://www.omdbapi.com/"
        api_key = globals().get('OMDB_API_KEY')
        movie = await asyncio.to_thread(lambda: requests.get(f"{api_base}?apikey={api_key}&i={movie_id}").json())
        poster_url = movie.get('Poster')

        if not poster_url or poster_url == "N/A":
            return await prog_msg.edit("ഈ സിനിമയ്ക്ക് പോസ്റ്റർ ലഭ്യമല്ല! ❌")

        temp_path = f"temp_{movie_id}.jpg"
        stk_path = f"sticker_{movie_id}.png"
        
        # 2. ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുന്നു
        download_success = False
        try:
            response = requests.get(poster_url, headers=HTTP_HEADERS, timeout=10)
            if response.status_code == 200 and len(response.content) > 100:
                with open(temp_path, 'wb') as f:
                    f.write(response.content)
                download_success = True
        except Exception:
            pass

        if not download_success:
            try:
                await prog_msg.edit("സെർവർ മാറ്റി ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യാൻ ശ്രമിക്കുന്നു... 🔄")
                sent_doc = await client.send_document(chat_id=user_id, document=poster_url)
                await client.download_media(message=sent_doc, file_name=temp_path)
                await sent_doc.delete()
                download_success = True
            except Exception:
                try:
                    fallback_url = re.sub(r'._V1_.*\.jpg', '._V1_SX300.jpg', poster_url)
                    response = requests.get(fallback_url, headers=HTTP_HEADERS, timeout=10)
                    if response.status_code == 200:
                        with open(temp_path, 'wb') as f:
                            f.write(response.content)
                        download_success = True
                except Exception:
                    download_success = False

        if not download_success or not os.path.exists(temp_path):
            return await prog_msg.edit("ഈ സിനിമയുടെ പോസ്റ്റർ ലിങ്ക് പൂർണ്ണമായും ബ്ലോക്ക് ചെയ്യപ്പെട്ടിരിക്കുന്നു! ❌")

        await prog_msg.edit("സ്റ്റിക്കർ ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു... 🎨")

        # 3. PIL ഇമേജ് കൺവെർഷൻ
        try:
            image = Image.open(temp_path)
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGBA")
        except Exception:
            try:
                with open(temp_path, 'rb') as f:
                    img_data = f.read()
                image = Image.open(BytesIO(img_data))
                image = image.convert("RGBA")
            except Exception:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                return await prog_msg.edit("സിനിമയുടെ ഫോട്ടോ ഫയൽ കേടായതാണ്, സ്റ്റിക്കർ ആക്കാൻ കഴിയില്ല! ❌")

        image.thumbnail((512, 512))
        new_image = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        new_image.paste(image, ((512 - image.width) // 2, (512 - image.height) // 2))
        new_image.save(stk_path, "PNG")

        if os.path.exists(temp_path):
            os.remove(temp_path)

        await prog_msg.edit("യഥാർത്ഥ സ്റ്റിക്കർ അയക്കുന്നു... 📤")

        # 4. Telegram Bot API വഴി സ്റ്റിക്കറും ബട്ടണും അയക്കുന്നു
        bot_token = client.bot_token
        inline_keyboard = {
            "inline_keyboard": [
                [{"text": "Pack ലേക്ക് ആഡ് ചെയ്യുക 🎭", "callback_data": f"add_to_pk#{movie_id}"}]
            ]
        }
        
        payload = {
            'chat_id': user_id,
            'reply_markup': json.dumps(inline_keyboard)
        }
        
        with open(stk_path, 'rb') as sticker_file:
            files = {'sticker': sticker_file}
            res_data = requests.post(
                f"https://api.telegram.org/bot{bot_token}/sendSticker",
                data=payload,
                files=files
            ).json()

        await prog_msg.delete()

        if not res_data.get("ok"):
            err_desc = res_data.get("description", "Unknown Error")
            await client.send_message(chat_id=user_id, text=f"സ്റ്റിക്കർ അയക്കാൻ കഴിഞ്ഞില്ല: `{err_desc}` ❌")

        if os.path.exists(stk_path):
            os.remove(stk_path)

    except Exception as e:
        await prog_msg.edit(f"ഒരു എറർ സംഭവിച്ചു: `{str(e)}`")


# --- STEP 2: ADD TO ONE SINGLE PACK PER USER & SEND STICKER ---
@Client.on_callback_query(filters.regex('^add_to_pk'))
async def add_to_pack_callback(client, quer_y):
    _, movie_id = quer_y.data.split('#')
    user_id = quer_y.from_user.id
    
    await quer_y.answer("പാക്കിലേക്ക് മാറ്റുന്നു... ⏳", show_alert=False)
    status_msg = await quer_y.message.reply_text("ടെലിഗ്രാം സെർവറുമായി ബന്ധിപ്പിക്കുന്നു... ⚙️")

    try:
        # 1. OMDB-യിൽ നിന്ന് വിവരങ്ങൾ എടുക്കുന്നു
        api_base = globals().get('IMDB_API_BASE') or "http://www.omdbapi.com/"
        api_key = globals().get('OMDB_API_KEY')
        movie = await asyncio.to_thread(lambda: requests.get(f"{api_base}?apikey={api_key}&i={movie_id}").json())
        poster_url = movie.get('Poster')
        movie_title = movie.get('Title', 'Movie')

        temp_path = f"temp_pk_{movie_id}.jpg"
        stk_path = f"sticker_pk_{movie_id}.png"
        
        # 2. ഫോട്ടോ പാക്കിലേക്ക് അപ്‌ലോഡ് ചെയ്യാൻ തയാറാക്കുന്നു
        download_success = False
        try:
            response = requests.get(poster_url, headers=HTTP_HEADERS, timeout=10)
            if response.status_code == 200:
                with open(temp_path, 'wb') as f:
                    f.write(response.content)
                download_success = True
        except Exception:
            pass

        if not download_success:
            try:
                sent_doc = await client.send_document(chat_id=user_id, document=poster_url)
                await client.download_media(message=sent_doc, file_name=temp_path)
                await sent_doc.delete()
                download_success = True
            except Exception:
                try:
                    fallback_url = re.sub(r'._V1_.*\.jpg', '._V1_SX300.jpg', poster_url)
                    response = requests.get(fallback_url, headers=HTTP_HEADERS, timeout=10)
                    if response.status_code == 200:
                        with open(temp_path, 'wb') as f:
                            f.write(response.content)
                        download_success = True
                except Exception:
                    download_success = False

        if not download_success or not os.path.exists(temp_path):
            return await status_msg.edit("പോസ്റ്റർ ലഭ്യമാക്കാൻ കഴിഞ്ഞില്ല! ❌")

        try:
            image = Image.open(temp_path)
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGBA")
        except Exception:
            try:
                with open(temp_path, 'rb') as f:
                    img_data = f.read()
                image = Image.open(BytesIO(img_data))
                image = image.convert("RGBA")
            except Exception:
                return await status_msg.edit("പോസ്റ്റർ ലഭ്യമാക്കാൻ കഴിഞ്ഞില്ല! ❌")

        image.thumbnail((512, 512))
        new_image = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        new_image.paste(image, ((512 - image.width) // 2, (512 - image.height) // 2))
        new_image.save(stk_path, "PNG")

        if os.path.exists(temp_path):
            os.remove(temp_path)

        # 3. ഫിക്സഡ് പാക്ക് നെയിം സെറ്റ് ചെയ്യുന്നു
        bot_info = await client.get_me()
        bot_username = bot_info.username.lower()
        
        pack_name = f"mov{user_id}_by_{bot_username}".lower()
        pack_title = f"My Movie Pack - @{bot_username}"

        bot_token = client.bot_token
        
        # 4. പാക്ക് ഉണ്ടോ എന്ന് ചെക്ക് ചെയ്യുന്നു
        check_pack = requests.get(f"https://api.telegram.org/bot{bot_token}/getStickerSet?name={pack_name}").json()
        
        uploaded_sticker_id = None
        
        if check_pack.get("ok"):
            # പാക്ക് ഉണ്ടെങ്കിൽ ആഡ് ചെയ്യുന്നു
            await status_msg.edit("നിങ്ങളുടെ നിലവിലുള്ള പാക്കിലേക്ക് സ്റ്റിക്കർ ചേർക്കുന്നു... ⚙️")
            
            sticker_payload = {
                "user_id": int(user_id),
                "name": str(pack_name),
                "sticker": json.dumps({"sticker": f"attach://{stk_path}", "emoji_list": ["🎬"]})
            }
            
            with open(stk_path, 'rb') as sticker_file:
                files = {stk_path: sticker_file}
                response_res = requests.post(
                    f"https://api.telegram.org/bot{bot_token}/addStickerToSet",
                    data=sticker_payload,
                    files=files
                ).json()
        else:
            # പാക്ക് ഇല്ലെങ്കിൽ പുതിയത് ക്രിയേറ്റ് ചെയ്യുന്നു
            await status_msg.edit("പുതിയ സ്റ്റിക്കർ പാക്ക് നിർമ്മിക്കുന്നു... ⚙️")
            
            stickers_payload = [{"sticker": f"attach://{stk_path}", "emoji_list": ["🎬"]}]
            sticker_data = {
                "user_id": int(user_id),
                "name": str(pack_name),
                "title": str(pack_title),
                "stickers": json.dumps(stickers_payload),
                "sticker_format": "static"
            }
            
            with open(stk_path, 'rb') as sticker_file:
                files = {stk_path: sticker_file}
                response_res = requests.post(
                    f"https://api.telegram.org/bot{bot_token}/createNewStickerSet",
                    data=sticker_data,
                    files=files
                ).json()

        # 5. റിസൾട്ട് കാണിക്കുകയും ലാസ്റ്റ് ആ സ്റ്റിക്കർ ബോട്ടിലേക്ക് സെൻഡ് ചെയ്യുകയും ചെയ്യുന്നു
        if response_res.get("ok"):
            await status_msg.edit(
                text=f"🎉 **{movie_title} നിങ്ങളുടെ സ്റ്റിക്കർ പാക്കിലേക്ക് ആഡ് ചെയ്തിട്ടുണ്ട്!**\n\n👇 താഴെയുള്ള ലിങ്കിൽ ക്ലിക്ക് ചെയ്ത് പാക്ക് കാണാം:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="Open Sticker Pack 🎭", url=f"https://t.me/addstickers/{pack_name}")]
                ])
            )
            
            # 💡 പുതിയ ഫീച്ചർ: പാക്കിലേക്ക് അപ്‌ലോഡ് ചെയ്ത ആ സ്റ്റിക്കർ ഫയൽ തന്നെ യൂസർക്ക് നേരിട്ട് ബോട്ടിലേക്ക് അയക്കുന്നു
            try:
                # ടെലിഗ്രാമിൽ നിന്ന് ആ പാക്കിലെ സ്റ്റിക്കർ വിവരങ്ങൾ എടുക്കുന്നു
                updated_pack = requests.get(f"https://api.telegram.org/bot{bot_token}/getStickerSet?name={pack_name}").json()
                if updated_pack.get("ok") and updated_pack["result"].get("stickers"):
                    # പാക്കിലെ ഏറ്റവും അവസാനത്തെ (ഇപ്പോൾ ആഡ് ചെയ്ത) സ്റ്റിക്കറിന്റെ file_id എടുക്കുന്നു
                    last_sticker_id = updated_pack["result"]["stickers"][-1]["file_id"]
                    
                    # ആ സ്റ്റിക്കർ ഐഡി വെച്ച് ബോട്ട് നേരിട്ട് ചാറ്റിലേക്ക് സെൻഡ് ചെയ്യുന്നു
                    await client.send_sticker(chat_id=user_id, sticker=last_sticker_id)
            except Exception:
                pass # സ്റ്റിക്കർ സെൻഡ് ചെയ്യുന്നതിൽ എന്തെങ്കിലും തടസ്സമുണ്ടായാൽ മെസ്സേജ് ബ്ലോക്ക് ആകാതിരിക്കാൻ
                
        else:
            desc = response_res.get("description", "Unknown Error")
            if "occupied" in desc or "already" in desc:
                await status_msg.edit(
                    text=f"🎉 **നിങ്ങളുടെ സ്റ്റിക്കർ പാക്ക് ലിങ്ക് ഇവിടെ ലഭ്യമാണ്:** 👇",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(text="Open Sticker Pack 🎭", url=f"https://t.me/addstickers/{pack_name}")]
                    ])
                )
            else:
                await status_msg.edit(f"ക്ഷമിക്കണം, പാക്കിലേക്ക് ആഡ് ചെയ്യാൻ കഴിഞ്ഞില്ല: `{desc}` ❌")

        if os.path.exists(stk_path):
            os.remove(stk_path)

    except Exception as e:
        await status_msg.edit(f"ഒരു എറർ സംഭവിച്ചു: `{str(e)}`")
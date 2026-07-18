import requests
print("Requests:", requests.__version__)

from PIL import Image
print("Pillow OK")

import pyrogram
import sys

print("Pyrogram:", pyrogram.__version__)
print("Python:", sys.version)

from pyrogram import Client, filters
import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media, Media2, choose_mediaDB, db as clientDB
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, SECONDDB_URI
from utils import temp, get_poster
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from sample_info import tempDict

from pyrogram import idle
from database.connections_mdb import db as connection_db
from info import *
import aiohttp
from plugins.index import resume_index_jobs
from plugins.index import index_files_to_db, resume_col
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ➕ [ADDITIONS FOR FIXING WEB PLAYER STREAMING]
from aiohttp import web
import os
import re
import asyncio

PORT = int(os.environ.get("PORT", 8080))

# 📺 വെബ്‌സൈറ്റിൽ പ്ലേ ചെയ്യാനും നേരിട്ട് ഡൗൺലോഡ് ചെയ്യാനുമുള്ള HTML പ്ലെയർ പേജ്
async def stream_handler(request):
    file_id = request.match_info.get('file_id')
    if not file_id:
        return web.Response(text="Invalid File ID", status=400)

    # ഡിഫോൾട്ട് പോസ്റ്റർ ലിങ്ക് (IMDb ലഭിച്ചില്ലെങ്കിൽ കാണിക്കാൻ)
    poster_url = "https://telegra.ph/file/fcc849db4bf5c517f0f8d.jpg" 
    movie_title = "Nasrani Movies"
    movie_info = "" # IMDb വിവരങ്ങൾ കാണിക്കാൻ

    try:
        from database.ia_filterdb import get_file_details
        # 💡 ശ്രദ്ധിക്കുക: നിങ്ങളുടെ ബോട്ട് കോഡിൽ get_poster എവിടെ നിന്നാണോ ഇമ്പോർട്ട് ചെയ്തിരിക്കുന്നത് ആ പാത്ത് ഇവിടെ നൽകുക
        # ഉദാഹരണത്തിന്: from utils import get_poster അല്ലെങ്കിൽ from plugins.helper.imdb import get_poster
        from utils import get_poster 
        
        files_ = await get_file_details(file_id)
        if files_:
            file_name = files_[0].file_name
            # ഫയൽ നെയിമിൽ നിന്നുള്ള ഡോട്ടുകൾ മാറ്റി ക്ലീൻ ആയ ഒരു സെർച്ച് ക്വറി ഉണ്ടാക്കുന്നു
            search_query = file_name.replace(".", " ").split("(")[0].strip()
            
            # 🎬 IMDb-യിൽ നിന്ന് പോസ്റ്ററും ഡീറ്റെയിൽസും ഫെച്ച് ചെയ്യുന്നു
            imdb = await get_poster(search_query, file=file_name)
            
            if imdb:
                # IMDb-യിൽ നിന്ന് ലഭിക്കുന്ന പോസ്റ്റർ യുആർഎൽ സെറ്റ് ചെയ്യുന്നു
                poster_url = imdb.get("poster") or imdb.get("image") or poster_url
                f_title = imdb.get("title", search_query)
                f_genres = imdb.get("genres", "N/A")
                f_year = imdb.get("year", "N/A")
                f_rating = imdb.get("rating", "N/A")
                
                movie_title = f_title
                # വെബ് പേജിൽ കാണിക്കാൻ വേണ്ടിയുള്ള എച്ച്ടിഎംഎൽ കോഡ്
                movie_info = f"""
                <div class="movie-meta">
                    <p><strong>🎭 Genres:</strong> {f_genres}</p>
                    <p><strong>📆 Year:</strong> {f_year} | <strong>🌟 Rating:</strong> {f_rating} / 10</p>
                </div>
                """
            else:
                # IMDb ഡീറ്റെയിൽസ് കിട്ടിയില്ലെങ്കിൽ പഴയപോലെ ക്യാപ്ഷൻ ചെക്ക് ചെയ്യും
                if files_[0].caption:
                    match = re.search(r'(https?://[^\s]+(?:jpg|jpeg|png))', files_[0].caption)
                    if match:
                        poster_url = match.group(1)
    except Exception as e:
        print(f"IMDb Web Player Error: {e}")
        # എന്തെങ്കിലും എറർ ഉണ്ടായാൽ ബാക്കപ്പ് ആയി പഴയ ക്യാപ്ഷൻ ലോജിക് വർക്ക് ചെയ്യും
        try:
            if files_ and files_[0].caption:
                match = re.search(r'(https?://[^\s]+(?:jpg|jpeg|png))', files_[0].caption)
                if match:
                    poster_url = match.group(1)
        except:
            pass

    host = request.headers.get('Host', '')
    protocol = "https" if request.secure or request.headers.get('X-Forwarded-Proto', '') == 'https' else "http"
    local_download_url = f"{protocol}://{host}/download_file/{file_id}"
    bot_link = "https://t.me/your_bot_username" # ഇവിടെ നിങ്ങളുടെ ബോട്ട് ലിങ്ക് മാറ്റുക

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{movie_title} - Web Player</title>
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <style>
            body {{ margin: 0; padding: 20px; background-color: #ffffff; color: #000000; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
            .header {{ text-align: center; margin-bottom: 20px; width: 100%; }}
            .header h1 {{ 
                margin: 0; 
                font-family: 'Lobster', cursive; 
                font-size: 35px; 
                color: #fff;
                text-transform: uppercase;
                text-shadow: 0 0 5px #ff00de, 0 0 10px #ff00de, 0 0 20px #ff00de, 0 0 40px #ff00de;
                animation: neon 1.5s infinite alternate;
                word-wrap: break-word;
                padding: 0 10px;
            }}
            @keyframes neon {{
                from {{ text-shadow: 0 0 5px #ff00de, 0 0 10px #ff00de, 0 0 20px #ff00de; }}
                to {{ text-shadow: 0 0 10px #00d2ff, 0 0 20px #00d2ff, 0 0 30px #00d2ff; }}
            }}
            .header a {{ color: #555; text-decoration: none; font-weight: bold; font-size: 16px; display: block; margin-top: 10px; }}
            .player-container {{ width: 90%; max-width: 600px; background: #f8f9fa; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); text-align: center; }}
            img {{ width: 180px; height: auto; border-radius: 10px; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2); object-fit: cover; }}
            video {{ width: 100%; background: #000; border-radius: 8px; margin-top: 10px; }}
            .movie-meta {{ background: #eaeaea; padding: 10px; border-radius: 8px; margin-bottom: 15px; font-size: 14px; text-align: center; line-height: 1.5; }}
            .movie-meta p {{ margin: 5px 0; }}
            .download-btn {{ display: inline-block; background-color: #00c853; color: white; padding: 12px 30px; font-size: 16px; font-weight: bold; text-decoration: none; border-radius: 25px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>{movie_title}</h1>
            <a href="{bot_link}" target="_blank">🤖 Click Here to Join Nasrani BOT</a>
        </div>
        <div class="player-container">
            <img src="{poster_url}" alt="Movie Poster">
            {movie_info}
            <video controls autoplay preload="auto" playsinline>
                <source src="{local_download_url}" type="video/mp4">
            </video>
            <br>
            <a href="{local_download_url}" class="download-btn" download>📥 Fast Download File</a>
        </div>
    </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html') 
 




# 📥 [ADVANCED STREAM ENGINE WITH RANGE & TOTAL SIZE SUPPORT]
# 📥 [FAST STREAM ENGINE WITH FIXED PYROGRAM CHUNK CONTROLLER FOR SEEKING]
async def download_file_handler(request):
    file_id = request.match_info.get('file_id')
    if not file_id:
        return web.Response(text="Invalid File ID", status=400)

    try:
        file_size = None
        file_name = f"{file_id}.mp4"
        
        try:
            from database.ia_filterdb import get_file_details
            files_ = await get_file_details(file_id)
            if files_:
                file_size = files_[0].file_size
                file_name = getattr(files_[0], 'file_name', file_name)
        except Exception:
            pass

        range_header = request.headers.get('Range', None)
        
        headers = {
            'Content-Type': 'video/mp4',
            'Accept-Ranges': 'bytes',
            'Content-Disposition': f'attachment; filename="{file_name}"',
            'Access-Control-Allow-Origin': '*'
        }

        # 💡 സിനിമ അടിച്ചു വിടുമ്പോൾ ഉള്ള കണക്ഷൻ ബ്ലോക്കിംഗ് ഒഴിവാക്കാനുള്ള ലോജിക്
        if range_header and file_size:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else file_size - 1
                
                headers['Content-Range'] = f'bytes {start}-{end}/{file_size}'
                headers['Content-Length'] = str(end - start + 1)
                headers['Connection'] = 'close' # 🛑 പഴയ കണക്ഷൻ ക്ലോസ് ചെയ്ത് റാം ഫ്രീ ആക്കുന്നു
                
                response = web.StreamResponse(status=206, reason='Partial Content', headers=headers)
                await response.prepare(request)
                
                # chunk_size കുറച്ച് നൽകുന്നതിലൂടെ വലിയ ഫയലുകൾ പ്ലേ ചെയ്യുമ്പോൾ സെർവറിന് ലോഡ് വരില്ല
                async for chunk in app.stream_media(file_id, offset=start):
                    try:
                        await response.write(chunk)
                    except (ConnectionResetError, BrokenPipeError):
                        break # ബ്രൗസർ കണക്ഷൻ നിർത്തിയാൽ ഉടൻ പൈത്തൺ കോഡും സ്റ്റോപ്പ് ചെയ്യും
                return response

        # സാധാരണ ഡൗൺലോഡ് രീതി
        if file_size:
            headers['Content-Length'] = str(file_size)
        headers['Connection'] = 'keep-alive'

        response = web.StreamResponse(status=200, reason='OK', headers=headers)
        await response.prepare(request)
        
        async for chunk in app.stream_media(file_id):
            await response.write(chunk)
        return response

    except Exception as e:
        logging.error(f"Streaming Engine Error: {e}")
        return web.Response(text="Error playing file.", status=500)


# 🌐 മെയിൻ ലിങ്ക് പേജ്
async def main_page_handler(request):
    return web.Response(
        text="🚀 Nasrani Bot Stream Server is Live and Running via JustRunMy.App!",
        content_type="text/plain"
    )

async def start_jrma_server():
    server = web.Application()
    server.router.add_get('/', main_page_handler)
    server.router.add_get('/watch/{file_id}', stream_handler)
    server.router.add_get('/download_file/{file_id}', download_file_handler)
    
    runner = web.AppRunner(server)
    await runner.setup()
    
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logging.info(f"🚀 JustRunMy.App Web Server active via HTTPS on Port {PORT}")


# 🔄 Render-ൽ ബോട്ട് എപ്പോഴും ഓൺ ആയിരിക്കാൻ 5 മിനിറ്റ് കൂടുമ്പോൾ പിങ് ചെയ്യാനുള്ള ലോജിക്
 # 💡 ഫയലിന്റെ മുകളിൽ ഇല്ലെങ്കിൽ ഇത് ചേർക്കുക

# 🔄 Render-ൽ ബോട്ട് എപ്പോഴും ഓൺ ആയിരിക്കാൻ Async പിങ് ലോജിക്
async def send_ping(client):
    # ബോട്ട് സ്റ്റാർട്ട് ആയി 5 മിനിറ്റ് കഴിഞ്ഞ് മാത്രം ആദ്യത്തെ പിങ് (സെർവർ ഫ്രീ ആകാൻ)
    await asyncio.sleep(300) 
    while True:
        try:
            local_url = f"http://localhost:{PORT}"
            
            # 💡 requests-ന് പകരം കോഡിനെ ബ്ലോക്ക് ചെയ്യാത്ത aiohttp ഉപയോഗിക്കുന്നു
            async with aiohttp.ClientSession() as session:
                async with session.get(local_url, timeout=30) as response:
                    status = response.status
                    
                    if status == 200:
                        print(f"🟢 [PING SYSTEM] Self-Ping Successful: Status Code {status}", flush=True)
                        
                        # 📢 ടെലിഗ്രാം LOG_CHANNEL-ലേക്ക് മെസ്സേജ് അയക്കുന്നു
                        try:
                            await client.send_message(
                                chat_id=LOG_CHANNEL, 
                                text=f"🟢 **Self-Ping Successful**\nStatus Code: `{status}`\nTime: `{datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %I:%M:%S %p')}`"
                            )
                        except Exception as tg_err:
                            logging.error(f"Telegram Ping Log Failed: {tg_err}")
                    else:
                        raise Exception(f"Unexpected status code {status}")
                        
        except Exception as e:
            print(f"🔴 [PING SYSTEM] Self-Ping Failed: {e}", flush=True)
            
            # 📢 പരാജയപ്പെട്ടാൽ ചാനലിലേക്ക് അലേർട്ട് അയക്കുന്നു
            try:
                await client.send_message(
                    chat_id=LOG_CHANNEL, 
                    text=f"🔴 **Self-Ping Failed**\nError: `{e}`"
                )
            except:
                pass
                
        await asyncio.sleep(300) # 5 മിനിറ്റ് ഇടവേള


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        await Media2.ensure_indexes()
        
        await start_jrma_server()
        
        # 🔄 ഇവിടെ നമ്മൾ പിങ് ടാസ്ക് ബാക്ക്ഗ്രൗണ്ടിൽ സ്റ്റാർട്ട് ചെയ്യുന്നു
        asyncio.create_task(send_ping(self))

        stats = await clientDB.command('dbStats')
        free_dbSize = round(512-((stats['dataSize']/(1024*1024))+(stats['indexSize']/(1024*1024))), 2)
        if SECONDDB_URI and free_dbSize<10:
            tempDict["indexDB"] = SECONDDB_URI
            logging.info(f"Since Primary DB have only {free_dbSize} MB left, Secondary DB will be used to store datas.")
        elif SECONDDB_URI is None:
            logging.error("Missing second DB URI !\n\nAdd SECONDDB_URI now !\n\nExiting...")
            exit()
        else:
            logging.info(f"Since primary DB have enough space ({free_dbSize}MB) left, It will be used for storing datas.")
        await choose_mediaDB()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        logging.info(script.LOGO)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        custom_time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, custom_time))

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

app = Bot()
app.run()

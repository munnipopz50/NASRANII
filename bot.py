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


# 📺 വെബ്‌സൈറ്റിൽ പ്ലേ ചെയ്യാനും നേരിട്ട് ഡൗൺലോഡ് ചെയ്യാനുമുള്ള HTML പ്ലെയർ പേജ്
import re
import math
import urllib.parse  # 💡 ലിങ്ക് എൻകോഡ് ചെയ്യാൻ ഇത് വേണം
from aiohttp import web

PORT = int(os.environ.get("PORT", 8080))





def get_readable_file_size(size_in_bytes) -> str:
    if size_in_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_in_bytes / p, 2)
    return f"{s} {size_name[i]}"

async def stream_handler(request):
    file_id = request.match_info.get('file_id')
    if not file_id:
        return web.Response(text="Invalid File ID", status=400)

    poster_url = "https://telegra.ph/file/b25f4625752187f58385e.jpg" 
    movie_title = "Nasrani Movies"
    movie_info = ""
    display_name = "Unknown Movie"
    file_size = "N/A"

    try:
        from database.ia_filterdb import get_file_details
        from utils import get_poster 
        
        files_ = await get_file_details(file_id)
        if files_:
            file_name = files_[0].file_name
            display_name = file_name 
            file_size = get_readable_file_size(files_[0].file_size)
            
            search_query = file_name.replace(".", " ").split("(")[0].strip()
            imdb = await get_poster(search_query, file=file_name)
            
            caption_poster = None
            if files_[0].caption:
                match = re.search(r'(https?://[^\s]+(?:jpg|jpeg|png|webp))', files_[0].caption, re.IGNORECASE)
                if match:
                    caption_poster = match.group(1)

            if imdb and isinstance(imdb, dict):
                poster_url = imdb.get("poster") or imdb.get("image") or imdb.get("url") or caption_poster or poster_url
                f_title = imdb.get("title", search_query)
                f_genres = imdb.get("genres", "N/A")
                f_year = imdb.get("year", "N/A")
                f_rating = imdb.get("rating", "N/A")
                
                movie_title = f_title
                movie_info = f"""
                <div class="movie-meta">
                    <p><strong>🎭 Genres:</strong> {f_genres}</p>
                    <p><strong>📆 Year:</strong> {f_year} | <strong>🌟 Rating:</strong> {f_rating} / 10</p>
                </div>
                """
            else:
                if caption_poster:
                    poster_url = caption_poster
    except Exception as e:
        print(f"IMDb Web Player Error: {e}")
        try:
            if files_ and files_[0].caption:
                match = re.search(r'(https?://[^\s]+(?:jpg|jpeg|png|webp))', files_[0].caption, re.IGNORECASE)
                if match:
                    poster_url = match.group(1)
        except:
            pass

    host = request.headers.get('Host', '')
    protocol = "https" if request.secure or request.headers.get('X-Forwarded-Proto', '') == 'https' else "http"
    local_download_url = f"{protocol}://{host}/download_file/{file_id}"
    
    # 🛠️ MX Player-ന് വേണ്ടിയുള്ള ശരിയായ ആൻഡ്രോയിഡ് ഇന്റന്റ് ഘടന (Intent Syntax)
    mx_url = f"intent:{local_download_url}#Intent;package=com.mxtech.videoplayer.ad;S.title={urllib.parse.quote(display_name)};end"
    
    # 🛠️ VLC Player-ന് വേണ്ടിയുള്ള ശരിയായ ലിങ്ക് ഘടന
    vlc_url = f"vlc://{local_download_url}"
    
    bot_link = "https://t.me/your_bot_username" 

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{movie_title} - Web Player</title>
        <link href="https://fonts.googleapis.com/css2?family=Lobster&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{ margin: 0; padding: 20px; background-color: #141414; color: #ffffff; font-family: 'Poppins', sans-serif; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
            .header {{ text-align: center; margin-bottom: 20px; width: 100%; }}
            .header h1 {{ 
                margin: 0; font-family: 'Lobster', cursive; font-size: 38px; color: #fff; text-transform: uppercase;
                text-shadow: 0 0 5px #ff00de, 0 0 10px #ff00de, 0 0 20px #ff00de; animation: neon 1.5s infinite alternate; word-wrap: break-word; padding: 0 10px;
            }}
            @keyframes neon {{
                from {{ text-shadow: 0 0 5px #ff00de, 0 0 10px #ff00de, 0 0 20px #ff00de; }}
                to {{ text-shadow: 0 0 10px #00d2ff, 0 0 20px #00d2ff, 0 0 30px #00d2ff; }}
            }}
            .header a {{ color: #00d2ff; text-decoration: none; font-weight: bold; font-size: 16px; display: block; margin-top: 10px; }}
            .player-container {{ width: 95%; max-width: 650px; background: #1f1f1f; padding: 25px; border-radius: 15px; box-shadow: 0px 8px 25px rgba(0,0,0,0.5); text-align: center; box-sizing: border-box; }}
            .poster-img {{ width: 100%; max-width: 220px; height: 320px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0px 5px 15px rgba(0,0,0,0.6); object-fit: cover; border: 2px solid #333; }}
            
            /* 📺 വീഡിയോ കൺട്രോളുകൾ */
            video {{ width: 100%; background: #000; border-radius: 10px; margin-top: 15px; border: 1px solid #444; }}
            
            .file-details {{ background: #292929; padding: 15px; border-radius: 10px; text-align: left; margin-bottom: 15px; font-size: 14px; border-left: 4px solid #ff00de; }}
            .file-details p {{ margin: 6px 0; word-break: break-all; line-height: 1.4; }}
            .file-details strong {{ color: #00d2ff; }}
            
            .movie-meta {{ background: #292929; padding: 12px; border-radius: 10px; margin-bottom: 15px; font-size: 14px; text-align: center; border-left: 4px solid #00d2ff; }}
            .movie-meta p {{ margin: 5px 0; }}
            
            .apps-container {{ display: flex; justify-content: space-around; gap: 10px; margin: 20px 0 10px 0; flex-wrap: wrap; }}
            .app-btn {{ flex: 1; min-width: 140px; padding: 12px; font-weight: bold; text-decoration: none; border-radius: 8px; font-size: 14px; color: white; transition: 0.2s; text-align: center; display: inline-flex; align-items: center; justify-content: center; }}
            .vlc-btn {{ background-color: #ff8800; box-shadow: 0 4px 10px rgba(255,136,0,0.3); }}
            .mx-btn {{ background-color: #0055ff; box-shadow: 0 4px 10px rgba(0,85,255,0.3); }}
            .app-btn:hover {{ transform: translateY(-2px); }}

            .download-btn {{ display: block; width: 100%; background: linear-gradient(135deg, #00c853, #00b0ff); color: white; padding: 12px 20px; font-size: 16px; font-weight: bold; text-decoration: none; border-radius: 30px; margin-top: 15px; transition: 0.3s; box-shadow: 0 4px 15px rgba(0,200,83,0.4); box-sizing: border-box; }}
            .download-btn:hover {{ transform: scale(1.02); }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>{movie_title}</h1>
            <a href="{bot_link}" target="_blank">🤖 Click Here to Join Nasrani BOT</a>
        </div>
        
        <div class="player-container">
            <img src="{poster_url}" class="poster-img" alt="Movie Poster" onerror="this.src='https://telegra.ph/file/b25f4625752187f58385e.jpg';">
            
            <div class="file-details">
                <p><strong>🎬 File Name:</strong> {display_name}</p>
                <p><strong>💾 File Size:</strong> {file_size}</p>
            </div>

            {movie_info}
            
            <!-- 📺 വീഡിയോ പ്ലെയർ: അടിച്ചുവിടുമ്പോൾ കറക്കം മാറാൻ (preload="none" മാറ്റി ആവശ്യാനുസരണം ലോഡ് ചെയ്യാൻ ക്രമീകരിച്ചു) -->
            <video controls autoplay playsinline>
                <source src="{local_download_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>

            <!-- 📱 ആപ്പ് ബട്ടണുകൾ -->
            <div class="apps-container">
                <a href="{vlc_url}" class="app-btn vlc-btn">🧡 Watch in VLC</a>
                <a href="{mx_url}" class="app-btn mx-btn">💙 Watch in MX Player</a>
            </div>
            
            <a href="{local_download_url}" class="download-btn" download>📥 Fast Download File</a>
        </div>
    </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')
            
        
        



# 📥 [ADVANCED STREAM ENGINE WITH RANGE & TOTAL SIZE SUPPORT]

# 📥 [FAST STREAM ENGINE - FIXED PYROGRAM CHUNK CONTROLLER FOR SEEKING]
async def download_file_handler(request):
    file_id = request.match_info.get('file_id')
    if not file_id:
        return web.Response(text="Invalid File ID", status=400)

    try:
        file_size = None
        file_name = f"{file_id}.mp4"
        tg_file = None  # ടെലിഗ്രാം ഫയൽ ഒബ്ജക്റ്റ് സൂക്ഷിക്കാൻ
        
        try:
            from database.ia_filterdb import get_file_details
            files_ = await get_file_details(file_id)
            if files_:
                tg_file = files_[0] # 💡 നിങ്ങളുടെ ഡാറ്റാബേസിലെ ഫയൽ ഒബ്ജക്റ്റ്
                file_size = tg_file.file_size
                file_name = getattr(tg_file, 'file_name', file_name)
        except Exception as e:
            logging.error(f"DB Fetch Error: {e}")

        # ഡാറ്റാബേസിൽ ഫയൽ ഇല്ലെങ്കിൽ ലിങ്ക് വർക്ക് ആകില്ല
        if not tg_file:
            return web.Response(text="File not found in database", status=404)

        range_header = request.headers.get('Range', None)
        
        headers = {
            'Content-Type': 'video/mp4',
            'Accept-Ranges': 'bytes',
            'Content-Disposition': f'attachment; filename="{file_name}"',
            'Access-Control-Allow-Origin': '*'
        }

        # Pyrogram സാധാരണ ഉപയോഗിക്കുന്ന ചങ്ക് സൈസ് (1MB = 1024 * 1024 bytes)
        # നിങ്ങളുടെ ബോട്ട് നിർമ്മിച്ച ആൾ മാറ്റം വരുത്തിയിട്ടുണ്ടെങ്കിൽ അതനുസരിച്ച് ഇതും മാറ്റാം
        CHUNK_SIZE = 1024 * 1024 

        # 💡 സിനിമ അടിച്ചു വിടുമ്പോൾ (Seek ചെയ്യുമ്പോൾ) ഉള്ള ലോജിക്
        if range_header and file_size:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else file_size - 1
                
                # 🛠️ PYROGRAM CHUNK OFFSET கணക്കുകൂട്ടൽ (ഇതാണ് ഏറ്റവും പ്രധാനം)
                # ബൈറ്റുകളെ ചങ്കുകളുടെ എണ്ണത്തിലേക്ക് മാറ്റുന്നു
                chunk_offset = start // CHUNK_SIZE
                
                headers['Content-Range'] = f'bytes {start}-{end}/{file_size}'
                headers['Content-Length'] = str(end - start + 1)
                headers['Connection'] = 'close'
                
                response = web.StreamResponse(status=206, reason='Partial Content', headers=headers)
                await response.prepare(request)
                
                current_position = chunk_offset * CHUNK_SIZE
                
                # tg_file നേരിട്ട് നൽകുന്നു (ഇതിൽ യഥാർത്ഥ ഫയൽ ഐഡി ഉണ്ടാകും)
                async for chunk in app.stream_media(tg_file, offset=chunk_offset):
                    # പ്ലെയർ ആവശ്യപ്പെട്ടതിലും കൂടുതൽ ഡാറ്റ പോകാതിരിക്കാൻ
                    if current_position + len(chunk) > start:
                        # ആദ്യത്തെ ചങ്കിലെ ആവശ്യമില്ലാത്ത മുൻഭാഗം കളയാൻ (Skip bytes)
                        if current_position < start:
                            chunk = chunk[start - current_position:]
                        
                        # പ്ലെയർ ആവശ്യപ്പെട്ട ലിമിറ്റ് കഴിഞ്ഞാൽ കട്ട് ചെയ്യാൻ
                        if current_position + len(chunk) > end:
                            chunk = chunk[:end - current_position + 1]
                            try:
                                await response.write(chunk)
                            except:
                                break
                            break
                        
                        try:
                            await response.write(chunk)
                        except (ConnectionResetError, BrokenPipeError):
                            break
                    
                    current_position += len(chunk)
                return response

        # ⏳ സാധാരണ തുടക്കം മുതൽ ഉള്ള പ്ലേ അല്ലെങ്കിൽ ഡൗൺലോഡ് രീതി
        if file_size:
            headers['Content-Length'] = str(file_size)
        headers['Connection'] = 'keep-alive'

        response = web.StreamResponse(status=200, reason='OK', headers=headers)
        await response.prepare(request)
        
        async for chunk in app.stream_media(tg_file):
            try:
                await response.write(chunk)
            except (ConnectionResetError, BrokenPipeError):
                break
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

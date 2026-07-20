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
import plugins.sticker
print("MANUAL IMPORT SUCCESS")
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ➕ [ADDITIONS FOR FIXING WEB PLAYER STREAMING]
from aiohttp import web
import os
import re
import asyncio
import math
import urllib.parse  # 💡 ലിങ്ക് എൻകോഡ് ചെയ്യാൻ ഇത് വേണം

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

    # 🛠️ MX Player-ന് വേണ്ടിയുള്ള ശരിയായ ആൻഡ്രോയിഡ് ഇന്റന്റ് ഘടന
    mx_url = f"intent:{local_download_url}#Intent;type=video/*;package=com.mxtech.videoplayer.ad;S.title={urllib.parse.quote(display_name)};S.file_extension=.m3u;end"

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
            
            <video controls autoplay playsinline webkit-playsinline allowfullscreen="true">
                <source src="{local_download_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>

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

async def download_file_handler(request):
    file_id = request.match_info.get('file_id')
    if not file_id:
        return web.Response(text="Invalid File ID", status=400)

    # request.app['bot'] വഴി ശരിയായ പൈറോഗ്രാം ക്ലയന്റ് ഒബ്ജക്റ്റ് എടുക്കുന്നു
    bot_client = request.app.get('bot')
    if not bot_client:
        return web.Response(text="Bot client not initialized in web server", status=500)

    try:
        file_size = None
        file_name = f"{file_id}.mp4"
        tg_file = None

        try:
            from database.ia_filterdb import get_file_details
            files_ = await get_file_details(file_id)
            if files_:
                tg_file = files_[0] 
                file_size = tg_file.file_size
                file_name = getattr(tg_file, 'file_name', file_name)
        except Exception as e:
            logging.error(f"DB Fetch Error: {e}")

        if not tg_file:
            return web.Response(text="File not found in database", status=404)

        range_header = request.headers.get('Range', None)

        headers = {
            'Content-Type': 'video/mp4',
            'Accept-Ranges': 'bytes',
            'Content-Disposition': f'attachment; filename="{file_name}"',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Expose-Headers': 'Content-Range, Content-Length, Accept-Ranges'
        }

        CHUNK_SIZE = 1024 * 1024 

        if range_header and file_size:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else file_size - 1

                chunk_offset = start // CHUNK_SIZE

                headers['Content-Range'] = f'bytes {start}-{end}/{file_size}'
                headers['Content-Length'] = str(end - start + 1)
                headers['Connection'] = 'keep-alive'

                response = web.StreamResponse(status=206, reason='Partial Content', headers=headers)
                await response.prepare(request)

                current_position = chunk_offset * CHUNK_SIZE

                # 🛠️ ഫിക്സ് ചെയ്ത വരി: ഇവിടെ 'async' ഒഴിവാക്കി വെറും അസൈൻമെന്റ് ആക്കി മാറ്റി
                toggle_stream = bot_client.stream_media(tg_file, offset=chunk_offset)
                async for chunk in toggle_stream:
                    if current_position + len(chunk) > start:
                        if current_position < start:
                            chunk = chunk[start - current_position:]

                        if current_position + len(chunk) > end:
                            chunk = chunk[:end - current_position + 1]
                            try:
                                await response.write(chunk)
                                await response.drain()
                            except:
                                break
                            break

                        try:
                            await response.write(chunk)
                            await response.drain()
                        except (ConnectionResetError, BrokenPipeError):
                            break

                    current_position += len(chunk)
                return response

        if file_size:
            headers['Content-Length'] = str(file_size)
        headers['Connection'] = 'keep-alive'

        response = web.StreamResponse(status=200, reason='OK', headers=headers)
        await response.prepare(request)

        async for chunk in bot_client.stream_media(tg_file):
            try:
                await response.write(chunk)
                await response.drain()
            except (ConnectionResetError, BrokenPipeError):
                break
        return response

    except Exception as e:
        logging.error(f"Streaming Engine Error: {e}")
        return web.Response(text="Error playing file.", status=500)

async def main_page_handler(request):
    return web.Response(
        text="🚀 Nasrani Bot Stream Server is Live and Running via JustRunMy.App!",
        content_type="text/plain"
    )

async def start_jrma_server(bot_instance):
    server = web.Application()
    # ബോട്ട് ഇൻസ്റ്റൻസ് വെബ് ആപ്പിലേക്ക് സേവ് ചെയ്യുന്നു (handlers-ൽ ഉപയോഗിക്കാൻ വേണ്ടി)
    server['bot'] = bot_instance
    
    server.router.add_get('/', main_page_handler)
    server.router.add_get('/watch/{file_id}', stream_handler)
    server.router.add_get('/download_file/{file_id}', download_file_handler)

    runner = web.AppRunner(server)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logging.info(f"🚀 JustRunMy.App Web Server active via HTTPS on Port {PORT}")

async def send_ping(client):
    CRON_API_KEY = "H0kpdbZCFdx7g38U9dOYdIMjXPNSA03IOzN1d4yorWY="
    YOUR_RENDER_URL = "https://nasranii.onrender.com/"

    await asyncio.sleep(120) 

    cron_api_url = "https://api.cron-job.org/jobs"
    cron_headers = {
        "Authorization": f"Bearer {CRON_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        async with aiohttp.ClientSession(headers=cron_headers) as session:
            async with session.get(cron_api_url) as resp:
                if resp.status == 200:
                    jobs_data = await resp.json()
                    job_exists = any(job.get('url') == YOUR_RENDER_URL for job in jobs_data.get('jobs', []))

                    if not job_exists:
                        new_job = {
                            "job": {
                                "title": "Nasrani Render Controller",
                                "url": YOUR_RENDER_URL,
                                "enabled": True,
                                "schedule": {
                                    "timezone": "Asia/Kolkata",
                                    "expiresAt": 0,
                                    "hours": [-1],
                                    "mdays": [-1],
                                    "minutes": [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57],
                                    "months": [-1],
                                    "wdays": [-1]
                                }
                            }
                        }
                        await session.post(cron_api_url, json=new_job)
                        logging.info("🚀 Cron-Job successfully registered for Render URL!")
    except Exception as e:
        logging.error(f"Cron-Job Auto-Setup Error: {e}")

    while True:
        try:
            current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %I:%M:%S %p')
            log_message = (
                "🟢 **Render Server Status Alert**\n\n"
                f"**Status:** Awake & Active\n"
                f"**Trigger:** Cron-Job External Ping\n"
                f"**Interval:** Every 3 Minutes\n"
                f"**Time:** `{current_time}`"
            )
            await client.send_message(chat_id=LOG_CHANNEL, text=log_message)
        except Exception as tg_err:
            logging.error(f"Telegram Ping Log Failed: {tg_err}")

        await asyncio.sleep(180)

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

        # വെബ് സെർവർ സ്റ്റാർട്ട് ചെയ്യുമ്പോൾ self (bot instance) കൂടി പാസ്സ് ചെയ്യുന്നു
        await start_jrma_server(self)

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
        await resume_index_jobs(self)

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

async def send_active_notification(bot):
    chats = await db.get_all_chats()
    for chat in chats:
        try:
            await bot.send_message(
                chat["id"],
                "✅ <b>Bot Activated Successfully</b>\n\n"
                "🤖 Bot is now online and working properly."
            )
        except Exception as e:
            print(f"{chat['id']} : {e}")

app = Bot()
app.run()
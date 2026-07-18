from info import *
from difflib import SequenceMatcher
from database.users_chats_db import db
requestdb = db.xp

from datetime import datetime, date

import requests
import logging
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid, ChatAdminRequired
from info import AUTH_CHANNEL, LONG_IMDB_DESCRIPTION, MAX_LIST_ELM, SHORTLINK_URL, SHORTLINK_API, LOG_CHANNEL, GRP_LNK, CHNL_LNK, CUSTOM_FILE_CAPTION, IS_VERIFY, VERIFY2_URL, VERIFY2_API, PROTECT_CONTENT, HOW_TO_VERIFY
from imdb import Cinemagoer 
import asyncio
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import enums
from typing import Union
from Script import script
import pytz
import random 
import re
import os
from datetime import datetime, timedelta, date, time
import string
from typing import List
from database.users_chats_db import db
from bs4 import BeautifulSoup
import requests
import aiohttp
from shortzy import Shortzy
import http.client
import json
from urllib.parse import quote_plus
from info import OMDB_API_KEY
from database.movie_mapdb import (
    get_movie_map,
    add_movie_map
)
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


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\((buttonurl|buttonalert):(?:/{0,2})(.+?)(:same)?\))"
)

# OMDB_API_KEY = "http://www.omdbapi.com/?i=tt3896198&apikey=b6d00b5c"
IMDB_API_BASE = "https://www.omdbapi.com/"

HTTP_TIMEOUT = 10

imdb = Cinemagoer()
TOKENS = {}
VERIFIED = {}
BANNED = {}
SMART_OPEN = '“'
SMART_CLOSE = '”'
START_CHAR = ('\'', '"', SMART_OPEN)
TMDB_API_KEY = "229c6b13681d95ffc03362a0c53904e7"
# temp db for banned 
class temp(object):
    BANNED_USERS = []
    BANNED_CHATS = []
    ME = None
    CURRENT=int(os.environ.get("SKIP", 2))
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None
# temp.py
    INDEX_YEAR = None
    SETTINGS = {}
    VERIFY = {}
    SEND_ALL_TEMP = {}
    KEYWORD = {}
    IMDB_CAP = {}
    GETALL = {}
    SHORT = {}
    BACK_BUTTONS = {}
    BACK_DATA = {}
async def is_subscribeed(bot, query=None, userid=None):
    try:
        if userid == None and query != None:
            user = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
        else:
            user = await bot.get_chat_member(AUTH_CHANNEL, int(userid))
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if user.status != enums.ChatMemberStatus.BANNED:
            return True

    return False


async def is_subscribed(bot, query):
    try:
        user = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if user.status != enums.ChatMemberStatus.BANNED:
            return True

    return False


async def is_subscribe(bot, query):
    try:
        # check if query has 'from_user', else treat as user_id
        user_id = query.from_user.id if hasattr(query, "from_user") else query
        user = await bot.get_chat_member(AUTH_CHANNEL, user_id)
    except UserNotParticipant:
        return False
    except Exception as e:
        logger.exception(e)
        return False
    else:
        if user.status != enums.ChatMemberStatus.BANNED:
            return True
    return False

def _get_json(url):
    response = requests.get(url, timeout=HTTP_TIMEOUT)
    response.raise_for_status()
    return response.json()


#def search_imdb(query, page=1):
#    search_url = f"{IMDB_API_BASE}?q={quote_plus(query)}&page={page}"
#    data = _get_json(search_url)
#    return {
##        "results": data.get("Search") or [],
#        "page": int(data.get("page") or page),
##        "next_page": data.get("nextPage"),
#       "total_results": int(data.get("totalResults") or 0),
#    }



def search_imdb(query, page=1):

    search_url = f"https://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query}"
#    print(search_url)

    data = _get_json(search_url)

    if data.get("Response") == "False":
        return {
            "results": [],
            "page": 1,
            "next_page": None,
            "total_results": 0,
        }

    return {
        "results": data.get("Search") or [],
        "page": 1,
        "next_page": None,
        "total_results": len(data.get("Search") or []),
    }

async def search_imdb_async(query, page=1):
    return await asyncio.to_thread(search_imdb, query, page)


from difflib import SequenceMatcher





async def fetch_landscape_backdrop(imdb_id):
    """
    IMDb ID ഉപയോഗിച്ച് TMDb API-യിൽ നിന്ന് landscape backdrop fetch ചെയ്യുന്നു
    """
    try:
        url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={TMDB_API_KEY}&external_source=imdb_id"
        data = await asyncio.to_thread(lambda: requests.get(url).json())
        results = data.get("movie_results")
        if results and results[0].get("backdrop_path"):
            return f"https://image.tmdb.org/t/p/original{results[0]['backdrop_path']}"
    except Exception as e:
        print(f"TMDb error: {e}")
    return None



async def get_poster(query, bulk=False, id=False, file=None, landscape_mode=False):
    print("BULK =", bulk)

    if not id:

        query = query.strip()
        movie_map = await get_movie_map()

        for wrong, correct in movie_map.items():
            if wrong in query.lower():
                query = correct
                break

        title = query
        print("OMDB QUERY =", title)
        year = re.findall(r'[1-2]\d{3}$', query, re.IGNORECASE)

        if year:
            year = list_to_str(year[:1])
            title = (query.replace(year, "")).strip()

        elif file is not None:

            year = re.findall(r'[1-2]\d{3}', file, re.IGNORECASE)

            if year:
                year = list_to_str(year[:1])

        else:
            year = None
        cache_key = f"{title.lower()}_{year or ''}"

#        cached = await db.get_cached_imdb(cache_key)
#        if cached:
#            return cached["data"]
        cached = await db.get_cached_imdb(cache_key)

        if cached and not bulk:
            return cached["data"]
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={title}"

        search_data = await asyncio.to_thread(
            lambda: requests.get(url).json()
        )

        movie_list = search_data.get("Search") or []

        print(search_data)
        print("MOVIE_LIST =", movie_list)

        # FALLBACK OMDB SEARCH
        
        if not movie_list:
            return None

        # FILTER YEAR
        if year:

            filtered = [
                m for m in movie_list
                if str(m.get("Year")) == str(year)
            ]

            if not filtered:
                filtered = movie_list

        else:
            filtered = movie_list

        movie_list = filtered

        # FUZZY MATCH
        if bulk:

            matched = []

            for movie in movie_list:

                titlex = (
                    movie.get("Title")
                    or movie.get("title")
                    or ""
                )

                ratio = SequenceMatcher(
                    None,
                    query.lower(),
                    titlex.lower()
                ).ratio()

                if (
                    query.lower() in titlex.lower()
                    or ratio > 0.40
                ):

                    matched.append(movie)

            return matched if matched else movie_list[:10]

        movieid = movie_list[0].get("imdbID")

    else:
        movieid = query

    details_url = f"{IMDB_API_BASE}?apikey={OMDB_API_KEY}&i={movieid}"

    movie = await asyncio.to_thread(
        lambda: requests.get(details_url).json()
    )

    plot = movie.get("Plot") or ""

    if plot and len(plot) > 800:
        plot = plot[:800] + "..."
    poster_img = movie.get('Poster')

    poster_img = movie.get('Poster')

    # landscape_mode True ആണെങ്കിൽ മാത്രം TMDB-യിൽ നിന്ന് ലാൻഡ്സ്കേപ്പ് ഫോട്ടോ എടുക്കും
    if landscape_mode == True:
        backdrop = await fetch_landscape_backdrop(movie.get("imdbID"))
        if backdrop:
            poster_img = backdrop

    result = {
        'title': movie.get('Title'),
        'votes': "N/A",
        "aka": "N/A",
        "seasons": "N/A",
        "box_office": "N/A",
        'localized_title': movie.get('Title'),
        'kind': movie.get("Type", "movie"),
        "imdb_id": movie.get('imdbID'),
        "cast": movie.get("Stars", "N/A"),
        "runtime": movie.get("Runtime", "N/A"),
        "countries": "N/A",
        "certificates": "N/A",
        "languages": movie.get("Language") or movie.get("languages") or "N/A",
        "director": movie.get("Director", "N/A"),
        "writer": movie.get("Writer", "N/A"),
        "producer": "N/A",
        "composer": "N/A",
        "cinematographer": "N/A",
        "music_team": "N/A",
        "distributors": "N/A",
        'release_date': movie.get("Released") or movie.get("Year") or "N/A",
        'year': movie.get('Year'),
        'genres': movie.get("Genre", "N/A"),
        'poster': poster_img,
        'plot': plot,
        'rating': str(movie.get("imdbRating", "N/A")),
        'url': f"https://www.imdb.com/title/{movieid}"
    }
    await db.save_cached_imdb(cache_key, result)

    return result
# https://github.com/odysseusmax/animated-lamp/blob/2ef4730eb2b5f0596ed6d03e7b05243d93e3415b/bot/utils/broadcast.py#L37

async def get_tmdb_poster(query, bulk=False, id=False, file=None, landscape_mode=False):
    """
    TMDb API ഉപയോഗിച്ച് സിനിമയുടെ വിവരങ്ങളും പോസ്റ്ററുകളും ഫെച്ച് ചെയ്യുന്നു
    """
    if not id:
        query = query.strip()
        movie_map = await get_movie_map()
        for wrong, correct in movie_map.items():
            if wrong in query.lower():
                query = correct
                break

        title = query
        year_match = re.findall(r'[1-2]\d{3}$', query, re.IGNORECASE)
        if year_match:
            year = list_to_str(year_match[:1])
            title = (query.replace(year, "")).strip()
        elif file is not None:
            year_match = re.findall(r'[1-2]\d{3}', file, re.IGNORECASE)
            year = list_to_str(year_match[:1]) if year_match else None
        else:
            year = None

        cache_key = f"tmdb_{title.lower()}_{year or ''}"
        cached = await db.get_cached_imdb(cache_key)
        if cached and not bulk:
            return cached["data"]

        # TMDb Search URL
        url = f"https://api.themoviedb.org/3/search/multi?api_key={TMDB_API_KEY}&query={title}"
        if year:
            url += f"&year={year}"

        search_data = await asyncio.to_thread(lambda: requests.get(url).json())
        results = search_data.get("results") or []

        if not results:
            return None

        # Filter out person/etc results, keep only movie or tv
        results = [r for r in results if r.get("media_type") in ["movie", "tv"]]
        if not results:
            return None
            
        movie_id = results[0].get("id")
        media_type = results[0].get("media_type", "movie")
    else:
        # ID ആണ് പാസ് ചെയ്തതെങ്കിൽ (e.g., tmdb_id)
        movie_id = query
        media_type = "movie" # Default to movie or handle dynamically

    # Get Detailed Info from TMDb
    details_url = f"https://api.themoviedb.org/3/{media_type}/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=external_ids,credits"
    movie = await asyncio.to_thread(lambda: requests.get(details_url).json())

    if not movie or "success" in movie and not movie["success"]:
        return None

    # Title handling (TMDb uses 'name' for TV Shows and 'title' for Movies)
    f_title = movie.get("title") or movie.get("name") or "N/A"
    
    # Plot/Overview
    plot = movie.get("overview") or ""
    if len(plot) > 800:
        plot = plot[:800] + "..."

    # Poster & Landscape/Backdrop Mode
# Poster & Landscape/Backdrop Mode
    poster_path = movie.get("poster_path")
    backdrop_path = movie.get("backdrop_path")
    
    # ആദ്യം സാധാരണ വെർട്ടിക്കൽ പോസ്റ്റർ സെറ്റ് ചെയ്യുന്നു
    poster_img = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    
    # landscape_mode True ആണെങ്കിൽ മാത്രം ലാൻഡ്സ്കേപ്പ് ഫോട്ടോ ആക്കി മാറ്റും
    if landscape_mode == True and backdrop_path:
        poster_img = f"https://image.tmdb.org/t/p/original{backdrop_path}"

    # Genres parsing
    genres_list = [g.get("name") for g in movie.get("genres", [])]
    genres = ", ".join(genres_list) if genres_list else "N/A"

    # Director / Cast from credits
    credits = movie.get("credits", {})
    cast_list = [c.get("name") for c in credits.get("cast", [])[:5]]
    stars = ", ".join(cast_list) if cast_list else "N/A"
    
    director = "N/A"
    if media_type == "movie":
        directors = [crew.get("name") for crew in credits.get("crew", []) if crew.get("job") == "Director"]
        if directors:
            director = ", ".join(directors)

    release_date = movie.get("release_date") or movie.get("first_air_date") or "N/A"
    year_val = release_date.split("-")[0] if release_date != "N/A" else "N/A"
    runtime = f"{movie.get('runtime') or movie.get('episode_run_time', [0])[0]} min"

    result = {
        'title': f_title,
        'votes': str(movie.get("vote_count", "N/A")),
        "aka": "N/A",
        "seasons": str(movie.get("number_of_seasons", "N/A")),
        "box_office": "N/A",
        'localized_title': f_title,
        'kind': media_type,
        "imdb_id": movie.get("external_ids", {}).get("imdb_id") or "N/A",
        "cast": stars,
        "runtime": runtime,
        "countries": "N/A",
        "certificates": "N/A",
        "languages": movie.get("original_language", "N/A"),
        "director": director,
        "writer": "N/A",
        "producer": "N/A",
        "composer": "N/A",
        "cinematographer": "N/A",
        "music_team": "N/A",
        'release_date': release_date,
        'year': year_val,
        'genres': genres,
        'poster': poster_img,
        'plot': plot,
        'rating': str(movie.get("vote_average", "N/A")),
        'url': f"https://www.themoviedb.org/{media_type}/{movie_id}"
    }

    if not id:
        await db.save_cached_imdb(cache_key, result)

    return result




async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await db.delete_user(int(user_id))
        logging.info(f"{user_id}-Rᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ Dᴀᴛᴀʙᴀsᴇ, sɪɴᴄᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ.")
        return False, "Deleted"
    except UserIsBlocked:
        logging.info(f"{user_id} -Bʟᴏᴄᴋᴇᴅ ᴛʜᴇ ʙᴏᴛ.")
        return False, "Blocked"
    except PeerIdInvalid:
        await db.delete_user(int(user_id))
        logging.info(f"{user_id} - PᴇᴇʀIᴅIɴᴠᴀʟɪᴅ")
        return False, "Error"
    except Exception as e:
        return False, "Error"

async def search_gagala(text):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/61.0.3163.100 Safari/537.36'
        }
    text = text.replace(" ", '+')
    url = f'https://www.google.com/search?q={text}'
    response = requests.get(url, headers=usr_agent)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all( 'h3' )
    return [title.getText() for title in titles]


async def get_settings(group_id):
    # Fetch from cache
    settings = temp.SETTINGS.get(group_id)
    
    if not settings:
        # Fetch from DB if not in cache
        settings = await db.get_settings(group_id)
        if not settings:
            settings = {}

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
            "gfilter": True
        }

        for key, value in defaults.items():
            settings.setdefault(key, value)

        # Update cache
        temp.SETTINGS[group_id] = settings
    
    return settings


async def get_settingss(group_id):
    group_id = int(group_id)

    settings = temp.SETTINGS.get(group_id)
    if not settings:
        settings = await db.get_settings(group_id)
        temp.SETTINGS[group_id] = settings

    return settings
    
async def save_group_settings(group_id, key, value):

    group_id = int(group_id)

    current = await get_settings(group_id)

    # 🔥 FIX: handle None
    if not current:
        current = {}

    # 🔥 update value
    current[key] = value

    # 🔥 cache update (safe)
    if not hasattr(temp, "SETTINGS"):
        temp.SETTINGS = {}

    temp.SETTINGS[group_id] = current

    # 🔥 DB update
    await db.update_settings(group_id, current)
    
    
    
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]  

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

def extract_user(message: Message) -> Union[int, str]:
    """extracts the user from a message"""
    # https://github.com/SpEcHiDe/PyroGramBot/blob/f30e2cca12002121bad1982f68cd0ff9814ce027/pyrobot/helper_functions/extract_user.py#L7
    user_id = None
    user_first_name = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_first_name = message.reply_to_message.from_user.first_name

    elif len(message.command) > 1:
        if (
            len(message.entities) > 1 and
            message.entities[1].type == enums.MessageEntityType.TEXT_MENTION
        ):
           
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            # don't want to make a request -_-
            user_first_name = user_id
        try:
            user_id = int(user_id)
        except ValueError:
            pass
    else:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
    return (user_id, user_first_name)

def list_to_str(k):
    if not k:
        return "N/A"
    elif len(k) == 1:
        return str(k[0])
    elif MAX_LIST_ELM:
        k = k[:int(MAX_LIST_ELM)]
        return ' '.join(f'{elem}, ' for elem in k)
    else:
        return ' '.join(f'{elem}, ' for elem in k)

def last_online(from_user):
    time = ""
    if from_user.is_bot:
        time += "🤖 Bot :("
    elif from_user.status == enums.UserStatus.RECENTLY:
        time += "Recently"
    elif from_user.status == enums.UserStatus.LAST_WEEK:
        time += "Within the last week"
    elif from_user.status == enums.UserStatus.LAST_MONTH:
        time += "Within the last month"
    elif from_user.status == enums.UserStatus.LONG_AGO:
        time += "A long time ago :("
    elif from_user.status == enums.UserStatus.ONLINE:
        time += "Currently Online"
    elif from_user.status == enums.UserStatus.OFFLINE:
        time += from_user.last_online_date.strftime("%a, %d %b %Y, %H:%M:%S")
    return time


def split_quotes(text: str) -> List:
    if not any(text.startswith(char) for char in START_CHAR):
        return text.split(None, 1)
    counter = 1  # ignore first char -> is some kind of quote
    while counter < len(text):
        if text[counter] == "\\":
            counter += 1
        elif text[counter] == text[0] or (text[0] == SMART_OPEN and text[counter] == SMART_CLOSE):
            break
        counter += 1
    else:
        return text.split(None, 1)

    # 1 to avoid starting quote, and counter is exclusive so avoids ending
    key = remove_escapes(text[1:counter].strip())
    # index will be in range, or `else` would have been executed and returned
    rest = text[counter + 1:].strip()
    if not key:
        key = text[0] + text[0]
    return list(filter(None, [key, rest]))

def gfilterparser(text, keyword):
    if "buttonalert" in text:
        text = (text.replace("\n", "\\n").replace("\t", "\\t"))
    buttons = []
    note_data = ""
    prev = 0
    i = 0
    alerts = []
    for match in BTN_URL_REGEX.finditer(text):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and text[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            note_data += text[prev:match.start(1)]
            prev = match.end(1)
            if match.group(3) == "buttonalert":
                # create a thruple with button label, url, and newline status
                if bool(match.group(5)) and buttons:
                    buttons[-1].append(InlineKeyboardButton(
                        text=match.group(2),
                        callback_data=f"gfilteralert:{i}:{keyword}"
                    ))
                else:
                    buttons.append([InlineKeyboardButton(
                        text=match.group(2),
                        callback_data=f"gfilteralert:{i}:{keyword}"
                    )])
                i += 1
                alerts.append(match.group(4))
            elif bool(match.group(5)) and buttons:
                buttons[-1].append(InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(4).replace(" ", "")
                ))
            else:
                buttons.append([InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(4).replace(" ", "")
                )])

        else:
            note_data += text[prev:to_check]
            prev = match.start(1) - 1
    else:
        note_data += text[prev:]

    try:
        return note_data, buttons, alerts
    except:
        return note_data, buttons, None

def parser(text, keyword):
    if "buttonalert" in text:
        text = (text.replace("\n", "\\n").replace("\t", "\\t"))
    buttons = []
    note_data = ""
    prev = 0
    i = 0
    alerts = []
    for match in BTN_URL_REGEX.finditer(text):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and text[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            note_data += text[prev:match.start(1)]
            prev = match.end(1)
            if match.group(3) == "buttonalert":
                # create a thruple with button label, url, and newline status
                if bool(match.group(5)) and buttons:
                    buttons[-1].append(InlineKeyboardButton(
                        text=match.group(2),
                        callback_data=f"alertmessage:{i}:{keyword}"
                    ))
                else:
                    buttons.append([InlineKeyboardButton(
                        text=match.group(2),
                        callback_data=f"alertmessage:{i}:{keyword}"
                    )])
                i += 1
                alerts.append(match.group(4))
            elif bool(match.group(5)) and buttons:
                buttons[-1].append(InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(4).replace(" ", "")
                ))
            else:
                buttons.append([InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(4).replace(" ", "")
                )])

        else:
            note_data += text[prev:to_check]
            prev = match.start(1) - 1
    else:
        note_data += text[prev:]

    try:
        return note_data, buttons, alerts
    except:
        return note_data, buttons, None

def remove_escapes(text: str) -> str:
    res = ""
    is_escaped = False
    for counter in range(len(text)):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
    return res


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

async def get_shortlink(chat_id, link):
    settings = await get_settings(chat_id) #fetching settings for group
    if 'shortlink' in settings.keys():
        URL = settings['shortlink']
        API = settings['shortlink_api']
    else:
        URL = SHORTLINK_URL
        API = SHORTLINK_API
    if URL.startswith("shorturllink") or URL.startswith("terabox.in") or URL.startswith("urlshorten.in"):
        URL = SHORTLINK_URL
        API = SHORTLINK_API
    if URL == "api.shareus.io":
        # method 1:
        # https = link.split(":")[0] #splitting https or http from link
        # if "http" == https: #if https == "http":
        #     https = "https"
        #     link = link.replace("http", https) #replacing http to https
        # conn = http.client.HTTPSConnection("api.shareus.io")
        # payload = json.dumps({
        #   "api_key": "4c1YTBacB6PTuwogBiEIFvZN5TI3",
        #   "monetization": True,
        #   "destination": link,
        #   "ad_page": 3,
        #   "category": "Entertainment",
        #   "tags": ["trendinglinks"],
        #   "monetize_with_money": False,
        #   "price": 0,
        #   "currency": "INR",
        #   "purchase_note":""
        
        # })
        # headers = {
        #   'Keep-Alive': '',
        #   'Content-Type': 'application/json'
        # }
        # conn.request("POST", "/generate_link", payload, headers)
        # res = conn.getresponse()
        # data = res.read().decode("utf-8")
        # parsed_data = json.loads(data)
        # if parsed_data["status"] == "success":
        #   return parsed_data["link"]
    #method 2
        url = f'https://{URL}/easy_api'
        params = {
            "key": API,
            "link": link,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.text()
                    return data
        except Exception as e:
            logger.error(e)
            return link
    else:
        shortzy = Shortzy(api_key=API, base_site=URL)
        link = await shortzy.convert(link)
        return link

async def get_verify_shorted_link(num, link):
    if int(num) == 1:
        API = SHORTLINK_API
        URL = SHORTLINK_URL
    else:
        API = VERIFY2_API
        URL = VERIFY2_URL
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)

    if URL == "api.shareus.in":
        url = f"https://{URL}/shortLink"
        params = {"token": API,
                  "format": "json",
                  "link": link,
                  }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.json(content_type="text/html")
                    if data["status"] == "success":
                        return data["shortlink"]
                    else:
                        logger.error(f"Error: {data['message']}")
                        return f'https://{URL}/shortLink?token={API}&format=json&link={link}'

        except Exception as e:
            logger.error(e)
            return f'https://{URL}/shortLink?token={API}&format=json&link={link}'
    else:
        url = f'https://{URL}/api'
        params = {'api': API,
                  'url': link,
                  }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.json()
                    if data["status"] == "success":
                        return data["shortenedUrl"]
                    else:
                        logger.error(f"Error: {data['message']}")
                        if URL == 'clicksfly.com':
                            return f'https://{URL}/api?api={API}&url={link}'
                        else:
                            return f'https://{URL}/api?api={API}&link={link}'
        except Exception as e:
            logger.error(e)
            if URL == 'clicksfly.com':
                return f'https://{URL}/api?api={API}&url={link}'
            else:
                return f'https://{URL}/api?api={API}&link={link}'

async def check_token(bot, userid, token):
    user = await bot.get_users(userid)
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(user.id, user.mention))
    if user.id in TOKENS.keys():
        TKN = TOKENS[user.id]
        if token in TKN.keys():
            is_used = TKN[token]
            if is_used == True:
                return False
            else:
                return True
    else:
        return False

async def get_token(bot, userid, link, fileid):
    user = await bot.get_users(userid)
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(user.id, user.mention))
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    TOKENS[user.id] = {token: False}
    url = f"{link}verify-{user.id}-{token}-{fileid}"
    status = await get_verify_status(user.id)
    date_var = status["date"]
    time_var = status["time"]
    hour, minute, second = time_var.split(":")
    year, month, day = date_var.split("-")
    last_date, last_time = str((datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second)))-timedelta(hours=12)).split(" ")
    tz = pytz.timezone('Asia/Kolkata')
    curr_date, curr_time = str(datetime.now(tz)).split(" ")
    if last_date == curr_date:
        vr_num = 2
    else:
        vr_num = 1
    shortened_verify_url = await get_verify_shorted_link(vr_num, url)
    return str(shortened_verify_url)

async def send_all(bot, userid, files, ident, chat_id, user_name, query):
    settings = await get_settings(chat_id)
    if 'is_shortlink' in settings.keys():
        ENABLE_SHORTLINK = settings['is_shortlink']
    else:
        await save_group_settings(message.chat.id, 'is_shortlink', False)
        ENABLE_SHORTLINK = False
    try:
        if ENABLE_SHORTLINK:
            for file in files:
                title = file.file_name
                size = get_size(file.file_size)
                await bot.send_message(chat_id=userid, text=f"<b>Hᴇʏ ᴛʜᴇʀᴇ {user_name} 👋🏽 \n\n✅ Sᴇᴄᴜʀᴇ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ғɪʟᴇ ʜᴀs sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴇᴇɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴅᴏᴡɴʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ\n\n🗃️ Fɪʟᴇ Nᴀᴍᴇ : {title}\n🔖 Fɪʟᴇ Sɪᴢᴇ : {size}</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📤 Dᴏᴡɴʟᴏᴀᴅ 📥", url=await get_shortlink(chat_id, f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"))]]))
        else:
            for file in files:
                    f_caption = file.caption
                    title = file.file_name
                    size = get_size(file.file_size)
                    if CUSTOM_FILE_CAPTION:
                        try:
                            f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                                    file_size='' if size is None else size,
                                                                    file_caption='' if f_caption is None else f_caption)
                        except Exception as e:
                            print(e)
                            f_caption = f_caption
                    if f_caption is None:
                        f_caption = f"{title}"
                    await bot.send_cached_media(
                        chat_id=userid,
                        file_id=file.file_id,
                        caption=f_caption,
                        protect_content=True if ident == "filep" else False,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=GRP_LNK),
                                InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                            ],[
                                InlineKeyboardButton("Bᴏᴛ Oᴡɴᴇʀ", url="t.me/Kgashok04")
                                ]
                            ]
                        )
                    )
    except UserIsBlocked:
        await query.answer('Uɴʙʟᴏᴄᴋ ᴛʜᴇ ʙᴏᴛ ᴍᴀʜɴ !', show_alert=True)
    except PeerIdInvalid:
        await query.answer('Hᴇʏ, Sᴛᴀʀᴛ Bᴏᴛ Fɪʀsᴛ Aɴᴅ Cʟɪᴄᴋ Sᴇɴᴅ Aʟʟ', show_alert=True)
    except Exception as e:
        await query.answer('Hᴇʏ, Sᴛᴀʀᴛ Bᴏᴛ Fɪʀsᴛ Aɴᴅ Cʟɪᴄᴋ Sᴇɴᴅ Aʟʟ', show_alert=True)


async def get_tutorial(chat_id):
    settings = await get_settings(chat_id) #fetching settings for group
    if 'tutorial' in settings.keys():
        if settings['is_tutorial']:
            TUTORIAL_URL = settings['tutorial']
        else:
            TUTORIAL_URL = TUTORIAL
    else:
        TUTORIAL_URL = TUTORIAL
    return TUTORIAL_URL




async def get_verify_status(userid):
    status = temp.VERIFY.get(userid)
    if not status:
        status = await db.get_verified(userid)
        temp.VERIFY[userid] = status
    return status
    
async def update_verify_status(userid, date_temp, time_temp):
    status = await get_verify_status(userid)
    status["date"] = date_temp
    status["time"] = time_temp
    temp.VERIFY[userid] = status
    await db.update_verification(userid, date_temp, time_temp)

async def verify_user(bot, userid, token):
    user = await bot.get_users(int(userid))
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(user.id, user.mention))
    TOKENS[user.id] = {token: True}
    tz = pytz.timezone('Asia/Kolkata')
    date_var = datetime.now(tz)+timedelta(hours=12)
    temp_time = date_var.strftime("%H:%M:%S")
    date_var, time_var = str(date_var).split(" ")
    await update_verify_status(user.id, date_var, temp_time)

async def check_verification(bot, userid):
    user = await bot.get_users(int(userid))
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(user.id, user.mention))
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    curr_time = now.strftime("%H:%M:%S")
    hour1, minute1, second1 = curr_time.split(":")
    curr_time = time(int(hour1), int(minute1), int(second1))
    status = await get_verify_status(user.id)
    date_var = status["date"]
    time_var = status["time"]
    years, month, day = date_var.split('-')
    comp_date = date(int(years), int(month), int(day))
    hour, minute, second = time_var.split(":")
    comp_time = time(int(hour), int(minute), int(second))
    if comp_date<today:
        return False
    else:
        if comp_date == today:
            if comp_time<curr_time:
                return False
            else:
                return True
        else:
            return True


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


async def get_cap(settings, remaining_seconds, files, query, total_results, search):
    # Aᴅᴅᴇᴅ Bʏ @TᴇᴀᴍHMT_Bᴏᴛs & Fɪxᴇᴅ Bʏ Gᴇᴍɪɴɪ
    
    # 🟢 IMDb സെറ്റിങ്സ് ഓഫ് ആണെങ്കിലും ഡാറ്റ കിട്ടാൻ വേണ്ടി ബാക്ക്ഗ്രൗണ്ടിൽ ഫെച്ച് ചെയ്യുന്നു
    imdb = await get_poster(search, file=(files[0]).file_name)
    
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

    # എപ്പോഴും ഒരേ ഫോർമാറ്റിലുള്ള ഭംഗിയുള്ള ക്യാപ്ഷൻ ബേസ് ഉണ്ടാക്കുന്നു
    cap = (
        f"<b>𝐇𝐞𝐥𝐥𝐨 {query.from_user.mention}: 𝐘𝐨𝐮𝐫 {search} 𝐑𝐞𝐚𝐝𝐲..\n\n"
        f"🏷 𝐓𝐢𝐭𝐥𝐞 : {f_title}\n\n"
        f"🎭 𝐆𝐞𝐧𝐫𝐞𝐬 : {f_genres}\n\n"
        f"📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {f_year}\n\n"
        f"📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {f_runtime}\n\n"
        f"🌟 𝐑𝐚𝐭𝐢𝐧𝐠 :  {f_rating} / 10\n\n</b>"
    )

    # 🔗 ഹൈപ്പർലിങ്ക് ഫയലുകൾ ക്യാപ്ഷനിലേക്ക് ചേർക്കുന്നു
    cap += "<b><u>📚 Requested Files 👇</u></b>\n\n"
    for file in files:
        EMOJI = random.choice(RUN_STRINGS)
        file_clean_name = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))
        cap += f"<b>{EMOJI} <a href='https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}'>[{get_size(file.file_size)}] {file_clean_name}\n\n</a></b>"
            
    # ടോപ്പ് റിക്വസ്റ്റേഴ്സ് കൗണ്ടോടെ ആഡ് ചെയ്യുന്നു
    top = await get_top_requesters()
    cap += (
        "\n<b>𝐓𝐨𝐩 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐫𝐬</b>\n"
        f"1. {top[0]}\n"
        f"2. {top[1]}\n"
        f"3. {top[2]}"
    )

    return cap






async def send_all_files(bot, userid, files, ident):
    if AUTH_CHANNEL and not await is_subscribed(bot=bot, userid=userid):
        try:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Mᴀᴋᴇ sᴜʀᴇ Bᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ Fᴏʀᴄᴇsᴜʙ ᴄʜᴀɴɴᴇʟ")
            return
        if ident == 'filep' or 'checksubp':
            pre = 'checksubp'
        else:
            pre = 'checksub' 
        btn = [[
                InlineKeyboardButton("❆ Jᴏɪɴ Oᴜʀ Bᴀᴄᴋ-Uᴘ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link)
            ],[
                InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", callback_data=f"{pre}#send_all")
            ]]
        await bot.send_message(
            chat_id=userid,
            text="**Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ ᴏᴜʀ Bᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ sᴏ ʏᴏᴜ ᴅᴏɴ'ᴛ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ...\n\nIғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '❆ Jᴏɪɴ Oᴜʀ Bᴀᴄᴋ-Uᴘ Cʜᴀɴɴᴇʟ ❆' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '↻ Tʀʏ Aɢᴀɪɴ' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ...\n\nTʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇs...**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return 'fsub'
    
    if IS_VERIFY and not await check_verification(bot, userid):
        btn = [[
            InlineKeyboardButton("Vᴇʀɪғʏ", url=await get_token(bot, userid, f"https://telegram.me/{temp.U_NAME}?start=", 'send_all')),
            InlineKeyboardButton("Hᴏᴡ Tᴏ Vᴇʀɪғʏ", url=HOW_TO_VERIFY)
        ]]
        await bot.send_message(
            chat_id=userid,
            text="<b>Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ!\nKɪɴᴅʟʏ ᴠᴇʀɪғʏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ Sᴏ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴀᴄᴄᴇss ᴛᴏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴜɴᴛɪʟ 12 ʜᴏᴜʀs ғʀᴏᴍ ɴᴏᴡ !</b>",
            protect_content=True if PROTECT_CONTENT else False,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return 'verify'
    
    for file in files:
        f_caption = file.caption
        title = file.file_name
        size = get_size(file.file_size)
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                        file_size='' if size is None else size,
                                                        file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                print(e)
                f_caption = f_caption
        if f_caption is None:
            f_caption = f"{title}"
        try:
            await bot.send_cached_media(
                chat_id=userid,
                file_id=file.file_id,
                caption=f_caption,
                protect_content=True if ident == "filep" else False,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=GRP_LNK),
                        InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)
                    ],[
                        InlineKeyboardButton("Bᴏᴛ Oᴡɴᴇʀ", url="t.me/creatorbeatz")
                        ]
                    ]
                )
            )
        except UserIsBlocked:
            logger.error(f"Usᴇʀ: {userid} ʙʟᴏᴄᴋᴇᴅ ᴛʜᴇ ʙᴏᴛ. Uɴʙʟᴏᴄᴋ ᴛʜᴇ ʙᴏᴛ!")
            return "Usᴇʀ ɪs ʙʟᴏᴄᴋᴇᴅ ᴛʜᴇ ʙᴏᴛ ! Uɴʙʟᴏᴄᴋ ᴛᴏ sᴇɴᴅ ғɪʟᴇs!"
        except PeerIdInvalid:
            logger.error("Eʀʀᴏʀ: Pᴇᴇʀ ID ɪɴᴠᴀʟɪᴅ !")
            return "Pᴇᴇʀ ID ɪɴᴠᴀʟɪᴅ !"
        except Exception as e:
            logger.error(f"Eʀʀᴏʀ: {e}")
            return f"Eʀʀᴏʀ: {e}"
    return 'done'

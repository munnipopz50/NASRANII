from pyrogram import Client, filters
from database.ia_filterdb import (
    save_batch_collection,
    batch_exists,
    get_all_batch_collections,
    get_batch_collection,
    batch_col
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *
import re

BATCH_MODE = {}

@Client.on_message(filters.command("batch") & filters.private)
async def batch_start(client, message):
    BATCH_MODE[message.from_user.id] = {"files": []}
    await message.reply_text("Batch started. Send files now. Use /done <name> to save.")

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def collect_files(client, message):
    uid = message.from_user.id
    if uid not in BATCH_MODE: return
    media = message.document or message.video or message.audio
    BATCH_MODE[uid]["files"].append({
        "file_id": media.file_id,
        "file_name": getattr(media, "file_name", "Unknown"),
        "file_size": getattr(media, "file_size", 0)
    })
    await message.reply_text(f"Added {len(BATCH_MODE[uid]['files'])} files")


@Client.on_message(filters.command("done") & filters.private)
async def finish_batch(client, message):
    uid = message.from_user.id
    if uid not in BATCH_MODE:
        return await message.reply_text("No batch session found.")
    
    data = BATCH_MODE[uid]
    total = len(data["files"])
    if total < 1:
        return await message.reply_text("Need at least 1 file.")

    # 1. പേര് കണ്ടെത്താനുള്ള ലോജിക്
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1:
        # ഉപയോക്താവ് പേര് നൽകിയാൽ അത് ഉപയോഗിക്കുന്നു
        name = parts[1].strip().lower()
    else:
        # പേര് നൽകിയില്ലെങ്കിൽ ആദ്യ ഫയലിൽ നിന്ന് എടുക്കുന്നു
        first_file_name = data["files"][0]["file_name"]
        
        # Regex ഉപയോഗിച്ച് "Name" + "Year" മാത്രം എടുക്കുന്നു (ഉദാ: Aashaan 2026)
        # ഇത് ഫയൽ പേരിലെ അനാവശ്യ വാക്കുകളെ (Malayalam, Movie മുതലായവ) ഒഴിവാക്കാൻ സഹായിക്കും
        match = re.search(r"([a-zA-Z]+)\s*.*?(\d{4})", first_file_name)
        if match:
            name = f"{match.group(1)} {match.group(2)}".lower()
        else:
            # മാച്ച് ചെയ്തില്ലെങ്കിൽ ഫയലിന്റെ ആദ്യ ഭാഗം എടുക്കുന്നു
            name = first_file_name.split()[0].lower()

    if await batch_exists(name):
        return await message.reply_text(f"Collection '{name}' already exists.")

    await save_batch_collection(name, uid, data["files"])
    del BATCH_MODE[uid]

    await message.reply_text(
        f"✅ Collection Saved\n\n"
        f"📦 Name: {name}\n"
        f"📁 Files: {total}"
    )


@Client.on_message(filters.command("viewfilter") & (filters.group | filters.private))
async def view_batch_filter(client, message):
    if len(message.command) < 2: return await message.reply_text("Use: /viewfilter <collection_name>")
    name = message.command[1].lower()
    data = await get_batch_collection(name)
    if not data: return await message.reply_text("Collection not found.")
    text = f"📦 Batch: **{name}**\n\n"
    for i, f in enumerate(data["files"], start=1):
        text += f"{i}. {f['file_name']}\n"
    await message.reply_text(text)

@Client.on_message(filters.command("delete_filter") & (filters.group | filters.private))
async def delete_batch_filter(client, message):
    if len(message.command) < 2: return await message.reply_text("Use: /delete_filter <collection_name>")
    name = message.command[1].lower()
    if not await batch_col.find_one({"_id": name}): return await message.reply_text("Not found.")
    await batch_col.delete_one({"_id": name})
    await message.reply_text(f"Batch **{name}** deleted ✅")

@Client.on_message(filters.command("batch_list") & (filters.group | filters.private))
async def batch_list(client, message):
    data = await get_all_batch_collections()
    if not data: return await message.reply_text("No batch collections found.")
    text = "📦 Saved Batch Collections:\n\n"
    for i, batch in enumerate(data, start=1):
        text += f"{i}. {batch['_id']} ({len(batch.get('files', []))} files)\n"
    await message.reply_text(text)

@Client.on_message(filters.command("clearallbatch") & filters.user(ADMINS)) # അഡ്മിന് മാത്രം ഉപയോഗിക്കാൻ
async def clear_all_batches(client, message):
    await batch_col.delete_many({}) # ഡാറ്റാബേസിലെ എല്ലാ ബാച്ചുകളും കളയുന്നു
    await message.reply_text("✅ All saved batch collections deleted from database!")


# ✅ NEW COMMAND ADDED
@Client.on_message(filters.command("clearbatch") & (filters.group | filters.private))
async def clear_batch_session(client, message):
    uid = message.from_user.id
    if uid in BATCH_MODE:
        del BATCH_MODE[uid]
        await message.reply_text("✅ Current batch session cleared successfully!")
    else:
        await message.reply_text("❌ No active batch session found.")
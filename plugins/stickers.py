import os
import requests
from PIL import Image
from pyrogram import Client, filters
from info import *
# ================= CONFIG =================


# ================= STORAGE =================
TEMP_FILES = {}
USER_PACKS = {}

# ================= SAVE FILE =================
@Client.on_message(
    filters.private &
    (
        filters.photo |
        filters.document |
        filters.video
    )
)
async def save_file(client, message):

    msg = await message.reply_text(
        "📥 Downloading..."
    )

    file_path = await message.download()

    file_type = None

    # ================= PHOTO =================
    if message.photo:

        new_path = (
            f"{message.from_user.id}.png"
        )

        # Open image
        img = Image.open(file_path)

        # Resize image
        img.thumbnail((512, 512))

        # Save PNG
        img.save(
            new_path,
            "PNG"
        )

        try:
            os.remove(file_path)
        except:
            pass

        file_path = new_path

        file_type = "photo"

    # ================= VIDEO =================
    elif file_path.endswith(".webm"):

        file_type = "video"

    else:

        try:
            os.remove(file_path)
        except:
            pass

        return await msg.edit_text(
            "❌ Only Photo or .webm supported."
        )

    TEMP_FILES[
        message.from_user.id
    ] = {
        "path": file_path,
        "type": file_type
    }

    await msg.edit_text(
        "✅ File Saved\n\n"
        "Now send:\n"
        "/kang PackName"
    )

# ================= CREATE PACK =================
@Client.on_message(
    filters.command("kang")
)
async def kang_pack(client, message):

    user_id = message.from_user.id

    if user_id not in TEMP_FILES:

        return await message.reply_text(
            "❌ Send photo or .webm first."
        )

    if len(message.command) < 2:

        return await message.reply_text(
            "Usage:\n/kang PackName"
        )

    pack_title = message.command[1]

    data = TEMP_FILES[user_id]

    file_path = data["path"]

    file_type = data["type"]

    msg = await message.reply_text(
        "📤 Creating Sticker Pack..."
    )

    try:

        bot_username = (
            await client.get_me()
        ).username

        short_name = (
            f"{pack_title}_{user_id}"
            f"_by_{bot_username}"
        ).lower()

        url = (
            f"https://api.telegram.org/bot"
            f"{BOT_TOKEN}/createNewStickerSet"
        )

        payload = {
            "user_id": user_id,
            "name": short_name,
            "title": pack_title,
            "emojis": "🔥"
        }

        # ================= PHOTO STICKER =================
        if file_type == "photo":

            with open(file_path, "rb") as sticker:

                response = requests.post(
                    url,
                    data=payload,
                    files={
                        "png_sticker": sticker
                    }
                )

        # ================= VIDEO STICKER =================
        else:

            with open(file_path, "rb") as sticker:

                response = requests.post(
                    url,
                    data=payload,
                    files={
                        "webm_sticker": sticker
                    }
                )

        result = response.json()

        # ================= SUCCESS =================
        if result.get("ok"):

            if user_id not in USER_PACKS:
                USER_PACKS[user_id] = []

            USER_PACKS[user_id].append(
                {
                    "title": pack_title,
                    "short": short_name
                }
            )

            await msg.edit_text(
                f"✅ Sticker Pack Created!\n\n"
                f"https://t.me/addstickers/"
                f"{short_name}"
            )

        else:

            await msg.edit_text(
                f"❌ Error:\n"
                f"{result}"
            )

    except Exception as e:

        await msg.edit_text(
            f"❌ Error:\n{e}"
        )

    # ================= CLEANUP =================
    try:
        os.remove(file_path)
    except:
        pass

    TEMP_FILES.pop(user_id, None)

# ================= PACK LIST =================
@Client.on_message(
    filters.command("packs")
)
async def packs_list(client, message):

    user_id = message.from_user.id

    if user_id not in USER_PACKS:

        return await message.reply_text(
            "❌ No packs found."
        )

    text = "📦 Your Sticker Packs\n\n"

    for num, pack in enumerate(
        USER_PACKS[user_id],
        start=1
    ):

        text += (
            f"{num}. "
            f"{pack['title']}\n"
            f"https://t.me/addstickers/"
            f"{pack['short']}\n\n"
        )

    await message.reply_text(
        text,
        disable_web_page_preview=True
    )

# ================= START BOT =================

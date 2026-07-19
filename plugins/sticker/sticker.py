from pyrogram import Client, filters
# from pyrogram.types import InputStickerSetItem
from PIL import Image
from info import *
import os

from pyrogram.raw.types import InputStickerSetItem

app = Client("sticker_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 1. /kang കമാൻഡ് - ഫോട്ടോയെ സ്റ്റിക്കറാക്കി മാറ്റാൻ
@Client.on_message(filters.command("kang") & filters.reply)
def make_sticker(client, message):
    replied = message.reply_to_message
    if replied.photo or replied.document:
        msg = message.reply("പ്രോസസ്സ് ചെയ്യുന്നു, ദയവായി കാത്തിരിക്കുക...")
        path = client.download_media(replied)
        
        # സ്റ്റിക്കർ സൈസിലേക്ക് (512x512) മാറ്റുന്നു
        img = Image.open(path)
        img.thumbnail((512, 512))
        img.save("sticker.webp", "WEBP")
        
        # സ്റ്റിക്കർ അയക്കുന്നു
        client.send_sticker(message.chat.id, "sticker.webp")
        msg.delete()
        
        os.remove(path)
        os.remove("sticker.webp")
    else:
        message.reply("ദയവായി ഒരു ഫോട്ടോയ്ക്ക് മറുപടിയായി '/kang' എന്ന് അയക്കുക.")

# 2. /pack കമാൻഡ് - സ്റ്റിക്കർ പാക്ക് നിർമ്മിക്കാൻ/ആഡ് ചെയ്യാൻ
@Client.on_message(filters.command("pack") & filters.reply)
def add_to_pack(client, message):
    replied = message.reply_to_message
    if replied.sticker:
        # പാക്കിന്റെ പേര് (യുണീക്ക് ആയിരിക്കണം)
        pack_name = f"sticker_pack_{message.from_user.id}"
        pack_title = f"{message.from_user.first_name}'s Pack"
        
        try:
            # ആദ്യം പാക്ക് ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു, ഇല്ലെങ്കിൽ നിർമ്മിക്കുന്നു
            client.create_sticker_set(
                user_id=message.from_user.id,
                name=pack_name,
                title=pack_title,
                stickers=[InputStickerSetItem(file_id=replied.file_id, emojis="⭐")]
            )
            message.reply("പുതിയ സ്റ്റിക്കർ പാക്ക് വിജയകരമായി നിർമ്മിച്ചു!")
        except Exception:
            # പാക്ക് നിലവിലുണ്ടെങ്കിൽ സ്റ്റിക്കർ മാത്രം ആഡ് ചെയ്യുന്നു
            try:
                client.add_sticker_to_set(
                    user_id=message.from_user.id,
                    name=pack_name,
                    sticker=InputStickerSetItem(file_id=replied.file_id, emojis="⭐")
                )
                message.reply("ഈ സ്റ്റിക്കർ നിങ്ങളുടെ പാക്കിലേക്ക് വിജയകരമായി ചേർത്തു!")
            except Exception as e:
                message.reply(f"പിശക് സംഭവിച്ചു: {e}")
    else:
        message.reply("ദയവായി ഒരു സ്റ്റിക്കറിന് മറുപടിയായി '/pack' എന്ന് അയക്കുക.")


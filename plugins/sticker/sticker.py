import os
import asyncio
from pyrogram import Client, filters
from PIL import Image
from info import *

# ടെമ്പററി ഫയൽ നെയിം യുണീക്ക് ആക്കുന്നതിനായി os.path ഉപയോഗിക്കുന്നു
TEMP_STICKER = "temp_sticker.webp"

def resize_image(photo_path):
    """ഫോട്ടോയെ ടെലിഗ്രാം സ്റ്റിക്കർ സൈസിലേക്ക് (512x512) മാറ്റുന്നു"""
    with Image.open(photo_path) as im:
        # im.thumbnail സൈസ് കൃത്യമായി 512x512 ആക്കാൻ resize ഉപയോഗിക്കുന്നതാണ് നല്ലത്
        im = im.convert("RGBA")
        im.thumbnail((512, 512))
        im.save(TEMP_STICKER, "WEBP", quality=95)
    return TEMP_STICKER

from pyrogram import Client, filters
from PIL import Image
import os

# ശ്രദ്ധിക്കുക: നിങ്ങളുടെ പ്രധാന ഫയലിലെ ക്ലയന്റ് നെയിം (ഉദാ: Bot, App, userbot) ഇവിടെ നൽകുക
# മിക്കവാറും ഇത് 'Bot' എന്നോ 'app' എന്നോ ആയിരിക്കും.
# നിങ്ങളുടെ main.py ഫയലിൽ 'App = Client(...)' എന്നാണെങ്കിൽ ഇവിടെയും 'App' എന്ന് കൊടുക്കുക.
@Client.on_message(filters.command("kang") & filters.reply)
async def kang_image(client, message):
    # ലോഗ് ചെയ്യാൻ പ്രിന്റ് ചേർത്തു
    print("Kang command triggered!") 
    
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("ദയവായി ഒരു ഫോട്ടോയ്ക്ക് റിപ്ലൈ ആയി ഈ കമാൻഡ് അയക്കുക!")
        return

    status = await message.reply_text("ഫോട്ടോ സ്റ്റിക്കർ ആക്കി മാറ്റുന്നു... ⏳")
    
    # ഫയൽ പാത്ത് യുണീക്ക് ആക്കാൻ (ഒരേ സമയം പലർ ഉപയോഗിച്ചാൽ പ്രശ്നം വരാതിരിക്കാൻ)
    # message.from_user.id ഉപയോഗിക്കുന്നു
    user_id = message.from_user.id
    photo_path = f"photo_{user_id}.jpg"
    sticker_path = f"sticker_{user_id}.webp"

    try:
        await message.reply_to_message.download(file_name=photo_path)
        
        with Image.open(photo_path) as im:
            im = im.convert("RGBA")
            im.thumbnail((512, 512))
            im.save(sticker_path, "WEBP", quality=95)
        
        await message.reply_sticker(sticker_path)
        await status.delete()

    except Exception as e:
        await status.edit(f"❌ Error: {e}")
        print(f"Error: {e}")
    
    # ഫയലുകൾ ഡിലീറ്റ് ചെയ്യുന്നു
    if os.path.exists(photo_path): os.remove(photo_path)
    if os.path.exists(sticker_path): os.remove(sticker_path)
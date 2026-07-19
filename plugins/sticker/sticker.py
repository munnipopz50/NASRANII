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

@Client.on_message(filters.command("kang") & filters.reply)
async def kang_image(client, message):
    # ഫോട്ടോ ഉണ്ടോ എന്ന് ഉറപ്പുവരുത്താൻ
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("ദയവായി ഒരു ഫോട്ടോയ്ക്ക് റിപ്ലൈ ആയി ഈ കമാൻഡ് അയക്കുക!")
        return

    status = await message.reply_text("ഫോട്ടോ സ്റ്റിക്കർ ആക്കി മാറ്റുന്നു... ⏳")
    
    try:
        # ഡൗൺലോഡ് ചെയ്യുന്നത് നേരിട്ട് ഫയൽ പാത്ത് ആയി എടുക്കുന്നു
        photo_path = await message.reply_to_message.download(file_name="temp_photo.jpg")
        
        # സ്റ്റിക്കർ റീസൈസ് ചെയ്യുന്നു
        sticker_file = resize_image(photo_path)
        
        # സ്റ്റിക്കർ അയക്കുന്നു
        await message.reply_sticker(sticker_file)
        
        # താൽക്കാലിക ഫയലുകൾ ഡിലീറ്റ് ചെയ്യുന്നു
        await status.delete()
        if os.path.exists(photo_path): os.remove(photo_path)
        if os.path.exists(TEMP_STICKER): os.remove(TEMP_STICKER)

    except Exception as e:
        await status.edit(f"❌ Error: {e}")
        print(f"Error in kang command: {e}") # ടെർമിനലിൽ എറർ കാണാൻ

@Client.on_message(filters.command("pack") & filters.reply)
async def make_pack(client, message):
    if not message.reply_to_message.sticker:
        await message.reply_text("ഞാൻ ഉണ്ടാക്കി തന്ന സ്റ്റിക്കറിന് റിപ്ലൈ ആയി വേണം `/pack` എന്ന് അയക്കാൻ!")
        return

    user_name = message.from_user.first_name

    await message.reply_text(
        f"ഹലോ {user_name},\n\nഈ സ്റ്റിക്കർ നിങ്ങളുടെ സ്വന്തം പാക്കിലേക്ക് ചേർക്കാൻ താഴെ പറയുന്നവ ചെയ്യുക:\n\n"
        "1. @Stickers ബോട്ട് സ്റ്റാർട്ട് ചെയ്യുക.\n"
        "2. `/newpack` എന്ന് അയക്കുക.\n"
        "3. മുകളിലെ സ്റ്റിക്കർ അവർക്ക് ഫോർവേഡ് ചെയ്യുക."
    )
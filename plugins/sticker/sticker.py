import os
from pyrogram import Client, filters
from PIL import Image
from info import * 

# വേരിയബിൾ പേര് 'Client' എന്ന് തന്നെയാക്കുന്നു


TEMP_STICKER = "temp_sticker.webp"

def resize_image(photo_path):
    """ഫോട്ടോയെ ടെലിഗ്രാം സ്റ്റിക്കർ സൈസിലേക്ക് (512x512) മാറ്റുന്നു"""
    im = Image.open(photo_path)
    im.thumbnail((512, 512))
    im.save(TEMP_STICKER, "WEBP")
    return TEMP_STICKER

@Client.on_message(filters.command("kang") & filters.reply)
async def kang_image(client, message):
    if not message.reply_to_message.photo:
        await message.reply_text("ദയവായി ഒരു ഫോട്ടോയ്ക്ക് റിപ്ലൈ ആയി ഈ കമാൻഡ് അയക്കുക!")
        return
    
    status = await message.reply_text("ഫോട്ടോ സ്റ്റിക്കർ ആക്കി മാറ്റുന്നു... ⏳")
    photo_path = await message.reply_to_message.download()
    
    try:
        sticker_file = resize_image(photo_path)
        await message.reply_sticker(sticker_file)
        await status.delete()
        os.remove(photo_path)
        
    except Exception as e:
        await status.edit(f"Error: {e}")
        if os.path.exists(photo_path):
            os.remove(photo_path)

@Client.on_message(filters.command("pack") & filters.reply)
async def make_pack(client, message):
    if not message.reply_to_message.sticker:
        await message.reply_text("ഞാൻ ഉണ്ടാക്കി തന്ന സ്റ്റിക്കറിന് റിപ്ലൈ ആയി വേണം `/pack` എന്ന് അയക്കാൻ!")
        return
    
    user_name = message.from_user.first_name
    
    await message.reply_text(
        f"ഹലോ {user_name},\n\nഈ സ്റ്റിക്കർ നിങ്ങളുടെ സ്വന്തം പാക്കിലേക്ക് ചേർക്കാൻ താഴെ പറയുന്നവ ചെയ്യുക:\n"
        "1. @Stickers ബോട്ട് സ്റ്റാർട്ട് ചെയ്യുക.\n"
        "2. `/newpack` എന്ന് അയക്കുക.\n"
        "3. മുകളിലെ സ്റ്റിക്കർ അവർക്ക് ഫോർവേഡ് ചെയ്യുക."
    )


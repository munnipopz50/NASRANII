print("=== STICKER IMPORTED ===")
from pyrogram import Client, filters
from pyrogram.types import Message
# ടെലിഗ്രാമിന്റെ raw ഫങ്ക്ഷനുകൾ ഇംപോർട്ട് ചെയ്യുന്നു
from pyrogram.raw import functions
from pyrogram.raw.types import ReactionEmoji



from pyrogram import Client, filters
print("✅ STICKERS PLUGIN LOADED")

@Client.on_message(filters.command("s"))
async def stikcker(client, message):
    await message.reply_text("Working")
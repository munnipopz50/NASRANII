from pyrogram import Client, filters


print("✅ STICKERS PLUGIN LOADED")
print("=== STICKER IMPORTED ===")



@Client.on_message(filters.command("s"))
async def stikcker(client, message):
    await message.reply_text("Working")
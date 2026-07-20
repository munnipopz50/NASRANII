from pyrogram import Client, filters


print("✅ STICKERS PLUGIN LOADED")
@Client.on_message(filters.command("s"))
async def sticker(client, message):
    print("STICKER COMMAND RECEIVED")
    await message.reply_text("✅ Sticker command working")
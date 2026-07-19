from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

FONT_PATH = "arial.ttf"  # അല്ലെങ്കിൽ നിങ്ങളുടെ .ttf font
SIZE = (512, 512)

@Client.on_message(filters.command("sticker"))
async def text_to_sticker(client: Client, message: Message):

    if len(message.command) > 1:
        text = " ".join(message.command[1:])
    elif message.reply_to_message and message.reply_to_message.text:
        text = message.reply_to_message.text
    else:
        return await message.reply_text(
            "Usage:\n`/sticker Your text`\nഅല്ലെങ്കിൽ ഒരു text-ന് reply ചെയ്ത് `/sticker` അയക്കുക."
        )

    img = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, 42)
    except:
        font = ImageFont.load_default()

    wrapped = "\n".join(textwrap.wrap(text, width=18))

    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    x = (512 - w) // 2
    y = (512 - h) // 2

    draw.multiline_text(
        (x, y),
        wrapped,
        font=font,
        fill="white",
        align="center",
        stroke_width=2,
        stroke_fill="black"
    )

    output = "text_sticker.webp"
    img.save(output, "WEBP")

    await message.reply_sticker(output)

    os.remove(output)
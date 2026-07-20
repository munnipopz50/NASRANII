import os
import uuid
import textwrap

from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "fonts/NotoSansMalayalam-Regular.ttf"
SIZE = (512, 512)


@Client.on_message(filters.command("sticker"))
async def text_to_sticker(client: Client, message: Message):

    if len(message.command) > 1:
        text = " ".join(message.command[1:])
    elif message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
        if not text:
            return await message.reply_text(
                "Reply ചെയ്ത മെസ്സേജിൽ text അല്ലെങ്കിൽ caption ഇല്ല."
            )
    else:
        return await message.reply_text(
            "**Usage:**\n"
            "`/sticker Your text`\n\n"
            "അല്ലെങ്കിൽ ഒരു text/caption message-ന് reply ചെയ്ത് `/sticker` അയക്കുക."
        )

    img = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Auto font size
    font_size = 48

    while font_size >= 18:
        font = ImageFont.truetype(FONT_PATH, font_size)
        wrapped = "\n".join(textwrap.wrap(text, width=18))

        bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        if w <= 470 and h <= 470:
            break

        font_size -= 2

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

    output = f"{uuid.uuid4().hex}.webp"

    img.save(output, "WEBP", quality=100)

    await message.reply_sticker(output)

    if os.path.exists(output):
        os.remove(output)
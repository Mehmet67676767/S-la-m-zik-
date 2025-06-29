from pyrogram import filters
from pyrogram.types import Message
from ArchMusic import app

# Bot adı veya anahtar kelimeler
ANAHTAR_KELIMELER = ["Mustafa", "mustafa ragnar", "Ragnar",  "musto"]

@app.on_message(filters.text & filters.group)
async def bahsedilince_etiketle(_, message: Message):
    if not message.text:
        return

    metin = message.text.lower()
    if any(kelime in metin for kelime in ANAHTAR_KELIMELER):
        user = message.from_user
        mention = f"[@{user.username}](tg://user?id={user.id})" if user.username else f"[{user.first_name}](tg://user?id={user.id})"
        await message.reply_text(f"🎧 {mention}, o benim babam?")
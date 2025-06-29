from pyrogram import filters
from pyrogram.types import Message
from ArchMusic import app  # ArchMusic bot objesi
from httpx import AsyncClient
from io import BytesIO

http = AsyncClient()

@app.on_message(filters.command(["q", "r"]) & filters.reply)
async def quote_command(_, message: Message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("⛔ Bir mesaja yanıt ver.")

    await message.reply("🎨 Alıntı hazırlanıyor...")

    messages = [replied]
    if message.command[0] == "r":
        messages.insert(0, message)

    try:
        msg_data = [{
            "text": m.text or m.caption or "",
            "author": {
                "name": m.from_user.first_name,
                "id": m.from_user.id,
                "username": m.from_user.username or ""
            }
        } for m in messages]

        response = await http.post("https://bot.lyo.su/quote/generate.png", json={
            "type": "quote",
            "format": "png",
            "backgroundColor": "#1e1e1e",
            "messages": msg_data
        })

        img = BytesIO(response.content)
        img.name = "quote.png"
        await message.reply_document(img, caption="✅ Alıntı hazır!")
    except Exception as e:
        await message.reply(f"❌ Hata: {e}")
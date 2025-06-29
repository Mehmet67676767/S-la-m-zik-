from pyrogram import filters
from pyrogram.types import Message
from ArchMusic import app
import asyncio
import random
from datetime import datetime

AKTIF_GRUP = -1002064126671  # Sohbet yapılacak grup ID'si

# Zaman zaman kendiliğinden konuşacağı cümleler
OTOMATIK_SOZLER = [
    "Buralar ne sessiz böyle... 😴",
    "Birisi müzik ister mi? 🎶",
    "Hadi biraz sohbet edelim!",
    "Selam! Nasılsınız? 🙂",
    "Ben buradayım, siz neredesiniz?"
]

# Kullanıcı mesajına cevap verilecek kelimelere göre yanıtlar
SOHBET_YANITLARI = {
    "selam": ["Merhaba!", "Selamlar!", "Hoş geldin!"],
    "nasılsın": ["İyiyim, ya sen?", "Gayet iyiyim, teşekkür ederim!"],
    "ne yapıyorsun": ["Bekliyorum ki biri sohbet etsin 😄", "Sohbet başlatmaya hazırım!"],
    "bot": ["Ben bir yapay zekayım. Müzik ve sohbet konusunda iyiyim!"]
}

# Rastgele aralıklarla kendi kendine konuşma
async def otomatik_sohbet():
    await app.start()
    while True:
        await asyncio.sleep(random.randint(60, 120))  # 1-2 dakika arası
        try:
            mesaj = random.choice(OTOMATIK_SOZLER)
            await app.send_message(AKTIF_GRUP, mesaj)
        except Exception as e:
            print(f"Otomatik mesaj hatası: {e}")

@app.on_message(filters.text & filters.group)
async def cevapla(_, message: Message):
    if message.chat.id != AKTIF_GRUP:
        return
    if message.from_user.is_bot or message.text.startswith("/"):
        return

    metin = message.text.lower()
    for kelime, yanitlar in SOHBET_YANITLARI.items():
        if kelime in metin:
            cevap = random.choice(yanitlar)
            await message.reply(cevap)
            break

# Otomatik konuşma döngüsünü başlat
app.loop.create_task(otomatik_sohbet())
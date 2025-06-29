from pyrogram import filters
from pyrogram.types import Message
from ArchMusic import app
import random

KELIMELER = ["elma", "kitap", "masa", "bardak", "araba", "telefon", "kedi", "oyun", "robot"]
OYUNLAR = {}

@app.on_message(filters.command("turet") & filters.group)
async def oyun_baslat(_, message: Message):
    kelime = random.choice(KELIMELER)
    chat_id = message.chat.id
    OYUNLAR[chat_id] = {
        "ana": kelime,
        "puan": {}
    }
    await message.reply(f"🎮 *Kelimeyi Türet* başladı!\nBaşlangıç kelimesi: `{kelime}`\n\nYeni kelime türetin!", quote=True)

@app.on_message(filters.text & filters.group)
async def kontrol_et(_, message: Message):
    chat_id = message.chat.id
    if chat_id not in OYUNLAR:
        return
    oyun = OYUNLAR[chat_id]
    kelime = message.text.lower()
    if len(kelime) < 3:
        return
    if kelime == oyun["ana"]:
        return
    if all(harf in oyun["ana"] for harf in kelime):
        oyuncu_id = message.from_user.id
        oyun["puan"][oyuncu_id] = oyun["puan"].get(oyuncu_id, 0) + 1
        await message.reply(f"✅ Geçerli kelime! +1 puan 🏆\nKelime: `{kelime}`")
    else:
        await message.reply("❌ Bu kelime başlangıç kelimesinden türetilemez!")

@app.on_message(filters.command("puanlar") & filters.group)
async def puan_tablosu(_, message: Message):
    chat_id = message.chat.id
    if chat_id not in OYUNLAR or not OYUNLAR[chat_id]["puan"]:
        return await message.reply("🔹 Henüz puan yok.")
    puanlar = OYUNLAR[chat_id]["puan"]
    sirali = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)
    metin = "🏅 *Puan Tablosu*:\n\n"
    for sira, (uid, puan) in enumerate(sirali, 1):
        kullanici = await app.get_users(uid)
        metin += f"{sira}. {kullanici.first_name} – {puan} puan\n"
    await message.reply(metin)
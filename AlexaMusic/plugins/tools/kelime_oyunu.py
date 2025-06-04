
from pyrogram import Client, filters
import random
import asyncio

# Kelime listesini yükle
with open("turkce_kelimeler.txt", "r", encoding="utf-8") as f:
    GECERLI_KELIMELER = set(line.strip() for line in f)

# Ana kelimeler
ANA_KELIMELER = ["kalem", "kitap", "bardak", "telefon", "çanta", "bilgisayar", "sandalye", "defter", "masa", "kablo"]

aktif_oyunlar = {}  # user_id: {"ana": str, "uretilen": set}

app = Client("kelime_oyunu_bot", api_id=123456, api_hash="your_api_hash", bot_token="your_bot_token")

@app.on_message(filters.command("oyun") & filters.private)
async def oyun_baslat(client, message):
    kelime = random.choice(ANA_KELIMELER)
    aktif_oyunlar[message.from_user.id] = {"ana": kelime, "uretilen": set()}
    await message.reply(f"""🧠 Kelime türetme oyunu başladı!
🔤 Ana kelime: {kelime.upper()}
Bir kelime türet ve gönder.""")

@app.on_message(filters.text & filters.private)
async def tahmin_kontrol(client, message):
    user_id = message.from_user.id
    if user_id not in aktif_oyunlar:
        return

    tahmin = message.text.strip().lower()
    oyun = aktif_oyunlar[user_id]
    ana = oyun["ana"]

    if tahmin in oyun["uretilen"]:
        return await message.reply("❗ Bu kelimeyi zaten kullandın.")
    if not all(tahmin.count(harf) <= ana.count(harf) for harf in tahmin):
        return await message.reply("❌ Bu kelime, verilen harflerle oluşturulamaz.")
    if tahmin not in GECERLI_KELIMELER:
        return await message.reply("❌ Bu gerçek bir Türkçe kelime değil.")

    oyun["uretilen"].add(tahmin)
    await message.reply(f"✅ Kabul edildi: `{tahmin}`")

app.run()

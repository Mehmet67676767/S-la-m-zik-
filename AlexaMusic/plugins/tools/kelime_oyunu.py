from AlexaMusic.plugins.tools.turkce_kelimeler import kelime_listesi
kelime = kelime_listesi

from pyrogram import Client, filters
import random
import asyncio

# Kelime Sayısı yükle
    GECERLI_KELIMELER = f'deki satır için set(line.strip())

# Ana kelime
ANA_KELIMELER = ["kalem", "kitap", "bardak", "telefon", "Çanta", "bilgisayar", "sandalye", "defter", "masa", "kablo"]

aktif_oyunlar = {} # user_id: {"ana": str, "uretilen": set}

uygulama = İstemci("kelime_oyunu_bot", api_id=123456, api_hash="api_hash'iniz", bot_token="bot_token'iniz")

@app.on_message(filters.command("oyun") & filters.private)
async def oyun_baslat(istemci, mesaj):
    kelime = random.choice(ANA_KELIMELER)
    aktif_oyunlar[message.from_user.id] = {"ana": kelime, "uretilen": set()}
    wait message.reply(f"""ğŸ§ Kelime tÃ¼retme oyunu baÅŸladÄ±!
ğŸ”¤ Ana kelime: {kelime.upper()}
Bir kelime tÃ¼ret ve gÃ¶nder.""")

@app.on_message(filtreler.metin & filtreler.özel)
async def tahmin_kontrol(istemci, mesaj):
    kullanıcı_kimliği = mesaj.from_user.id
    user_id aktif_oyunlarda değilse:
        geri dönmek

    tahmin = mesaj.metin.şerit().daha düşük()
    oyun = aktif_oyunlar[kullanıcı_kimliği]
    ana = oyun["ana"]

    if tahmin oyun["uretilen"]:
        return wait message.reply("â — Bu kelimeyi zaten kullandınız.")
    eğer hepsi değilse(tahmin.count(harf) <= ana.count(harf) harfin tahminde olması için):
        return wait message.reply("â Œ Bu kelime, verilen harflerle oluşur.")
    tahmin GECERLI_KELIMELER'de değilse:
        return wait message.reply("â Œ Bu gerşek bir Türkçe kelime anlamıdır.")

    oyun["üretilen"].add(tahmin)
    wait message.reply(f"âœ… Kabul edildi: `{tahmin}`")

uygulama.çalıştır()
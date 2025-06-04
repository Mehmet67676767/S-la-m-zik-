from datetime import datetime
from config import LOG, LOG_GROUP_ID
import psutil
from AlexaMusic import app
from AlexaMusic.utils.database import is_on_off
from AlexaMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from AlexaMusic.utils.database import get_served_chats

async def play_logs(message, streamtype):
    chat_id = message.chat.id
    try:
        member_count = await app.get_chat_members_count(chat_id)
    except Exception:
        member_count = "Bilinmiyor"

    toplam_grup = len(await get_served_chats())
    aktif_sesli = len(await get_active_chats())
    aktif_video = len(await get_active_video_chats())

    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if not await is_on_off(LOG):
        return

    chat_title = message.chat.title or "Bilinmiyor"
    chat_username = f"@{message.chat.username}" if message.chat.username else "🔐 Gizli Grup"
    user_mention = message.from_user.mention if message.from_user else "Bilinmiyor"
    user_username = f"@{message.from_user.username}" if message.from_user and message.from_user.username else "Yok"
    user_id = message.from_user.id if message.from_user else "Yok"
    query = message.text or "Yok"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logger_text = f"""
╭━━━[ 🔊 **YENİ MÜZİK BAŞLATILDI** ]━━━➤
┃
┃ 🏷️ **Grup:** {chat_title}
┃ 🆔 **Grup ID:** `{chat_id}`
┃ 🔗 **Link:** {chat_username}
┃ 👥 **Üyeler:** {member_count}
┃
┃ 🙋 **Kullanıcı:** {user_mention}
┃ 🧾 **Kullanıcı Adı:** {user_username}
┃ 🆔 **ID:** `{user_id}`
┃
┃ 🎧 **Yayın Türü:** `{streamtype}`
┃ 🔎 **Sorgu:** `{query}`
┃
┃ 📊 **Sistem Durumu**
┃ ├ 🖥️ CPU: `{cpu}%`
┃ ├ 💾 RAM: `{mem}%`
┃ └ 📦 Disk: `{disk}%`
┃
┃ 📌 **Genel Durum**
┃ ├ 🌐 Toplam Grup: `{toplam_grup}`
┃ ├ 🔈 Aktif Sesli: `{aktif_sesli}`
┃ └ 🎥 Aktif Video: `{aktif_video}`
┃
┃ 🕒 **Zaman:** `{now}`
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━➤
"""

    if chat_id != LOG_GROUP_ID:
        try:
            await app.send_message(
                LOG_GROUP_ID,
                logger_text,
                disable_web_page_preview=True,
            )
        except Exception as e:
            print(f"Log gönderilemedi: {e}")
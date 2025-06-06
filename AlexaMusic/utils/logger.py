from config import LOG, LOG_GROUP_ID
import psutil
from AlexaMusic import app
from AlexaMusic.utils.database import is_on_off
from AlexaMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from AlexaMusic.utils.database import (
    get_served_chats)

async def play_logs(message, streamtype):
    chat_id = message.chat.id
    member_count = await app.get_chat_members_count(chat_id)
    total_groups = len(await get_served_chats())
    active_voice = len(await get_active_chats())
    active_video = len(await get_active_video_chats())

    # Sistem bilgileri
    cpu = f"{psutil.cpu_percent(interval=0.5)}%"
    ram = f"{psutil.virtual_memory().percent}%"
    disk = f"{psutil.disk_usage('/').percent}%"

    # Loglama açık mı?
    if not await is_on_off(LOG):
        return

    # Grup bağlantısı (herkese açık repo için gösterilmez)
    if message.chat.username:
        group_link = f"https://t.me/{message.chat.username}"
    else:
        group_link = "Bağlantı gizlendi (özel grup)"

    # Kullanıcı bilgisi
    user = message.from_user
    user_name = f"@{user.username}" if user.username else user.first_name
    user_mention = user.mention if hasattr(user, "mention") else user_name

    # Log metni
    log_text = f"""
📌 **Grup:** {message.chat.title} [`{chat_id}`]
👥 **Üye Sayısı:** {member_count}
👤 **Kullanıcı:** {user_mention}
🔢 **Kullanıcı ID:** `{user.id}`
🔗 **Grup Linki:** {group_link}
🔎 **Sorgu:** {message.text or "Komut"}

🖥️ **CPU:** {cpu} | **RAM:** {ram} | **Disk:** {disk}
📊 **Toplam Gruplar:** {total_groups}
🎧 **Aktif Sesli:** {active_voice} | 📹 **Aktif Video:** {active_video}
"""

    # Log grubuna gönder
    if chat_id != LOG_GROUP_ID:
        try:
            await app.send_message(
                LOG_GROUP_ID,
                log_text,
                disable_web_page_preview=True
            )
        except Exception as e:
            print(f"Log gönderimi başarısız: {e}")
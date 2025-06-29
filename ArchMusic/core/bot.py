import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class ArchMusic(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "ArchMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        try:
            get_me = await self.get_me()
            self.username = get_me.username
            self.id = get_me.id

            video_url = "https://www.kapwing.com/videos/686148e2f05fa4d65fe3cf21"
            caption = "Bot Started"

            try:
                await self.send_video(
                    config.LOG_GROUP_ID,
                    video=video_url,
                    caption=caption,
                )
            except:
                LOGGER(__name__).error(
                    "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
                )
                sys.exit()

            if config.SET_CMDS == str(True):
                try:
                    await self.set_bot_commands(
                        [
                            BotCommand("play", "🎙 Müziği oynatır"),
                            BotCommand("voynat", "📺 Videoyu oynatır"),
                            BotCommand("atla", "⏭️ Sonraki Parçaya Geçer"),
                            BotCommand("duraklat", "⏸️ Çalan Parçayı Durdurur"),
                            BotCommand("devam", "▶️ Çalan Parçayı Devam Ettirir"),
                            BotCommand("son", "⏹️ Çalan Parçayı Kapatır"),
                            BotCommand("karistir", "🔀 Çalan Parçayı Karıştırır"),
                            BotCommand("dongu", "🔄 Çalan Parçayı Tekrarlar"),
                            BotCommand("ilerisar", "⏩ Parçayı İleri Sarar"),
                            BotCommand("gerisar", "⏪ Parçayı Geri Sarar"),
                            BotCommand("playlist", "📖 Çalma Listenizi Gösterir"),
                            BotCommand("bul", "📩 Seçtiğiniz Parçayı İndirir"),
                            BotCommand("sarki", "🎵Şarkı önerir Armağan eder."),
                            BotCommand("ayarlar", "⚙️ Bot Ayarlarını Gösterir"),
                            BotCommand("playmode", "⚙️Admin ayarları"),
                            BotCommand("restart", "🔃 Botu Yeniden Başlatır"),
                            BotCommand("reload", "❤️‍🔥 Yönetici Önbelleğini Günceller"),
                        ]
                    )
                except:
                    pass
            else:
                pass

            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Please promote Bot as Admin in Logger Group"
                )
                sys.exit()

        except Exception as e:
            LOGGER(__name__).error(f"Error during bot start: {e}")
            sys.exit()

        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name

        LOGGER(__name__).info(f"MusicBot Started as {self.name}")

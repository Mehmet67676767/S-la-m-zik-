import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

import config

from ..logging import LOGGER


private_commands = [
    BotCommand("start", "🎧 Botu başlatır"),
    BotCommand("yardim", "📖 Yardım menüsünü gösterir"),
]



group_commands = [
    BotCommand("help", "️ℹ️Bot hakkında yardım. "),
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
    BotCommand("tag", "🏷️Tek tek etiketler.ı"),
    BotCommand("utag", "🏷️Çoklu etiketler."),
    BotCommand("etag", "🏷️Emoji ile etiketler."),
    BotCommand("btag", "🏷️Bayrak ile etiketler."),
    BotCommand("sorutag", "🏷️Sorularla etiketler."),
    BotCommand("stag", "🏷️Sözlerle etiketler."),
    BotCommand("igtag", "🏷️İyigeceler sözleri ile etiketler."),
    BotCommand("guntag", "🏷️Günaydın sözleri ile etiketler."),
    BotCommand("cancel", "❌Etiket İşlemini Bitirir."),
    BotCommand("chatmode", "💬 sohbet aç - kapat."),
    BotCommand("eros", "💘Eros oku atar."),
    BotCommand("burc", "⚖️Burçlarınızı yorumlarım.ı"),
    BotCommand("mani", "📜Mani söylerim."),
    BotCommand("saka", "😋Rasgele birine şaka yap."),
    BotCommand("slap", "👋Birini tokatlayın."),
    BotCommand("zar", "🎲Rastgele bir zar atın."),
    BotCommand("dart", "🎯Dart atar."),
    BotCommand("slot", "🎰Şans slot'u çevirir."),
    BotCommand("bowling", "🎳Bowling atar."),
    BotCommand("futbol", "⚽Kaleye top atar."),
    BotCommand("basket", "🏀Basket atar."),
    BotCommand("cash", "🪙Rastgele bir para atın."),
    BotCommand("para", "😜Rastgele bir şaka gönderin"),
    BotCommand("tts", "🗣️Bir metni sese çevirir."),
    BotCommand("ping", "📈Bot'un ping değerini gösterir."),
   
]

async def set_commands(client):
    
    await client.set_bot_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
    
    
    await client.set_bot_commands(group_commands, scope=BotCommandScopeAllGroupChats())

class ArchMusic(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Bot Başlatılıyor..")
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

            video_url = "https://telegra.ph/file/36221d40afde82941ffff.mp4"
            caption = "__Bot Başlatılıyor . . . ⚡️__"
            
            try:
                await self.send_video(
                    config.LOG_GROUP_ID,
                    video=video_url,
                    caption=caption,
                )
            except:
                LOGGER(__name__).error(
                    "Bot log grubuna erişemedi. Log kanalınıza botunuzu eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
                )
                sys.exit()

            await set_commands(self)  


            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Lütfen Logger Grubunda Botu Yönetici Olarak Terfi Ettirin"
                )
                sys.exit()

        except Exception as e:
            LOGGER(__name__).error(f"Bot başlatılırken hata oluştu: {e}")
            sys.exit()

        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name

        LOGGER(__name__).info(f"MusicBot {self.name} olarak başlatıldı")

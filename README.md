# 🌟 KRISH X STAR - Telegram Music Bot 🌟

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import config
from player import MusicPlayer
from queue_manager import QueueManager

# 🔥 Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_NAME = "✨ KRISH X STAR ✨"


# 🎵 MAIN BOT CLASS
class KrishXStarBot:
    def __init__(self):
        self.player = MusicPlayer()
        self.queue = QueueManager()

    # ───────── START ─────────
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user

        text = f"""
🌟 <b>WELCOME {user.first_name}</b> 🌟

🎧 <b>KRISH X STAR MUSIC BOT</b>
💫 Ultra Fast Music Experience

━━━━━━━━━━━━━━
🔥 Type /play song_name
🎵 Enjoy unlimited music
👑 Powered by KRISH
━━━━━━━━━━━━━━
"""

        keyboard = [
            [InlineKeyboardButton("🎵 Play Music", callback_data="play")],
            [
                InlineKeyboardButton("📜 Help", callback_data="help"),
                InlineKeyboardButton("👑 Owner", callback_data="owner")
            ],
            [InlineKeyboardButton("⭐ GitHub", url=config.GITHUB_LINK)]
        ]

        await update.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="HTML"
        )

    # ───────── HELP ─────────
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = """
🎵 <b>COMMANDS</b>

/play <name> - Play Song
/pause - Pause
/resume - Resume
/skip - Skip Song
/stop - Stop Music
/queue - Show Queue
"""

        await update.message.reply_text(text, parse_mode="HTML")

    # ───────── PLAY ─────────
    async def play(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = " ".join(context.args)

        if not query:
            await update.message.reply_text("❌ Song name likho: /play song")
            return

        await update.message.reply_text(f"🎵 Searching: {query}")

        result = await self.player.search_and_play(query, update.effective_chat.id)

        if result:
            await update.message.reply_text(f"▶️ Now Playing: {query}")
        else:
            await update.message.reply_text("❌ Song not found")

    # ───────── STOP ─────────
    async def stop(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.player.stop(update.effective_chat.id)
        await update.message.reply_text("⏹️ Stopped")

    # ───────── PAUSE ─────────
    async def pause(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.player.pause(update.effective_chat.id)
        await update.message.reply_text("⏸️ Paused")

    # ───────── RESUME ─────────
    async def resume(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.player.resume(update.effective_chat.id)
        await update.message.reply_text("▶️ Resumed")

    # ───────── SKIP ─────────
    async def skip(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        song = await self.player.skip(update.effective_chat.id)
        if song:
            await

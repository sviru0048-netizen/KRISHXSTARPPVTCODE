from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls.types.input_stream import AudioPiped
from config import *
from bot import app, call_py
from utils.queue import add
import yt_dlp

@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Song name do")

    query = message.text.split(None, 1)[1]

    ydl_opts = {"format": "bestaudio", "quiet": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        url = info["entries"][0]["url"]
        title = info["entries"][0]["title"]

    add(message.chat.id, url, title)

    await call_py.join_group_call(
        message.chat.id,
        AudioPiped(url)
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⏸ Pause", callback_data="pause"),
            InlineKeyboardButton("▶ Resume", callback_data="resume"),
        ],
        [
            InlineKeyboardButton("⏭ Skip", callback_data="skip"),
            InlineKeyboardButton("🛑 Stop", callback_data="stop"),
        ]
    ])

    await message.reply(
        f"🎶 **{title}**\n👑 Powered by {OWNER_NAME}",
        reply_markup=buttons
    )
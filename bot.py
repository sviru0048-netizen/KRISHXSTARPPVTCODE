from pyrogram import Client
from pytgcalls import PyTgCalls
from config import *

app = Client(
    "krishstar",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

call_py = PyTgCalls(app)

# Import plugins
import plugins.player
import plugins.controls
import plugins.autoplay

app.start()
call_py.start()

print(f"🔥 {BOT_NAME} Started | Owner: {OWNER_NAME}")

import asyncio
asyncio.get_event_loop().run_forever()
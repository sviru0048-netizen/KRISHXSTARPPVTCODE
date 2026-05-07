from pytgcalls.types.stream import StreamAudioEnded
from bot import call_py
from utils.queue import pop, get
import yt_dlp

@call_py.on_stream_end()
async def stream_end(_, update: StreamAudioEnded):
    chat_id = update.chat_id

    pop(chat_id)
    queue = get(chat_id)

    if queue:
        next_song = queue[0]["url"]

        from pytgcalls.types.input_stream import AudioPiped
        await call_py.change_stream(chat_id, AudioPiped(next_song))
    else:
        # autoplay
        ydl_opts = {"format": "bestaudio", "quiet": True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("ytsearch:latest songs", download=False)
            url = info["entries"][0]["url"]

        from pytgcalls.types.input_stream import AudioPiped
        await call_py.change_stream(chat_id, AudioPiped(url))
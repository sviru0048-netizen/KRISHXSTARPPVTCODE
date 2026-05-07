from pyrogram.types import CallbackQuery
from bot import app, call_py
from utils.queue import pop, get

@app.on_callback_query()
async def controls(_, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id

    if data == "pause":
        await call_py.pause_stream(chat_id)
        await query.answer("⏸ Paused")

    elif data == "resume":
        await call_py.resume_stream(chat_id)
        await query.answer("▶ Resumed")

    elif data == "stop":
        await call_py.leave_group_call(chat_id)
        await query.answer("🛑 Stopped")

    elif data == "skip":
        pop(chat_id)
        queue = get(chat_id)

        if not queue:
            await call_py.leave_group_call(chat_id)
            return await query.answer("Queue Empty")

        next_song = queue[0]["url"]

        from pytgcalls.types.input_stream import AudioPiped
        await call_py.change_stream(chat_id, AudioPiped(next_song))

        await query.answer("⏭ Skipped")
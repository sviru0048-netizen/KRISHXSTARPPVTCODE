queues = {}

def add(chat_id, song, title):
    if chat_id not in queues:
        queues[chat_id] = []
    queues[chat_id].append({"url": song, "title": title})

def get(chat_id):
    return queues.get(chat_id, [])

def pop(chat_id):
    if chat_id in queues and queues[chat_id]:
        return queues[chat_id].pop(0)

def clear(chat_id):
    queues[chat_id] = []
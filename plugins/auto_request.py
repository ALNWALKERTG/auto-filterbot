import pyrogram
from pyrogram import Client, filters

@Client.on_chat_join_request()
async def request_handler(client: user, update):
    user_id = update.from_user.id
    chat_title = update.chat.title
    chat_id = update.chat.id

    await client.approve_chat_join_request(chat_id=chat_id, user_id=user_id)

    await client.send_message(
        chat_id=user_id,
        text=f"Hello {user_id}! Welcome to {chat_title}"
    )

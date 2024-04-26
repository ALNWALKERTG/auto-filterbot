import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_chat_join_request()
async def request_handler(client, update):
    user_id = update.from_user.id
    user_m = update.from_user.mention
    chat_title = update.chat.title
    chat_id = update.chat.id

    await client.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
    photo_path = "https://telegra.ph/file/4ee563b2e8a1efc87e582.jpg"  
    caption = f"Hello {user_m} ✨️\n\nYour Request to Join {chat_title} has been Approved.\n\nSend /start to know more.\nJoin US 👇👇"
    buttons = [
        [InlineKeyboardButton("requesting group", url="https://t.me/+N-d6LxO8-VozOTc9")],
        [InlineKeyboardButton("latest movies", url="https://t.me/+ASrQmyP1AGIwOTU9")]
    ]
    await client.send_photo(
        chat_id=user_id,
        photo=photo_path,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

from bot_telegram import bot
from aiogram import Dispatcher, types


# @dp.message_handler(content_types=types.ContentType.ANY, state='*')
async def cmd_DeleteMessage(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cmd_DeleteMessage, content_types=types.ContentType.ANY, state='*')

from aiogram.utils import executor
from bot_telegram import dp
from handlers.Client import register_handlers_client

from database.db_client import connect_db


register_handlers_client(dp)

async def on_start_up(_):
    print('The bot is running')
    connect_db()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
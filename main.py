from aiogram.utils import executor
from bot_telegram import dp
from handlers.Client import register_handlers_client

from database.db_test import connect_db
from database.db_client import create_table_User_Information


register_handlers_client(dp)

async def on_start_up(_):
    print('The bot is running')
    connect_db()
    create_table_User_Information()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
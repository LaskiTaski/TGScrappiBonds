from aiogram.utils import executor
from bot_telegram import dp
from handlers.Client import register_handlers_client
from handlers.Client_settings import register_handlers_settings_client
from database import db_create, db_test

register_handlers_client(dp)
register_handlers_settings_client(dp)

async def on_start_up(_):
    print('The bot is running')
    db_test.connect_db()
    db_create.CT_User_Information()
    db_create.CT_User_settings()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
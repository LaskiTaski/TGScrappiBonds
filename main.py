from aiogram.utils import executor
from bot_telegram import dp
from handlers.Client.Client import register_handlers_client
from handlers.Client.Client_settings import register_handlers_client_settings
from handlers.Client.Settings_window import register_handlers_settings_window
from handlers.Client.Client_bonds import register_handlers_client_bonds
from handlers.Payments.Payment import register_handlers_payment
from handlers.other import register_handlers_other

from database import db_UserInformation
from database import db_UserSettings
from database import db_UserTransactions

register_handlers_payment(dp)
register_handlers_client(dp)
register_handlers_client_settings(dp)
register_handlers_settings_window(dp)
register_handlers_client_bonds(dp)
register_handlers_other(dp)

async def on_start_up(_):
    print('The bot is running')
    db_UserInformation.CREATE_UserInformation()
    db_UserSettings.CREATE_UserSettings()
    db_UserTransactions.CREATE_UserTransactions()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
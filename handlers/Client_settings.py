from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_dictionary
from handlers.Client import FSMClient
from database.db_insert_change import IC_User_Setting
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMClient_settings(StatesGroup):
    STSE_ToTheEnd = State()


# @dp.callback_query_handlers(text='STSE_to_the_end', state=(FSMClient.main_menu, FSMClient_settings.STSE_ToTheEnd))
async def cb_setting_to_the_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])

    await FSMClient_settings.STSE_ToTheEnd.set()
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Введите сколько процентов годовых вы хотите получить при погашении?',
                           reply_markup=kb)


# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=(FSMClient_settings.STSE_ToTheEnd))
async def cmd_setting_to_the_end(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    settings_user = (message.from_user.id, message.text, 'repayment')
    IC_User_Setting(settings_user)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id - 1)


def register_handlers_settings_client(dp: Dispatcher):
    dp.register_callback_query_handler(cb_setting_to_the_end, text='STSE_to_the_end',
                                       state=(FSMClient.strategy_to_the_end, FSMClient_settings.STSE_ToTheEnd))

    dp.register_message_handler(cmd_setting_to_the_end, content_types=types.ContentTypes.TEXT,
                                state=FSMClient_settings.STSE_ToTheEnd)


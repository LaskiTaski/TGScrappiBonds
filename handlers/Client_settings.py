from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_dictionary
from database.db_insert_change import IC_User_Setting
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMClient_settings(StatesGroup):
    STSE_Quoting = State()
    STSE_End = State()
    STSE_Nominal = State()
    STSE_Market = State()
    STSE_Frequency = State()
    STSE_Days = State()
    STSE_Qualification = State()


# @dp.callback_query_handlers(text='STSE_Quoting', state='*')
async def cb_setting_quoting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])

    await FSMClient_settings.STSE_Quoting.set()
    await bot.send_message(chat_id=callback.from_user.id,
                           text='По какой минимум цене должна котироваться бумага?',
                           reply_markup=kb)


# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=(FSMClient_settings.STSE_Quoting))
async def cmd_setting_quoting(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    settings_user = (message.from_user.id, message.text, 'quoting')
    IC_User_Setting(settings_user)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id - 1)


# @dp.callback_query_handlers(text='STSE_end', state='*')
async def cb_setting_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])

    await FSMClient_settings.STSE_End.set()
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Какую минимальную доходность к погашению вы хотите получить?',
                           reply_markup=kb)


# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=(FSMClient_settings.STSE_End))
async def cmd_setting_end(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    settings_user = (message.from_user.id, message.text, 'repayment')
    IC_User_Setting(settings_user)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id - 1)


# @dp.callback_query_handlers(text='STSE_nominal', state='*')
async def cb_setting_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])

    await FSMClient_settings.STSE_Nominal.set()
    print('Nominal, State=Nominal')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Какую минимальную доходность купона относительно номинала вы хотите получить?',
                           reply_markup=kb)

# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=(FSMClient_settings.STSE_Nominal))
async def cmd_setting_nominal(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    settings_user = (message.from_user.id, message.text, 'nominal')
    IC_User_Setting(settings_user)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id - 1)

# @dp.callback_query_handlers(text='STSE_market', state='*')
async def cb_setting_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])

    await FSMClient_settings.STSE_Market.set()
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Какую минимальную доходность купона относительно рыночной цены вы хотите получить?',
                           reply_markup=kb)

# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=(FSMClient_settings.STSE_Market))
async def cmd_setting_market(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    settings_user = (message.from_user.id, message.text, 'market')
    IC_User_Setting(settings_user)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id - 1)

def register_handlers_settings_client(dp: Dispatcher):
    dp.register_callback_query_handler(cb_setting_quoting, text='STSE_quoting', state='*')
    dp.register_message_handler(cmd_setting_quoting, content_types=types.ContentTypes.TEXT,
                                state=FSMClient_settings.STSE_Quoting)

    dp.register_callback_query_handler(cb_setting_end, text='STSE_end', state='*')
    dp.register_message_handler(cmd_setting_end, content_types=types.ContentTypes.TEXT,
                                state=FSMClient_settings.STSE_End)

    dp.register_callback_query_handler(cb_setting_nominal, text='STSE_nominal', state='*')
    dp.register_message_handler(cmd_setting_nominal, content_types=types.ContentTypes.TEXT,
                                state=FSMClient_settings.STSE_Nominal)

    dp.register_callback_query_handler(cb_setting_market, text='STSE_market', state='*')
    dp.register_message_handler(cmd_setting_market, content_types=types.ContentTypes.TEXT,
                                state=FSMClient_settings.STSE_Market)


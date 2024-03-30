from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from keyboards.kb_client_settings import keyboard_settings
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
    kb.add(*keyboard_settings["Котировка"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Quoting.set()
    await callback.message.edit_text(
        'Выберите цену облигации, которую вы предпочли бы использовать.[ ](https://clck.ru/39m4xT)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['< 0', '< 25', '< 50', '< 75', '< 90'],
#                     state=(FSMClient_settings.STSE_Quoting,))
async def cmd_setting_quoting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'quoting')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m4xT)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_end', state='*')
async def cb_setting_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К погашению"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_End.set()
    await callback.message.edit_text(
        'Какой размер доходности к погашению вас интересует?[ ](https://clck.ru/39m5tU)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'],
#                     state=(FSMClient_settings.STSE_End,))
async def cmd_setting_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'repayment')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m5tU)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_nominal', state='*')
async def cb_setting_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К номиналу"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Nominal.set()
    await callback.message.edit_text(
        'Какой размер купоной доходности относительно номинала вас интересует?[ ](https://clck.ru/39m6XQ)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'],
#                     state=(FSMClient_settings.STSE_Nominal,))
async def cmd_setting_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'nominal')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m6XQ)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_market', state='*')
async def cb_setting_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К рынку"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Market.set()
    await callback.message.edit_text(
        'Какой размер купоной доходности относительно рыночной цены вас интересует?[ ](https://clck.ru/39mRvK)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'], state=(FSMClient_settings.STSE_Market,))
async def cmd_setting_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'nominal')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39mRvK)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_frequency', state='*')
async def cb_setting_frequency(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Купон"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Frequency.set()
    await callback.message.edit_text(
        'Выберите предпочтительную частоту выплаты купона.[ ](https://clck.ru/39kZiS)',
        reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x in ['< 0', '< 2', '< 4', '< 8', '< 12'],
#                             state=(FSMClient_settings.STSE_Frequency,))
async def cmd_setting_frequency(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'frequency')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39kZiS)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_days', state='*')
async def cb_setting_days(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Погашение ДО"])
    kb.row(*keyboard_settings["Погашение ОТ"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Days.set()
    await callback.message.edit_text(
        'Выберите количество дней до погашения облигации.[ ](https://clck.ru/39m3HL)',
        reply_markup=kb)
    print('OKKK')


# @dp.callback_query_handlers(lambda x: x.data in ['< 7', '< 31', '< 95', '< 180', '< 365', '> 365'],
#                             state=(FSMClient_settings.STSE_Days,))
async def cmd_setting_days(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'days')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m3HL)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='STSE_qualification', state='*')
async def cb_setting_qualification(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Квал"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await FSMClient_settings.STSE_Qualification.set()
    await callback.message.edit_text(
        'У вас есть статус квалифицированного инвестора?[ ](https://clck.ru/39kZgx)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['Да', 'Нет'],
#                     state=(FSMClient_settings.STSE_Qualification,))
async def cmd_setting_qualification(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    settings_user = (callback.from_user.id, callback.data, 'qualification')
    IC_User_Setting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39kZgx)',
        reply_markup=kb)


def register_handlers_settings_client(dp: Dispatcher):
    dp.register_callback_query_handler(cb_setting_quoting, text='STSE_quoting', state='*')
    dp.register_callback_query_handler(cmd_setting_quoting,
                                       lambda x: x.data in ['< 0', '< 25', '< 50', '< 75', '< 90'],
                                       state=(FSMClient_settings.STSE_Quoting,))

    dp.register_callback_query_handler(cb_setting_end, text='STSE_end', state='*')
    dp.register_callback_query_handler(cmd_setting_end,
                                       lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'],
                                       state=(FSMClient_settings.STSE_End,))

    dp.register_callback_query_handler(cb_setting_nominal, text='STSE_nominal', state='*')
    dp.register_callback_query_handler(cmd_setting_nominal,
                                       lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'],
                                       state=(FSMClient_settings.STSE_Nominal,))

    dp.register_callback_query_handler(cb_setting_market, text='STSE_market', state='*')
    dp.register_callback_query_handler(cmd_setting_market,
                                       lambda x: x.data in ['< 5', '< 10', '< 15', '< 20', '< 25'],
                                       state=(FSMClient_settings.STSE_Market,))

    dp.register_callback_query_handler(cb_setting_frequency, text='STSE_frequency', state='*')
    dp.register_callback_query_handler(cmd_setting_frequency,
                                       lambda x: x.data in ['< 0', '< 2', '< 4', '< 8', '< 12'],
                                       state=(FSMClient_settings.STSE_Frequency,))

    dp.register_callback_query_handler(cb_setting_days, text='STSE_days', state='*')
    dp.register_callback_query_handler(cmd_setting_days,
                                       lambda x: x.data in ['< 7', '< 31', '< 95', '< 180', '< 365', '> 365'],
                                       state=(FSMClient_settings.STSE_Days,))

    dp.register_callback_query_handler(cb_setting_qualification, text='STSE_qualification', state='*')
    dp.register_callback_query_handler(cmd_setting_qualification, lambda x: x.data in ['Да', 'Нет'],
                                       state=(FSMClient_settings.STSE_Qualification,))

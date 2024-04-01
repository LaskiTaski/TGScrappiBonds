from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from database.db_insert_change import IC_UserSetting
from handlers.Client.Client_settings import FSMClientSettings


# @dp.message_handler(lambda x: x.data in ['> 25', '> 50', '> 75', '> 90'],
#                     state=(FSMClientSettings.QuotingState,))
async def cmd_SettingQuoting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'quoting')
    IC_UserSetting(settings_user)

    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m4xT)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
#                     state=(FSMClientSettings.EndState,))
async def cmd_SettingEnd(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'repayment')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m5tU)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
#                     state=(FSMClientSettings.NominalState,))
async def cmd_SettingNominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'nominal')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m6XQ)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
#                     state=(FSMClientSettings.MarketState,))
async def cmd_SettingMarket(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'market')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39mRvK)',
        reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x in ['2', '4', '12'],
#                             state=(FSMClientSettings.FrequencyState,))
async def cmd_SettingFrequency(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'frequency')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39kZiS)',
        reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in ['< 7', '< 31', '< 90', '< 182', '< 365', '> 365'],
#                             state=(FSMClientSettings.DaysState,))
async def cmd_SettingDays(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'days')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39m3HL)',
        reply_markup=kb)


# @dp.message_handler(lambda x: x.data in ['Да', 'Нет'],
#                     state=(FSMClientSettings.QualificationState,))
async def cmd_SettingQualification(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    settings_user = (callback.from_user.id, callback.data, 'qualification')
    IC_UserSetting(settings_user)
    await callback.message.edit_text(
        'Вернитесь в меню или проверьте "Мои параметры 📋".[ ](https://clck.ru/39kZgx)',
        reply_markup=kb)


def register_handlers_settings_window(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_SettingQuoting,
                                       lambda x: x.data in ['> 25', '> 50', '> 75', '> 90'],
                                       state=(FSMClientSettings.QuotingState,))

    dp.register_callback_query_handler(cmd_SettingEnd,
                                       lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
                                       state=(FSMClientSettings.EndState,))

    dp.register_callback_query_handler(cmd_SettingNominal,
                                       lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
                                       state=(FSMClientSettings.NominalState,))

    dp.register_callback_query_handler(cmd_SettingMarket,
                                       lambda x: x.data in ['> 5', '> 10', '> 15', '> 20'],
                                       state=(FSMClientSettings.MarketState,))

    dp.register_callback_query_handler(cmd_SettingFrequency,
                                       lambda x: x.data in ['2', '4', '12'],
                                       state=(FSMClientSettings.FrequencyState,))

    dp.register_callback_query_handler(cmd_SettingDays,
                                       lambda x: x.data in ['< 7', '< 31', '< 90', '< 182', '< 365', '> 365'],
                                       state=(FSMClientSettings.DaysState,))

    dp.register_callback_query_handler(cmd_SettingQualification, lambda x: x.data in ['Да', 'Нет'],
                                       state=(FSMClientSettings.QualificationState,))

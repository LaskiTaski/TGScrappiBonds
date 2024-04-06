from aiogram import Dispatcher, types

from keyboards.kb_client import keyboard_menu
from keyboards.kb_client_settings import keyboard_settings

from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMClientSettings(StatesGroup):
    QuotingState = State()
    EndState = State()
    NominalState = State()
    MarketState = State()
    FrequencyState = State()
    DaysState = State()
    QualificationState = State()


# @dp.callback_query_handlers(text='StQuoting', state='*')
async def cb_SettingQuoting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Котировка"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.QuotingState.set()

    await callback.message.edit_text(
        'Выберите цену облигации, которую вы предпочли бы использовать.[ ](https://clck.ru/39m4xT)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StEnd', state='*')
async def cb_SettingEnd(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К погашению"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.EndState.set()

    await callback.message.edit_text(
        'Какой размер доходности к погашению вас интересует?[ ](https://clck.ru/39m5tU)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StNominal', state='*')
async def cb_SettingNominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К номиналу"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.NominalState.set()

    await callback.message.edit_text(
        'Какой размер купоной доходности относительно номинала вас интересует?[ ](https://clck.ru/39m6XQ)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StMarket', state='*')
async def cb_SettingMarket(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["К рынку"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.MarketState.set()

    await callback.message.edit_text(
        'Какой размер купоной доходности относительно рыночной цены вас интересует?[ ](https://clck.ru/39mRvK)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StFrequency', state='*')
async def cb_SettingFrequency(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Купон"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.FrequencyState.set()

    await callback.message.edit_text(
        'Выберите предпочтительную частоту выплаты купона.[ ](https://clck.ru/39kZiS)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StDays', state='*')
async def cb_SettingDays(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*keyboard_settings["Погашение"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.DaysState.set()

    await callback.message.edit_text(
        'Выберите количество дней до погашения облигации.[ ](https://clck.ru/39m3HL)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='StQualification', state='*')
async def cb_SettingQualification(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(*keyboard_settings["Квал"])
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await FSMClientSettings.QualificationState.set()

    await callback.message.edit_text(
        'У вас есть статус квалифицированного инвестора?[ ](https://clck.ru/39kZgx)',
        reply_markup=kb)


def register_handlers_client_settings(dp: Dispatcher):
    dp.register_callback_query_handler(cb_SettingQuoting, text='StQuoting', state='*')

    dp.register_callback_query_handler(cb_SettingEnd, text='StEnd', state='*')
    dp.register_callback_query_handler(cb_SettingNominal, text='StNominal', state='*')
    dp.register_callback_query_handler(cb_SettingMarket, text='StMarket', state='*')

    dp.register_callback_query_handler(cb_SettingFrequency, text='StFrequency', state='*')
    dp.register_callback_query_handler(cb_SettingDays, text='StDays', state='*')
    dp.register_callback_query_handler(cb_SettingQualification, text='StQualification', state='*')

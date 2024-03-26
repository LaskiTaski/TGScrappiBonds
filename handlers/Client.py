from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_dictionary
from database.db_insert_change import IC_User_Information


# @dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_dictionary["Стратегии"])
    kb.row(*keyboard_dictionary["Меню настроек"])
    kb.row(*keyboard_dictionary["Прочее"])

    information_user = (message.from_user.id, message.from_user.first_name, message.from_user.username, 'False')
    IC_User_Information(information_user)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите стратегию для сортировки[ ](https://goo.su/VKUr)',
                           reply_markup=kb)

# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_dictionary["Стратегии"])
    kb.row(*keyboard_dictionary["Меню настроек"])
    kb.row(*keyboard_dictionary["Прочее"])
    await callback.message.edit_text('Выберите стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_end', state='*')
async def cb_to_the_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Доходность к погашению"])
    kb.add(*keyboard_dictionary["Общие параметры"])

    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)

    if True:
        await callback.answer(text='Этот раздел требует настройки⚠️', show_alert=True)
    # Прописать проверку, требует ли раздел настройки?


# @dp.callback_query_handlers(text='Menu_nominal', state='*')
async def cb_the_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Доходность купона к номиналу"])
    kb.add(*keyboard_dictionary["Общие параметры"])

    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)

    if True:
        await callback.answer(text='Этот раздел требует настройки⚠️', show_alert=True)
    # Прописать проверку, требует ли раздел настройки?


# @dp.callback_query_handlers(text='Menu_market', state='*')
async def cb_the_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Доходность купона к рынку"])
    kb.add(*keyboard_dictionary["Общие параметры"])

    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)

    if True:
        await callback.answer(text='Этот раздел требует настройки⚠️', show_alert=True)
    # Прописать проверку, требует ли раздел настройки?


# @dp.callback_query_handlers(text='Setting', state='*')
async def cb_setting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_dictionary["Доходность к погашению"])
    kb.row(*keyboard_dictionary["Доходность купона к номиналу"])
    kb.row(*keyboard_dictionary["Доходность купона к рынку"])
    kb.add(*keyboard_dictionary["Общие параметры"])
    kb.row(*keyboard_dictionary["Вернуться в меню"], *keyboard_dictionary["Мои параметры"])
    await callback.message.edit_text('[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)', reply_markup=kb)
    await callback.answer(text='Этот раздел предназначен для детальной настройки⚠️', show_alert=True)


# @dp.callback_query_handlers(text='Information', state='*')
async def cb_information(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_dictionary["Вернуться в меню"])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_menu, text='Menu', state='*')
    dp.register_callback_query_handler(cb_to_the_end, text='Menu_end', state='*')
    dp.register_callback_query_handler(cb_the_nominal, text='Menu_nominal', state='*')
    dp.register_callback_query_handler(cb_the_market, text='Menu_market', state='*')

    dp.register_callback_query_handler(cb_setting, text='Setting', state='*')
    dp.register_callback_query_handler(cb_information, text='Information', state='*')

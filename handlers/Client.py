from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from database.db_insert_change import IC_User_Information
from database.db_receive import RE_User_settings

# @dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])

    information_user = (message.from_user.id, message.from_user.first_name, message.from_user.username, 'False')
    IC_User_Information(information_user)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите стратегию для сортировки[ ](https://goo.su/VKUr)',
                           reply_markup=kb)

# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    await callback.message.edit_text('Выберите стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_end', state='*')
async def cb_to_the_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность к погашению"])
    kb.add(*keyboard_menu["Общие параметры"])

    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_nominal', state='*')
async def cb_the_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к номиналу"])
    kb.add(*keyboard_menu["Общие параметры"])

    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_market', state='*')
async def cb_the_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к рынку"])
    kb.add(*keyboard_menu["Общие параметры"])

    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Setting', state='*')
async def cb_setting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность к погашению"])
    kb.row(*keyboard_menu["Доходность купона к номиналу"])
    kb.row(*keyboard_menu["Доходность купона к рынку"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])
    await callback.message.edit_text('[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)', reply_markup=kb)
    await callback.answer(text='Этот раздел предназначен для опытных пользователей⚠️', show_alert=True)


# @dp.callback_query_handlers(text='Params', state='*')
async def cb_params(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"])

    information_params = RE_User_settings(callback.from_user.id,)

    information_params = {name_table: value_table if value_table not in ('', None) else '—' for name_table, value_table in information_params.items()}
    await callback.message.edit_text(f'*Котировка облигаций:* \n🔸_{information_params["quoting"]}_\n\n'
                                     f'*Доходность к погашению:* \n🔸_{information_params["repayment"]}_\n\n'
                                     f'*Доходность купона относительно номинала:* \n🔸_{information_params["nominal"]}_\n\n'
                                     f'*Доходность купона относительно рыночной цены:* \n🔸_{information_params["market"]}_\n\n'
                                     f'*Частота купона:* \n🔸_{information_params["frequency"]}_\n\n'
                                     f'*Дней до погашения:* \n🔸_{information_params["days"]}_\n\n'
                                     f'*Если ли у вас статус квал. инвестора:* \n🔸_{information_params["qualification"]}_\n\n',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Information', state='*')
async def cb_information(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Вернуться в меню"])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_menu, text='Menu', state='*')
    dp.register_callback_query_handler(cb_to_the_end, text='Menu_end', state='*')
    dp.register_callback_query_handler(cb_the_nominal, text='Menu_nominal', state='*')
    dp.register_callback_query_handler(cb_the_market, text='Menu_market', state='*')

    dp.register_callback_query_handler(cb_setting, text='Setting', state='*')
    dp.register_callback_query_handler(cb_params, text='Params', state='*')
    dp.register_callback_query_handler(cb_information, text='Information', state='*')

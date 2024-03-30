from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from database.db_insert_change import IC_UserInformation, IC_UserClearSetting
from database.db_receive import RE_UserSettings


previous_button_data = {}
# @dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])

    information_user = (message.from_user.id, message.from_user.first_name, message.from_user.username, 'False')
    IC_UserInformation(information_user)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите стратегию для сортировки[ ](https://goo.su/VKUr)',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])
    await callback.message.edit_text('Выберите стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_end', state='*')
async def cb_to_the_end(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность к погашению"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_nominal', state='*')
async def cb_the_nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к номиналу"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Menu_market', state='*')
async def cb_the_market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к рынку"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

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

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Params', state='*')
async def cb_params(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Очистить"])

    information_params = RE_UserSettings(callback.from_user.id, )
    information_params = {name_table: value_table if value_table not in ('', None) else '—' for name_table, value_table
                          in information_params.items()}

    await callback.message.edit_text(
        f'*Котировка облигаций:* \n🔸 _{"N" if information_params["quoting"] != "—" else ""} '
        f'{information_params["quoting"]}{"%" if information_params["quoting"] != "—" else ""}_\n\n'
        
        f'*Доходность к погашению:* \n🔸_{"N" if information_params["repayment"] != "—" else ""} '
        f'{information_params["repayment"]}{"%" if information_params["repayment"] != "—" else ""}_\n\n'
        
        f'*Доходность купона относительно номинала:* \n🔸_{"N" if information_params["nominal"] != "—" else ""} '
        f'{information_params["nominal"]}{"%" if information_params["nominal"] != "—" else ""}_\n\n'
        
        f'*Доходность купона относительно рыночной цены:* \n🔸_{"N" if information_params["market"] != "—" else ""} '
        f'{information_params["market"]}{"%" if information_params["market"] != "—" else ""}_\n\n'
        
        f'*Частота купона:* \n🔸_{"N" if information_params["frequency"] != "—" else ""} '
        f'{information_params["frequency"]} {"раз в год" if information_params["frequency"] != "—" else ""}_\n\n'
        
        f'*Дней до погашения:* \n🔸_{"N" if information_params["days"] != "—" else ""} {information_params["days"]} '
        f'{"дней" if information_params["days"] != "—" else ""}_\n\n'
        
        f'*Если ли у вас статус квал. инвестора:* \n🔸_{information_params["qualification"]}_\n\n',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Information', state='*')
async def cb_information(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Вернуться в меню"])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Back', state='*')
async def cb_back(callback: types.CallbackQuery):
    back = previous_button_data[callback.from_user.id]
    if back == "Menu_end":
        await cb_to_the_end(callback)
    elif back == "Menu_nominal":
        await cb_the_nominal(callback)
    elif back == "Menu_market":
        await cb_the_market(callback)
    elif back == "Setting":
        await cb_setting(callback)

# @dp.callback_query_handlers(text='Clear', state='*')
async def cb_clear(callback: types.CallbackQuery):
    IC_UserClearSetting(callback.from_user.id, )
    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text='Ваши настройки сброшены!',
                                    show_alert=True)
    await cb_params(callback)


# @dp.message_handler(content_types=types.ContentType.TEXT, state='*')
async def cmd_delete_message(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_menu, text='Menu', state='*')

    dp.register_callback_query_handler(cb_to_the_end, text='Menu_end', state='*')
    dp.register_callback_query_handler(cb_the_nominal, text='Menu_nominal', state='*')
    dp.register_callback_query_handler(cb_the_market, text='Menu_market', state='*')
    dp.register_callback_query_handler(cb_setting, text='Setting', state='*')

    dp.register_callback_query_handler(cb_params, text='Params', state='*')
    dp.register_callback_query_handler(cb_clear, text='Clear', state='*')
    dp.register_callback_query_handler(cb_back, text='Back', state='*')

    dp.register_callback_query_handler(cb_information, text='Information', state='*')
    dp.register_message_handler(cmd_delete_message, content_types=types.ContentType.TEXT, state='*')

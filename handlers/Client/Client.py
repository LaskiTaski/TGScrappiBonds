from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from keyboards.kb_client_settings import keyboard_settings
from database.db_insert_change import IC_UserInformation, IC_UserStartSetting, \
    IC_UserClearSetting, IC_UserResetSetting, IC_UserBonds
from database.db_receive import RE_UserSettings, RE_GetPapers, RE_UserPappers
from database.db_create import CT_UserBonds

previous_paggen_data = {}


# @dp.message_handler(commands=['start'], state='*')
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])

    information_user = (message.from_user.id, message.from_user.first_name, message.from_user.username, 'False')
    IC_UserInformation(information_user)
    IC_UserStartSetting(information_user[0])
    CT_UserBonds(information_user[0])

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите стратегию для сортировки[ ](https://goo.su/VKUr)',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_Menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])
    await callback.message.edit_text('Выберите стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


# @dp.callback_query_handlers(text='MenuSetting', state='*')
async def cb_Setting(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность к погашению"])
    kb.row(*keyboard_menu["Доходность купона к номиналу"])
    kb.row(*keyboard_menu["Доходность купона к рынку"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='CollectPapers', state='*')
async def cb_CollectPapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    previous_paggen_data[callback.from_user.id] = 0
    IC_UserClearSetting(callback.from_user.id, )
    bonds = RE_GetPapers(callback.from_user.id, )
    if bonds is not None and len(bonds) != 0:
        IC_UserBonds(tuple([callback.from_user.id, bonds]))
        await cb_GetPapers(callback)
    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению бумаг с данными параметрами сейчас нет.\n'
                                             'Измените параметры!', show_alert=True)


# @dp.callback_query_handlers(text='GetPapers', state='*')
async def cb_GetPapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    next = types.InlineKeyboardButton('След. ▶️', callback_data='Next')
    pagen = types.InlineKeyboardButton(f'{previous_paggen_data[callback.from_user.id]}', callback_data='None')
    back = types.InlineKeyboardButton('◀️ Пред.', callback_data='Back')
    kb.row(back, pagen, next)
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])
    bond = RE_UserPappers(callback.from_user.id, previous_paggen_data[callback.from_user.id])
    if bond is not None:
        await callback.message.edit_text(f'URL: {bond[0]}\n\n'
                                         f'Название: {bond[1]}\n\n'
                                         f'Котировка: {bond[2]}%\n\n'
                                         f'К погашению: {bond[3]}%\n\n'
                                         f'К рынку: {bond[4]}%\n\n'
                                         f'К номиналу: {bond[5]}%\n\n'
                                         f'Частота купона: {bond[6]} раз в год\n\n'
                                         f'Дата погашения: {bond[7]}\n\n'
                                         f'Дней до погашения: {bond[8]} дней\n\n'
                                         f'ISIN: {bond[9]}\n\n'
                                         f'Код бумаги: {bond[10]}\n\n'
                                         f'Только для квалов? {bond[11]}\n\n'
                                         f'Последнее обновление: \n{bond[12]}\n\n', reply_markup=kb)


# @dp.callback_query_handlers(text='Next', state='*')
async def cb_NextPapers(callback: types.CallbackQuery):
    previous_paggen_data[callback.from_user.id] += 1
    await cb_GetPapers(callback)


# @dp.callback_query_handlers(text='Back', state='*')
async def cb_BackPapers(callback: types.CallbackQuery):
    if previous_paggen_data[callback.from_user.id] != 0:
        previous_paggen_data[callback.from_user.id] -= 1
        await cb_GetPapers(callback)
    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Там ничего нет!', show_alert=True)
        await cb_CollectPapers(callback)


# @dp.callback_query_handlers(text='Params', state='*')
async def cb_Params(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Очистить"], *keyboard_menu["Вернуться в меню"])

    information_params = RE_UserSettings(callback.from_user.id, )

    await callback.message.edit_text(
        f'*Котировка облигаций:* \n🔸_{"N" if information_params["quoting"] != "—" else ""} '
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
async def cb_Information(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Вернуться в меню"])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Reset', state='*')
async def cb_Reset(callback: types.CallbackQuery):
    IC_UserResetSetting(callback.from_user.id, )
    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text='Ваши настройки сброшены!',
                                    show_alert=True)
    await cb_Params(callback)


# @dp.message_handler(content_types=types.ContentType.ANY, state='*')
async def cmd_DeleteMessage(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_Menu, text='Menu', state='*')
    dp.register_callback_query_handler(cb_Setting, text='MenuSetting', state='*')

    dp.register_callback_query_handler(cb_Params, text='Params', state='*')
    dp.register_callback_query_handler(cb_Reset, text='Reset', state='*')

    dp.register_callback_query_handler(cb_Information, text='Information', state='*')

    dp.register_callback_query_handler(cb_CollectPapers, text='CollectPapers', state='*')

    dp.register_callback_query_handler(cb_NextPapers, text='Next', state='*')
    dp.register_callback_query_handler(cb_GetPapers, text='GetPapers', state='*')
    dp.register_callback_query_handler(cb_BackPapers, text='Back', state='*')

    dp.register_message_handler(cmd_DeleteMessage, content_types=types.ContentType.ANY, state='*')

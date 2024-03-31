from time import sleep

from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from database.db_insert_change import IC_UserInformation, IC_UserStartSetting, \
                                      IC_UserClearSetting, IC_UserResetSetting
from database.db_receive import RE_UserSettings, RE_GetPapers


previous_button_data = {}
# @dp.message_handler(commands=['start'], state='*')
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])

    information_user = (message.from_user.id, message.from_user.first_name, message.from_user.username, 'False')
    IC_UserInformation(information_user)
    IC_UserStartSetting(information_user[0])

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите стратегию для сортировки[ ](https://goo.su/VKUr)',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_Menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*keyboard_menu["Стратегии"])
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])
    await callback.message.edit_text('Выберите стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


# @dp.callback_query_handlers(text='MenuEnd', state='*')
async def cb_End(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность к погашению"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='MenuNominal', state='*')
async def cb_Nominal(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к номиналу"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='MenuMarket', state='*')
async def cb_Market(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Доходность купона к рынку"])
    kb.add(*keyboard_menu["Общие параметры"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    if callback.data != 'Back':
        previous_button_data[callback.from_user.id] = callback.data

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='MenuSetting', state='*')
async def cb_Setting(callback: types.CallbackQuery):
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


# @dp.callback_query_handlers(text='GetPapers', state='*')
async def cb_GetPapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Мои параметры"])

    IC_UserClearSetting(callback.from_user.id, )
    bonds = RE_GetPapers(callback.from_user.id, )

    for bond in bonds[:5]:
        await bot.send_message(chat_id=callback.message.chat.id, text=f'Название: {bond[1]}\n\n'
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
                                                                      f'Последнее обновление: \n{bond[12]}\n\n')
        sleep(0.3)

    await callback.message.edit_text(
        '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Params', state='*')
async def cb_Params(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Вернуться в меню"], *keyboard_menu["Очистить"])

    information_params = RE_UserSettings(callback.from_user.id,)

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


# @dp.callback_query_handlers(text='Back', state='*')
async def cb_Back(callback: types.CallbackQuery):
    back = previous_button_data[callback.from_user.id]
    if back == "MenuEnd":
        await cb_End(callback)
    elif back == "MenuNominal":
        await cb_Nominal(callback)
    elif back == "MenuMarket":
        await cb_Market(callback)
    elif back == "MenuSetting":
        await cb_Setting(callback)


# @dp.callback_query_handlers(text='Reset', state='*')
async def cb_Reset(callback: types.CallbackQuery):
    IC_UserResetSetting(callback.from_user.id, )
    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text='Ваши настройки сброшены!',
                                    show_alert=True)
    await cb_Params(callback)


# @dp.message_handler(content_types=types.ContentType.TEXT, state='*')
async def cmd_DeleteMessage(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=['start'], state='*')
    dp.register_message_handler(cmd_DeleteMessage, content_types=types.ContentType.TEXT, state='*')

    dp.register_callback_query_handler(cb_Menu, text='Menu', state='*')

    dp.register_callback_query_handler(cb_End, text='MenuEnd', state='*')
    dp.register_callback_query_handler(cb_Nominal, text='MenuNominal', state='*')
    dp.register_callback_query_handler(cb_Market, text='MenuMarket', state='*')
    dp.register_callback_query_handler(cb_Setting, text='MenuSetting', state='*')

    dp.register_callback_query_handler(cb_Params, text='Params', state='*')
    dp.register_callback_query_handler(cb_Reset, text='Reset', state='*')
    dp.register_callback_query_handler(cb_Back, text='Back', state='*')

    dp.register_callback_query_handler(cb_Information, text='Information', state='*')
    dp.register_callback_query_handler(cb_GetPapers, text='GetPapers', state='*')

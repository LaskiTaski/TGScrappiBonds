from bot_telegram import bot
from aiogram import Dispatcher, types
from keyboards.kb_client import keyboard_menu
from keyboards.kb_client_settings import keyboard_settings

from database.db_create import CT_UserBonds
from database.db_insert_change import IC_UserInformation, IC_UserStartSetting, IC_UserBonds
from database.db_receive import RE_UserSettings, RE_SuitablePapers, RE_GetPaper, RE_GetPages


previous_pagen_data = {}


# @dp.message_handler(commands=['start'], state='*')
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Меню настроек"])
    kb.row(*keyboard_menu["Прочее"])
    kb.row(*keyboard_menu["Бумаги"])

    information_user = {
        "ID": message.from_user.id,
        "Name": message.from_user.first_name,
        "User_name": message.from_user.username,
        "Access": 'False'
    }

    IC_UserInformation(information_user)
    IC_UserStartSetting(information_user["ID"])
    CT_UserBonds(information_user["ID"])

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

    previous_pagen_data[callback.from_user.id] = 1
    bonds = RE_SuitablePapers(callback.from_user.id, )
    if bonds is not None:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Пожалуйста подождите, мы уже ищем подходящие бумаги', show_alert=True)
        IC_UserBonds((callback.from_user.id, bonds))
        await cb_GetPapers(callback)
    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению бумаг с данными параметрами сейчас нет.\n'
                                             'Измените параметры!', show_alert=True)


# @dp.callback_query_handlers(text='GetPapers', state='*')
async def cb_GetPapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    
    kb.row(*keyboard_settings["Страницы"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    bond = RE_GetPaper(callback.from_user.id, previous_pagen_data[callback.from_user.id])
    total_pages = RE_GetPages(callback.from_user.id)
    if bond is not None:
        await callback.message.edit_text(f'URL: {bond["URL"]}\n\n'
                                         f'Название облигации: {bond["Название"]}\n\n'
                                         f'Котировка облигации: {bond["Котировка"]}%\n\n'
                                         f'Доходность к погашению: {bond["К погашению"]}%\n\n'
                                         f'Доходность купона относительно рыночной цены: {bond["К рынку"]}%\n\n'
                                         f'Доходность купона относительно номинальной цены: {bond["К номиналу"]}%\n\n'
                                         f'Частота купона: {bond["Частота"]} раз в год\n\n'
                                         f'Дата погашения облигации: {bond["Дата"]}\n\n'
                                         f'Дней до погашения: {bond["Дней"]} дней\n\n'
                                         f'ISIN: {bond["ISIN"]}\n\n'
                                         f'Код облигации: {bond["Код"]}\n\n'
                                         f'Только для квалов? {bond["Статус"]}\n\n'
                                         f'Последнее обновление: \n{bond["Обновление"]}\n\n'
                                         f'{" "*30}*{previous_pagen_data[callback.from_user.id]} из {total_pages}*',
                                         reply_markup=kb)


# @dp.callback_query_handlers(text='Next', state='*')
async def cb_NextPapers(callback: types.CallbackQuery):
    total_pages = RE_GetPages(callback.from_user.id)
    if previous_pagen_data[callback.from_user.id] < total_pages:
        previous_pagen_data[callback.from_user.id] += 1
        await cb_GetPapers(callback)
    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Это были все бумаги соответствующие вашему запросу!', show_alert=True)
        await cb_GetPapers(callback)

# @dp.callback_query_handlers(text='Back', state='*')
async def cb_BackPapers(callback: types.CallbackQuery):
    if previous_pagen_data[callback.from_user.id] != 1:
        previous_pagen_data[callback.from_user.id] -= 1
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
        f'*Котировка облигаций:* \n🔸_{"N >" if information_params["quoting"] != "—" else ""} '
        f'{information_params["quoting"]}{"%" if information_params["quoting"] != "—" else ""}_\n\n'

        f'*Доходность к погашению:* \n🔸_{"N >" if information_params["repayment"] != "—" else ""} '
        f'{information_params["repayment"]}{"%" if information_params["repayment"] != "—" else ""}_\n\n'

        f'*Доходность купона относительно номинала:* \n🔸_{"N >" if information_params["nominal"] != "—" else ""} '
        f'{information_params["nominal"]}{"%" if information_params["nominal"] != "—" else ""}_\n\n'

        f'*Доходность купона относительно рыночной цены:* \n🔸_{"N >" if information_params["market"] != "—" else ""} '
        f'{information_params["market"]}{"%" if information_params["market"] != "—" else ""}_\n\n'

        f'*Частота купона:* \n🔸_{"N =" if information_params["frequency"] != "—" else ""} '
        f'{information_params["frequency"]} {"раз(а) в год" if information_params["frequency"] != "—" else ""}_\n\n'

        f"""*Дней до погашения:* \n🔸_{f'N {">=" if information_params["days"] == 365 else "<"}' if information_params["days"] != "—" else ""} {information_params["days"]}"""
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
    IC_UserStartSetting(callback.from_user.id, )
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

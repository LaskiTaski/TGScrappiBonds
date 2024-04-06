from bot_telegram import bot
from aiogram import Dispatcher, types

from datetime import datetime

from handlers.Client.Client import cb_Menu

from keyboards.kb_client import keyboard_menu
from keyboards.kb_client_settings import keyboard_settings

from database.db_UserBonds import GET_SuitablePapers, SET_UserBonds, GET_GetPaper, GET_GetPages
from database.db_UserTransactions import CHECK_UserDaysLeft, UPDATE_UserDaysLeft

page_information = {}


# @dp.callback_query_handlers(text='CollectPapers', state='*')
async def cb_PreparePapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    page_information[callback.from_user.id] = 1

    information_user = {
        "ID": callback.from_user.id,
        "Name": callback.from_user.first_name,
        "User_name": callback.from_user.username,
        "Registration": datetime.now().strftime("%d.%m.%Y"),
    }

    UPDATE_UserDaysLeft(information_user)
    DaysLeft = CHECK_UserDaysLeft(information_user)

    if DaysLeft is None:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению вы ещё не оплатили подписку.\n'
                                             'Для получения подходящих бумаг требуется произвести оплату.',
                                        show_alert=True)
        await cb_Menu(callback)
    elif DaysLeft == 0:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению ваша подписка истекла.\n'
                                             'Для получения подходящих бумаг требуется произвести оплату.',
                                        show_alert=True)
    else:
        bonds = GET_SuitablePapers(callback.from_user.id, )
        if bonds is not None:
            await bot.answer_callback_query(callback_query_id=callback.id,
                                            text='Пожалуйста подождите, мы уже ищем подходящие бумаги',
                                            show_alert=True)
            SET_UserBonds((callback.from_user.id, bonds))
            await cb_GetPapers(callback)
        else:
            await bot.answer_callback_query(callback_query_id=callback.id,
                                            text='К сожалению бумаг с данными параметрами сейчас нет.\n'
                                                 'Измените параметры!',
                                            show_alert=True)


# @dp.callback_query_handlers(text='GetPapers', state='*')
async def cb_GetPapers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.row(*keyboard_settings["Страницы"])
    kb.row(*keyboard_menu["Мои параметры"], *keyboard_menu["Вернуться в меню"])

    bond = GET_GetPaper(callback.from_user.id, page_information[callback.from_user.id])
    total_pages = GET_GetPages(callback.from_user.id)

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
                                         f'{" " * 30}*{page_information[callback.from_user.id]} из {total_pages}*',
                                         reply_markup=kb)


# @dp.callback_query_handlers(text='Next', state='*')
async def cb_NextPapers(callback: types.CallbackQuery):
    pages = GET_GetPages(callback.from_user.id)

    if page_information[callback.from_user.id] < pages:
        page_information[callback.from_user.id] += 1
        await cb_GetPapers(callback)

    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Это все бумаги соответствующие вашему запросу!',
                                        show_alert=True)
        await cb_GetPapers(callback)


# @dp.callback_query_handlers(text='Back', state='*')
async def cb_BackPapers(callback: types.CallbackQuery):
    if page_information[callback.from_user.id] != 1:
        page_information[callback.from_user.id] -= 1
        await cb_GetPapers(callback)
    else:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='Там ничего нет!', show_alert=True)
        await cb_PreparePapers(callback)


def register_handlers_client_bonds(dp: Dispatcher):
    dp.register_callback_query_handler(cb_PreparePapers, text='CollectPapers', state='*')

    dp.register_callback_query_handler(cb_NextPapers, text='Next', state='*')
    dp.register_callback_query_handler(cb_GetPapers, text='GetPapers', state='*')
    dp.register_callback_query_handler(cb_BackPapers, text='Back', state='*')

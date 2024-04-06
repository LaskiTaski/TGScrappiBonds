from bot_telegram import bot
from aiogram import Dispatcher, types

from datetime import datetime

from keyboards.kb_client import keyboard_menu

from database.db_UserInformation import SET_UserInformation
from database.db_UserSettings import SET_UserStartSettings, GET_UserSettings
from database.db_UserTransactions import CHECK_UserDaysLeft, UPDATE_UserDaysLeft


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
        "Registration": datetime.now().strftime("%d.%m.%Y"),
        "Access": 'False'
    }

    SET_UserInformation(information_user)
    SET_UserStartSettings(information_user["ID"])

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

    information_user = {
        "ID": callback.from_user.id,
        "Name": callback.from_user.first_name,
        "User_name": callback.from_user.username,
        "Registration": datetime.now().strftime("%d.%m.%Y"),
        "Access": 'False'
    }

    UPDATE_UserDaysLeft(information_user)
    DaysLeft = CHECK_UserDaysLeft(information_user)

    if DaysLeft is None:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению вы ещё не оплатили подписку.\n'
                                             'Перед тем как приступить к настройкам, необходимо внести оплату.',
                                        show_alert=True)
        await cb_Menu(callback)

    elif DaysLeft == 0:
        await bot.answer_callback_query(callback_query_id=callback.id,
                                        text='К сожалению ваша подписка истекла.\n'
                                             'Перед тем как приступить к настройкам, необходимо внести оплату.',
                                        show_alert=True)
    else:
        await callback.message.edit_text(
            '[Ознакомиться с параметрами для сортировки бумаг](https://telegra.ph/Kak-nastroit-parametry-03-19)',
            reply_markup=kb)


# @dp.callback_query_handlers(text='Params', state='*')
async def cb_Params(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(*keyboard_menu["Назад"])
    kb.row(*keyboard_menu["Очистить"], *keyboard_menu["Вернуться в меню"])

    settings = GET_UserSettings(callback.from_user.id, )

    await callback.message.edit_text(
        f'*Котировка облигаций:* \n🔸_{"N >" if settings["quoting"] != "—" else ""} '
        f'{settings["quoting"]}{"%" if settings["quoting"] != "—" else ""}_\n\n'

        f'*Доходность к погашению:* \n🔸_{"N >" if settings["repayment"] != "—" else ""} '
        f'{settings["repayment"]}{"%" if settings["repayment"] != "—" else ""}_\n\n'

        f'*Доходность купона относительно номинала:* \n🔸_{"N >" if settings["nominal"] != "—" else ""} '
        f'{settings["nominal"]}{"%" if settings["nominal"] != "—" else ""}_\n\n'

        f'*Доходность купона относительно рыночной цены:* \n🔸_{"N >" if settings["market"] != "—" else ""} '
        f'{settings["market"]}{"%" if settings["market"] != "—" else ""}_\n\n'

        f'*Частота купона:* \n🔸_{"N =" if settings["frequency"] != "—" else ""} '
        f'{settings["frequency"]} {"раз(а) в год" if settings["frequency"] != "—" else ""}_\n\n'

        f"""*Дней до погашения:* \n🔸_{f'N {">=" if settings["days"] == 365 else "<"}' if settings["days"] != "—" else ""} {settings["days"]}"""
        f'{"дней" if settings["days"] != "—" else ""}_\n\n'

        f'*Если ли у вас статус квал. инвестора:* \n🔸_{settings["qualification"]}_\n\n',
        reply_markup=kb)


# @dp.callback_query_handlers(text='Information', state='*')
async def cb_Information(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Вернуться в меню"])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Reset', state='*')
async def cb_ResetSettings(callback: types.CallbackQuery):
    SET_UserStartSettings(callback.from_user.id, )
    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text='Ваши настройки сброшены!',
                                    show_alert=True)
    await cb_Params(callback)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_Menu, text='Menu', state='*')
    dp.register_callback_query_handler(cb_Setting, text='MenuSetting', state='*')

    dp.register_callback_query_handler(cb_Params, text='Params', state='*')
    dp.register_callback_query_handler(cb_ResetSettings, text='Reset', state='*')

    dp.register_callback_query_handler(cb_Information, text='Information', state='*')

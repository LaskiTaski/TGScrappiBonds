from aiogram import Dispatcher, types
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentTypes

from datetime import datetime, timedelta

from bot_telegram import bot, YOOKASSA_PROVIDER_TOKEN

from keyboards.kb_client import keyboard_menu

from database.db_UserBonds import CREATE_UserBonds
from database.db_UserTransactions import SET_UserInformTransactions
from database.db_UserInformation import GET_UserDateRegistration


# @dp.callback_query_handlers(text='Payment', state='*')
async def cb_Payment(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(*keyboard_menu["Вернуться в меню"])

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Advisor',
        description='Этот бот поможет вам быстрее находить бумаги, отвечающие вашим требованиям.',
        payload='Payload',
        provider_token=YOOKASSA_PROVIDER_TOKEN,
        currency='rub',
        prices=[LabeledPrice(label='Подписка на 1 месяц', amount=250_00)],
        photo_url='https://clck.ru/39tbmi',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        reply_markup=None
    )



async def PreCheckoutQuery(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def SuccessfulPayment(message: Message):
    information_user = {
        "ID": message.from_user.id,
        "Name": message.from_user.first_name,
        "User_name": message.from_user.username,
        "Registration": datetime.now().strftime("%d.%m.%Y"),
        "Access": 'True'
    }

    DatePayment = datetime.now()
    EndSubscription = DatePayment + timedelta(days=30)
    DaysLeft = int((EndSubscription - DatePayment).days)

    information_transactions = {
        "ID": message.from_user.id,
        "DateRegistration": GET_UserDateRegistration(information_user)[0],
        "DatePayment": DatePayment.strftime("%d.%m.%Y"),
        "EndSubscription": EndSubscription.strftime("%d.%m.%Y"),
        "DaysLeft": DaysLeft
    }
    CREATE_UserBonds(information_user["ID"])
    SET_UserInformTransactions(information_transactions)

    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)


def register_handlers_payment(dp: Dispatcher):
    dp.register_callback_query_handler(cb_Payment, text='Payment', state='*')

    dp.register_pre_checkout_query_handler(PreCheckoutQuery)
    dp.register_message_handler(SuccessfulPayment, content_types=ContentTypes.SUCCESSFUL_PAYMENT)

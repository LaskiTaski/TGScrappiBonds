from aiogram import types

Yookassa = types.InlineKeyboardButton('Юкасса', callback_data='Yookassa')
Sberbank = types.InlineKeyboardButton('Сбербанк', callback_data='Sberbank')

keyboard_payments = {

    'Способы оплаты': [Yookassa, Sberbank]
}
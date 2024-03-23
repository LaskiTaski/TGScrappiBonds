from aiogram import types

to_the_end = types.InlineKeyboardButton('Доходность к погашению 📈📅', callback_data='To_the_end')
the_nominal = types.InlineKeyboardButton('Купон относительно номинала 🎫📊', callback_data='The_nominal')
the_market = types.InlineKeyboardButton('Купон относительно рынка 🎫🛒', callback_data='The_market')

parameters = types.InlineKeyboardButton('Мои параметры 📋', callback_data='My_Params')

setting = types.InlineKeyboardButton('Свои настройки ⚙️', callback_data='Setting')


stse_to_the_end = types.InlineKeyboardButton("🔸Доходность к погашению🔸", callback_data='stse_to_the_end')
stse_the_nominal = types.InlineKeyboardButton('🔸Доходность купона к номиналу🔸', callback_data='stse_the_nominal')
stse_the_market = types.InlineKeyboardButton('🔸Доходность купона к рынку🔸', callback_data='stse_the_market')

stse_quote_bonds = types.InlineKeyboardButton('Котировка облигаций', callback_data='quote_bonds')
stse_frequency_coupons = types.InlineKeyboardButton('Частота купона', callback_data='stse_frequency_coupons')
stse_days_to_maturity = types.InlineKeyboardButton('Дней до погашения', callback_data='stse_days_to_maturity')
stse_your_qualification = types.InlineKeyboardButton('У вас есть статус квал?', callback_data='stse_your_qualification')


information = types.InlineKeyboardButton('О нас ℹ️', callback_data='Information')
payment = types.InlineKeyboardButton('Оплатить 💳', callback_data='Payment')

go_back_menu = types.InlineKeyboardButton('Главное меню ↩️', callback_data='Menu')


keyboard_dictionary = {
    "Стратегии": [to_the_end, the_nominal, the_market],
    "Меню настроек": [setting],
    "Доходность к погашению": [stse_to_the_end],
    "Доходность купона к номиналу": [stse_the_nominal],
    "Доходность купона к рынку": [stse_the_market],
    "Мои параметры": [parameters],
    "Общие параметры": [
        stse_quote_bonds, stse_frequency_coupons,
        stse_days_to_maturity, stse_your_qualification
        ],
    "Прочее": [information, payment],
    "Вернуться в меню": [go_back_menu]

}

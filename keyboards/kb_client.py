from aiogram import types

to_the_end = types.InlineKeyboardButton('Доходность к погашению 📈📅', callback_data='Menu_end')
the_nominal = types.InlineKeyboardButton('Купон относительно номинала 🎫📊', callback_data='Menu_nominal')
the_market = types.InlineKeyboardButton('Купон относительно рынка 🎫🛒', callback_data='Menu_market')

parameters = types.InlineKeyboardButton('Мои параметры 📋', callback_data='Params')

setting = types.InlineKeyboardButton('Свои настройки ⚙️', callback_data='Setting')


stse_quoting = types.InlineKeyboardButton('Котировка облигаций', callback_data='STSE_quoting')
stse_end = types.InlineKeyboardButton("🔸Доходность к погашению🔸", callback_data='STSE_end')
stse_nominal = types.InlineKeyboardButton('🔸Доходность купона к номиналу🔸', callback_data='STSE_nominal')
stse_market = types.InlineKeyboardButton('🔸Доходность купона к рынку🔸', callback_data='STSE_market')
stse_frequency = types.InlineKeyboardButton('Частота купона', callback_data='STSE_frequency')
stse_days = types.InlineKeyboardButton('Дней до погашения', callback_data='STSE_days')
stse_qualification = types.InlineKeyboardButton('У вас есть статус квал?', callback_data='STSE_qualification')


information = types.InlineKeyboardButton('О нас ℹ️', callback_data='Information')
payment = types.InlineKeyboardButton('Оплатить 💳', callback_data='Payment')

go_back_menu = types.InlineKeyboardButton('Главное меню ↩️', callback_data='Menu')


keyboard_dictionary = {
    "Стратегии": [to_the_end, the_nominal, the_market],
    "Меню настроек": [setting],
    "Доходность к погашению": [stse_end],
    "Доходность купона к номиналу": [stse_nominal],
    "Доходность купона к рынку": [stse_market],
    "Мои параметры": [parameters],
    "Общие параметры": [
        stse_quoting, stse_frequency,
        stse_days, stse_qualification
        ],
    "Прочее": [information, payment],
    "Вернуться в меню": [go_back_menu]

}

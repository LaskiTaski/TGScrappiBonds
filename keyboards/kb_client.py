from aiogram import types

to_the_end = types.InlineKeyboardButton('Доходность к погашению 📈📅', callback_data='MenuEnd')
the_nominal = types.InlineKeyboardButton('Купон относительно номинала 🎫📊', callback_data='MenuNominal')
the_market = types.InlineKeyboardButton('Купон относительно рынка 🎫🛒', callback_data='MenuMarket')
setting = types.InlineKeyboardButton('Детальные настройки ⚙️', callback_data='MenuSetting')

parameters = types.InlineKeyboardButton('Мои параметры 📋', callback_data='Params')


stse_quoting = types.InlineKeyboardButton(f'Котировка \nоблигаций', callback_data='StQuoting')
stse_end = types.InlineKeyboardButton("🔸Доходность к погашению бумаги🔸", callback_data='StEnd')
stse_nominal = types.InlineKeyboardButton('🔸Доходность купона к номиналу🔸', callback_data='StNominal')
stse_market = types.InlineKeyboardButton('🔸Доходность купона к рынку🔸', callback_data='StMarket')
stse_frequency = types.InlineKeyboardButton('Частота \nкупона', callback_data='StFrequency')
stse_days = types.InlineKeyboardButton('Дней до \nпогашения', callback_data='StDays')
stse_qualification = types.InlineKeyboardButton('У вас есть статус квал?', callback_data='StQualification')


information = types.InlineKeyboardButton('О нас ℹ️', callback_data='Information')
get_papers = types.InlineKeyboardButton('Получить бумаги 🗃️', callback_data='GetPapers')
payment = types.InlineKeyboardButton('Оплатить 💳', callback_data='Payment')

back = types.InlineKeyboardButton('Назад 🔙', callback_data='Back')
menu = types.InlineKeyboardButton('Главное меню ↩️', callback_data='Menu')
reset = types.InlineKeyboardButton('Сбросить настройки ♻️', callback_data='Reset')


keyboard_menu = {
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
    "Назад": [back],
    "Очистить": [reset],
    "Прочее": [information, payment],
    "Бумаги": [get_papers],
    "Вернуться в меню": [menu]

}

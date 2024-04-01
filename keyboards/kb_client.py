from aiogram import types


setting = types.InlineKeyboardButton('Настройки \nсортировки облигаций ⚙️', callback_data='MenuSetting')
parameters = types.InlineKeyboardButton('Мои параметры 📋', callback_data='Params')

stse_quoting = types.InlineKeyboardButton(f'Котировка \nоблигаций', callback_data='StQuoting')
stse_end = types.InlineKeyboardButton("🔸Доходность к погашению бумаги🔸", callback_data='StEnd')
stse_nominal = types.InlineKeyboardButton('Доходность купона\n🔸относительно номинала🔸', callback_data='StNominal')
stse_market = types.InlineKeyboardButton('Доходность купона\n🔸к рыночной цене🔸', callback_data='StMarket')
stse_frequency = types.InlineKeyboardButton('Частота \nкупона', callback_data='StFrequency')
stse_days = types.InlineKeyboardButton('Дней до \nпогашения', callback_data='StDays')
stse_qualification = types.InlineKeyboardButton('У вас есть статус квал?', callback_data='StQualification')
reset = types.InlineKeyboardButton('Сбросить настройки ♻️', callback_data='Reset')

information = types.InlineKeyboardButton('О нас ℹ️', callback_data='Information')
payment = types.InlineKeyboardButton('Оплатить 💳', callback_data='Payment')

collect_papers = types.InlineKeyboardButton('Получить бумаги 🗃️', callback_data='CollectPapers')

menu = types.InlineKeyboardButton('Главное меню ↩️', callback_data='Menu')
back = types.InlineKeyboardButton('Назад 🔙', callback_data='MenuSetting')



keyboard_menu = {
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
    "Бумаги": [collect_papers],
    "Вернуться в меню": [menu]

}

from aiogram import types

# Сбросить настройки 🔁

frequency_zero = types.InlineKeyboardButton('Больше 0', callback_data='< 0')
frequency_two = types.InlineKeyboardButton('Больше 2', callback_data='< 2')
frequency_four = types.InlineKeyboardButton('Больше 4', callback_data='< 4')
frequency_eight = types.InlineKeyboardButton('Больше 8', callback_data='< 8')
frequency_twelve = types.InlineKeyboardButton('Больше 12', callback_data='< 12')

days_week = types.InlineKeyboardButton('До недели', callback_data='< 7')
days_month = types.InlineKeyboardButton('До Месяца', callback_data='< 31')
days_quarter = types.InlineKeyboardButton('До квартала', callback_data='< 95')
days_term = types.InlineKeyboardButton('До полугода', callback_data='< 180')
days_year = types.InlineKeyboardButton('До года', callback_data='< 365')
days_more_years = types.InlineKeyboardButton('Год и более', callback_data='> 365')

yes = types.InlineKeyboardButton('Да ✅', callback_data='Да')
no = types.InlineKeyboardButton('Нет ❌', callback_data='Нет')

keyboard_settings = {
    "Купон": [frequency_zero, frequency_two, frequency_four, frequency_eight, frequency_twelve],
    "Погашение ДО": [days_week, days_month, days_quarter, days_term, days_year],
    "Погашение ОТ": [days_more_years],
    "Квал": [yes, no]
}

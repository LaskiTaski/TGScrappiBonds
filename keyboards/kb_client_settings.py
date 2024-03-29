from aiogram import types

# 0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔁
frequency_zero = types.InlineKeyboardButton('Больше 0', callback_data='< 0')
frequency_two = types.InlineKeyboardButton('Больше 2', callback_data='< 2')
frequency_four = types.InlineKeyboardButton('Больше 4', callback_data='< 4')
frequency_eight = types.InlineKeyboardButton('Больше 8', callback_data='< 8')
frequency_twelve = types.InlineKeyboardButton('Больше 12', callback_data='< 12')

days_week = types.InlineKeyboardButton('< 7', callback_data='0')
days_month = types.InlineKeyboardButton('< 30', callback_data='2')
days_trimester = types.InlineKeyboardButton('< 90', callback_data='4')
days_term = types.InlineKeyboardButton('< 180', callback_data='8')
days_year = types.InlineKeyboardButton('< 365', callback_data='12')
days_more_years = types.InlineKeyboardButton('> 365', callback_data='12')

yes = types.InlineKeyboardButton('Да ✅', callback_data='Да')
no = types.InlineKeyboardButton('Нет ❌', callback_data='Нет')

keyboard_settings = {
    "Купон": [frequency_zero, frequency_two, frequency_four, frequency_eight, frequency_twelve],
    "Погашение": [days_week, days_month, days_trimester, days_term, days_year, days_more_years],
    "Квал": [yes, no]
}

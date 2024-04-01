from aiogram import types

quoting_twentyfive = types.InlineKeyboardButton('Больше 25', callback_data='> 25')
quoting_fifty = types.InlineKeyboardButton('Больше 50', callback_data='> 50')
quoting_seventyfive = types.InlineKeyboardButton('Больше 75', callback_data='> 75')
quoting_ninety = types.InlineKeyboardButton('Больше 90', callback_data='> 90')

end_five = types.InlineKeyboardButton('Больше 5', callback_data='> 5')
end_ten = types.InlineKeyboardButton('Больше 10', callback_data='> 10')
end_fifteen = types.InlineKeyboardButton('Больше 15', callback_data='> 15')
end_twenty = types.InlineKeyboardButton('Больше 20', callback_data='> 20')

nominal_five = types.InlineKeyboardButton('Больше 5', callback_data='> 5')
nominal_ten = types.InlineKeyboardButton('Больше 10', callback_data='> 10')
nominal_fifteen = types.InlineKeyboardButton('Больше 15', callback_data='> 15')
nominal_twenty = types.InlineKeyboardButton('Больше 20', callback_data='> 20')

market_five = types.InlineKeyboardButton('Больше 5', callback_data='> 5')
market_ten = types.InlineKeyboardButton('Больше 10', callback_data='> 10')
market_fifteen = types.InlineKeyboardButton('Больше 15', callback_data='> 15')
market_twenty = types.InlineKeyboardButton('Больше 20', callback_data='> 20')

frequency_two = types.InlineKeyboardButton('2', callback_data='2')
frequency_four = types.InlineKeyboardButton('4', callback_data='4')
frequency_twelve = types.InlineKeyboardButton('12', callback_data='12')

days_week = types.InlineKeyboardButton('До недели', callback_data='< 7')
days_month = types.InlineKeyboardButton('До месяца', callback_data='< 31')
days_quarter = types.InlineKeyboardButton('До квартала', callback_data='< 90')
days_term = types.InlineKeyboardButton('До полугода', callback_data='< 182')
days_year = types.InlineKeyboardButton('До года', callback_data='< 365')
days_more_years = types.InlineKeyboardButton('Год и более', callback_data='> 365')

yes = types.InlineKeyboardButton('Да ✅', callback_data='Да')
no = types.InlineKeyboardButton('Нет ❌', callback_data='Нет')


next = types.InlineKeyboardButton('След. ▶️', callback_data='Next')
back = types.InlineKeyboardButton('◀️ Пред.', callback_data='Back')

keyboard_settings = {
    "Котировка": [quoting_twentyfive, quoting_fifty, quoting_seventyfive, quoting_ninety],
    "К погашению": [end_five, end_ten, end_fifteen, end_twenty],
    "К номиналу": [nominal_five, nominal_ten, nominal_fifteen, nominal_twenty],
    "К рынку": [market_five, market_ten, market_fifteen, market_twenty],
    "Купон": [frequency_two, frequency_four, frequency_twelve],
    "Погашение ДО": [days_week, days_month, days_quarter, days_term, days_year],
    "Погашение ОТ": [days_more_years],
    "Квал": [yes, no],
    "Страницы": [back, next]
}

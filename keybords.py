from aiogram import types

# Определение кнопок
buttons1 = types.KeyboardButton(text='/start')
buttons2 = types.KeyboardButton(text='/stop')
buttons3 = types.KeyboardButton(text='число')
buttons4 = types.KeyboardButton(text='лису')

# Создание клавиатуры
keyboard1 = [
    [buttons1, buttons2, buttons3, buttons4]
]

# Инициализация клавиатуры с использованием types.ReplyKeyboardMarkup
keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
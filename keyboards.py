from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Tashkent'),
            KeyboardButton('Samarkand'),
            KeyboardButton('Andijan'),
        ], 
        [
            KeyboardButton('Urgench'),
            KeyboardButton('Navoi'),
            KeyboardButton('Bukhara'),
        ],
        [
            KeyboardButton('Termez'),
            KeyboardButton('Qarshi'),
            KeyboardButton('Gulistan'),
        ],
        [
            KeyboardButton('Jizzakh'),
            KeyboardButton('Fergana'),
            KeyboardButton('Namangan'),
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Suralar"),
            KeyboardButton("Namoz vaqti")
        ]
    ],
    resize_keyboard=True
)
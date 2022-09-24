from ctypes import resize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuLanguage = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🇺🇿 Tilni tanlang"),
            KeyboardButton(text="🇺🇿 Тилни танланг"),
            KeyboardButton(text="🇷🇺 Выберите язык"),
        ],
    ],
    resize_keyboard = True
)


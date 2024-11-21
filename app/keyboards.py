from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True),
     KeyboardButton(text='Отправить контакт', request_contact=True)]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com/@sudoteach')],
    [InlineKeyboardButton(text='Telegram', url='https://t.me/sudoteach')]
])
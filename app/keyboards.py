from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True),
     KeyboardButton(text='Отправить контакт', request_contact=True)]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])


async def brands():
    all_data = ("Nike", "Adidas", "Reebok")

    keyboard = ReplyKeyboardBuilder()
    for brand in all_data:
        keyboard.add(KeyboardButton(text=brand))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)    
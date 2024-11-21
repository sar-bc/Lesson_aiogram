from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject
from aiogram.enums import ChatAction
import asyncio
import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет!', reply_markup=kb.inline_main)


@router.message(F.text == 'Корзина')
async def cmd_basket(message: Message):
    await message.answer("Ваша корзина пуста")    


@router.callback_query(F.data =='catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer("Вы открыли каталог", show_alert=True)
    await callback.message.answer("Каталог")


@router.callback_query(F.data =='contacts')
async def cmd_contacts(callback: CallbackQuery):
    await callback.answer("Вы открыли контаты")
    await callback.message.answer("Контакты")    
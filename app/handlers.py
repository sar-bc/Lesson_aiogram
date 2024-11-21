from aiogram import Router, F
from aiogram.types import Message
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

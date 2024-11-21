from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject
from aiogram.enums import ChatAction
import asyncio
import app.keyboards as kb
from app.state import *

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state : FSMContext):
    await state.set_state(Reg.name)
    await message.answer(f'Привет! Введи свое имя')


@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Отправьте свой номер")


@router.message(Reg.number)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.photo)
    await message.answer("Отправьте фото")

@router.message(Reg.photo)
async def reg_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file._id)
    data = await state.get_data()
    await message.answer_photo(photo=date['photo'], caption=f"Информация о Вас: {data['name']}, {data['number']}")
    await state.clear()    


@router.message(F.text == 'Корзина')
async def cmd_basket(message: Message):
    await message.answer("Ваша корзина пуста")    


@router.callback_query(F.data =='catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer("Вы открыли каталог", show_alert=True)
    await callback.message.answer("Каталог", reply_markup=await kb.brands())


@router.callback_query(F.data =='contacts')
async def cmd_contacts(callback: CallbackQuery):
    await callback.answer("Вы открыли контаты")
    await callback.message.answer("Контакты")    
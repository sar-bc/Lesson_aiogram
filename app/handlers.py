from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject
from aiogram.enums import ChatAction
import asyncio

router = Router()

@router.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
async def cmd_start(message: Message, command: CommandObject):
    await message.answer(f'Привет! Ты пришел от {command.args}')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')

@router.message(F.text == '123')
async def echo(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
    action=ChatAction.TYPING)
    await asyncio.sleep(4)
    await message.answer("hello")    
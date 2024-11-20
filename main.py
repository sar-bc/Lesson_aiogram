import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import logging

load_dotenv()



bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет")

@dp.message()
async def echo(message: Message):
    await message.answer("Неизвестная команда")

async def main():
    await dp.start_polling(bot)



if __name__== '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')


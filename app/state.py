from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Reg(StatesGroup):
    name = State()
    number = State()
    photo = State()
    
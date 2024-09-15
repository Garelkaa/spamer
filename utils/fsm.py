from aiogram.fsm.state import State, StatesGroup


class StartBomber(StatesGroup):
    number = State()
    time = State()
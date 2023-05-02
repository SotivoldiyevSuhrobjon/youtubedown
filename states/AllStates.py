from aiogram.dispatcher.filters.state import StatesGroup, State


class MyStates(StatesGroup):
    url = State()

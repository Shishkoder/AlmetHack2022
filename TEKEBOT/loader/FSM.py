from aiogram.dispatcher.filters.state import StatesGroup, State

class MyText(StatesGroup):
    """
    FSM class for accepting a message from the user

    Args:
        StatesGroup (_type_): _description_
    """
    text = State()
    accept_text = State()
from Config import getToken
from loader import storage
from aiogram import Bot, Dispatcher, executor


bot = Bot(getToken())
dispather = Dispatcher(bot, storage=storage)


if __name__ == "__main__":
    from Handler.handler import dispather, get_default_commands
    from Channel.chanel import dispather
    executor.start_polling(dispather, on_startup=get_default_commands)

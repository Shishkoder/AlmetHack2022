from Config import getAdminIdList
from main import bot, dispather
from aiogram import types
from aiogram.dispatcher.filters import Command


async def get_default_commands(dispather):
    """
    Function that executes instructions when starting or restarting the bot
    1. Sending a message to administrators that the bot is running
    2. Displaying a side menu in a bot

    Args:
        dispather (_type_): ORM class, for the work of the aiogram library
    """
    for admin_id in getAdminIdList():
        try:
            await bot.send_message(chat_id=admin_id, text="Бот запущен")
        except Exception as error:
            pass


@dispather.message_handler(Command('start'))
async def command_start(message: types.Message):
    await message.answer("Бот, который вам продеманстрирует MVP технологии QR2S")

# --------------------------------------- Mytext Branch -----------------------------------------


@dispather.message_handler(Command('MyText'))
async def command_(message: types.Message):
    pass

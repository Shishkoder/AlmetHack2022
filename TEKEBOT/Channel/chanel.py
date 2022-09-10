from main import bot, dispather
from aiogram import types
from Config import get_service_channel_chat_id


@dispather.channel_post_handler()
async def get_post_servise_chanel(message: types.Message):
    print(message.text)
    print(message.chat.id)

import logging
from bing_image_urls import bing_image_urls
from aiogram import Bot, Dispatcher, executor, types

import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply(f"Привет,{message.from_user.first_name} я бот для важных переговоров! ")


@dp.message_handler()
async def get_user_message(message):
    url =  bing_image_urls(f'{message.text}', limit=1)
    await bot.send_photo(chat_id=message.chat.id , photo=" ".join(map(str,url)))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
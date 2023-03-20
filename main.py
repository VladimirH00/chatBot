import pyautogui
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from src.classes.Config import Config
from src.classes.WindowsOS import WindowsOS
from aiogram.utils import executor
from src.extensions.keyboards.KeyboardWrapper import KeyboardWrapper
import os
import sys

sys.path.append(os.getcwd())

bot = Bot(token='6078090631:AAHbvc6d9T3W0LJGXjRK2ok5zgUdZw76_E0')
dp = Dispatcher(bot)

greet_kb = KeyboardWrapper()
greet_kb.add_button(text="/🖥ВЫКЛЮЧИТЬ🖥").add_button("/♻️Перезагрузить♻️")
second_keyboard = KeyboardWrapper()
second_keyboard.add_button('123').add_button('345')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ZNERF Давай это сделаем ZNERF ", reply_markup=greet_kb.keyboard)


if __name__ == '__main__':

    config_file = open('config/env')
    config = Config(file=config_file)
    config_file.close()
    windows_os = WindowsOS(dp=dp, bot=bot, config=config)
    dp.message_handlers('/', windows_os.screen())
    # executor.start_polling(dp, skip_updates=True)

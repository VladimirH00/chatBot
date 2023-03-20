import os

import pyautogui
from aiogram import types

from src.classes import Config
from src.interfaces.OSInterface import OSInterface


class WindowsOS(OSInterface):

    def __init__(self, dp, bot, config: Config):
        self.__dp = dp
        self.__bot = bot
        self.__application_config = config

    async def shutdown(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, "Выключаю...")
        os.system('shutdown -s -t 0')

    async def screenshot(self, message: types.Message):
        self.screen()
        file = open('screenshot.png', 'rb')
        await self.__bot.send_photo(message.chat.id, file, 'Вот скрин вашего экрана')

    async def reboot(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, 'Перезапускаю...')
        os.system('shutdown -r -t 0')

    def screen(self):
        screenshot = pyautogui.screenshot()
        path = self.__application_config.get_param('root_dir') \
               + '\\' + self.__application_config.get_param('media_path') + '\screenshot\screenshot.png'
        screenshot.save(path)

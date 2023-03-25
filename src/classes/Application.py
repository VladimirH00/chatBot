from aiogram import types

from src.classes.Config import Config
from src.classes.WindowsOS import WindowsOS
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types


class Application:

    def __init__(self, config: Config, keyboard):
        self.__config = config
        self.__keyboard = keyboard
        self.__bot = Bot(token=config.get_param('token'))
        self.__dp = Dispatcher(self.__bot)

        os = config.get_param('os')
        if os is None:
            raise Exception('Not found os')
        if os == 'linux':
            # self.__os = LinuxOS(self.__dp, self.__bot, self.__config, self.__keyboard)
            pass
        elif os == 'windows':
            self.__os = WindowsOS(self.__dp, self.__bot, self.__config, self.__keyboard.keyboard)
        else:
            raise Exception('Not found support os')

    async def show_help(self, message: types.Message):
        await self.__bot.send_message(message.from_user.id, self.__keyboard.help, reply_markup=self.__keyboard.keyboard)

    def register_handlers(self):
        self.__dp.register_message_handler(self.show_help, commands=['help'])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["📸СКРИНШОТ📸"])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["📹ВИДЕО📹"])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["🚮УДАЛИТЬ🚮"])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["🚮УДАЛИТЬ🚮"])
        # self.__dp.register_message_handler(self.__os.disk_area, commands=["♻️Перезагрузить♻️"])

    def run(self):
        executor.start_polling(self.__dp, skip_updates=True)

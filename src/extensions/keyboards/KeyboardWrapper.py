from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class KeyboardWrapper:
    def __init__(self, resize_keyboard=True):
        self.__keyboard = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
        self.__help = dict()

    def add_button(self, text, description):
        button = KeyboardButton(text)
        self.__help[text] = description
        self.__keyboard.add(button)
        return self

    @property
    def keyboard(self):
        return self.__keyboard

    @property
    def help(self):
        content = ''
        for key in self.__help:
            content += key + ' - ' + self.__help.get(key) + '\n'

        return content

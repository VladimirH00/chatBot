from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class KeyboardWrapper:
    def __init__(self, resize_keyboard=True):
        self.__keyboard = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)

    def add_button(self, text):
        button = KeyboardButton(text)
        self.__keyboard.add(button)
        return self

    @property
    def keyboard(self):
        return self.__keyboard

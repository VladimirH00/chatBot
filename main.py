from src.classes.Application import Application
from src.classes.Config import Config
from src.extensions.keyboards.KeyboardWrapper import KeyboardWrapper

if __name__ == '__main__':

    config_file = open('config/env')
    config = Config(file=config_file)
    config_file.close()

    greet_kb = KeyboardWrapper()
    greet_kb.add_button(text="/🖥ВЫКЛЮЧИТЬ🖥", description='мгновенное выключение компьютера')\
        .add_button("/♻️Перезагрузить♻️", description='мгновенная перезагрузка компьютера')\
        .add_button("/📸КАМЕРА📸", description='сделать фото')

    application = Application(config, greet_kb)
    application.register_handlers()
    application.run()
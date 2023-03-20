from aiogram import types


class OSInterface:

    async def shutdown(self, message: types.Message):
        pass

    async def make_screenshot(self, message: types.Message):
        pass

    async def delete_file(self, message: types.Message):
        pass

    async def get_system_characteristics(self, message: types.Message):
        pass

    async def reboot(self, message: types.Message):
        pass

    async def disk_area(self, message: types.Message):
        pass

    async def get_temperature(self, message: types.Message):
        pass

    async def make_photo(self, message: types.Message):
        pass

from aiogram.utils.keyboard import InlineKeyboardBuilder

class UserKb:
    @staticmethod
    async def main_menu():
        buttons = [
            ("🚀 Запустить бомбер 🚀", "start_spamer"),
            ("❓ Как работает бомбер ❓", "what_work_spamer")
        ]

        menu = InlineKeyboardBuilder()

        for text, callback_data in buttons:
            menu.button(text=text, callback_data=callback_data)
        return menu.adjust(1).as_markup()
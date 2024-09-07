from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from signature import MyBot

from handlers.hello_text import start_text, info_text

from keyboards.client_kb import UserKb

class Client:
    def __init__(self, bot_inc: MyBot):
        self.bot = bot_inc.bot
        self.dp = bot_inc.dp
        self.db = bot_inc.db
    
    
    async def register_handlers(self):
        self.dp.message(CommandStart())(self.start_handler)
        self.dp.callback_query(F.data == 'what_work_spamer')(self.what_work_spamer)
        self.dp.callback_query(F.data == 'back_menu')(self.back_menu_handler)
        
        
    async def start_handler(self, m: Message):
        username = m.from_user.username if m.from_user.username else m.from_user.first_name
        await self.db.add_user(m.from_user.id, username)
        await m.answer(start_text, reply_markup=await UserKb.main_menu())
    
    
    async def what_work_spamer(self, call: CallbackQuery):
        await call.message.delete()
        await call.message.answer(info_text, parse_mode='HTML', reply_markup=await UserKb.back_menu())
    
    
    async def back_menu_handler(self, call: CallbackQuery):
        await call.message.delete()
        await call.message.answer(start_text, reply_markup=await UserKb.main_menu())
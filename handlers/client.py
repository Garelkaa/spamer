from aiogram.types import Message
from aiogram.filters import CommandStart
from signature import MyBot


class Client:
    def __init__(self, bot_inc: MyBot):
        self.bot = bot_inc.bot
        self.dp = bot_inc.dp
    
    
    async def register_handlers(self):
        self.dp.message(CommandStart())(self.start_handler)
        
        
    async def start_handler(self, m: Message):
        await m.answer("Здарова брат")
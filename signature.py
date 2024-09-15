import os
from aiogram import Dispatcher, Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv

from database.requests import DBUsers


load_dotenv() 


class MyBot:
    def __init__(self):
        self.dp = Dispatcher()
        self.bot = Bot(token=os.getenv('TELEGRAM_API_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.db = DBUsers()
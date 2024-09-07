import os
from aiogram import Dispatcher, Bot

from dotenv import load_dotenv

from database.requests import DBUsers


load_dotenv() 


class MyBot:
    def __init__(self):
        self.dp = Dispatcher()
        self.bot = Bot(token=os.getenv('TELEGRAM_API_TOKEN'))
        self.db = DBUsers()
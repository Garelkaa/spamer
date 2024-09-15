import logging

from aiogram import F
import phonenumbers
from signature import MyBot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext

from utils.fsm import StartBomber

from utils.utils import SmsSpam

logging.basicConfig(level=logging.DEBUG)

class StartSpammer:
    def __init__(self, bot_inc: MyBot):
        self.bot = bot_inc.bot
        self.dp = bot_inc.dp
        self.db = bot_inc.db
        self.spam = SmsSpam()
        
    async def register_handlers(self):        
        self.dp.callback_query(F.data == 'start_spamer')(self.start_fsm)
        self.dp.message(StartBomber.number)(self.get_number)
        self.dp.message(StartBomber.time)(self.get_time)
        
    async def start_fsm(self, call: CallbackQuery, state: FSMContext) -> None:
        # if self.db.check_invoice(call.from_user.id):
        await state.set_state(StartBomber.number)
        await call.message.answer(
            "📞 Please enter the target phone number.\n\n"
            "Make sure to include the country code (e.g., +1234567890)."
        )

    async def get_number(self, m: Message, state: FSMContext) -> None:
        phone_number = m.text.strip()
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            
            if not phonenumbers.is_valid_number(parsed_number):
                await m.answer(
                    "❌ The phone number you entered is invalid. Please double-check the number and try again.\n\n"
                    "Make sure it is in the correct international format, like +1234567890."
                )
                return  
            
            await state.update_data(number=m.text)
            await state.set_state(StartBomber.time)  
            await m.answer(
                "<b>✅ Phone number accepted!</b> 🎉\n\n"
                "Let's proceed...\n\n"
                "⌛ Please enter the duration of the attack in minutes."
            )
            
        except phonenumbers.NumberParseException:
            await m.answer(
                "⚠️ Incorrect phone number format.\n\n"
                "Please ensure the number is in the international format, for example, +1234567890."
            )
            return  

    async def get_time(self, m: Message, state: FSMContext) -> None:
        data = await state.update_data(time=m.text)
        logging.debug(data)
        await state.clear() 
        await m.answer(
            "<b>🕒 Time is set!</b> ⏰\n\n"
            "🚀 The attack has started. Please wait..."
        )
        print(data.get('number')[4:])
        await self.spam.send_sms(number=data.get('number'))

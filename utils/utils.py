import os
from signature import load_dotenv

from twilio.rest import Client

load_dotenv

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

# Создание клиента
client = Client(account_sid, auth_token)
class SmsSpam:
    @staticmethod
    async def send_sms(number) -> None:
        message = client.messages.create(
            body="Текст вашего сообщения",
            from_=os.getenv('PHONE_NUMBER'),
            to=f'{number}'
        )
    
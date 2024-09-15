import asyncio
from signature import MyBot
from handlers.client import Client
from handlers.spamer import StartSpammer
from utils.logging import setup_logger


async def main():
    await setup_logger(level="DEBUG")
    bot_inc = MyBot()
    
    handler_client = Client(bot_inc)
    handler_spamer = StartSpammer(bot_inc)
    await handler_client.register_handlers()
    await handler_spamer.register_handlers()
    await bot_inc.db.create_tables()
    print("𝙱𝚈 𝙷𝚂 𝚃𝙴𝙰𝙼")
    await bot_inc.dp.start_polling(bot_inc.bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    
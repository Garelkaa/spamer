import logging
from .models import Base, engine 

logging.basicConfig(level=logging.INFO)

class DBUsers:
    def __init__(self):
        self.engine = engine 

    async def create_tables(self):
        async with self.engine.begin() as conn:  
            await conn.run_sync(Base.metadata.create_all)

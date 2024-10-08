import logging

from sqlalchemy import select
from .models import Base, engine, AsyncSessionLocal, User

logging.basicConfig(level=logging.INFO)

class DBUsers:
    def __init__(self) -> None:
        self.engine = engine 
        self.session = AsyncSessionLocal()

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:  
            await conn.run_sync(Base.metadata.create_all)

    async def add_user(self, user_id, username) -> None:
        async with self.session.begin():
            try:
                new_user = User(user_id_tg=user_id, username=username)
                self.session.add(new_user)
                await self.session.commit()
            except Exception as e:
                logging.error(f"Failed to add user: {e}")
                await self.session.rollback()
                
    async def find_user(self, user_id) -> bool:
        async with self.session.begin():
            try:
                result = await self.session.execute(select(User).where(User.user_id_tg == user_id))
                user = result.scalars().first()
        
                if user:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f"Failed to find the user: {e}")
                await self.session.rollback()
                return False

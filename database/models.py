from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+asyncpg://postgres:1111@localhost/spamer'
engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)
    user_id_tg = Column(BigInteger, primary_key=True)
    username = Column(String)
    
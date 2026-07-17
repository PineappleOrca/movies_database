from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, String, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgressql import UUID
from sqlalchemy.exy.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, date
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyDatabase
from fastapi import Depends

DATABASE_URL = "sqlite+aiosqlite:///../database/movies.db"

class Base(DeclarativeBase):
    pass 

class User(SQLAlchemyBaseUserTableUUID, Base):
    posts = relationship(argument="Movies", back_populates="user")

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String)
    content_type = Column(String)
    genre = Column(String)
    watch_status = Column(String)
    total_episodes = Column(Integer, default=1)
    episodes_watched = Column(Integer, default=1)
    event_date = Column(Date)
    user = relationship(argument="User", back_populates="posts")

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_movies_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyDatabase(session, User)
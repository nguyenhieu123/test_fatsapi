import asyncio
import sqlalchemy.ext.declarative as _declarative
from sqlalchemy.ext.asyncio import create_async_engine
import sqlalchemy.orm as _orm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql+asyncpg://localhost:5432/test1'

# engine = create_async_engine(
#     DATABASE_URL, pool_size=15, max_overflow=5, pool_pre_ping=True, echo=True)

engine = create_async_engine(
        "postgresql+asyncpg://scott:tiger@localhost/test", echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

Base = _declarative.declarative_base()


# async def filter(async_pred, iterable):
#     for item in iterable:
#         should_yield = await async_pred(item)
#         if should_yield:
#             yield item

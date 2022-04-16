import sqlalchemy.ext.declarative as _declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://localhost:5432/test1'

engine = create_engine(
    DATABASE_URL, pool_size=15, max_overflow=5, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = 'postgresql://localhost:5432/test1'

engine = _sql.create_engine(
    DATABASE_URL, pool_size=15, max_overflow=5, pool_pre_ping=True)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()

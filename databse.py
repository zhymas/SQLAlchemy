from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres", echo=True) # created engine for database
async_engine = create_async_engine('postgresql+asyncpg://postgres:postgres@localhost:5432/postgres')

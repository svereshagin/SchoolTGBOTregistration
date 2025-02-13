from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.configs.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def init_db():
    """Создание таблиц в базе данных"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

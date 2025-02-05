from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import settings

master_engine = create_async_engine(settings.MASTER_DB_URL, echo=True)
MasterSessionLocal = sessionmaker(bind=master_engine, class_=AsyncSession, expire_on_commit=False)

async def get_master_db():
    async with MasterSessionLocal() as session:
        yield session

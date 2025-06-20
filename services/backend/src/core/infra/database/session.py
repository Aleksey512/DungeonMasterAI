from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.config.settings import settings

engine = create_async_engine(settings.database_url, echo=True)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

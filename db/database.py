from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from db.config import settings

engine = create_async_engine(settings.db_url, echo=settings.db_echo)

# AsyncSession будет хранить объекты в памяти и отслеживать
# любые необходимые изменения данных и использует движок для взаимодействия
# с базой данных
# async_sessionmaker - фабрика сессий
# фабрика сессий
AsyncSession = async_sessionmaker(bind=engine)


# Функция для получения сессии
async def get_session():
    async with AsyncSession() as session:
        yield session

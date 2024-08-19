
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    # echo: bool = False
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v0"

    db: DbSettings = DbSettings()

    # db_echo: bool = True


settings = Settings()

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    AsyncSession,
    async_sessionmaker
    
) 
from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    mapped_column, 
    declared_attr,
    sessionmaker
)


#хз что это используется в models 
class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)

#настройки создание движка бдшки, может использовть в utils/db_operations.py
sync_engine = create_engine(
    url=settings.db.url,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.db.url,
    echo=True,
)

#фабрика сессий используется во views
session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)




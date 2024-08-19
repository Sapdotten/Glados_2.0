from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker


#настройки создание движка бдшки, может использовть в utils/db_operations.py
def GET_LINK_DB():
    return f"sqlite+aiosqlite:///myfile.db"

engine = create_async_engine("sqlite+aiosqlite:///myfile.db")

#хз что это используется в models 
Base = declarative_base()

#фабрика сессий используется во views
async_session = async_sessionmaker(engine, class_=AsyncSession)
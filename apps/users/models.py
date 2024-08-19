import re
import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://qglpmgcg:bsKsGrHGGRpqr4fjKbBBVXoRDj-_J6ks@satao.db.elephantsql.com:5432/qglpmgcg"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
Base = declarative_base()

class UserRole(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

class UserModel(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    
    user_login = Column(String(64), unique=True, nullable=False, comment='Имя пользователя')
    user_password = Column(String(128), unique=True, nullable=False, comment='Пароль пользователя')
    
    is_active = Column(Boolean, default=True, nullable=False, comment='Активен')
    user_role = Column(Enum(UserRole), default=UserRole.USER, nullable=False, comment='Роль пользователя')
    
    user_Last_name = Column(String(32), nullable=False, comment='Фамилия')
    user_first_name = Column(String(32), nullable=False, comment='Имя')
    user_patronymic = Column(String(32), nullable=False, comment='Отчество')
    
    user_group_number = Column(String, nullable=True, comment='Номер группы')
    
    user_phone = Column(String, unique=True, nullable=False, comment='Телефон')
    
    user_vk = Column(String, unique=True, nullable=True, comment='VK')
    user_telegram = Column(String, unique=True, nullable=True, comment='Telegram')
    user_email = Column(String, unique=True, nullable=True, comment='Email')
    

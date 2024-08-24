import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship

from config.settings import Base


class UserRole(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

class UserModel(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    
    user_login = Column(String(64), unique=True, nullable=False, comment='Имя пользователя')
    user_hashed_password = Column(String, nullable=False)    
    
    is_active = Column(Boolean, default=True, nullable=False, comment='Активен')
    user_role = Column(Enum(UserRole), default=UserRole.USER, nullable=False, comment='Роль пользователя')
    
    user_Last_name = Column(String(32), nullable=False, comment='Фамилия')
    user_first_name = Column(String(32), nullable=False, comment='Имя')
    user_patronymic = Column(String(32), nullable=False, comment='Отчество')
    
    user_group_number = Column(String, nullable=True, comment='Номер группы')
    
    user_phone = Column(String, unique=True, nullable=False, comment='Телефон')
    
    phones = relationship("PhoneModel", back_populates="user")
    emails = relationship("EmailModel", back_populates="user")
    social_accounts = relationship("SocialAccountModel", back_populates="user")
    
class PhoneModel(Base):
    __tablename__ = 'Телефоны_клубовцев'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    phone = Column(String, nullable=False, comment='Телефон')
    
    user = relationship("UserModel", back_populates="phones")

class EmailModel(Base):
    __tablename__ = 'Почты_клубовцев'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    email = Column(String, nullable=False, comment='Email')
    
    user = relationship("UserModel", back_populates="emails")


class UserRole(enum.Enum):
    TELEGRAM = 'telegram'
    VK = 'vk'
    DISCORD = 'discord'

class SocialAccountModel(Base):
    __tablename__ = 'Соц_сети_клубовцев'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    account_type = Column(String, nullable=False, comment='Тип аккаунта')
    account_id = Column(String, nullable=False, comment='Идентификатор аккаунта')
    
    user = relationship("UserModel", back_populates="social_accounts")
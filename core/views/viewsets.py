from dataclasses import dataclass, field
from typing import Union

from fastapi.responses import JSONResponse
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

from config.settings import async_session_factory

@dataclass
class BaseAPIView:
    '''
        класс для создания асинхронных сессий
    '''
    db: AsyncSession = field(default=None)
    
    def __init__(self, db: AsyncSession = None, **kwargs):
        """
        Конструктор. Может содержать дополнительные параметры.
        Какие? да хуй его знает.
        """
        if db is not None:
            self.db = db
        for key, value in kwargs.items():
            setattr(self, key, value)
        # print('---> ', self.__dict__)
    
    @classmethod
    async def create_session(cls):
        db = await async_session_factory().__aenter__()
        instance = cls(db=db)
        try:
            yield instance
        finally:
            await db.__aexit__(None, None, None)

    async def handle_errors(self, func):
        try:
            return await func()
        except HTTPException as e:
            raise e  # Если это HTTPException, просто пробрасываем её дальше
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Resource not found.")
        except SQLAlchemyError:
            await self.db.rollback()
            raise HTTPException(status_code=500, detail="An error occurred while processing the request.")

    async def to_json(self, instance: Union[dict, JSONResponse]):
        if isinstance(instance, JSONResponse):
            print('Instance is already a JSON response.')
            return instance
        elif hasattr(instance, 'to_dict'):
            # Assuming your model has a to_dict method for serialization
            return JSONResponse(instance.to_dict())
        elif isinstance(instance, dict):
            # Directly return a dictionary as JSON
            return JSONResponse(instance)
        elif hasattr(instance, '__dict__'):
            return JSONResponse(vars(instance))  # Use vars() to get instance attributes as a dict.
        else:
            raise ValueError("Instance cannot be converted to JSON.")

    async def get_permission(self):
        '''
            must be list/tuple
        '''
        ...
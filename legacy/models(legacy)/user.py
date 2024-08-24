'''
        Добавь базу данных нашу где она указана
        дока по бдшка в пиве: https://docs.peewee-orm.com/en/latest/peewee/database.html
        
        ->как в пиве подключается бдшка<-

        #пример 1
        from playhouse.postgres_ext import PostgresqlExtDatabase
        psql_db = PostgresqlExtDatabase('my_database', user='postgres')
        
        #пример 2
        from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE
        db = PostgresqlDatabase('my_app', user='postgres', host='db-host',
                        isolation_level=ISOLATION_LEVEL_SERIALIZABLE)

        --> указние бдшки в моделях <--

        class BaseModel(Model):
        """A base model that will use our Sqlite database."""
            class Meta:
                database = sqlite_db #тут подключается 
'''



import re

from peewee import *

from models.base_model import BaseModel


pg_db = PostgresqlDatabase('qglpmgcg', user='qglpmgcg', password='bsKsGrHGGRpqr4fjKbBBVXoRDj-_J6ks',
                           host='satao.db.elephantsql.com', port=5432)


class UserModel(BaseModel):
    id                  =   PrimaryKeyField(unique=True)

    user_login          =   CharField(max_length=64,  unique=True, verbose_name='Имя пользователя')
    user_password       =   CharField(max_length=128, unique=True, verbose_name='Пароль пользователя')  #надо написать хэш функцию
    user_Last_name      =   CharField(max_length=32, help_text='Фамилия', verbose_name='Фамилия')
    user_first_name     =   CharField(max_length=32, help_text='Имя', verbose_name='Имя')
    user_patronymic     =   CharField(max_length=32, help_text='Отчество', verbose_name='Отчество')
    user_group_number   =   CharField(null=True, help_text='Номер вашей учебной группы', verbose_name='Номер группы')                    #под это надо написать валидатор
    user_phone          =   CharField(unique=True, help_text='Номер вашего телефона', verbose_name='Телефон')                  #под это надо написать валидатор
    user_vk             =   CharField(null=True, unique=True, help_text='Ваш профиль вконтакте', verbose_name='VK')
    user_telegram       =   CharField(null=True, unique=True, help_text='Ваш профиль телеграм', verbose_name='Telegram')
    user_email          =   CharField(null=True, unique=True, help_text='Ваша почта', verbose_name='Email')                  #под это надо написать валидатор

    class Meta:
        order_by = id
        db_table = 'Users'


    def validate_user_group_number(value):
        pattern = r'^\d{4}-\d{6}[A-Z]$'
        if not re.match(pattern, value):
            raise ValueError('Неверный формат номера группы')

    def validate_user_phone(self, num):
        clear_phone = re.sub(r'\D', '', num)
        result = re.match(r'^[78]?\d{10}$', clear_phone)
        pass

    def validate_user_email(self):
        # Напишите свою логику валидации почты здесь
        pass

    def hash_password(self, password):
        # Напишите свою логику хэширования пароля здесь
        pass

#надстройка чтобы распрасить в\из json
# class starletteCodpiecAPIView(CodpiecAPIView):
#     # async def list(self, request: Request):
#     #     result = await super().list()
#     #     return JSONResponse([item.dict() for item in result])

#     # async def retrieve(self, request: Request):
#     #     codpiece_id = int(request.path_params['codpiece_id'])
#     #     result = await super().retrieve(codpiece_id)
#     #     return JSONResponse(result.dict())

#     # async def create(self, request: Request):
#     #     data = await request.json()
#     #     result = await super().create(data)
#     #     return JSONResponse(result.dict())

#     # async def update(self, request: Request):
#     #     codpiece_id = int(request.path_params['codpiece_id'])
#     #     data = await request.json()
#     #     result = await super().update(codpiece_id, data)
#     #     return JSONResponse(result.dict())

#     # async def partial_update(self, request: Request):
#     #     codpiece_id = int(request.path_params['codpiece_id'])
#     #     data = await request.json()
#     #     result = await super().partial_update(codpiece_id, data)
#     #     return JSONResponse(result.dict())

#     # async def destroy(self, request: Request):
#     #     codpiece_id = int(request.path_params['codpiece_id'])
#     #     result = await super().destroy(codpiece_id)
#     #     return JSONResponse(result)
    
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
import re, datetime

from peewee import *

from database_settings import SQL_DB

from . import User


def set_file_name(id):
    """ID#####__%d_%m_%Y"""
    return datetime.datetime.now().strftime(f"ID{id}__%d_%m_%Y")

def set_file_path(file_name):
    return datetime.datetime.now().strftime(f'media_storage/%Y/%m/%d/{file_name}.docx')

class BaseFileModel(Model):
    id                  = PrimaryKeyField(unique=True)
    file_name           = CharField(unique=True)  
    file_author         = ForeignKeyField(User, backref='BaseFileModels')
    file_date_created   = DateTimeField(default=datetime.datetime.now)
    file_path           = CharField(unique=True)

    def save(self, *args, **kwargs):
        if not self.file_name or None:
            print(self.id)
            self.file_name = set_file_name(self.id)
        if not self.file_path or None:
            self.file_path = set_file_path(self.file_name)
        return super(BaseFileModel, self).save(*args, **kwargs)
    

    class Meta:
        database = SQL_DB
        order_by = id
        db_table = 'Files'


class Message(BaseFileModel):
    message_recipients  = ManyToManyField(User, backref='DocMessages')
    message_type        = CharField(choices=['благодарность', 'отпускные'])
    message_title       = CharField(help_text='за что блана/отпускной заголовок')
    message_body        = TextField(help_text='за что блага/отпускной')
    message_date        = DateTimeField(default=datetime.datetime.now)
    

    class Meta:
        database = SQL_DB
        order_by = id
        db_table = 'Documents_messages'

file = Message.create(
    file_author=1,
    message_type='благодарность',
    message_title='За хакатон в Роботика',
    message_body='За хакатон в Роботика'
)

id = file.id
file.file_name = set_file_name(id)
file.file_path = set_file_path(file.file_name)
file.save()
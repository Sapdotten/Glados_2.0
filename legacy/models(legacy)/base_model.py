from database_settings import SQL_DB
from peewee import *

class BaseModel(Model):
    class Meta:
        database = SQL_DB
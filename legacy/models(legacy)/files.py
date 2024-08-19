from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime



class BaseFileModel(Base):
    __tablename__ = 'Files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, unique=True)
    file_author_id = Column(Integer, ForeignKey('Users.id'))
    file_author = relationship('User', backref='BaseFileModels')
    file_date_created = Column(DateTime, default=datetime.datetime.now)
    file_path = Column(String, unique=True)

    def save(self, *args, **kwargs):
        if not self.file_name or self.file_name is None:
            self.file_name = set_file_name(self.id)
        if not self.file_path or self.file_path is None:
            self.file_path = set_file_path(self.file_name)
        return super(BaseFileModel, self).save(*args, **kwargs)

class Message(BaseFileModel):
    __tablename__ = 'Documents_messages'

    id = Column(Integer, ForeignKey('Files.id'), primary_key=True)
    message_type = Column(String)
    message_title = Column(String)
    message_body = Column(Text)
    message_date = Column(DateTime, default=datetime.datetime.now)

    message_recipients = relationship('User', secondary='message_recipients', backref='DocMessages')


def set_file_name(id):
    """ID#####__%d_%m_%Y"""
    return datetime.datetime.now().strftime(f"ID{id}__%d_%m_%Y")

def set_file_path(file_name):
    return datetime.datetime.now().strftime(f'media_storage/%Y/%m/%d/{file_name}.docx')
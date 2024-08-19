from sqlalchemy import Column, Integer, String
from config.settings import Base

class Gulfiks(Base):
    __tablename__ = "гульфики"
    id = Column(Integer, primary_key=True)
    gulfik_model_name = Column(String)
    gulfik_model_descriptions = Column(String)
    gulfik_model_size = Column(Integer)

    def __repr__(self):
        return f"<Gulfik(name='{self.gulfik_model_name}', descriptions='{self.gulfik_model_descriptions}', size='{self.gulfik_model_size}')>"







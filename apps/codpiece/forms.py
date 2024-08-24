from typing import Optional
from pydantic import BaseModel

# Определение моделей
class CodpieceBase(BaseModel):
    gulfik_model_name: str
    gulfik_model_descriptions: str
    gulfik_model_size: int

class CodpieceCreate(CodpieceBase):
    pass

class CodpieceUpdate(CodpieceBase):
    pass

class CodpiecePartialUpdate(CodpieceBase):
    gulfik_model_name: Optional[str] = None
    gulfik_model_descriptions: Optional[str] = None
    gulfik_model_size: Optional[int] = None

class Codpiece(CodpieceBase):
    id: int

    class Config:
        orm_mode = True  # Позволяет использовать модели ORM
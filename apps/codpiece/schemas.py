from pydantic import BaseModel

class CodpieceBase(BaseModel):
    gulfik_model_name: str
    gulfik_model_descriptions: str
    gulfik_model_size: int

class CodpieceCreate(CodpieceBase):
    pass

class CodpieceUpdate(CodpieceBase):
    pass

class Codpiece(CodpieceBase):
    id: int

    class Config:
        orm_mode = True
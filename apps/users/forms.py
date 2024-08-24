from pydantic import BaseModel, EmailStr, Field, validator
from typing import List

class PhoneCreate(BaseModel):
    phone: str

class EmailCreate(BaseModel):
    email: EmailStr

class SocialAccountCreate(BaseModel):
    account_type: str
    account_id: str

class UserCreate(BaseModel):
    user_login: str
    user_hashed_password: str
    user_Last_name: str
    user_first_name: str
    user_patronymic: str
    user_group_number: str = None
    phones: List[PhoneCreate] = Field(..., min_items=1)  # Гарантирует, что будет хотя бы один телефон
    emails: List[EmailCreate] = []
    social_accounts: List[SocialAccountCreate] = []

    @validator('phones')
    def check_at_least_one_phone(cls, v):
        if not v:
            raise ValueError('At least one phone number is required')
        return v

class UserInDB(UserCreate):
    id: int
    is_active: bool
    user_role: UserRole

    class Config:
        orm_mode = True
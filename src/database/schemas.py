import datetime

from pydantic import BaseModel, EmailStr


class DbUser(BaseModel):
    fullname: str
    login: str
    password: str
    birthday: datetime.date
    email: EmailStr
    country: str
    city: str

    class Config:
        orm_mode = True

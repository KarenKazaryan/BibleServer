import datetime

from pydantic import BaseModel


class DbUser(BaseModel):
    fullname: str
    login: str
    password: str
    birthday: datetime.date
    country: str
    city: str
    email: str

    class Config:
        orm_mode = True
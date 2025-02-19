from sqlalchemy import Column, Integer, String, Date

from src.database.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)

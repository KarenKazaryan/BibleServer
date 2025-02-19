from typing import List

from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.database.models import User
from src.database.schemas import DbUser

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/create", response_model=DbUser)
async def create_user(user: DbUser, db: Session = Depends(get_db)) -> User:
    db_user = User(fullname=user.fullname,
                   birthday=user.birthday,
                   login=user.login,
                   password=user.password,
                   email=user.email,
                   country=user.country,
                   city=user.city
                   )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.post("/login", response_model=DbUser)
async def login(login: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.login == login, User.password == password).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.get("/read_all", response_model=List[DbUser])
async def read_users(db: Session = Depends(get_db)) -> List[User]:
    db_user = db.query(User).all()
    return db_user


@router.get("/read/{id}", response_model=DbUser)
async def read_users(id: int, db: Session = Depends(get_db)) -> User:
    db_user = db.query(User).filter(User.id == id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.put("/update/{id}", response_model=DbUser)
async def update_user(id: int, user: DbUser, db: Session = Depends(get_db)) -> User:
    db_user = db.query(User).filter(User.id == id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.fullname = user.fullname
    db_user.login = user.login
    db_user.password = user.password
    db_user.birthday = user.birthday
    db_user.country = user.country
    db_user.city = user.city
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/delete/{id}", response_model=bool)
async def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return True

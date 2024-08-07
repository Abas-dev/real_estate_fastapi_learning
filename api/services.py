from sqlalchemy.orm import Session
from api.models import User
from api.schema import UserCreate

def check_user_exist(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user 

def insert_new_user(db: Session, user: UserCreate):
    new_user = User(email= user.email, password= user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
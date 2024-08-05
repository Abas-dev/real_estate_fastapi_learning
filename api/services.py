from sqlalchemy.orm import Session
from api.models import User

def check_user_exist(db: Session, email: str):
    user = db.query(User).filter(User.email == email)
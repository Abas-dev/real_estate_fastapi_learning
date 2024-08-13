from fastapi import APIRouter,status,Depends,HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from api.schema import UserCreate 
from api.utils import hash_password, verify_password
from api.services import check_user_exist, insert_new_user


router = APIRouter(prefix="/api/v1/auth", tags=["User Authentication"])

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    emial_check = check_user_exist(db, email= user.email)

    if emial_check: 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with this email already exist in my db")

    user.password = hash_password(user.password)

    user = insert_new_user(db, user=user)
    #check if email already exist
    #hash user password 
    #create new user 
    #send email notification 
    
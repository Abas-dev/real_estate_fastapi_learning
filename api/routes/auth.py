from fastapi import APIRouter,status,Depends,HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from api.schema import UserCreate 


router = APIRouter(prefix="/api/v1/auth", tags=["User Authentication"])

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    ...

    #check if email already exist
    #hash user password 
    #create new user 
    #send email notification 
    
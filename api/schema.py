from pydantic import BaseModel,Field,EmailStr

class UserBase(BaseModel):
    email: EmailStr = Field(...,title="This is to provide the user email",examples="example@gmail.com")

class UserCreate(UserBase):  #this is going to be used for the request data type 
    password: str = Field(...,title="This is for the user password", examples="Password12@")

class User(UserBase):   #this is to be used as the response data type 
    id: int
    is_active: bool
    is_verified: bool        
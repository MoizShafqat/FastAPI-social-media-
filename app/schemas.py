from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    
    model_config = {
        "from_attributes": True
    }
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str    

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class UserResponse(BaseModel):      
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True    

class UserLogin(BaseModel):
    email: EmailStr
    password: str
        
class Token(BaseModel):
    access_token : str
    token_type: str        

class TokenData(BaseModel):
    id: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserResponse
    likes: int = 0          # 👈 add this

    class Config:
        from_attributes = True


class Vote(BaseModel):
    post_id: int
    dir: int  # 1 = like, 0 = unlike
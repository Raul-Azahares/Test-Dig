from pydantic import BaseModel
from typing import List,Optional
from .post import Post




class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True
from pydantic import BaseModel
from typing import List
from .tag import Tag



class PostBase(BaseModel):
    title: str

class PostCreate(PostBase):
    owner_id: int
    tags: List[int] = []

class Post(PostBase):
    id: int
    owner_id: int
    tags: List[Tag] = []

    class Config:
        orm_mode = True

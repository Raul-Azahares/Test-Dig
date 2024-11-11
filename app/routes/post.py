from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.auth import get_current_user
from app.models.user import User
from ..schemas.post import Post, PostCreate
from ..crud.post import add_post,read_post
from ..core.database import get_db

router = APIRouter(prefix="/posts")


@router.post("/", response_model=Post)
async def create_post_endpoint(post: PostCreate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    return await add_post(db, post, post.owner_id)

@router.get("/", response_model=List[Post])
async def list_users_endpoint(db: AsyncSession = Depends(get_db)):
    return await read_post(db)

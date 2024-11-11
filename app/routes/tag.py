from typing import List
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from app.schemas.tag import Tag, TagCreate,TagUpdate
from app.schemas.user import User
from app.crud.tag import add_tag,read_tags,update_tag
from app.core.database import init_db,get_db
from app.crud.auth import get_current_user

router = APIRouter(prefix="/tags")


@router.post("/", response_model=Tag)
async def create_tag_endpoint(tag: TagCreate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    return await add_tag(db, tag)

@router.get("/", response_model=List[Tag])
async def list_tags_endpoint(db: AsyncSession = Depends(get_db)):
    return await read_tags(db)

@router.put("/{tag_id}", response_model=Tag)
async def update_tag_endpoint(tag_id: int, tag_update: TagUpdate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        return await update_tag(db, tag_id, tag_update)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Tag not found")
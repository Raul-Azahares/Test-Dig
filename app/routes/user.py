from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.crud.auth import get_current_user
from ..schemas.user import User, UserCreate,UserUpdate
from ..crud.user import add_user,read_users, update_user,read_active_users,delete_user_soft
from ..core.database import get_db

router = APIRouter(prefix="/users")


@router.post("/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    return await add_user(db, user)

@router.get("/", response_model=List[User])
async def list_users_endpoint(db: AsyncSession = Depends(get_db)):
    return await read_users(db)

@router.put("/{user_id}", response_model=User)
async def update_user_endpoint(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        return await update_user(db, user_id, user_update)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/active", response_model=List[User])
async def list_active_users_endpoint(db: AsyncSession = Depends(get_db)):
    return await read_active_users(db)


@router.delete("/{user_id}")
async def soft_delete_user(user_id: int, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    user = await delete_user_soft(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User soft-deleted successfully"}
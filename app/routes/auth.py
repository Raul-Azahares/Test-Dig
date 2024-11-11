from datetime import timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, register_user, verify_password
from app.crud.user import get_user
from app.schemas.token import Token



router = APIRouter(prefix="/auth")


@router.post("/register")
async def register(name: str, password: str, db: Session = Depends(get_db), full_name: Optional[str] = None):
    user = await register_user(name,password,db, full_name)
    return {"msg": "User registered successfully", "name": user.name}

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: AsyncSession = Depends(get_db)
):
    user = await get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app.schemas.user import UserCreate, UserUpdate, User
from app.models.user import User as UserModel
from fastapi import HTTPException, status




async def add_user(db: AsyncSession, user: UserCreate):
    db_user = UserModel(name=user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return User(**db_user.__dict__)


async def read_users(db: AsyncSession):
    result = await db.execute(select(UserModel))
    users = result.scalars().all()
    return [User(**user.__dict__) for user in users]


async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    db_user = result.scalars().first()
    if not db_user:
        raise NoResultFound(f"User with id {user_id} not found")
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    await db.commit()
    await db.refresh(db_user)
    return User(**db_user.__dict__)


async def delete_user_soft(db: AsyncSession, user_id: int):
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalars().first()
    if user:
        user.soft_delete()
        await db.commit()
    return user


async def read_active_users(db: AsyncSession):
    result = await db.execute(select(UserModel).filter(UserModel.is_deleted == False))
    users = result.scalars().all()
    return [User(**user.__dict__) for user in users]


async def get_user(db: AsyncSession, name: str):
    result = await db.execute(select(UserModel).where(UserModel.name == name))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with name '{name}' not found"
        )
    return user

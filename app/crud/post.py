from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas.post import PostCreate, Post
from app.models.post import Post as PostModel




async def add_post(db: AsyncSession, post: PostCreate, user_id: int):
    db_post = PostModel(title=post.title, owner_id=user_id)
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return Post(**db_post.__dict__)

async def read_post(db: AsyncSession):
    result = await db.execute(select(PostCreate))
    posts = result.scalars().all()
    return [Post(**post.__dict__) for post in posts]
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app.schemas.tag import TagCreate, Tag, TagUpdate
from app.models.tag import Tag as TagModel




async def add_tag(db: AsyncSession, tag: TagCreate):
    db_tag = TagModel(name=tag.name)
    db.add(db_tag)
    await db.commit()
    await db.refresh(db_tag)
    return Tag(**db_tag.__dict__)

async def read_tags(db: AsyncSession):
    result = await db.execute(select(TagCreate))
    tags = result.scalars().all()
    return [Tag(**tag.__dict__) for tag in tags]


async def update_tag(db: AsyncSession, tag_id: int, tag_update: TagUpdate):
    result = await db.execute(select(TagModel).where(TagModel.id == tag_id))
    db_tag = result.scalars().first()
    if not db_tag:
        raise NoResultFound(f"Tag with id {tag_id} not found")
    for key, value in tag_update.dict(exclude_unset=True).items():
        setattr(db_tag, key, value)

    await db.commit()
    await db.refresh(db_tag)
    return Tag(**db_tag.__dict__)
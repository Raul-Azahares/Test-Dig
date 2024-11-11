from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


DATABASE_URL = "postgresql+asyncpg://postgres:909090@localhost:5432/crud_app"
#DATABASE_URL = "postgresql://postgres:909090@localhost:5432/crud_app"


engine = create_async_engine(DATABASE_URL, echo=True)
#engine = create_engine(DATABASE_URL, echo=True)


AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


#def init_db():
#    with engine.begin() as conn:
#        Base.metadata.create_all(bind=conn)
#def get_db() -> Session:
#    with SessionLocal() as session:
#        yield session
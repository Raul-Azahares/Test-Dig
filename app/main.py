from fastapi import FastAPI
from app.middlewares.request_time import RequestTimeMiddleware
from .routes.user import router as user_router
from .routes.post import router as post_router
from .routes.tag import router as tag_router
from .routes.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(tag_router)
app.add_middleware(RequestTimeMiddleware)
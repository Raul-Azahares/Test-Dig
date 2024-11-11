from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from .association_tables import post_tags
from app.mixins.soft_delete_mixin import SoftDeleteMixin
from app.mixins.times_tamp_mixin import TimestampMixin


class Post(Base,SoftDeleteMixin,TimestampMixin):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")
    owner = relationship("User", back_populates="posts")
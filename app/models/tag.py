from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from .association_tables import post_tags
from app.mixins.soft_delete_mixin import SoftDeleteMixin
from app.mixins.times_tamp_mixin import TimestampMixin


class Tag(Base,SoftDeleteMixin,TimestampMixin):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

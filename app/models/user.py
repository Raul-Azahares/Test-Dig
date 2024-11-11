from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.mixins.soft_delete_mixin import SoftDeleteMixin
from app.mixins.times_tamp_mixin import TimestampMixin


class User(Base,SoftDeleteMixin,TimestampMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String) 
    posts = relationship("Post", back_populates="owner")

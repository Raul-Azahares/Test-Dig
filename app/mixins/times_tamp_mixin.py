from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=func.now, nullable=False)

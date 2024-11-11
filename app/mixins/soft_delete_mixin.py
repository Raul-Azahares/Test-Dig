from sqlalchemy import Column, Boolean




class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False, nullable=False)

    def soft_delete(self):
        self.is_deleted = True

    @classmethod
    def query_active(cls, session):
        return session.query(cls).filter(cls.is_deleted == False)

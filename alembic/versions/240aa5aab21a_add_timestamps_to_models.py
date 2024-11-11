"""Add timestamps to models

Revision ID: 240aa5aab21a
Revises: 24aa0d7660b6
Create Date: 2024-11-10 19:20:18.871507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '240aa5aab21a'
down_revision: Union[str, None] = '24aa0d7660b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('posts', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('tags', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.add_column('tags', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('tags', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tags', 'updated_at')
    op.drop_column('tags', 'created_at')
    op.drop_column('tags', 'is_deleted')
    op.drop_column('posts', 'updated_at')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'is_deleted')
    # ### end Alembic commands ###

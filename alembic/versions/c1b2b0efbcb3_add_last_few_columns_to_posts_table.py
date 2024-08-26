"""add last few columns to posts table

Revision ID: c1b2b0efbcb3
Revises: 88fd2b28ba4c
Create Date: 2024-08-25 23:52:54.499675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1b2b0efbcb3'
down_revision: Union[str, None] = '88fd2b28ba4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

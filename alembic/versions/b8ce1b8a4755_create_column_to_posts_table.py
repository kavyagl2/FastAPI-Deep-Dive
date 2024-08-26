"""create column to posts table

Revision ID: b8ce1b8a4755
Revises: 048bdba2f529
Create Date: 2024-08-25 23:35:14.663262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8ce1b8a4755'
down_revision: Union[str, None] = '048bdba2f529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

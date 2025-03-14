"""add-user-is-active

Revision ID: 16c69aabb0f5
Revises: dd7a927a285d
Create Date: 2025-03-07 18:12:59.158613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16c69aabb0f5'
down_revision: Union[str, None] = 'dd7a927a285d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###

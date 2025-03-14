"""Add MetalRoll is_deleted field

Revision ID: 46aa9e6e5bc6
Revises: 5e9f23986586
Create Date: 2025-03-13 18:45:13.711811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46aa9e6e5bc6'
down_revision: Union[str, None] = '5e9f23986586'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('metal_roll', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('metal_roll', 'is_deleted')
    # ### end Alembic commands ###

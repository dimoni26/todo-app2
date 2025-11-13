"""create todos table

Revision ID: 499a869fed87
Revises: ad1c380734f8
Create Date: 2025-11-11 16:20:55.079340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '499a869fed87'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

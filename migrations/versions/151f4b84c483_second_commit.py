"""Second commit

Revision ID: 151f4b84c483
Revises: 3bb567dd0be5
Create Date: 2024-08-13 13:33:04.615260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '151f4b84c483'
down_revision: Union[str, None] = '3bb567dd0be5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

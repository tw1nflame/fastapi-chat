"""Second commit

Revision ID: 4b831d8634cd
Revises: 151f4b84c483
Create Date: 2024-08-13 13:37:02.813526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b831d8634cd'
down_revision: Union[str, None] = '151f4b84c483'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

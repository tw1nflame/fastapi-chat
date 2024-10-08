"""обновление столбца

Revision ID: d0bf96e74ce4
Revises: 4b831d8634cd
Create Date: 2024-08-13 13:40:43.028491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0bf96e74ce4'
down_revision: Union[str, None] = '4b831d8634cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE "user" ALTER COLUMN "created_at" TYPE TIMESTAMP WITHOUT TIME ZONE USING created_at::timestamp without time zone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'created_at',
                    existing_type=sa.TIMESTAMP(),
                    type_=sa.VARCHAR(),
                    existing_nullable=True)
    # ### end Alembic commands ###

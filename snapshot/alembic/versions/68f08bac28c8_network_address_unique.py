"""network_address_unique

Revision ID: 68f08bac28c8
Revises: 6fdef2f11302
Create Date: 2024-09-19 18:52:49.210397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '68f08bac28c8'
down_revision: Union[str, None] = '6fdef2f11302'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FET_balance_snapshot_20240919',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('network', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('stake_key', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('balance', mysql.DECIMAL(precision=65, scale=0), nullable=False),
    sa.Column('stake', mysql.BIGINT(), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address', 'network', name='uq_address_network')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FET_balance_snapshot_20240919')
    # ### end Alembic commands ###

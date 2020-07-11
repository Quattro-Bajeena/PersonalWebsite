"""nicknames table

Revision ID: 44142c1b1afa
Revises: d62b8d73aaf5
Create Date: 2020-07-11 16:01:33.366607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44142c1b1afa'
down_revision = 'd62b8d73aaf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('alternative_nickname', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'alternative_nickname')
    # ### end Alembic commands ###

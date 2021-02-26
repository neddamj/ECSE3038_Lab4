"""empty message

Revision ID: 5ff10f53fd07
Revises: 45cd20b122da
Create Date: 2021-02-26 13:29:50.764237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ff10f53fd07'
down_revision = '45cd20b122da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tanks_lat_key', 'tanks', type_='unique')
    op.drop_constraint('tanks_long_key', 'tanks', type_='unique')
    op.drop_constraint('tanks_percentage_full_key', 'tanks', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tanks_percentage_full_key', 'tanks', ['percentage_full'])
    op.create_unique_constraint('tanks_long_key', 'tanks', ['long'])
    op.create_unique_constraint('tanks_lat_key', 'tanks', ['lat'])
    # ### end Alembic commands ###
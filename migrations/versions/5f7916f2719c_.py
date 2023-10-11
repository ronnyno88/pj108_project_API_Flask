"""empty message

Revision ID: 5f7916f2719c
Revises: 48629e9d2de4
Create Date: 2023-10-10 21:55:30.242573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f7916f2719c'
down_revision = '48629e9d2de4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('api_key', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'api_key')
    # ### end Alembic commands ###
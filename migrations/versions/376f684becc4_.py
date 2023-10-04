"""empty message

Revision ID: 376f684becc4
Revises: 766beaf4ae03
Create Date: 2023-10-03 21:57:14.673712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '376f684becc4'
down_revision = '766beaf4ae03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

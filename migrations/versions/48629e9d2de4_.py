"""empty message

Revision ID: 48629e9d2de4
Revises: 0830fde6453e
Create Date: 2023-10-09 21:30:29.088155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48629e9d2de4'
down_revision = '0830fde6453e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_adm', sa.Boolean(), nullable=True))
    op.drop_column('user', 'id_adm')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id_adm', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('user', 'is_adm')
    # ### end Alembic commands ###

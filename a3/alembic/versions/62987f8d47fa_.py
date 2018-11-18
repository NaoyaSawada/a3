"""empty message

Revision ID: 62987f8d47fa
Revises: 
Create Date: 2018-11-16 23:17:03.818901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62987f8d47fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('M_ACCOUNT',
    sa.Column('UUID', sa.String(length=1024), nullable=False),
    sa.Column('MAIL', sa.String(length=1024), nullable=True),
    sa.Column('HASH', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('UUID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('M_ACCOUNT')
    # ### end Alembic commands ###

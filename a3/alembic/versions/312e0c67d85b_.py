"""empty message

Revision ID: 312e0c67d85b
Revises: 
Create Date: 2018-12-01 20:04:54.624326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312e0c67d85b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('M_ACCOUNT',
    sa.Column('ID', sa.String(length=1024), nullable=False),
    sa.Column('MAIL', sa.String(length=1024), nullable=True),
    sa.Column('HASH', sa.String(length=1024), nullable=True),
    sa.Column('LOCK', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('M_APPLICATION',
    sa.Column('ID', sa.String(length=1024), nullable=False),
    sa.Column('NAME', sa.String(length=1024), nullable=True),
    sa.Column('CALLBACK_URL', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('M_APPLICATION')
    op.drop_table('M_ACCOUNT')
    # ### end Alembic commands ###

"""ADDS THE PASSWORD COLUMN IN THE USER TABLE

Revision ID: 89fb1db0adec
Revises: a9c3fa0f2dad
Create Date: 2021-11-06 12:57:31.995885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89fb1db0adec'
down_revision = 'a9c3fa0f2dad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###

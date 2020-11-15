"""Agregado username a User

Revision ID: 47b7e6b9c5ba
Revises: 2ea86f0445a5
Create Date: 2020-10-03 17:31:49.553962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47b7e6b9c5ba'
down_revision = '2ea86f0445a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
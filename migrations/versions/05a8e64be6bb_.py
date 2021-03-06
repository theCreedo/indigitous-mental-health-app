"""empty message

Revision ID: 05a8e64be6bb
Revises: 643669da75d6
Create Date: 2017-09-23 21:30:06.863897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05a8e64be6bb'
down_revision = '643669da75d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dish_url', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dish_url')
    # ### end Alembic commands ###

"""empty message

Revision ID: 415874baeefd
Revises: 92a48a09f922
Create Date: 2023-02-02 16:38:22.188811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '415874baeefd'
down_revision = '92a48a09f922'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('found', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'found')
    # ### end Alembic commands ###

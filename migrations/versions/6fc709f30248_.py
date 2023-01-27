"""empty message

Revision ID: 6fc709f30248
Revises: 81d77115a0df
Create Date: 2023-01-26 13:59:39.116616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc709f30248'
down_revision = '81d77115a0df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'user', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'user_id')
    # ### end Alembic commands ###

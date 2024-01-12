"""Add columns to Item model

Revision ID: 71106d9d8739
Revises: 65c5f8c9debd
Create Date: 2023-12-22 12:10:14.981479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71106d9d8739'
down_revision = '65c5f8c9debd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('image_url')
        batch_op.drop_column('price')

    # ### end Alembic commands ###

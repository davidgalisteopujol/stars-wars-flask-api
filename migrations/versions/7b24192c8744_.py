"""empty message

Revision ID: 7b24192c8744
Revises: b8762487b42c
Create Date: 2022-11-27 10:08:29.209565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b24192c8744'
down_revision = 'b8762487b42c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites_planets', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites_planets', schema=None) as batch_op:
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

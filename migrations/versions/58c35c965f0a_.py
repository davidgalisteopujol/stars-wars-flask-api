"""empty message

Revision ID: 58c35c965f0a
Revises: 52b001b6421b
Create Date: 2022-11-26 18:32:58.802078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c35c965f0a'
down_revision = '52b001b6421b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['people.id'], name='favorites_character_id_fkey'),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], name='favorites_planet_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorites_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorites_pkey')
    )
    op.drop_table('favorites_planets')
    op.drop_table('favorites_people')
    # ### end Alembic commands ###

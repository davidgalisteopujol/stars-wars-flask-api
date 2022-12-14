"""empty message

Revision ID: a53bb6025325
Revises: eff0ff927d90
Create Date: 2022-11-24 19:42:33.287507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a53bb6025325'
down_revision = 'eff0ff927d90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('skin_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('birthday_year', sa.Integer(), nullable=True),
    sa.Column('Gender', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###

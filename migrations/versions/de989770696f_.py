"""empty message

Revision ID: de989770696f
Revises: 
Create Date: 2019-03-18 02:56:08.872351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de989770696f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'photo')
    op.drop_column('user_profiles', 'location')
    op.drop_column('user_profiles', 'biography')
    op.drop_column('user_profiles', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('date', sa.VARCHAR(length=12), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('biography', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('location', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('photo', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

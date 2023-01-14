"""Create_Clubs_table

Revision ID: 2c8dacd200fb
Revises: 7c28007ac853
Create Date: 2022-12-09 10:40:11.872814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c8dacd200fb'
down_revision = '7c28007ac853'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Clubs',
    sa.Column('club_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('club_name', sa.String(), nullable=False),
    sa.Column('club_image', sa.String(), nullable=False),
    sa.Column('club_icon_image', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('contact_info', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('club_id', 'club_name')
    )
    op.create_index(op.f('ix_Clubs_club_id'), 'Clubs', ['club_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Clubs_club_id'), table_name='Clubs')
    op.drop_table('Clubs')
    # ### end Alembic commands ###

"""Create_Students_images_table

Revision ID: 0aaeeae2651e
Revises: b861ca49cb38
Create Date: 2022-12-09 10:39:28.378160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aaeeae2651e'
down_revision = 'b861ca49cb38'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('studentImages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imagePath', sa.String(), nullable=False),
    sa.Column('imageName', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studentImages')
    # ### end Alembic commands ###
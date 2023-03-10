"""Edit Student Table

Revision ID: 094104abb217
Revises: 01130a3937ad
Create Date: 2022-12-31 15:09:07.156585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094104abb217'
down_revision = '01130a3937ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('gpa', sa.Float(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'gpa')
    # ### end Alembic commands ###

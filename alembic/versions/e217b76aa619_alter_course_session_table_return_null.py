"""Alter_Course_Session_table_Return_Null

Revision ID: e217b76aa619
Revises: 73a718710c3e
Create Date: 2022-12-12 11:14:22.016361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e217b76aa619'
down_revision = '73a718710c3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courseSessions', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courseSessions', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

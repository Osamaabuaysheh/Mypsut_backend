"""Create_Tutors_table

Revision ID: f961dea3ac3e
Revises: caf872a2f622
Create Date: 2022-12-09 10:41:22.063246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f961dea3ac3e'
down_revision = 'caf872a2f622'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tutors',
    sa.Column('tutor_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tutor_name', sa.String(), nullable=False),
    sa.Column('gpa', sa.Float(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('tutor_id')
    )
    op.create_index(op.f('ix_tutors_tutor_id'), 'tutors', ['tutor_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tutors_tutor_id'), table_name='tutors')
    op.drop_table('tutors')
    # ### end Alembic commands ###

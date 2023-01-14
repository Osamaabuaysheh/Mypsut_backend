"""Create_Jobs_table

Revision ID: 7ee3d577056b
Revises: 31a73e0df269
Create Date: 2022-12-09 10:40:31.521964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee3d577056b'
down_revision = '31a73e0df269'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Jobs',
    sa.Column('job_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('college', sa.String(), nullable=False),
    sa.Column('job_responsanbilities', sa.String(), nullable=False),
    sa.Column('job_requierments', sa.String(), nullable=False),
    sa.Column('job_Deadline', sa.Date(), nullable=False),
    sa.Column('job_icon_image', sa.String(), nullable=False),
    sa.Column('job_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_index(op.f('ix_Jobs_job_id'), 'Jobs', ['job_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Jobs_job_id'), table_name='Jobs')
    op.drop_table('Jobs')
    # ### end Alembic commands ###

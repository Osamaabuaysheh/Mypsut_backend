"""Create Call Logs Table

Revision ID: e9ba09310653
Revises: ff6791101179
Create Date: 2023-01-02 10:41:01.808696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9ba09310653'
down_revision = 'ff6791101179'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CallLogsStudent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caller', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['caller'], ['students.student_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['receiver'], ['students.student_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_CallLogsStudent_id'), 'CallLogsStudent', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_CallLogsStudent_id'), table_name='CallLogsStudent')
    op.drop_table('CallLogsStudent')
    # ### end Alembic commands ###

"""create file_detail table

Revision ID: a4fd98c8762f
Revises: 
Create Date: 2022-06-14 23:33:58.787508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4fd98c8762f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_detail',
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=200), nullable=False),
    sa.Column('uploaded_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('file_id')
    )
    op.create_index(op.f('ix_file_detail_file_id'), 'file_detail', ['file_id'], unique=False)
    op.create_index(op.f('ix_file_detail_file_name'), 'file_detail', ['file_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_file_detail_file_name'), table_name='file_detail')
    op.drop_index(op.f('ix_file_detail_file_id'), table_name='file_detail')
    op.drop_table('file_detail')
    # ### end Alembic commands ###
"""add table userchat and relationships

Revision ID: eb90b8fd70c2
Revises: 295fd734fe70
Create Date: 2024-12-04 19:15:13.942747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb90b8fd70c2'
down_revision: Union[str, None] = '295fd734fe70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_chats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('auth_user', sa.Integer(), nullable=False),
    sa.Column('companion', sa.Integer(), nullable=False),
    sa.Column('last_message_id', sa.Integer(), nullable=True),
    sa.Column('last_message_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['auth_user'], ['users.id'], ),
    sa.ForeignKeyConstraint(['companion'], ['users.id'], ),
    sa.ForeignKeyConstraint(['last_message_id'], ['messages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_chats')
    # ### end Alembic commands ###
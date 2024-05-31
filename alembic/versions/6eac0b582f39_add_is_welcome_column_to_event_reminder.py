"""Add is_welcome column to event_reminder

Revision ID: 6eac0b582f39
Revises: 
Create Date: 2024-05-28 11:15:53.357958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6eac0b582f39'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Add the new column is_welcome to the event_reminder table
    op.add_column('event_reminders', sa.Column('is_welcome', sa.Boolean(), nullable=False, server_default=sa.false()))

def downgrade():
    # Remove the is_welcome column from the event_reminder table
    op.drop_column('event_reminders', 'is_welcome')
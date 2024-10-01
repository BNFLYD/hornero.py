"""Add full-text index to posts

Revision ID: a8c322d0ab37
Revises: 
Create Date: 2024-09-23 16:25:33.459777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8c322d0ab37'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        "CREATE INDEX IF NOT EXISTS posts_content_idx ON posts USING GIN (to_tsvector('simple', content));"
    )

def downgrade():
    op.execute("DROP INDEX IF EXISTS posts_content_idx;")
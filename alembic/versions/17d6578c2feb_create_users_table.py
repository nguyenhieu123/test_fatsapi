"""create users table

Revision ID: 17d6578c2feb
Revises: 
Create Date: 2022-04-11 12:22:00.419176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17d6578c2feb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
   
    op.create_table(
        'users',
        sa.Column('id', sa.Integer()),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password_hash', sa.String),
        sa.Column('created_at', sa.DateTime),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("users")


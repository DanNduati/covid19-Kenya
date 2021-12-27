"""change column data_type

Revision ID: 1c07321df2ef
Revises: 
Create Date: 2021-10-25 04:57:07.375817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c07321df2ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('data', 'new_cases_per_m',
               existing_type=sa.INTEGER(),
               type_=sa.FLOAT(),
               existing_nullable=True)


def downgrade():
    pass

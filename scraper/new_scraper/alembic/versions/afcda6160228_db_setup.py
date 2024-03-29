"""DB setup

Revision ID: afcda6160228
Revises: 
Create Date: 2022-01-01 01:24:57.317779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'afcda6160228'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('country_name', sa.String(length=5), nullable=False),
    sa.Column('total_cases', mysql.INTEGER(display_width=255), nullable=False),
    sa.Column('new_cases', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('total_deaths', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('new_deaths', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('total_recovered', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('new_recovered', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('active_cases', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('serious_cases', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('total_cases_per_m', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('deaths_per_m', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('total_tests', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('tests_per_m', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('population', mysql.INTEGER(display_width=255), nullable=True),
    sa.Column('new_cases_per_m', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###

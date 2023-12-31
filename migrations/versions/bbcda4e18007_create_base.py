"""create base

Revision ID: bbcda4e18007
Revises: 
Create Date: 2023-07-27 20:02:19.151164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbcda4e18007'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_number', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('adr', sa.Integer(), nullable=False),
    sa.Column('k', sa.Float(), nullable=False),
    sa.Column('no_connection_counter', sa.Boolean(), nullable=True),
    sa.Column('indikator_value', sa.Integer(), nullable=True),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('speed_line', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_dt', sa.DateTime(), nullable=True),
    sa.Column('updated_dt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('line_number'),
    sa.UniqueConstraint('name')
    )
    op.create_table('trends',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('temp_in_house', sa.Float(), nullable=True),
    sa.Column('temp_outdoor', sa.Float(), nullable=True),
    sa.Column('temp_heating_collector', sa.Float(), nullable=True),
    sa.Column('pressure_water_collector', sa.Float(), nullable=True),
    sa.Column('value_electricity_meter', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_role'), ['role'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_role'))

    op.drop_table('user')
    op.drop_table('trends')
    op.drop_table('lines')
    # ### end Alembic commands ###

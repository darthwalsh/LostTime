"""empty message

Revision ID: fd598f7e0a5e
Revises: 9e4b007acbe1
Create Date: 2017-05-20 13:58:58.264197

"""

# revision identifiers, used by Alembic.
revision = 'fd598f7e0a5e'
down_revision = '9e4b007acbe1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('type', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'type')
    ### end Alembic commands ###

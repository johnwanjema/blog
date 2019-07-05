"""blog migration update

Revision ID: 8a6e67fc9ea7
Revises: 9e3a96dd9ce9
Create Date: 2019-07-05 14:15:33.542137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a6e67fc9ea7'
down_revision = '9e3a96dd9ce9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('posted', sa.Time(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'posted')
    # ### end Alembic commands ###
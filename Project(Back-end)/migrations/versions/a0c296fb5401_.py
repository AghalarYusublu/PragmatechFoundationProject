"""empty message

Revision ID: a0c296fb5401
Revises: 58faf723ca01
Create Date: 2021-05-08 13:49:36.548433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0c296fb5401'
down_revision = '58faf723ca01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p_name', sa.String(length=100), nullable=True),
    sa.Column('p_price', sa.String(length=50), nullable=True),
    sa.Column('p_txt', sa.String(length=250), nullable=True),
    sa.Column('p_menu_pdf_url', sa.String(length=200), nullable=True),
    sa.Column('product_img', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###

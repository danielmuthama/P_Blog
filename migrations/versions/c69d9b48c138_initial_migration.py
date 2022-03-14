"""Initial Migration

Revision ID: c69d9b48c138
Revises: 1abb9b6805a5
Create Date: 2021-09-27 19:08:50.509710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c69d9b48c138'
down_revision = '1abb9b6805a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('comment')
    )
    op.add_column('blog', sa.Column('comments_blog', sa.String(), nullable=True))
    op.create_foreign_key(None, 'blog', 'comments', ['comments_blog'], ['comment'])
    op.drop_column('blog', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.drop_column('blog', 'comments_blog')
    op.drop_table('comments')
    # ### end Alembic commands ###

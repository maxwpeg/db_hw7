"""Insert olympics.

Revision ID: 45bd7025c7f3
Revises: 5f8d12ab4ce2
Create Date: 2024-10-30 19:51:12.501232
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "45bd7025c7f3"
down_revision: Union[str, None] = "5f8d12ab4ce2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        insert into public.olympics (olympic_id, country_id, city, year, startdate, enddate)
values  ('SYD2000', 'AUS', 'Sydney                                            ', 2000, '2000-09-15', '2000-10-01'),
        ('ATH2004', 'GRE', 'Athens                                            ', 2004, '2004-07-19', '2004-08-04');
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM public.olympics;")

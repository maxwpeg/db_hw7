"""Create tables.

Revision ID: 030ddd966fb8
Revises: 
Create Date: 2024-10-30 19:41:37.308645

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "030ddd966fb8"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        create table countries
(
    name       char(40),
    country_id char(3)
        primary key ,
    area_sqkm  integer,
    population integer
);

create table olympics
(
    olympic_id char(7)
        primary key,
    country_id char(3)
        references countries (country_id),
    city       char(50),
    year       integer,
    startdate  date,
    enddate    date
);

create table players
(
    name       char(40),
    player_id  char(10)
        primary key,
    country_id char(3)
        references countries (country_id),
    birthdate  date
);

create table events
(
    event_id            char(7)
        primary key,
    name                char(40),
    eventtype           char(20),
    olympic_id          char(7)
        references olympics (olympic_id),
    is_team_event       integer
        constraint events_is_team_event_check
            check (is_team_event = ANY (ARRAY [0, 1])),
    num_players_in_team integer,
    result_noted_in     char(100)
);

create table results
(
    result_id serial primary key,
    event_id  char(7)
        references events (event_id),
    player_id char(10)
        references players (player_id),
    medal     char(7),
    result    double precision
);
        """
    )

def downgrade() -> None:
    op.drop_table("results", if_exists=True)
    op.drop_table("teams", if_exists=True)
    op.drop_table("events", if_exists=True)
    op.drop_table("athletes", if_exists=True)
    op.drop_table("olympics", if_exists=True)
    op.drop_table("countries", if_exists=True)

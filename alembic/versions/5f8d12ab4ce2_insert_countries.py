"""Insert countries.

Revision ID: 5f8d12ab4ce2
Revises: 030ddd966fb8
Create Date: 2024-10-30 19:46:37.217281
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5f8d12ab4ce2"
down_revision: Union[str, None] = "030ddd966fb8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
insert into public.countries (name, country_id, area_sqkm, population)
values  ('Algeria                                 ', 'ALG', 2381741, 32853800),
        ('Argentina                               ', 'ARG', 2780400, 38747150),
        ('Australia                               ', 'AUS', 7682300, 21050000),
        ('Austria                                 ', 'AUT', 83858, 8189444),
        ('The Bahamas                             ', 'BAH', 13878, 323063),
        ('Barbados                                ', 'BAR', 430, 269556),
        ('Belarus                                 ', 'BLR', 207600, 9755106),
        ('Brazil                                  ', 'BRA', 8514877, 186404900),
        ('Bulgaria                                ', 'BUL', 110912, 7725965),
        ('Canada                                  ', 'CAN', 9970610, 33390141),
        ('China                                   ', 'CHN', 9596961, 1323324000),
        ('Cameroon                                ', 'CMR', 475442, 16321860),
        ('Costa Rica                              ', 'CRC', 51100, 4327228),
        ('Croatia                                 ', 'CRO', 56538, 4551338),
        ('Cuba                                    ', 'CUB', 110861, 11269400),
        ('Czech Republic                          ', 'CZR', 78866, 10403136),
        ('Denmark                                 ', 'DEN', 43094, 5471590),
        ('Dominican Republic                      ', 'DOM', 48671, 9365818),
        ('Eritrea                                 ', 'ERI', 117600, 4401357),
        ('Spain                                   ', 'ESP', 506030, 45200737),
        ('Estonia                                 ', 'EST', 45100, 1329697),
        ('Ethiopia                                ', 'ETH', 1104300, 77430700),
        ('Finland                                 ', 'FIN', 338145, 5302060),
        ('France                                  ', 'FRA', 551500, 60495540),
        ('United Kingdom                          ', 'GBR', 242900, 60776238),
        ('Germany                                 ', 'GER', 357022, 82689210),
        ('Greece                                  ', 'GRE', 131957, 11119890),
        ('Hungary                                 ', 'HUN', 93032, 10097730),
        ('Ireland                                 ', 'IRL', 70273, 4147901),
        ('Iceland                                 ', 'ISL', 103000, 309672),
        ('Italy                                   ', 'ITA', 301318, 58092740),
        ('Jamaica                                 ', 'JAM', 10991, 2650713),
        ('Japan                                   ', 'JPN', 377873, 128084700),
        ('Kazakhstan                              ', 'KAZ', 2724900, 14825110),
        ('Kenya                                   ', 'KEN', 580367, 34255720),
        ('Saudi Arabia                            ', 'KSA', 2149690, 24573100),
        ('Latvia                                  ', 'LAT', 64600, 2306988),
        ('Lithuania                               ', 'LTU', 65300, 3369600),
        ('Morocco                                 ', 'MAR', 446550, 31478460),
        ('Mexico                                  ', 'MEX', 1958201, 107029400),
        ('Mozambique                              ', 'MOZ', 801590, 19792300),
        ('Netherlands                             ', 'NED', 41528, 16423431),
        ('Nigeria                                 ', 'NGR', 923768, 131529700),
        ('Norway                                  ', 'NOR', 385155, 4751236),
        ('Poland                                  ', 'POL', 312685, 38529560),
        ('Portugal                                ', 'POR', 91982, 10494500),
        ('Romania                                 ', 'ROM', 238391, 21711470),
        ('South Africa                            ', 'RSA', 1221037, 47431830),
        ('Russia                                  ', 'RUS', 17098242, 143201600),
        ('Slovenia                                ', 'SLO', 20256, 2066814),
        ('Sri Lanka                               ', 'SRI', 65610, 20742910),
        ('Slovakia                                ', 'SVK', 49033, 5400908),
        ('Sweden                                  ', 'SWE', 449964, 9041262),
        ('Trinidad and Tobago                     ', 'TRI', 5130, 1305236),
        ('Turkey                                  ', 'TUR', 783562, 70586256),
        ('Ukraine                                 ', 'UKR', 603700, 46480700),
        ('United States                           ', 'USA', 9629091, 301140000),
        ('Zimbabwe                                ', 'ZIM', 390757, 13009530);"""
    )


def downgrade() -> None:
    op.execute("DELETE FROM public.countries;")

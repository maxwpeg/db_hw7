from datetime import datetime

import sqlalchemy.orm as orm

from sqlalchemy import ForeignKey

_mc = orm.mapped_column

_int = orm.Mapped[int]
_str = orm.Mapped[str]
_float = orm.Mapped[float]
_bool = orm.Mapped[bool]
_datetime = orm.Mapped[datetime]


class Base(orm.DeclarativeBase):
    type_annotation_map = {}


class Country(Base):
    __tablename__ = "countries"
    country_id: _str = _mc(primary_key=True)
    name: _str
    area_sqkm: _int
    population: _int


class Olympics(Base):
    __tablename__ = "olympics"
    olympic_id: _str = _mc(primary_key=True)
    country_id: _str = _mc(ForeignKey("countries.country_id"))
    city: _str
    year: _int
    startdate: _datetime
    enddate: _datetime


class Player(Base):
    __tablename__ = "players"
    player_id: _str = _mc(primary_key=True)
    name: _str
    birthdate: _datetime
    country_id: _str = _mc(ForeignKey("countries.country_id"))


class Event(Base):
    __tablename__ = "events"
    event_id: _str = _mc(primary_key=True)
    name: _str
    eventtype: _str
    olympic_id: _str = _mc(ForeignKey("olympics.olympic_id"))
    is_team_event: _bool
    num_players_in_team: _int
    result_noted_in: _str


class Result(Base):
    __tablename__ = "results"
    result_id: _int = _mc(primary_key=True)
    event_id: _str = _mc(ForeignKey("events.event_id"))
    player_id: _str = _mc(ForeignKey("players.player_id"))
    medal: _str
    result: _float

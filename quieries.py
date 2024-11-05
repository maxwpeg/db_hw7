import pprint
import tables
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import func, extract

DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres"

# Запрос 1: Подсчет количества игроков, родившихся в разных годах, которые выиграли золото
query_gold_by_birth_year = (
    sa.select(
        extract('year', tables.Player.birthdate).label('birth_year'),
        func.count(sa.distinct(tables.Player.player_id)).label('distinct_gold_players'),
        func.count().label('total_gold')
    )
    .select_from(tables.Player)
    .join(tables.Result, tables.Result.player_id == tables.Player.player_id)
    .filter(tables.Result.medal == 'GOLD')
    .group_by(extract('year', tables.Player.birthdate))
)

# Запрос 2: События, в которых минимум два золота в одиночных дисциплинах
query_single_event_gold = (    sa.select(tables.Event.event_id, tables.Event.name)
    .where(tables.Event.is_team_event == 0)    .where(
        sa.select(sa.func.count("*"))        .select_from(tables.Result)
        .where(tables.Result.medal == "GOLD")        .where(tables.Result.event_id == tables.Event.event_id)
        .scalar_subquery()        >= 2
    )
)

# Запрос 3: Уникальные игроки и их олимпийские события
query_player_event = (
    sa.select(
        sa.distinct(tables.Player.player_id),
        tables.Event.olympic_id
    )
    .join(tables.Result, sa.and_(
        tables.Result.player_id == tables.Player.player_id,
        tables.Result.medal.isnot(None)
    ))
    .join(tables.Event, tables.Event.event_id == tables.Result.event_id)
)

# Запрос 4: Страны с наибольшей долей спортсменов, чьи имена начинаются на гласную
query_country_vowel_athletes = (
    sa.select(sa.text("c_id"), sa.text("c_name"))
    .select_from(
        sa.select(
            tables.Country.country_id.label("c_id"),
            tables.Country.name.label("c_name"),
            sa.func.count("*").label("athletes_count"),
        )
        .join(tables.Player, tables.Player.country_id == tables.Country.country_id)
        .group_by(tables.Country.country_id)
        .subquery()
    )
    .join(tables.Player, tables.Player.country_id == sa.text("c_id"))
    .where(tables.Player.name.regexp_match(r"^[AOEIU]"))
    .group_by(sa.text("c_id"), sa.text("c_name"), sa.text("athletes_count"))
    .order_by(sa.desc(sa.func.count("*") / sa.text("athletes_count")))
    .limit(1)
)

# Запрос 5: Страны с наименьшей пропорцией медалей на душу населения в 2000 году
query_medals_per_population = (
    sa.select(
        tables.Country.name,
        (func.count() / tables.Country.population).label("medals_population_ratio")
    )
    .join(tables.Player, tables.Player.country_id == tables.Country.country_id)
    .join(
        tables.Result, sa.and_(
            tables.Result.player_id == tables.Player.player_id,
            tables.Result.medal.isnot(None)
        )
    )
    .join(tables.Event, tables.Event.event_id == tables.Result.event_id)
    .where(
        tables.Event.olympic_id == (
            sa.select(tables.Olympics.olympic_id)
            .where(tables.Olympics.year == '2000')
            .scalar_subquery()
        )
    )
    .group_by(tables.Country.country_id)
    .order_by(sa.asc('medals_population_ratio'))
    .limit(5)
)

engine = sa.create_engine(DB_URI)

queries = {
    "Gold by Birth Year": query_gold_by_birth_year,
    "Single Event Gold": query_single_event_gold,
    "Player Event": query_player_event,
    "Country Vowel Athletes": query_country_vowel_athletes,
    "Medals per Population": query_medals_per_population
}

def process_query_results(query_name, query, session):
    print(f"{query_name}")
    result = session.execute(query).all()
    pprint.pprint(result, compact=True)


with orm.Session(engine) as session:
    for query_name, query in queries.items():
        process_query_results(query_name, query, session)
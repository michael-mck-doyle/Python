import sqlalchemy
import pymysql
from pprint import pprint

# run a select statement on a db table and introduce the "WHERE" filter
engine = sqlalchemy.create_engine('mysql+pymysql://root:$C0d1nGPyth0N@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

# AND query
#query = sqlalchemy.select([film]).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating == "PG"))

# NOT query
#query = sqlalchemy.select([film]).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating != "PG"))

# OR query
query = sqlalchemy.select([film]).where(sqlalchemy.or_(film.columns.length > 60, film.columns.rating == "PG"))



result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
#result_set = result_proxy.fetchmany(5)
pprint(result_set)

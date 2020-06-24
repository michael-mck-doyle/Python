import sqlalchemy
import pymysql
from pprint import pprint

# run a select statement on a db table
engine = sqlalchemy.create_engine('mysql+pymysql://root:fidessa01@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([film]).order_by(sqlalchemy.asc(film.columns.replacement_cost))


#query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

#result_set = result_proxy.fetchall()
result_set = result_proxy.fetchmany(5)
pprint(result_set)



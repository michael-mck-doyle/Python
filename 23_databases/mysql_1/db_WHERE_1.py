import sqlalchemy
import pymysql
from pprint import pprint

# run a select statement on a db table and introduce the "WHERE" filter
engine = sqlalchemy.create_engine('mysql+pymysql://root:add_pwd@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'PENELOPE')
#query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
#result_set = result_proxy.fetchmany(5)
pprint(result_set)
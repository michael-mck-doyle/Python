import sqlalchemy
import pymysql
from pprint import pprint


# create a connection and return keys and metadata from a db table shown below
engine = sqlalchemy.create_engine('mysql+pymysql://root:fidessa01@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
print(actor.columns.keys())
print(repr(metadata.tables['actor']))
#connection = engine.drop


# run a select statement on a db table
engine = sqlalchemy.create_engine('mysql+pymysql://root:fidessa01@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

#result_set = result_proxy.fetchall()
result_set = result_proxy.fetchmany(5)
pprint(result_set)

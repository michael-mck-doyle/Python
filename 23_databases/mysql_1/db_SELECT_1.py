import sqlalchemy
import pymysql
from pprint import pprint

# run a select statement on a db table
engine = sqlalchemy.create_engine('mysql+pymysql://root:$C0d1nGPyth0N@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

#result_set = result_proxy.fetchall()
result_set = result_proxy.fetchmany(5)
pprint(result_set)

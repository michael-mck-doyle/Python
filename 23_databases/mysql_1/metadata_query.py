import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:$C0d1nGPyth0N@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

print(actor.columns.keys())
print(repr(metadata.tables['actor']))

print()
print(film.columns.keys())
print(repr(metadata.tables['film']))

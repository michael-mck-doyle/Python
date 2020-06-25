import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:add_pwd@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('salaries', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 100000)
results = connection.execute(query)
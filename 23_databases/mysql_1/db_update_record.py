import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:add_pwd@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('salaries', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(newTable).values(salary=100000).where(newTable.columns.Id == 1)

result = connection.execute(query)

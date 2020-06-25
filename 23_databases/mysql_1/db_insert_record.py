import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:$C0d1nGPyth0N@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newRecord = sqlalchemy.Table('salaries', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.insert(newRecord).values(Id=1, name='Joe', salary=60000.00, active=True)
result_proxy = connection.execute(query)

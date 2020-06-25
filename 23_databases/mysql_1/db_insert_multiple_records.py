import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:add_pwd@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newRecord = sqlalchemy.Table('salaries', metadata, autoload=True, autoload_with=engine)

# showing how to insert one record below
# query = sqlalchemy.insert(newRecord).values(Id=1, name='Joe', salary=60000.00, active=True)

# showing how to insert multiple records
query = sqlalchemy.insert(newRecord)
new_records = [{'Id':'2', 'name':'Janet', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'Fiona', 'salary':70000, 'active':True},
                {'Id':'4', 'name':'Bob', 'salary':170000, 'active':True}]
result_proxy = connection.execute(query, new_records)

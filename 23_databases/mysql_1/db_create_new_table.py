import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:add_pwd@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newSalaryTable = sqlalchemy.Table('salaries', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       sqlalchemy.Column('name', sqlalchemy.String(5), nullable=False),
                       sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
              )

metadata.create_all(engine)


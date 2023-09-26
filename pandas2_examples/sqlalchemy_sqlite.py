# You need to create the sqlite db first

from sqlalchemy import create_engine

engine = create_engine('sqlite:///dbs/titanic.db')

with engine.connect() as con:
    query = "SELECT * FROM titanic"
    result = con.execute(query)

    data = result.fetchall()

    for row in data:
        print(row)

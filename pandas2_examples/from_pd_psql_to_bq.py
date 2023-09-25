import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Create a connection using psycopg2
conn = psycopg2.connect(
    dbname="itba-dev",
    host="localhost",
    port="5432"
)

# Transform a SQL query into a DataFrame using pandas
sql = "SELECT * FROM titanic"
df = pd.read_sql(sql, conn)


# Create the BigQuery engine
engine = create_engine(
    'bigquery://itoa-dev-2/itba-dev'
)

# Write the DataFrame to a BigQuery table
df.to_sql('titanic_2', engine)

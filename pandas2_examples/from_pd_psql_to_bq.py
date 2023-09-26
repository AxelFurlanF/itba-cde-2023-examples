import pandas as pd
from sqlalchemy import create_engine

# create postgres engine
engine = create_engine('postgresql://:@localhost:5432/itba-dev')

# Transform a SQL query into a DataFrame using pandas
sql = "SELECT * FROM titanic"
df = pd.read_sql(sql, engine)


# Write the DataFrame to a BigQuery table
# this is very slow:
# Create the BigQuery engine
# engine = create_engine(
#     'bigquery://itoa-dev-2/itba_dev'
# )
# df.to_sql('titanic_2', engine, index=False, if_exists='replace')

# this is faster:
df.to_gbq('itba_dev.titanic_2', project_id='itoa-dev-2', if_exists='replace')

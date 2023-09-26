import pandas as pd
from sqlalchemy import create_engine

# read using pandas-gbq
df = pd.read_gbq("SELECT * FROM itba_dev.titanic", project_id='itoa-dev-2')

# create postgres engine
engine = create_engine('postgresql://:@localhost:5432/itba-dev')

df.to_sql('titanic', engine, index=False, if_exists='replace')

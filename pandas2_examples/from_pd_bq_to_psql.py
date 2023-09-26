import pandas as pd
from sqlalchemy import create_engine
import common_env as ce

# read using pandas-gbq
df = pd.read_gbq(f"SELECT * FROM {ce.DATASET_ID}.titanic", project_id=ce.PROJECT_ID)

# create postgres engine
engine = create_engine('postgresql://:@localhost:5432/itba-dev')

df.to_sql('titanic', engine, index=False, if_exists='replace')

# Needs to be running postgres db

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://:@localhost:5432/itba-dev')


def from_query_to_df(query):
    df = pd.read_sql(query, engine)
    return df


def from_df_to_db(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace')


if __name__ == "__main__":
    # read csv
    df = pd.read_csv('titanic.csv')
    # post to postgres
    from_df_to_db(df, 'titanic')

    # read back from postgres using query
    df = from_query_to_df("SELECT * FROM titanic")

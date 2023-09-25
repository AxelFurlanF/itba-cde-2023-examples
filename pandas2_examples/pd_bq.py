from google.cloud import bigquery


def read_chicago_taxi_data_with_df():
    client = bigquery.Client()

    # Construct a reference to the "chicago_taxi_trips" dataset
    dataset_ref = client.dataset("chicago_taxi_trips", project="bigquery-public-data")

    # Construct a reference to the "taxi_trips" table
    table_ref = dataset_ref.table("taxi_trips")

    # API request - fetch the table
    table = client.get_table(table_ref)

    # to pandas df
    return client.list_rows(table, max_results=10).to_dataframe()


def read_chicago_taxi_data_with_sql():
    client = bigquery.Client()
    query = 'SELECT * FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` LIMIT 10'

    df = client.query(query).to_dataframe()
    return df


if __name__ == "__main__":
    print(read_chicago_taxi_data_with_df())
    print(read_chicago_taxi_data_with_sql())

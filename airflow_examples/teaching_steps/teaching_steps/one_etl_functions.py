from sqlalchemy import create_engine
import requests
import pandas as pd
import os

REDSHIFT_CONN_STRING = f"redshift+psycopg2://pdateacher:{os.environ['REDSHIFT_PASSWORD']}@redshift-pda-cluster.cnuimntownzt.us-east-2.redshift.amazonaws.com:5439/pda"


def extract_data(output_parquet: str):
    # Fetch data from the API
    response = requests.get('https://dummy-json.mock.beeceptor.com/posts')
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    path = os.path.join(output_parquet, 'data.parquet')
    # Save to Parquet
    df.to_parquet(path)

    print(f"Data extracted and saved to {path}")
    return path


def transform_data(input_parquet: str, output_parquet: str):
    # Load data from Parquet
    df = pd.read_parquet(input_parquet)

    # Perform some transformations (e.g., filtering, adding columns)
    df_transformed = df[df['comment_count'] > 10]  # Example transformation

    path = os.path.join(output_parquet, 'transformed_data.parquet')
    # Save the transformed data to another Parquet file
    df_transformed.to_parquet(path, index=False)

    print(f"Data transformed and saved to {path}")
    return path


def load_to_redshift(transformed_parquet: str, redshift_table: str, redshift_conn_string: str):
    # Load transformed data from Parquet
    df = pd.read_parquet(transformed_parquet)

    # Create SQLAlchemy engine for Redshift
    engine = create_engine(redshift_conn_string)

    # Load data to Redshift table
    df.to_sql(redshift_table, engine, if_exists='replace', index=False, method='multi')

    print(f"Data loaded into Redshift table {redshift_table}")


def main(data_path: str, redshift_table: str, redshift_conn_string: str):
    output_path = extract_data(data_path)
    transformed_data_path = transform_data(output_path, data_path)
    load_to_redshift(transformed_data_path, redshift_table, redshift_conn_string)


if __name__ == "__main__":
    # current path
    data_path = os.path.dirname(os.path.realpath(__file__))
    main(data_path=data_path, redshift_table='example.example_table', redshift_conn_string=REDSHIFT_CONN_STRING)

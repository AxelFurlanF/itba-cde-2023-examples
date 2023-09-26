import pandas as pd
import gcsfs
import common_env as ce
from google.cloud import bigquery


FILEPATH = 'itba_bucket/titanic.parquet'


def read_csv():
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    return df


def load_df_file_into_gcs(df):
    fs = gcsfs.GCSFileSystem(project=ce.PROJECT_ID)

    # Make sure that the "gs://" prefix is removed for the FILEPATH in to_parquet.
    with fs.open(FILEPATH, 'wb') as f:
        df.to_parquet(f)


def load_parquet_into_bq():
    # Initialize a BigQuery client
    bq_client = bigquery.Client()

    # Construct a BigQuery job configuration object
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.PARQUET

    uri = 'gs://' + FILEPATH
    # Make an API request to start the BigQuery job
    load_job = bq_client.load_table_from_uri(uri, 'itba_dev_parquet_load.titanic', job_config=job_config)
    load_job.result()  # Wait for the job to complete


if __name__ == "__main__":
    df = read_csv()
    load_df_file_into_gcs(df)
    load_parquet_into_bq()

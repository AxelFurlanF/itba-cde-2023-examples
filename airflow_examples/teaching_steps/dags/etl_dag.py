import os
from datetime import datetime

import pandas as pd
import requests
from airflow import DAG
from airflow.exceptions import AirflowSkipException
from airflow.operators.python import PythonOperator
from sqlalchemy import create_engine

# Define constants
REDSHIFT_CONN_STRING = f"redshift+psycopg2://pdateacher:{os.environ['REDSHIFT_PASSWORD']}@redshift-pda-cluster.cnuimntownzt.us-east-2.redshift.amazonaws.com:5439/pda"
DATA_PATH = os.path.dirname(os.path.realpath(__file__))
REDSHIFT_TABLE = 'example_table'

# Define functions


def extract_data(**kwargs):
    output_parquet = kwargs['output_parquet']
    response = requests.get('https://dummy-json.mock.beeceptor.com/posts')
    data = response.json()
    df = pd.DataFrame(data)
    path = os.path.join(output_parquet, 'data.parquet')
    df.to_parquet(path)
    if df.empty:
        raise AirflowSkipException('No data to transform')
    return path


def transform_data(**kwargs):
    # XCOM: cross communication between tasks
    input_parquet = kwargs['ti'].xcom_pull(task_ids='extract_data')
    output_parquet = kwargs['output_parquet']
    df = pd.read_parquet(input_parquet)
    df_transformed = df[df['comment_count'] > 10]
    path = os.path.join(output_parquet, 'transformed_data.parquet')
    df_transformed.to_parquet(path, index=False)
    return path


def load_to_redshift(**kwargs):
    transformed_parquet = kwargs['ti'].xcom_pull(task_ids='transform_data')
    redshift_table = kwargs['redshift_table']
    redshift_conn_string = kwargs['redshift_conn_string']
    df = pd.read_parquet(transformed_parquet)
    engine = create_engine(redshift_conn_string)
    df.to_sql(redshift_table, engine, if_exists='replace', index=False, method='multi', schema='airflow')


# Define DAG
with DAG(
    'etl_redshift_dag',
    default_args={
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
    },
    description='ETL pipeline to extract, transform, and load data into Redshift',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Extract data
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        op_kwargs={'output_parquet': DATA_PATH},
    )

    # Task 2: Transform data
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_kwargs={'output_parquet': DATA_PATH},
    )

    # Task 3: Load data into Redshift
    load_task = PythonOperator(
        task_id='load_to_redshift',
        python_callable=load_to_redshift,
        op_kwargs={
            'redshift_table': REDSHIFT_TABLE,
            'redshift_conn_string': REDSHIFT_CONN_STRING,
        },
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task

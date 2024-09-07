from airflow import DAG
from airflow.operators.python import PythonOperator
from etl_functions import extract_data, transform_data, load_to_redshift
import os

DATA_PATH = os.path.dirname(os.path.realpath(__file__))

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

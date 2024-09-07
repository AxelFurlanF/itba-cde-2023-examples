from airflow import DAG
from datetime import datetime

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
    start_date=datetime(2024, 9, 4),
    catchup=True,
) as dag:
    pass  # We will add tasks in the next step

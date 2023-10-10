from datetime import timedelta
from airflow import DAG
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStorageObjectSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
with DAG(
    'google_cloud_storage_sensor_dag',
    default_args=default_args,
    description='A simple DAG with Google Cloud Storage sensor',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    kickoff_dag = DummyOperator(
        task_id="kickoff_dag"
    )

    check_gcs_file_sensor = GoogleCloudStorageObjectSensor(
        task_id='check_gcs_file_sensor',
        bucket='your-gcs-bucket',
        object='your-gcs-object',
        google_cloud_conn_id='google_cloud_default'
    )

    proceed_after_gcs_object = DummyOperator(
        task_id="proceed_after_gcs_object"
    )

    kickoff_dag >> check_gcs_file_sensor >> proceed_after_gcs_object

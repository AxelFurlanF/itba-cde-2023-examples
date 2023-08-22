from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.http_sensor import HttpSensor

# Define the default_args dictionary
default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 1, 1),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# Instantiate the DAG
with DAG(
    dag_id="my_http_sensor_dag",
    description="DAG with HttpSensor",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    kickoff_dag = DummyOperator(
        task_id="kickoff_dag"
    )

    api_available = HttpSensor(
        task_id='http_sensor',
        http_conn_id='http_default',
        endpoint='/',
        method='GET',
        response_check=lambda response: response.status_code == 200,
        poke_interval=5,
        timeout=20,
    )

    proceed_after_api = DummyOperator(
        task_id="proceed_after_api"
    )

    kickoff_dag >> api_available >> proceed_after_api

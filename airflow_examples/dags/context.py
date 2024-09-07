import datetime as dt
import pprint
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_context(**context):
    pprint.pprint(context)


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 3, 20),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

with DAG('dag_using_context',
         default_args=default_args,
         schedule_interval='0 * * * *',
         catchup=True
         ) as dag:

    print_date = PythonOperator(
        task_id='print_context',
        python_callable=print_context,
        provide_context=True,  # makes sure **context is provided to the function
    )

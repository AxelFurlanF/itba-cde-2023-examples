import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_dates(**context):
    print('data_interval_start: ', context['data_interval_start'])
    print('data_interval_end: ', context['data_interval_end'])
    print('execution_date: ', context['execution_date'])


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2024, 9, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

with DAG('data_intervals_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=True
         ) as dag:

    print_date = PythonOperator(
        task_id='print_dates',
        python_callable=print_dates,
        provide_context=True,
    )

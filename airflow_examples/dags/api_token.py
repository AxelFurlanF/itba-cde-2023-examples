import datetime as dt
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator


def print_var():
    token = Variable.get('API_TOKEN')
    # write token to file
    with open('/tmp/token.txt', 'w') as f:
        f.write(token)


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 3, 20),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

with DAG('dag_using_secrets',
         default_args=default_args,
         schedule_interval='0 * * * *',
         catchup=True
         ) as dag:

    print_date = PythonOperator(
        task_id='print_var',
        python_callable=print_var,
    )

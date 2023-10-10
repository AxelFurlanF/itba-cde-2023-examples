# Importing necessary libraries

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Defining the Python functions that constitute our tasks


def print_hello():
    print('Hola gente de PDA 2023!')


def print_text():
    print('Airflow esta bueno!')

# Establish the default arguments for the DAG


default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple DAG with two tasks',
    schedule_interval=timedelta(days=1),
)

# Define the tasks

task1 = PythonOperator(
    task_id='task1',
    python_callable=print_hello,
    dag=dag,
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=print_text,
    dag=dag,
)

# Set the order of the tasks

task1 >> task2  # task2 is dependent on task1

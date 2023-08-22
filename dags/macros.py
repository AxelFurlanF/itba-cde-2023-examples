import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define some variables that will be templated
filename = "/tmp/exec_date_{{ ds_nodash }}.txt"
bash_command = "echo '{{ ds }}' > " + filename

# Defaults for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 10, 1),
}

# Define the DAG
with DAG('my_jinja_dag', default_args=default_args, schedule_interval='@daily') as dag:

    t1 = BashOperator(
        task_id="write_date",
        bash_command=bash_command,
    )

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Functions used in the DAG

# ti - task instance


def push_to_xcom(**context):
    data_to_push = 'Data pushed to XCom'
    context['ti'].xcom_push(key='my_key', value=data_to_push)


def pull_from_xcom(**context):
    data_pulled = context['ti'].xcom_pull(key='my_key')
    print(f'Data pulled from XCom: {data_pulled}')


# Default arguments
args = {
    'start_date': days_ago(1)
}

# Instantiate a DAG
with DAG('xcom_dag', schedule_interval="@daily", default_args=args, catchup=False) as dag:
    push_task = PythonOperator(
        task_id='push_to_xcom',
        python_callable=push_to_xcom,
        provide_context=True
    )

    pull_task = PythonOperator(
        task_id='pull_from_xcom',
        python_callable=pull_from_xcom,
        provide_context=True
    )

    push_task >> pull_task

from datetime import timedelta
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Start by defining the DAG
dag = DAG(
    'run_kubernetes_pod',
    default_args=default_args,
    description='A simple Ubuntu pod in using KubernetesPodOperator',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
)

# Define the KubernetesPodOperator task
run_pod = KubernetesPodOperator(
    task_id='<TASK_ID>',
    name='run-pod',
    namespace='<NAMESPACE>',
    image='ubuntu:16.04',
    cmds=["bash", "-cx"],
    arguments=["echo", "10", "do_stuff"],
    in_cluster=True,
    get_logs=True,
    dag=dag
)

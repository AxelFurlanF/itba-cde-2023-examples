from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago


print("esto no debería estar aca")


def decide_which_path():
    # return 'branch_a' or 'branch_b' depending on the weekday
    return 'branch_a' if (days_ago(1).weekday() < 5) else 'branch_b'


dag = DAG(
    dag_id='branch_operator_example',
    schedule_interval="@daily",
    start_date=days_ago(2),
    default_args={'owner': 'airflow'},
)

branch = BranchPythonOperator(
    task_id='branch_task',
    python_callable=decide_which_path,
    dag=dag,
)

branch_a = DummyOperator(
    task_id='branch_a',
    dag=dag,
)

branch_b = DummyOperator(
    task_id='branch_b',
    dag=dag,
)

join = DummyOperator(
    task_id='join',
    dag=dag,
    trigger_rule='one_success',
)

branch >> [branch_a, branch_b] >> join

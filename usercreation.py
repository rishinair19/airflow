#!/usr/bin/python3
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'retries': 10,
    'concurrency': 1
}

dag = DAG(
    dag_id=user_creation,
    default_args=default_args,
)

user_create = BashOperator(task_id='user_create_1',
                         bash_command="airflow users create --username Rishi --firstname Rishi --lastname Nair --role Admin --email rishi.nair@deepintent.com --password rishi",
                         dag=dag)
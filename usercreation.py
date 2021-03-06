#!/usr/bin/python3
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

my_dag_id = "user_creation"

default_args = {
    'retries': 10,
    'concurrency': 1

}

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2022, 6, 9),
    schedule_interval='@once'
)

user_create = BashOperator(task_id='user_create_1',
                         bash_command="airflow users create \
                                        --username Rishi4 \
                                        --firstname Rishi4 \
                                        --lastname N \
                                        --role Admin \
                                        --email admin3@example.org \
                                        --password password123",
                         dag=dag)


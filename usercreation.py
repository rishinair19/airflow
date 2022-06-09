from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime
from airflow import DAG

t2 = BashOperator(
    task_id='user_create',
    bash_command='airflow users create --username Rishi --firstname Rishi --lastname Nair --role Admin --email rishi.nair@deepintent.com --password rishi',
    retries=3,
    dag=dag)
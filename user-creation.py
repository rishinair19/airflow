from airflow.operators.bash_operator import BashOperator
from datetime import timedelta, datetime
from airflow import DAG

user_create = BashOperator(
    task_id='user_creation',
    bash_command='airflow users create --username Rishi --firstname Rishi --lastname Nair --role Admin --email rishi.nair@deepintent.com --password rishi'
)
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime
from airflow import DAG

user_creation = 'airflow users create --username Rishi --firstname Rishi --lastname Nair --role Admin --email rishi.nair@deepintent.com --password rishi'

user_creation_airflow = BashOperator(
   task_id='user_create', 
   bash_command=user_creation,
   dag=user_creation_airflow,
)
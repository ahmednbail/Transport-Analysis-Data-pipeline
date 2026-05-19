from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator


DBT_CLOUD_CONN_ID = 'dbt-cloud'
DBT_CLOUD_JOB_ID = 70506183131891 


with DAG(
    dag_id= 'dbt-dag',
    start_date= datetime(2026,5,16),
    schedule= '@daily',
    catchup= False,
    default_args={
        'owner': 'Ahmed Nabil',
        'retries': 3,
        'retry_delay': timedelta(minutes=1),
        'depends_on_past': False,
    },
    tags= ['dbt', 'data-pipeline']

) as dag: 
           dbt_run=DbtCloudRunJobOperator(
               task_id='dbt-run',
               conn_id=DBT_CLOUD_CONN_ID,
               job_id=DBT_CLOUD_JOB_ID,
           )
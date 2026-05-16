from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator


DBT_CLOUD_CONN_ID = 'dbt-cloud'
DBT_CLOUD_JOB_ID = '1'


with DAG(
    dage_id= 'dbt-dag',
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
            pass
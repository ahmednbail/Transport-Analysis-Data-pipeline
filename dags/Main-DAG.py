from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from upload import run as upload

with DAG(
    dag_id='pipeline_for_yellow_taxi',
    start_date=datetime(2026,5,14),
    schedule='@monthly',
    catchup=False
) as dag:
    
   pass

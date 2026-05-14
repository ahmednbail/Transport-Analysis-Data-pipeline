from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

POSTGRES_CONN_ID= 'PostgreSQL_connection'
GCS_BUCKET= '######'# bucket name فقط
GCS_PATH = "#####"          # folder داخل الباكت
GCS_FILENAME = "######"
BIGQUERY_DATASET = "#######"
BIGQUERY_TABLE = "#######"



with DAG(
    dag_id='pipeline_for_yellow_taxi',
    start_date=datetime(2026,5,14),
    schedule='@daily',
    catchup=False,
    default_args={
        'retries':1,
        'retry_delay':timedelta(minutes=1),
    },
    tags=['Data-Pipeline', 'Yellow-Taxi']
) as dag:
    
   pass

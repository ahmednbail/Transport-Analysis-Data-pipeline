from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.providers.google.cloud.hooks.gcs import GCSHook

POSTGRES_CONN_ID= 'PostgreSQL_connection'
GCS_BUCKET= 'transport-analysis'# bucket name فقط
GCS_PATH = "Yellow_Taxi"          # folder داخل الباكت
GCS_FILENAME = "ny-yellow-taxi-trips.json"
BIGQUERY_DATASET = "transport"
BIGQUERY_TABLE = "yellow_tripdata"
PROJECT_ID = "transport-analysis-496017"
GCP_CONN_ID = "gcp"

with DAG(
    dag_id='pipeline_for_yellow_taxi',
    start_date=datetime(2026,5,14),
    schedule='@daily',
    catchup=False,
    default_args={
        'owner':'Ahmed Nabil',
        'retries':2,
        'depends_on_past':False,
    },
    tags=['Data-Pipeline', 'Yellow-Taxi']
) as dag:

    def test_connections():
            # Test Postgres
            pg = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
            pg.get_conn()
            print("Postgres connected")

            # Test GCS
            gcs = GCSHook(gcp_conn_id=GCP_CONN_ID)
            gcs.list(GCS_BUCKET)
            print("GCS connected")

    verify_connections = PythonOperator(
        task_id='verify_connections',
        python_callable=test_connections,
    )

       
    extract_yellow_taxi_data = PostgresToGCSOperator(
        task_id='extract_yellow_taxi_data',
        postgres_conn_id=POSTGRES_CONN_ID,
        sql="SELECT * FROM yellow_taxi_trips",
        bucket=GCS_BUCKET,
        filename=GCS_PATH + "/" + GCS_FILENAME ,
        export_format = 'json',
        gcp_conn_id=GCP_CONN_ID
    )

    load_to_bigquery = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket=GCS_BUCKET,
        source_objects=[GCS_PATH + "/" + GCS_FILENAME],
        destination_project_dataset_table=PROJECT_ID + "." + BIGQUERY_DATASET + "." + BIGQUERY_TABLE,
        source_format='NEWLINE_DELIMITED_JSON',
        write_disposition='WRITE_TRUNCATE',
        create_disposition='CREATE_IF_NEEDED',
        autodetect=True,
        gcp_conn_id=GCP_CONN_ID
    )
    

    verify_connections >> extract_yellow_taxi_data >> load_to_bigquery

        

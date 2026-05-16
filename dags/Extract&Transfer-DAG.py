from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.google.cloud.hooks.gcs import GCSHook

POSTGRES_CONN_ID= 'PostgreSQL_connection'
GCS_BUCKET= 'transport-analysis'# bucket name فقط
GCS_PATH = "Yellow_Taxi/{{ ds_nodash }}"          # folder داخل الباكت
GCS_FILENAME = "ny-yellow-taxi-trips-{}.csv"
BIGQUERY_SOURCE_OBJECT = GCS_PATH + "/ny-yellow-taxi-trips-*.csv"
BIGQUERY_DATASET = "transport"
BIGQUERY_TABLE = "yellow_tripdata"
PROJECT_ID = "transport-analysis-496017"
GCP_CONN_ID = "gcp"

TAXI_COLUMNS = [
    "VendorID",
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "RatecodeID",
    "store_and_fwd_flag",
    "PULocationID",
    "DOLocationID",
    "payment_type",
    "fare_amount",
    "extra",
    "mta_tax",
    "tip_amount",
    "tolls_amount",
    "improvement_surcharge",
    "total_amount",
    "congestion_surcharge"
]

POSTGRES_SELECT_COLUMNS = ",".join(f'"{column}"' for column in TAXI_COLUMNS)

BIGQUERY_SCHEMA_FIELDS = [
    {"name": "VendorID", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "tpep_pickup_datetime", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "tpep_dropoff_datetime", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "passenger_count", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "trip_distance", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "RatecodeID", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "store_and_fwd_flag", "type": "STRING", "mode": "NULLABLE"},
    {"name": "PULocationID", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "DOLocationID", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "payment_type", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "fare_amount", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "extra", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "mta_tax", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "tip_amount", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "tolls_amount", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "improvement_surcharge", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "total_amount", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "congestion_surcharge", "type": "FLOAT", "mode": "NULLABLE"}
]

with DAG(
    dag_id='pipeline_for_yellow_taxi',
    start_date=datetime(2026,5,14),
    schedule='@daily',
    catchup=False,
    default_args={
        'owner':'Ahmed Nabil',
        'retries':3,
        'retry_delay': timedelta(minutes=1),
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
        sql=f"SELECT {POSTGRES_SELECT_COLUMNS} FROM yellow_taxi_data",
        bucket=GCS_BUCKET,
        filename=GCS_PATH + "/" + GCS_FILENAME,
        export_format='csv',
        field_delimiter=',',
        approx_max_file_size_bytes= 10 * 1024 * 1024,
        gcp_conn_id=GCP_CONN_ID
    )

    load_to_bigquery = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket=GCS_BUCKET,
        source_objects=[BIGQUERY_SOURCE_OBJECT],
        destination_project_dataset_table=PROJECT_ID + "." + BIGQUERY_DATASET + "." + BIGQUERY_TABLE,
        source_format='CSV',
        field_delimiter=',',
        schema_fields=BIGQUERY_SCHEMA_FIELDS,
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE',
        create_disposition='CREATE_IF_NEEDED',
        gcp_conn_id=GCP_CONN_ID
    )
    

    verify_connections >> extract_yellow_taxi_data >> load_to_bigquery


        

from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator


DBT_CLOUD_CONN_ID = 'dbt-cloud'
DBT_CLOUD_JOB_ID = 70506183131891


with DAG(
    dag_id='dbt-dag',
    start_date=datetime(2026, 5, 16),
    schedule=None,
    catchup=False,
    default_args={
        'owner': 'Ahmed Nabil',
        'retries': 2,
        'retry_delay': timedelta(minutes=1),
        'depends_on_past': False,
    },
    tags=['dbt', 'data-pipeline'],
) as dag:

    @task
    def check_dbt_connection():
        from airflow.providers.dbt.cloud.hooks.dbt import DbtCloudHook

        hook = DbtCloudHook(dbt_cloud_conn_id=DBT_CLOUD_CONN_ID)
        account_id = hook.connection.login
        response = hook._run_and_get_response(endpoint=f"{account_id}/")
        data = response.json()
        if data["status"]["is_success"]:
            print(f"Connected to dbt Cloud account: {data['data']['name']}")
        else:
            raise Exception(f"Connection failed: {data['status']['user_message']}")

    dbt_run = DbtCloudRunJobOperator(
        task_id='dbt-run',
        dbt_cloud_conn_id=DBT_CLOUD_CONN_ID,
        job_id=DBT_CLOUD_JOB_ID,
    )

    check_dbt_connection() >> dbt_run

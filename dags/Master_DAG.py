from airflow import DAG 
from datetime import datetime, timedelta
from airflow.providers.standard.operators.trigger_dagrun.TriggerDagRunOperator import TriggerDagRunOperator


with DAG(
    dag_id="Master_DAG",
    start_date=datetime(2026, 5, 16),
    schedule=None,
    catchup=False,
    default_args={
        "owner": "Ahmed Nabil",
        "retries": 2,
        "retry_delay": timedelta(minutes=1),
        "depends_on_past": False,
    }
) as dag:
    


    trigger_extraction_dag = TriggerDagRunOperator(
        task_id="trigger_extraction_dag",
        trigger_dag_id="pipeline_for_yellow_taxi",
    )

    trigger_dbt_dag = TriggerDagRunOperator(
        task_id="trigger_dbt_dag",  
        trigger_dag_id="dbt-dag",
    )

    trigger_extraction_dag >> trigger_dbt_dag
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.sql import SQLCheckOperator, SQLValueCheckOperator

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "airflow",
    "conn_id": "postgres_default"
}


with DAG(
    dag_id="Sprin4_Task1",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
    ) as dag:
 
    sql_check = SQLCheckOperator(task_id='user_order_log_isNull', sql='user_order_log_isNull_check.sql')
    sql_check2 = SQLCheckOperator(task_id='user_activity_log_isNull', sql="user_activity_log_isNull_check.sql")
    
    sql_check >> sql_check2

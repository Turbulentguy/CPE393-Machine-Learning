import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_manipulate import data_manipulate

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 10),
    'retries': 1,
}

# Define DAG
with DAG(
    'TBA_MLOps_Dag',
    default_args=default_args,
    schedule='0 0 * * *',  
    catchup=False,
    tags=['example'],
) as dag:

    start = EmptyOperator(task_id='start')

    data_manipulate = PythonOperator(
        task_id='data_manipulate',
        python_callable=data_manipulate
    )

    end = EmptyOperator(task_id='end')

    # Task Flow
    start >> data_manipulate >> end
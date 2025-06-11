from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task 1: Preprocess data
def preprocess_data():
    print("Preprocessing data")

# Task 2: Train model
def train_model():
    print("Training model")

# Task 3: Evaluate model
def evaluate_model():
    print("Evaluating model")

# Define the DAG
with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",  # Updated for Airflow 2.9+
    catchup=False,
    description="A basic ML pipeline DAG using Astro"
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model
    )

    var = preprocess >> train >> evaluate

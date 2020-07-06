from datetime import datetime
from airflow import DAG
from airflow.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.kubernetes_pod import KubernetesPodOperator
def print_hello():
    return 'Hello world!'

dag = DAG('hello_world', description='Hello to  DAG',
          schedule_interval='* * * * *',
          start_date=datetime(2020, 7, 6), catchup=False)

kubernetes_pod_operator = KubernetesPodOperator(task_id='dummy_task', retries=3, dag=dag)

kubernetes_pod = KubernetesPodOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

kubernetes_pod_operator >> kubernetes_pod

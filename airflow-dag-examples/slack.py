from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
SLACK_CONN_ID = 'https://hooks.slack.com/services'
def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    slack_msg = """
            :red_circle: Task Failed. 
            *Task*: {task}  
            *Dag*: {dag} 
            *Execution Time*: {exec_date}  
            *Log Url*: {log_url} 
            """.format(
            task=context.get('task_instance').task_id,
            dag=context.get('task_instance').dag_id,
            ti=context.get('task_instance'),
            exec_date=context.get('execution_date'),
            log_url=context.get('task_instance').log_url,
        )
    failed_alert = SlackWebhookOperator(
        task_id='slack_test',
        http_conn_id='airflow-slack',
        webhook_token=slack_webhook_token,
        message=slack_msg,
        username='admin')
    return failed_alert.execute(context=context)

default_args = {
    'owner': 'admin',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 0,
    'on_failure_callback': task_fail_slack_alert
}
dag = DAG(
    dag_id=DAG_NAME,
    default_args=default_args,
    schedule_interval=schedule_interval,
)

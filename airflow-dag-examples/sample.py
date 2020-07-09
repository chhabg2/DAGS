from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

slack_msg="Hi Wssup?"

slack_test =  SlackWebhookOperator(
    task_id='slack_test',
    http_conn_id='slack',
    webhook_token='/1234/abcd',
    message=slack_msg,
    channel='airflow_slack',
    username='airflow_'+os.environ['ENVIRONMENT'],
    icon_emoji=None,
    link_names=False,
    dag=dag)

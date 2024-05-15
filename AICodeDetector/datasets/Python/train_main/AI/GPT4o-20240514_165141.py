
    task_id = context['task_instance'].xcom_pull(task_ids='your_task_id')
    result = AsyncResult(task_id)
    return result.ready()

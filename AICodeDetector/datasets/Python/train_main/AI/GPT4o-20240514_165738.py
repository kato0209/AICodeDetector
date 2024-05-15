

    try:
        waiter = client.get_waiter('task_ended')
        waiter.wait(TaskId=task_id)
    except botocore.exceptions.WaiterError:
        # Exponential backoff
        max_attempts = 10
        base_delay = 1  # starting delay in seconds
        for attempt in range(max_attempts):
            try:
                response = client.describe_tasks(TaskIds=[task_id])
                if response['Tasks'][0
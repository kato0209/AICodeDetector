
    """
    Takes task_instances, which should have been set to queued, and enqueues them
    with the executor.

    :param simple_task_instances: TaskInstances to enqueue
    :type simple_task_instances: list[SimpleTaskInstance]
    :param simple_dag_bag: Should contains all of the task_instances' dags
    :type simple_dag_bag: airflow.utils.dag_processing.SimpleDagBag
    """
    for simple_task_instance in simple_task_instances:
        dag = simple_d
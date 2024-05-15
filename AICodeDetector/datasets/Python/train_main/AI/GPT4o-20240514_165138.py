
    """
    Returns all task reschedules for the task instance and try number,
    in ascending order.

    :param task_instance: the task instance to find task reschedules for
    :type task_instance: airflow.models.TaskInstance
    """

    return session.query(TaskReschedule).filter(
        TaskReschedule.dag_id == task_instance.dag_id,
        TaskReschedule.task_id == task_instance.task_id,
        TaskReschedule.execution_date == task_instance.execution_date,
        TaskReschedule.try
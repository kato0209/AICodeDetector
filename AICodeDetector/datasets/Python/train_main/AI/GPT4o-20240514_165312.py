

    """
    Sets tasks instances to skipped from the same dag run.

    :param dag_run: the DagRun for which to set the tasks to skipped
    :param execution_date: execution_date
    :param tasks: tasks to skip (not task_ids)
    :param session: db session to use
    """
    if session is None:
        session = provide_session()

    task_ids = [task.task_id for
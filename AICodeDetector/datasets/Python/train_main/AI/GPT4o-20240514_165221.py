
    """
    Verifies the DagRun by checking for removed tasks or tasks that are not in the
    database yet. It will set state to removed or add the task if required.
    """

    if session is None:
        session = Session()

    # Get the current tasks in the DAG
    current_task_ids = {task.task_id for task in self.dag.tasks}

    # Get the task instances from the database
    tis = session.query
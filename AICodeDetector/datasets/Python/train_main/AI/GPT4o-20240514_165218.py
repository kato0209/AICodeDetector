
    """
    Returns the task instances for this dag run
    """

    @provide_session
        query = session.query(TaskInstance).filter(TaskInstance.dag_id == self.dag_id, TaskInstance.execution_date == self.execution_date)
        if state:
            query = query.filter(TaskInstance.state == state)
        return query.all()

    return _get_task_instances(session=session)

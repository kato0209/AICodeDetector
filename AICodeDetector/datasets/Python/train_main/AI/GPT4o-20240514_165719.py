

    for dag_run in dag_runs:
        unfinished_tasks = session.query(TaskInstance).filter(
            TaskInstance.dag_id == dag_run.dag_id,
            TaskInstance.execution_date == dag_run.execution_date,
            TaskInstance.state.in_([State.NONE, State.SCHEDULED, State.QUEUED, State.RUNNING])
        ).all()

        if unfinished_tasks:
           
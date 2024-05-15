
    """
    This method schedules the tasks for a single DAG by looking at the
    active DAG runs and adding task instances that should run to the
    queue.
    """

    # Get active DAG runs
    dag_runs = session.query(DagRun).filter(
        DagRun.dag_id == dag.dag_id,
        DagRun.state == State.RUNNING
    ).all()

    for dag_run in dag_runs:
        # Get task
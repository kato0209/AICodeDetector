

    """
    Clears a set of task instances, but makes sure the running ones
    get killed.

    :param tis: a list of task instances
    :param session: current session
    :param activate_dag_runs: flag to check for active dag run
    :param dag: DAG object
    """
    if not tis:
        return

    task_ids = [ti.task_id for ti in tis]
    dag_ids
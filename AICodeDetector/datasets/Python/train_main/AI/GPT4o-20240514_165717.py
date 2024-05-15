
    """
    Returns a map of task instance key to task instance object for the tasks to
    run in the given dag run.

    :param dag_run: the dag run to get the tasks from
    :type dag_run: airflow.models.DagRun
    :param session: the database session object
    :type session: sqlalchemy.orm.session.Session
    """

    task_instances = (
        session.query(TaskInstance)
        .filter(TaskInstance.dag_id == dag_run.dag_id
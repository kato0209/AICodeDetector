
    """
    Wrapper around the private _get_dep_statuses method that contains some global
    checks for all dependencies.

    :param ti: the task instance to get the dependency status for
    :type ti: airflow.models.TaskInstance
    :param session: database session
    :type session: sqlalchemy.orm.session.Session
    :param dep_context: the context for which this dependency should be evaluated for
    :type dep_context: DepContext
    """
    # Perform any global checks here
    if not ti.are_dependencies_met
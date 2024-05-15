

    """
    Helper method that set dag run state in the DB.
    :param dag_id: dag_id of target dag run
    :param execution_date: the execution date from which to start looking
    :param state: target state
    :param session: database session
    """
    if session is None:
        raise ValueError("A valid session must be provided")

    dag_run = session
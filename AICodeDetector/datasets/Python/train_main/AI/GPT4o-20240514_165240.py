
    """
    Refreshes the task instance from the database based on the primary key

    :param lock_for_update: if True, indicates that the database should
        lock the TaskInstance (issuing a FOR UPDATE clause) until the
        session is committed.
    """
    if session is None:
        session = provide_session()

    query = session.query(self.__class__).filter_by(
        dag_id=self.dag_id,
        task_id=self.task_id,
        execution_date=self.execution_date

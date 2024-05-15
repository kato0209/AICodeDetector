

    if session is None:
        session = Session()

    # Find the DagRun for the given execution date
    dag_run = session.query(DagRun).filter(
        DagRun.dag_id == dag.dag_id,
        DagRun.execution_date == execution_date
    ).first()

    if not dag_run:
        return []

    # Set the state of the DagRun to running
   


    if session is None:
        session = Session()

    try:
        # Delete TaskInstances
        session.query(TaskInstance).filter(TaskInstance.dag_id == dag_id).delete()

        # Delete DagRuns
        session.query(DagRun).filter(DagRun.dag_id == dag_id).delete()

        # Optionally delete logs
        if not keep_records_in_log:
            session.query(Log).filter(Log.d

    # TODO(edgarRd): AIRFLOW-1444: Add consistency check on counts
    with create_session() as session:
        count = (
            session.query(DagRun)
           .filter(
                DagRun.dag_id == dag_id,
                DagRun.execution_date == execution_date,
                DagRun.state == state,
            )
          
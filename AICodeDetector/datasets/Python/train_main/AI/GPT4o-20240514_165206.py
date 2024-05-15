

    dagbag = DagBag()
    dag = dagbag.get_dag(dag_id)
    if not dag:
        raise ValueError(f"DAG with id {dag_id} not found")

    execution_date = timezone.utcnow()
    dag_run = DagRun(
        dag_id=dag_id,
        execution_date=execution_date,
        state=State.RUNNING,
        run_id=f"manual__{execution_date.isoformat()}",
    )
   
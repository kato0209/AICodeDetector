
        session = session or settings.Session()

        # update the state of the previously active dag runs
        dag_runs = DagRun.find(dag_id=dag.dag_id, state=State.RUNNING, session=session)
        active_dag_runs = []
        for run in dag_runs:
            self.log.info("Examining DAG run %s", run)
            # don't consider runs that are executed in the future
            if run.execution_date > timezone.utcnow():
             
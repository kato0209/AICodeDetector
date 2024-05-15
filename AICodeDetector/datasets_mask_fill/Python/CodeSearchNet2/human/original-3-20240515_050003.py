
        for dag_run in dag_runs:
            dag_run.update_state()
            if dag_run.state not in State.finished():
                dag_run.set_state(State.FAILED)
            session.merge(dag_run)
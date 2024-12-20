
    dag = dagbag.get_dag(dag_id)
    task = dag.get_task(task_id)
    return {
        "dag_id": dag_id,
        "task_id": task_id,
        "execution_date": getattr(task, "execution_date", None),
        "task_type": task.task_type,
        "start_date": task.start_date,
        "end_date": task.end_date,
        "duration": task.duration,
    }


def get_run_state(dag, execution_date):
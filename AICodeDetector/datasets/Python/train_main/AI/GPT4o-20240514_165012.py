

    dag_bag = DagBag()
    dag = dag_bag.get_dag(dag_id)
    if dag is None:
        return None
    task = dag.get_task(task_id)
    if task is None:
        return None
    execution_date = datetime.strptime(execution_date, '%Y-%m-%d')
    task_instance = TaskInstance(task, execution_date)
    task_instance.refresh_from_db()
    return task_instance.state


    dag_bag = DagBag()
    dag = dag_bag.get_dag(dag_id)
    task = dag.get_task(task_id)
    
    task_info = {var: getattr(task, var) for var in vars(task) if not var.startswith('_')}
    
    return json.dumps(task_info, default=str)

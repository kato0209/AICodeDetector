
    metrics = {}
    for arg in func_name.split("."):
        arg = arg.strip()
        if arg.startswith("dag_id"):
            metrics["dag_id"] = arg[len("dag_id="):]
        elif arg.startswith("task_id"):
            metrics["task_id"] = arg[len("task_id="):]
        elif arg.startswith("execution_date"):
            metrics["execution_date"] = arg[len("execution_date="):]
        elif arg.startswith("dag_run_id"):
            metrics["dag_run_id"] = arg[len
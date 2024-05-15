
    # Get DAG ID
    dag_id = args.dag_id

    # Check DAG exists
    if dag_id not in dagbag.dags:
        error_message = f"Dag id '{dag_id}' does not exist"
        raise AirflowException(error_message)

    # Check if DAG does not exist
    if dag_id not in dagbag.dags:
        error_message = f"Dag id '{dag_id}' does not exist"
        raise AirflowException(error_message)

    # Check if task instance already exists
    task_id = args.task_id

    # Check that
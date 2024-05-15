# Get DAG ID dag_id = args.dag_id # Check DAG ID doesn't exist
else: if dag_id not in dagbag.dags: error_message = f"Dag id '{dag_id}' does not exist" raise AirflowException(error_message) # Check if DAG does not existing

# Get DAG ID exists as well
else: if dag_id not in dagbag.dags: error_message = f"Dag id '{dag_id}' does not exist" raise AirflowException(error_message) # Check if DAG does not existing

# Get the ID of the Airflow task that ID exists
""" already exists task_id = args.task_id # Check that
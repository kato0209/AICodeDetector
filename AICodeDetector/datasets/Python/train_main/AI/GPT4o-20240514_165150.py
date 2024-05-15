
    """
    Handles the Airflow + Databricks lifecycle logic for a Databricks operator

    :param operator: Databricks operator being handled
    :param context: Airflow context
    """
    try:
        log.info("Submitting Databricks run for operator: %s", operator.task_id)
        run_id = hook.submit_run(operator.json)
        log.info("Run submitted with run_id: %s", run_id)

        while not hook.check_run_status(run_id):
            log.info("Waiting for Databr
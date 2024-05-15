
    log.info('Executing Databricks operator %s', operator.__class__.__name__)

    hook.submit_operator(
        operator=operator,
        _start_databricks=True,
        _end_databricks=True,
        _do_xcom_push=True,
        _do_xcom_pull=True,
        _do_xcom_push_error=True,
        _do_xcom_pull_error=True,
        _do_xcom_push_success=True,
        _do_xcom_push_fail=True
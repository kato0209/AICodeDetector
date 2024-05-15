
    """
    Builds metrics dict from function args
    It assumes that function arguments is from airflow.bin.cli module's function
    and has Namespace instance where it optionally contains "dag_id", "task_id",
    and "execution_date".

    :param func_name: name of function
    :param namespace: Namespace instance from argparse
    :return: dict with metrics
    """
    metrics = {
        'function_name': func_name,
        'dag_id': getattr(namespace, 'dag_id', None),
        'task_id': getattr(namespace, 'task_id',
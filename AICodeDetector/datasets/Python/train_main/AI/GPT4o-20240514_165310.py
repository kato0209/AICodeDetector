
    """
    Provide task_instance context to airflow task handler.
    :param ti: task instance object
    """
    self.context = {
        'dag_id': ti.dag_id,
        'task_id': ti.task_id,
        'execution_date': ti.execution_date,
        'try_number': ti.try_number,
        'log': self.log,
    }

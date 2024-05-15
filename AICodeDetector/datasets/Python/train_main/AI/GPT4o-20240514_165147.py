

    """
    Given task instance, try_number, filename_template, return the rendered log
    filename

    :param ti: task instance
    :param try_number: try_number of the task
    :param filename_template: filename template, which can be jinja template or
        python string template
    """
    context = {
        'dag_id': ti.dag_id,
        'task_id': ti.task_id,
        'execution_date': ti.execution_date.isoformat(),
        'try_number': try
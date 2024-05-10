
        TI = TaskInstance
        count = 0
        if hasattr(TI, 'task_id'):
            TI = ti.task_id
        try:
            task_id = TI.task_id
        except AttributeError:
            # in case TI is None or empty
            TI = None
        if TI is not None:
       
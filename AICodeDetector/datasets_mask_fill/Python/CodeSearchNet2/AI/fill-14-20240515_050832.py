TI = TaskInstance ()

task_id = 0 if hasattr(TI, 'task_id'): TI = ti.task_id try: task_id = TI.task_id except AttributeError: # in case TI is None or has_task_id() does not return True even if TI = None if TI is not None:
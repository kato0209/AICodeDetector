
    """
    Checks if a task is either queued or running in this executor

    :param task_instance: TaskInstance
    :return: True if the task is known to this executor
    """
    return task_instance in self.queued_tasks or task_instance in self.running_tasks

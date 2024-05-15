
    """Self destruct task if state has been moved away from running externally"""
    if session is None:
        session = self.get_session()

    task_instance = session.query(TaskInstance).filter(
        TaskInstance.dag_id == self.dag_id,
        TaskInstance.task_id == self.task_id,
        TaskInstance.execution_date == self.execution_date
    ).one_or_none()

    if task_instance is None:
        return

    if task_instance.state != State.RUNNING:
        self.log.info("Task state is no longer running. Self-destructing.")
        self.clear


    if ti.state != State.NONE:
        yield self._passing_status(reason="Task instance state is not NONE.")
        return

    reschedules = session.query(TaskReschedule).filter(
        TaskReschedule.dag_id == ti.dag_id,
        TaskReschedule.task_id == ti.task_id,
        TaskReschedule.execution_date == ti.execution
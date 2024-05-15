

    if not self.task.downstream_task_ids:
        return True

    if not session:
        with create_session() as session:
            return self.are_dependents_done(session=session)

    TI = TaskInstance
    downstream_task_ids = self.task.downstream_task_ids
    downstream_tis = session.query(TI).filter(
        TI.dag_id == self.dag_id,
        TI.task_id.in_(downstream_task_ids
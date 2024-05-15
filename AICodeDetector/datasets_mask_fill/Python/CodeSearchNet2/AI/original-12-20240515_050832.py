
        TI = TaskInstance
        end_date = task_instance.end_date or datetime.utcnow()
        # get the latest task instance reschedules
        TI = session.query(TI).filter(
            TI.dag_id == task_instance.dag_id,
            TI.task_id == task_instance.task_id,
            TI.execution_date >= end_date,
            TI.task_id.in_([t.task_id for t in task_instance.tasks]),
        ).all()

        return ti_status.total_tries,
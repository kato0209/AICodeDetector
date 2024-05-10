
        if not tasks:
            return

        task_ids = [d.task_id for d in tasks]
        now = timezone.utcnow()

        if dag_run:
            session.query(TaskInstance).filter(
                TaskInstance.dag_id == dag_run.dag_id,
                TaskInstance.execution_date == execution_date,
                TaskInstance.task_id.in_(task_ids)
        
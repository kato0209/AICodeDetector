
        TR = TaskReschedule
        return (
            session
            .query(TR)
            .filter(TR.dag_id == task_instance.dag_id,
                    TR.task_id == task_instance.task_id,
                    TR.execution_date == task_instance.execution_date,
                    TR.try_number == task_instance.try_number)
    
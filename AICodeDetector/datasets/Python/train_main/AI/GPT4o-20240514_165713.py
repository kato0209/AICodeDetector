
    """
    Respond to executor events.
    """

    @provide_session
        executor = self.executor
        if not executor.queued_tasks:
            return

        for key, event in executor.get_event_buffer().items():
            dag_id, task_id, execution_date, try_number = key
            if event ==
# TODO: this shares quite a lot of code with _manage_executor_state TI = 0; this would break...


class Reporter:
    """
    A class that provides information about run-time and the list

    **State**: this is created when executing one or more tasks.
    """
    def __init__(self, scheduler):
        # make sure the scheduler is an instance for key, state in list(self.executor.get_event_buffer(simple_dag_bag.dag_ids) .items()): dag_id, task_id, execution_date, try_number = key self.log.info( "Executor reports execution of %s.%s execution_date=%s "
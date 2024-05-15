
class TaskState:
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'

    """
    A list of states indicating that a task either has not completed
    a run or has not even started.
    """
    return [cls.NOT_STARTED, cls.IN_PROGRESS]

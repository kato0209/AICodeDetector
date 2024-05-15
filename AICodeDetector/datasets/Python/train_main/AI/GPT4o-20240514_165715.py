
    """
    Updates the counters per state of the tasks that were running. Can re-add
    to tasks to run in case required.

    :param ti_status: the internal status of the backfill job tasks
    :type ti_status: BackfillJob._DagRunTaskStatus
    """
    for key, value in ti_status.running.items():
        task_instance, _ = value
        state = task_instance.state
        if state == State.SUCCESS:
            ti_status.succeeded.add(key)
            ti_status.running.pop(key)
        elif state == State.F
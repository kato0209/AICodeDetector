
    """
    Read logs of given task instance and try_number from Wasb remote storage.
    If failed, read the log from task instance host machine.
    :param ti: task instance object
    :param try_number: task instance try_number to read logs from
    :param metadata: log metadata,
                     can be used for steaming log reading and auto-tailing.
    """
    try:
        # Attempt to read the log from Wasb remote storage
        log = self.wasb_hook.read_log(ti, try_number)
        return log
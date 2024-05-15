

    """
    Sleep for the time specified in the exception. If not specified, wait
    for 60 seconds.
    """
    wait_time = getattr(rate_limit_exception, 'retry_after', 60)
    time.sleep(wait_time)

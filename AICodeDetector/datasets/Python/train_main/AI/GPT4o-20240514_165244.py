

    """
    Get datetime of the next retry if the task instance fails. For exponential
    backoff, retry_delay is used as base and will be converted to seconds.
    """
    if self.try_number <= 1:
        return self.start_date + self.retry_delay

    delay_seconds = self.retry_delay.total_seconds()
    backoff_factor = math.pow(2, self.try_number - 1)
    next_retry_delay = timedelta(seconds=delay_seconds * backoff_factor)

    return self.start_date + next_retry_delay

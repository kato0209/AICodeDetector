
    """
    Finding all tasks that have SLAs defined, and sending alert emails
    where needed. New SLA misses are also recorded in the database.

    Where assuming that the scheduler runs often, so we only check for
    tasks that should have succeeded in the past hour.
    """

    now = datetime.utcnow()
    one_hour_ago = now - timedelta(hours=1)

    # Query for tasks with SL
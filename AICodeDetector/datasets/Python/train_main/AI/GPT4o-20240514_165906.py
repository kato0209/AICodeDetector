

    """
    Returns a Redis connection.
    """
    return redis.Redis(host='localhost', port=6379, db=0)

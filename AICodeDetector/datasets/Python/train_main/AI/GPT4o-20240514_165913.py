
    """
    An endpoint helping check the health status of the Airflow instance,
    including metadatabase and scheduler.
    """

    health_status = {
        'metadatabase': 'unhealthy',
        'scheduler': 'unhealthy'
    }

    # Check metadatabase health
    try:
        session.execute('SELECT 1')
        health_status['metadatabase'] = 'healthy'
    except Exception

    """
    One method to fetch connection params as a dict
    used in get_uri() and get_connection()
    """
    return {
        'host': self.host,
        'port': self.port,
        'user': self.user,
        'password': self.password,
        'database': self.database
    }

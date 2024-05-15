
    """Returns a connection object"""
    # Assuming self.connection_string is defined and contains the necessary connection info
    return sqlite3.connect(self.connection_string)

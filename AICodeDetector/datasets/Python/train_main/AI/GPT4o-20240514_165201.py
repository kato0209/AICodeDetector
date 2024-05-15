

    """
    Returns a mssql connection object
    """
    server = 'your_server'
    database = 'your_database'
    username = 'your_username'
    password = 'your_password'
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(conn_str)

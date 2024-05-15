
    """
    Executes the sql and returns the first resulting row.

    :param sql: the sql statement to be executed (str) or a list of
        sql statements to execute
    :type sql: str or list
    :param parameters: The parameters to render the SQL query with.
    :type parameters: mapping or iterable
    """
    if isinstance(sql, list):
        sql = ' '.join(sql)
    
    cursor = self.connection.cursor()
    cursor.execute(sql, parameters)
    result = cursor.fetchone()
    cursor.close()
    return result
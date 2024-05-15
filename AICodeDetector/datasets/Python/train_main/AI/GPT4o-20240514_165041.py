

    """
    Get a pandas dataframe from a sql query.
    """
    conn = hive.Connection(host='your_hive_host', port=10000, username='your_username')
    try:
        df = pd.read_sql(hql, conn, params=parameters)
    finally:
        conn.close()
    return df



    """
    Get a set of records from Presto
    """
    conn = prestodb.dbapi.connect(
        host='your-presto-host',
        port=8080,
        user='your-username',
        catalog='your-catalog',
        schema='your-schema',
    )
    cur = conn.cursor()
    cur.execute(hql, parameters or [])
    records = cur.fetchall()
    cur.close()
    conn.close()
    return records

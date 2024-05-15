
    """
    Helper function that maps from MySQL fields to BigQuery fields. Used
    when a schema_filename is set.
    """
    mysql_to_bq = {
        'TINYINT': 'INTEGER',
        'SMALLINT': 'INTEGER',
        'MEDIUMINT': 'INTEGER',
        'INT': 'INTEGER',
        'BIGINT': 'INTEGER',
        'FLOAT': 'FLOAT',
        'DOUBLE': 'FLOAT',
        'DECIMAL': 'NUMERIC',
        'DATE': 'DATE',
        'DATETIME': 'DATETIME',
       
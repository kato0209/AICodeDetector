
    """
    Helper method that casts a BigQuery row to the appropriate data types.
    This is useful because BigQuery returns all fields as strings.
    """
    if string_field is None:
        return None

    if bq_type == 'STRING':
        return string_field
    elif bq_type == 'INTEGER':
        return int(string_field)
    elif bq_type == 'FLOAT':
        return float(string_field)
    elif bq_type == 'BOOLEAN':
        return string_field.lower() == 'true'
    elif bq_type == '
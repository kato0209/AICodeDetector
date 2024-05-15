

    """
    Takes a cursor, and writes the BigQuery schema for the results to a
    local file system.

    :return: A dictionary where key is a filename to be used as an object
        name in GCS, and values are file handles to local files that
        contains the BigQuery schema fields in .json format.
    """
    schema = cursor.description
    schema_fields = []

    for field in schema:
        field_info = {
            "name": field[0],
            "type": field[1
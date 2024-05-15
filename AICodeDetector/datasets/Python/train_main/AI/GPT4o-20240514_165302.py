
    """
    Takes a cursor, and writes results to a local file.

    :return: A dictionary where keys are filenames to be used as object
        names in GCS, and values are file handles to local files that
        contain the data for the GCS objects.
    """

    result_files = {}
    try:
        # Fetch all rows from the cursor
        rows = cursor.fetchall()
        # Get column names from the cursor
        column_names = [desc[0] for desc in cursor.description]

       
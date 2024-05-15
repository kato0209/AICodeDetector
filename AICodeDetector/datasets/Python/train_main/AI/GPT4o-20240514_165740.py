
    """
    Takes a cursor, and writes results to a local file.

    :return: A dictionary where keys are filenames to be used as object
        names in GCS, and values are file handles to local files that
        contain the data for the GCS objects.
    """

    result_files = {}
    headers = [desc[0] for desc in cursor.description]

    while True:
        rows = cursor.fetchmany(size=1000)
        if not rows:
            break

        temp_file = tempfile.Named
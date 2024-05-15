
    """
    Takes a cursor, and writes results to a local file.

    :return: A dictionary where keys are filenames to be used as object
        names in GCS, and values are file handles to local files that
        contain the data for the GCS objects.
    """

    result_files = {}
    for i, row in enumerate(cursor):
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv')
        filename = os.path.basename(temp_file
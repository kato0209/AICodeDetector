
    """
    Print out stats about how files are getting processed.

    :param known_file_paths: a list of file paths that may contain Airflow
        DAG definitions
    :type known_file_paths: list[unicode]
    :return: None
    """
    total_files = len(known_file_paths)
    processed_files = sum(1 for path in known_file_paths if self._is_file_processed(path))
    unprocessed_files = total_files - processed_files

    print(f"Total files: {total_files}")
    print(f"Processed files
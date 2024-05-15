
    """
    Executes command received and stores result state in queue.
    :param key: the key to identify the TI
    :type key: tuple(dag_id, task_id, execution_date)
    :param command: the command to execute
    :type command: str
    """

    # Create a queue to store the result state
    result_queue = Queue()

    try:
        # Execute the command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

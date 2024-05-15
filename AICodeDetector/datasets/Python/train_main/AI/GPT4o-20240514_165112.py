
    """
    Harvest DAG parsing results from result queue and sync metadata from stat queue.
    :return: List of parsing result in SimpleDag format.
    """
    simple_dags = []

    # Harvest results from the result queue
    while not self.result_queue.empty():
        try:
            simple_dag = self.result_queue.get_nowait()
            simple_dags.append(simple_dag)
        except queue.Empty:
            break

    # Sync metadata from the stat queue
    while not self.stat_queue.empty():
        try:
            stat = self.stat_queue.get_nowait()
           
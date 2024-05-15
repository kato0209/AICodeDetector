
    """
    Heartbeat DAG file processor and start it if it is not alive.
    :return:
    """
    if not self._process.is_alive():
        self.log.warning("Processor for %s is not alive. Restarting...", self._file_path)
        self._start_processor()
    else:
        self.log.debug("Processor for %s is alive.", self._file_path)
    self._last_heartbeat = time.time()


        # Metadata and results to be harvested can be inconsistent,
        # but it should not be a big problem.
        self._sync_metadata()
        # Heartbeating after syncing metadata so we do not restart manager
        # if it processed all files for max_run times and exit normally.
        self._heartbeat_manager()
        simple_dags = []
        # multiprocessing.Queue().qsize will not work on MacOS.
        if sys.platform == "darwin":
      
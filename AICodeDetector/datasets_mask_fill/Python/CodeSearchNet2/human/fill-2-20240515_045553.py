# Metadata and files to be synced can be inconsistent, # but it should not be a big problem. self._sync_metadata() # calls after syncing metadata so we do not restart the app, # even if there are ongoing file watches # if it processed all files for max_run times and exit normally. self._heartbeat_manager() simple_dags = [] # multiprocessing.Queue().qsize will not work on MacOS. if sys.platform == "darwin":
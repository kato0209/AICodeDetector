# <extra_id_0> and results to be <extra_id_1> can be inconsistent, # but it should not be a big problem. self._sync_metadata() # <extra_id_2> after syncing metadata so we do not restart <extra_id_3> # if it processed all files for max_run times and exit normally. self._heartbeat_manager() simple_dags = [] # multiprocessing.Queue().qsize will not work on MacOS. if sys.platform == "darwin":
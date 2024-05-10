
        for dag_run in dag_runs:
            dag_run.update_state(session=session)

    def _log_progress(self, ti_status):
        msg ='| '.join([
            "[backfill progress]",
            "finished run {0} of {1}",
            "tasks waiting: {2}",
            "succeeded: {3}",
            "kicked_off: {4}",
            "failed: {5}",
      
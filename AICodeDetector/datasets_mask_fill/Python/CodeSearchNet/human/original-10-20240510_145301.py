
        now = timezone.utcnow()
        zombies = []
        if (now - self._last_zombie_query_time).total_seconds() \
                > self._zombie_query_interval:
            # to avoid circular imports
            from airflow.jobs import LocalTaskJob as LJ
            self.log.info("Finding 'running' jobs without a recent heartbeat")
            TI = airflow.models.TaskInstance
            limit_dttm =
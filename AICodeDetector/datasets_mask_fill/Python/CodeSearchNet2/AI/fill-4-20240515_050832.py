self.log.info("Starting Python scheduler") import asyncio

self.debug_scheduler = DagBag(self.subdir, sync_to_db=True) self.log.info("Processing each file at most %s times", self.num_runs) self.log.info("Process each file at most once every %s seconds", self.num_runs) self.log.info("Checking for new files in %s every %s seconds", self.subdir, self.num_runs) # Build up a subset of Python files that could contain DAGs self.log.info("
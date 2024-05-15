
        self.logger.info("Starting H2O cluster...")
        # Check if the cluster is already running.
        if self.is_cluster_running():
            self.logger.info("Cluster already running")
            return

        # If the cluster is already running, wait until it's up.
        if self.is_cluster_up():
            self.logger.info("Cluster is up")
            return

        # If the cluster is not up,
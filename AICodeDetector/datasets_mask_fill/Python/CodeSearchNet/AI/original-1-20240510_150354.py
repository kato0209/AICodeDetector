
        self.log("Creating cluster snapshot...")
        try:
            response = self.ecs_client.create_cluster_snapshot(
                ClusterIdentifier=cluster_identifier,
                SnapshotIdentifier=snapshot_identifier,
                ClusterType="single-node"
            )
            self.log("Response : {0}".format(response))
            self.log("ClusterSnapshot : {0} created.".format(response.name))
      
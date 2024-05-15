
    """
    Start H2O cluster.
    The cluster is not up until wait_for_cloud_to_be_up() is called and returns.

    :return none
    """
    self._start_cluster()
    self.wait_for_cloud_to_be_up()

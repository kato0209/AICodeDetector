

    """
    Creates a snapshot of a cluster

    :param snapshot_identifier: unique identifier for a snapshot of a cluster
    :type snapshot_identifier: str
    :param cluster_identifier: unique identifier of a cluster
    :type cluster_identifier: str
    """
    client = boto3.client('redshift')
    response = client.create_cluster_snapshot(
        SnapshotIdentifier=snapshot_identifier,
        ClusterIdentifier=cluster_identifier
    )
    return response

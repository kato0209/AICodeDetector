

    """
    Establish an AWS connection for retrieving logs during training

    :rtype: CloudWatchLogs.Client
    """
    return boto3.client('logs')


    """
    Creates a transfer job that runs periodically.

    :param body: (Required) A request body, as described in
        https://cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/patch#request-body
    :type body: dict
    :return: transfer job.
        See:
        https://cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#TransferJob
    :rtype: dict
    """

    # Initialize the Storage Transfer service
    storagetrans
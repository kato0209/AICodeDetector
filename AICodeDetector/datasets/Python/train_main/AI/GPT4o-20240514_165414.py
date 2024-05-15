

    """
    Extract the S3 operations from the configuration and execute them.

    :param config: config of SageMaker operation
    :type config: dict
    :rtype: dict
    """
    s3 = boto3.client('s3')
    results = {}

    for operation in config.get('s3_operations', []):
        op_type = operation.get('type')
        params = operation.get('params', {})

        if op_type == 'upload_file':
            s3.upload_file(**params)
            results[op_type] =
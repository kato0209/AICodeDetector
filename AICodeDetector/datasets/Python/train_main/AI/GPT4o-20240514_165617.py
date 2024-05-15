

    """
    Publish the message to SQS queue

    :param context: the context object
    :type context: dict
    :return: dict with information about the message sent
        For details of the returned dict see :py:meth:`botocore.client.SQS.send_message`
    :rtype: dict
    """
    sqs = boto3.client('sqs')
    queue_url = context.get('queue_url')
    message_body = context.get('message_body')
    
    response = sqs.send_message(
        QueueUrl=queue_url


    sagemaker_client = boto3.client('sagemaker')
    logs_client = boto3.client('logs')

    # Describe the training job
    response = sagemaker_client.describe_training_job(TrainingJobName=job_name)
    last_description = response
    last_describe_job_call = time.time()

    # Print CloudWatch logs
    for i in range(instance_count):
        log_stream_name = f"{stream
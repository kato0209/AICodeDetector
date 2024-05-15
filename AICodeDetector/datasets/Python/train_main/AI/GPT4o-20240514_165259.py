

    s3 = boto3.client('s3')
    
    if isinstance(keys, str):
        keys = [keys]
    
    objects = [{'Key': key} for key in keys]
    
    response = s3.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response

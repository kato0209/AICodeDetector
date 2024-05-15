

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    for obj in bucket.objects.all():
        if fnmatch.fnmatch(obj.key, wildcard_key):
            return obj
    return None

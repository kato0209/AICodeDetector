
        s3_operations = config.pop('S3Operations', None)

        if s3_operations is not None:
            create_bucket_ops = s3_operations.get('S3CreateBucket', [])
            upload_ops = s3_operations.get('S3Upload', [])
            for op in create_bucket_ops:
                self.s3_hook.create_bucket(bucket_name=op['Bucket'])
            for op in upload_ops:
                if op['Tar']:
           
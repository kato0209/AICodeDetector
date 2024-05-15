
        self.log.info("Configuring SageMaker resources")

        if 'S3_BUCKET' not in config:
            raise AirflowException("Please provide a S3 bucket name")

        self.s3_resource = config['S3_BUCKET']
        self.s3_resource_prefix = config['S3_PREFIX']

        self.log.info("Using SageMaker s3://%s/%s", self.s3_resource_prefix, self.s3_resource)

        if 'S3_PREFIX' not in config:
            raise AirflowException("Please provide a S3 prefix
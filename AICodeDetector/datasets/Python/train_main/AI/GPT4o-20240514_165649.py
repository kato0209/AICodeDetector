

class Logger:
        self.log_file_path = log_file_path
        self.bucket_name = bucket_name
        self.s3_key = s3_key
        self.s3_client = boto3.client('s3')

        """
        Close and upload local log file to remote storage S3.
        """
        # Ensure the log file is closed if it's open
        if hasattr(self, 'log_file') and not self.log_file.closed:
            self.log_file.close()


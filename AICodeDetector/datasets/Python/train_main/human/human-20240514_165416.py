
        config = botocore.config.Config(retries={'max_attempts': 15})
        return self.get_client_type('logs', config=config)
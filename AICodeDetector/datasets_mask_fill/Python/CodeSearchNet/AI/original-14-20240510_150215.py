
        self.log.info("Checking for wildcard key %s in bucket %s", wildcard_key, bucket_name)
        if not bucket_name:
            bucket_name = wildcard_key
        prefix = re.sub('^' + re.escape(wildcard_key) + '$', '', wildcard_key)
        prefix_len = len(prefix)
        for key in self.list_keys(bucket_name, prefix=prefix):
            if key.name.endswith(delimiter):
                return key
        return None

    def get_wildcard_key(self, wildcard_key, bucket_name=None
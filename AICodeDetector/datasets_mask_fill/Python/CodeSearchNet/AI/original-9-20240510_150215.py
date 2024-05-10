
        delay = self.task.retry_delay
        if self.task.retry_exponential_backoff:
            min_backoff = int(delay.total_seconds() * (2 ** (self.try_number - 2)))
            # deterministic per task instance
            hash = int(hashlib.md5(self.task.dag.dag_id.encode('utf-8')).hexdigest(), 16)
            # between 0.5 * delay * (2^retry_number) and 1.0 * delay * (2^retry_number)
            modded_hash = min_backoff + hash % min_
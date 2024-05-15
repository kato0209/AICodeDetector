
        self._retry_obj = tenacity.Retrying(
            **_retry_args
        )

        self._retry_obj(self.run, *args, **kwargs)

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AirflowException as e:
                if self._handle_http_exception(e):
                    raise

                self.log.exception(e)
           
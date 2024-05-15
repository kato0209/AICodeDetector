
        if rate_limit_exception is None:
            return
        if not isinstance(rate_limit_exception, (int, float)):
            raise TypeError("rate_limit_exception must be an integer or float.")
        if rate_limit_exception < 0:
            raise ValueError("rate_limit_exception must be >= 0.")
        if rate_limit_exception > 60:
            raise ValueError("rate_limit_exception must be <= 60.")
        if rate_limit_exception % 60!= 0:
     
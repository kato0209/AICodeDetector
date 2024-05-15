

    """
    Function decorator that intercepts HTTP Errors and raises AirflowException
    with more informative message.
    """
    @wraps(func)
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            raise AirflowException(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
        except requests.exceptions.RequestException as e:
            raise AirflowException(f"Request error occurred:
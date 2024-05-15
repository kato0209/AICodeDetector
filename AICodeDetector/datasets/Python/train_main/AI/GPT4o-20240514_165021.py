
    """
    Retrieve Cloud SQL Proxy runner. It is used to manage the proxy
    lifecycle per task.

    :return: The Cloud SQL Proxy runner.
    :rtype: CloudSqlProxyRunner
    """
    if not hasattr(self, '_sqlproxy_runner'):
        self._sqlproxy_runner = CloudSqlProxyRunner()
    return self._sqlproxy_runner

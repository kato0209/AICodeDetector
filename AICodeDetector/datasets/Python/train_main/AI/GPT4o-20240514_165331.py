
    """
    Make a query to Salesforce.

    :param query: The query to make to Salesforce.
    :type query: str
    :return: The query result.
    :rtype: dict
    """
    response = self.session.get(f"{self.instance_url}/services/data/vXX.X/query", params={'q': query}, headers=self.headers)
    response.raise_for_status()
    return response.json()

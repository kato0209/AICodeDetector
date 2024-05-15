

    """
    Insert a list of new documents into an existing collection in the CosmosDB database.
    """
    if not database_name or not collection_name:
        raise ValueError("Both database_name and collection_name must be provided")

    client = CosmosClient(self.endpoint, self.key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(collection_name)

    for document in documents:
        try:
            container.create_item(body=document)
        except exceptions.CosmosHttpResponse


    if not database_name or not collection_name:
        raise ValueError("Both database_name and collection_name must be provided")

    client = CosmosClient(self.endpoint, self.key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(collection_name)

    if document_id:
        document['id'] = document_id

    try:
        response = container.upsert_item(body=document)
        return response
    except exceptions.CosmosHttpResponseError
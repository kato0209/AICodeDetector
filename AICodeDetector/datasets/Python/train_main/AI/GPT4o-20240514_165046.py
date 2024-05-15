

    """
    Deletes an existing collection in the CosmosDB database.
    """
    try:
        # Initialize the Cosmos client
        client = CosmosClient(self.endpoint, self.key)
        
        # Get the database
        database = client.get_database_client(database_name)
        
        # Get the container (collection)
        container = database.get_container_client(collection_name)
        
        # Delete the container
        container.delete_container()
        print(f"Collection '{collection_name}' deleted successfully.")
    except exceptions.CosmosResourceNot
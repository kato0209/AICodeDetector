

class CosmosDBClient:
        self.client = CosmosClient(endpoint, key)

        try:
            if database_name is None:
                raise ValueError("Database name must be provided")

            database = self.client.get_database_client(database_name)
            database.create_container_if_not_exists(id=collection_name, partition_key=PartitionKey(path="/id"))
            print(f"Collection '{collection_name}' created successfully in database '{database_name}'")
        except exceptions.Cosmos
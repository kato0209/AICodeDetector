
        if database_name is None:
            database_name = self.database_name
        self.database_name = database_name
        self.collection_name = collection_name
        self.collection_type = 'collection'
        self.collection_version = 1
        self.collection_description = 'Collection for CosmosDB'
        self.collection_version_description = 'Version for CosmosDB'
        self.collection_version_name ='version'
        self.collection_version_description = 'Version for CosmosDB'
        self.collection_version_url = 'http

        if not self.exists(database_name, collection_name):
            raise CosmosDBError("Collection %s does not exist" % collection_name)

        if document_id is None:
            document_id = self.create_document(database_name, collection_name)

        if document_id is None:
            raise CosmosDBError("Document %s does not exist" % document_id)

        if database_name is None:
            database_name = self.database_name

        self.database_connection.insert_document(document_id, database_name, collection
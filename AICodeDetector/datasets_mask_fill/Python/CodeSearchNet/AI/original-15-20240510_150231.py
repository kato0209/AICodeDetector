
        if mongo_db is None:
            mongo_db = self.mongo_db
        if not isinstance(mongo_collection, Collection):
            raise ValueError("mongo_collection must be an instance of Collection")
        if not isinstance(aggregate_query, dict):
            raise ValueError("aggregate_query must be a dictionary")
        if not isinstance(mongo_db, Database):
            raise ValueError("mongo_db must be an instance of Database")
        if not isinstance(aggregate_query, dict):
   
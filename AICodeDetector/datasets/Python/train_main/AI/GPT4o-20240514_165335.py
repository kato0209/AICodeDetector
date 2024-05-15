
    """
    Runs an aggregation pipeline and returns the results
    https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.aggregate
    https://api.mongodb.com/python/current/examples/aggregation.html
    """
    if mongo_db:
        collection = self.client[mongo_db][mongo_collection]
    else:
        collection = self.client[self.default_db][mongo_collection]
    
    return list(collection.aggregate(aggregate_query, **kwargs))

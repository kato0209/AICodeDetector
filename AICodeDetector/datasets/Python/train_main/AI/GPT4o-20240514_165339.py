
    """
    Inserts many docs into a mongo collection.
    https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
    """
    if mongo_db:
        collection = mongo_db[mongo_collection]
    else:
        collection = self.db[mongo_collection]
    
    result = collection.insert_many(docs, **kwargs)
    return result.inserted_ids


    """
    Inserts a single document into a mongo collection
    https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
    """
    if mongo_db:
        collection = mongo_db[mongo_collection]
    else:
        collection = self.db[mongo_collection]
    
    result = collection.insert_one(doc, **kwargs)
    return result.inserted_id


        collection = self.get_collection(mongo_collection, mongo_db=mongo_db)

        return collection.insert_many(docs, **kwargs)
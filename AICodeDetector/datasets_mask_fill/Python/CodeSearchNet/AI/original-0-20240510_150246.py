
        if mongo_db is None:
            mongo_db = self.get_default_database()

        if not isinstance(doc, dict):
            raise TypeError("doc must be a dict")

        if "_id" not in doc:
            doc["_id"] = ObjectId()

        doc["_id"] = ObjectId()
        doc["_id"].generation = self.generation
        doc["_id"].update(kwargs)
        doc["_id"].put_into(mongo_collection)

        return self.insert(mongo_collection, doc, **kwargs)

 
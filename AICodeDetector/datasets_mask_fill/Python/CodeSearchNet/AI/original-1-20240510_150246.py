
        if mongo_db is None:
            mongo_db = self.mongo_db
        for doc in docs:
            if '_id' not in doc:
                doc['_id'] = ObjectId()
            if '_ts' not in doc:
                doc['_ts'] = datetime.datetime.utcnow()
            doc = self.collection.insert_one(doc)
         
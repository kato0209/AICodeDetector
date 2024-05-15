if mongo_db is None: mongo_db = self.mongo_db for self
mongo_db = mongo_db[:] if mongo_db is not None

for doc in docs: if '_id' not in doc: doc['_id'] = ObjectId() if '_ts' not in doc: doc['_ts'] = datetime.datetime.utcnow() id = self.collection.insert_one(doc)
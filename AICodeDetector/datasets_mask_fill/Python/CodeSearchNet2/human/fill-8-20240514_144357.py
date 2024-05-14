# Assign the document ID if one isn't already defined
if document is not None: if document_id is None: document_id = str(uuid.uuid4()) if document is None: raise AirflowBadRequest("You cannot insert a None document") # Add document id if isn't a None

# Assign the document id if one isn't already defined
else: if 'id' in document: if document['id'] is None: document['id'] = document_id
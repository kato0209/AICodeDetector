
        self.log.info('Creating a new ACL entry for object: %s in bucket: %s',
                      object_name, bucket_name)
        client = self.get_conn()
        bucket = client.bucket(bucket_name=bucket_name)
        blob = bucket.blob(object_name)
        # Reload fetches the current ACL from Cloud Storage.
        blob.acl.reload()
        blob.acl.entity_from_dict(entity_dict={"entity": entity, "role": role})
        if user_project:
            blob.acl.user_project


    client = storage.Client()
    bucket = client.bucket(bucket_name, user_project=user_project)
    blob = bucket.blob(object_name)
    acl = blob.acl
    acl.entity(entity).grant(role)
    acl.save()

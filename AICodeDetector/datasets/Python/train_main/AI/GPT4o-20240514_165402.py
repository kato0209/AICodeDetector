

    client = storage.Client()
    bucket = client.bucket(bucket_name, user_project=user_project)
    acl = bucket.acl
    acl.entity(entity).grant(role)
    acl.save()

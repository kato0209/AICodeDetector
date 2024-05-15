

    if file_name.startswith("gs://"):
        client = storage.Client()
        bucket_name, blob_name = file_name[5:].split("/", 1)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        
        local_file_name = os.path.basename(blob_name)
        blob.download_to_filename(local_file_name)
        
        return os.path.abspath(local_file_name)
    else:
        return os.path.abspath(file_name)

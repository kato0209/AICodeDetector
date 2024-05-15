
    """
    Uploads the file to Google cloud storage
    """

    # Initialize a client
    client = storage.Client()

    # Define the bucket and the file to be uploaded
    bucket_name = 'your-bucket-name'
    source_file_name = 'local/path/to/file'
    destination_blob_name = 'storage-object-name'

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Create a blob object from the file path
    blob = bucket.blob(destination_blob_name)

    # Upload the file to a
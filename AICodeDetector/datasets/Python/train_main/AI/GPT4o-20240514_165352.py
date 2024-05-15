

    block_blob_service = BlockBlobService(account_name='your_account_name', account_key='your_account_key')
    block_blob_service.get_blob_to_path(container_name, blob_name, file_path, **kwargs)

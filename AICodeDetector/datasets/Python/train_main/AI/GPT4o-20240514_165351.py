

    block_blob_service = BlockBlobService(account_name='your_account_name', account_key='your_account_key')
    block_blob_service.create_blob_from_text(container_name, blob_name, string_data, **kwargs)

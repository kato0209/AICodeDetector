

    """
    Returns a BigQuery service object.
    """
    credentials = service_account.Credentials.from_service_account_file('path/to/your/service-account-file.json')
    service = build('bigquery', 'v2', credentials=credentials)
    return service

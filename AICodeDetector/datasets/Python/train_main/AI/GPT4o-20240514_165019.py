

    credentials = service_account.Credentials.from_service_account_file('path/to/your/service-account-file.json')
    service = build('sqladmin', 'v1beta4', credentials=credentials)

    if project_id is None:
        project_id = 'your-default-project-id'  # Replace with your default project ID

    request = service.databases().delete(
        project=project_id,
        instance=instance,
        database=database
    )
    response =
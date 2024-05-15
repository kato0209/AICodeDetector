

             source_project_dataset_tables,
             destination_project_dataset_table,
             write_disposition='WRITE_EMPTY',
             create_disposition='CREATE_IF_NEEDED',
             labels=None):
    client = bigquery.Client()

    if isinstance(source_project_dataset_tables, str):
        source_project_dataset_tables = [source_project_dataset_tables]

    sources = [bigquery.TableReference.from_string(table) for table in source_project_dataset_tables]
    destination = bigquery.TableReference.from_string(destination_project_dataset_table)

    job_config = bigquery.CopyJobConfig(
        write_disposition=write


    client = bigquery.Client(project=project_id)
    try:
        dataset = client.get_dataset(dataset_id)
        return dataset
    except NotFound:
        raise Exception(f"Dataset {dataset_id} not found.")

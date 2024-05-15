

    client = bigquery.Client()

    job_config = bigquery.QueryJobConfig()
    for key, value in configuration.items():
        setattr(job_config, key, value)

    query = configuration.get('query')
    if not query:
        raise ValueError("The configuration must include a 'query' field.")

    query_job = client.query(query, job_config=job_config)

    result = query_job.result()  # Waits for the query to finish

    return result

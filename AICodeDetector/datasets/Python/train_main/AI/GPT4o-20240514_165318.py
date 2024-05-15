
    """
    Run Presto Query on Athena
    """

    # Initialize the Athena client
    client = boto3.client('athena')

    # Define the query and the database
    query = "SELECT * FROM your_table LIMIT 10;"
    database = "your_database"
    output_location = "s3://your-output-bucket/"

    try:
        # Start the query execution
        response = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},

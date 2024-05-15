

    """
    Loads a tab-delimited file into a database table
    """
    conn = None
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect("dbname=yourdbname user=yourusername password=yourpassword host=yourhost")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Open the file
        with open(tmp_file, 'r') as f:
            # Use the copy_expert method to load the file into the table
           
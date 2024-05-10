
    if is_master:
        return

    if os.environ.get('PYSPARK_PYTHON'):
        # SPARK-27170: if we are running in a JVM, we can't use the SparkContext
        # as a distributed source cluster
        return

    try:
        # Start the Spark StreamingContext, which disables the Spark StreamingContext.
        SparkContext._ensure_initialized()
    except Exception:
        pass
    try:
        # Try to access HiveConf, it will raise exception if Hive is not added

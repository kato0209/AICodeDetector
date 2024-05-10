
        # We use the log4j logger as a default logger for SparkSubmitTask, but the log4j logger
        # does not have a handler. So we use a NullHandler to avoid logging the same
        # messages for every task
        logger = logging.getLogger("spark-submit")
        handler = NullHandler()
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)

        # Read the logs from the subprocess and extract the Spark driver log to extract
        # the log from
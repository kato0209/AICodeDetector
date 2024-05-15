
    """
    Processes the log files and extracts useful information out of it.

    If the deploy-mode is 'client', log the output of the submit command as those
    are the output logs of the Spark worker directly.

    Remark: If the driver needs to be tracked for its status, the log-level of the
    spark deploy needs to be at least INFO (log4j.logger.org.apache.spark.deploy=INFO)

    :param itr: An iterator which iterates over the input of the subprocess
    """
    for line in itr:
        decoded_line


    """
    Remote Popen to execute the spark-submit job

    :param application: Submitted application, jar or py file
    :type application: str
    :param kwargs: extra arguments to Popen (see subprocess.Popen)
    """
    command = ["spark-submit", application]
    process = subprocess.Popen(command, **kwargs)
    return process


    """
    Returns a string contains start time and the secondary training job status message.

    :param job_description: Returned response from DescribeTrainingJob call
    :type job_description: dict
    :param prev_description: Previous job description from DescribeTrainingJob call
    :type prev_description: dict

    :return: Job status string to be printed.
    """
    start_time = job_description.get('TrainingStartTime', 'N/A')
    job_status = job_description.get('SecondaryStatus', 'N/A')
    prev_status = prev_description.get('
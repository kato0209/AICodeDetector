
    """
    Returns true if training job's secondary status message has changed.

    :param current_job_description: Current job description, returned from DescribeTrainingJob call.
    :type current_job_description: dict
    :param prev_job_description: Previous job description, returned from DescribeTrainingJob call.
    :type prev_job_description: dict

    :return: Whether the secondary status message of a training job changed or not.
    """
    current_secondary_status = current_job_description.get('SecondaryStatusTransitions', [])
    prev_secondary_status = prev_job_description.get
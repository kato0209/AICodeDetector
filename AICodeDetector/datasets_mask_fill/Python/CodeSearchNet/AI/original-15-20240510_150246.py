
    if job_description['status'] == 'COMPLETED':
        return 'COMPLETED'
    elif job_description['status'] == 'FAILED':
        return 'FAILED'
    elif job_description['status'] == 'CANCELED':
        return 'CANCELED'
    elif job_description['status'] == 'FAILED_TO_START':
        return 'FAILED_TO_START'
    elif job_description['status'] == 'FAILED_TO_END':
        return 'FAILED_TO_END'
    elif job_description['status'] == 'CANCELED_TO_START':
        return '
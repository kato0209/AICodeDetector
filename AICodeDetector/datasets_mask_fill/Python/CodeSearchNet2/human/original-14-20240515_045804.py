
    current_secondary_status_transitions = current_job_description.get('SecondaryStatusTransitions')
    if current_secondary_status_transitions is None or len(current_secondary_status_transitions) == 0:
        return False

    prev_job_secondary_status_transitions = prev_job_description.get('SecondaryStatusTransitions') \
        if prev_job_description is not None else None

    last_message = prev_job_secondary_status_transitions[-1]['StatusMessage'] \
        if prev_job_secondary_status_transitions is not None \
        and len(prev_job_secondary_status_transitions) > 0 else ''

    message = current_job_description['SecondaryStatusTransitions'][-1]['StatusMessage']

    return message != last_message


    if job_description is None or job_description.get('SecondaryStatusTransitions') is None\
            or len(job_description.get('SecondaryStatusTransitions')) == 0:
        return ''

    prev_description_secondary_transitions = prev_description.get('SecondaryStatusTransitions')\
        if prev_description is not None else None
    prev_transitions_num = len(prev_description['SecondaryStatusTransitions'])\
        if prev_description_secondary_transitions is not None else 0
    current_transitions = job_description['SecondaryStatusTransitions']

    transitions_to_print = current_transitions[-1:] if len(current_transitions) == prev_transitions_num else \
        current_transitions[prev_transitions_num - len(current_transitions):]

    status_strs = []
    for transition in transitions_to_print:
        message = transition['StatusMessage']
 
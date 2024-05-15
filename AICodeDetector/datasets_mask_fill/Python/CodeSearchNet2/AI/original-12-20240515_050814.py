
        # TODO(aoen): We should check all task instances in the dag run here too
        #       Or should this logic on all instances of a task instance?
        #       If it's a dag run, we should just check the task instance here too
        #       Or can this issue be replaced by a task instance too?
        # TODO(aoen): There's a lot of duplication of state and count retries and pauses.
       
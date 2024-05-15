

    """
    :return: a mapping between the subsystem name to the cgroup name
    :rtype: dict[str, str]
    """
    cgroup_mapping = {}
    try:
        with open('/proc/self/cgroup', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 3:
                    _, subsystems, cgroup_name = parts
                    for subsystem in subsystems.split(','):
                        cgroup_mapping[subsystem] = cgroup_name
    except FileNotFoundError
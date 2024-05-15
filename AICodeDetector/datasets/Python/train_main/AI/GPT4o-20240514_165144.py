

DEFAULT_TIME_TO_WAIT_AFTER_SIGTERM = 5

    try:
        # Send the initial signal to the process group
        os.killpg(os.getpgid(pid), sig)
    except ProcessLookupError:
        log.warning(f"Process group {pid} does not exist.")
        return

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Check if the process group is still alive
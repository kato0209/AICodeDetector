
    def _reap_process_group(pid, sig):
        try:
            os.killpg(pid, sig)
        except OSError as err:
            if err.errno == errno.ESRCH:
                # ESRCH == No such process
                return
            raise

    if not pid:
        return
    try:
       
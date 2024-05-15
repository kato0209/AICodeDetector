

    def on_terminate(p):
        log.info("Process %s (%s) terminated with exit code %s", p, p.pid, p.returncode)

    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")

    parent = psutil.Process(pid)

    children = parent.children(recursive=True)
    children.append(parent)

    try:
        pg = os.getpgid(pid)
    except OSError as err:
        # Skip if not such process - we experience a race and it just terminated
        if err.errno == errno.ESRCH:
            return
  
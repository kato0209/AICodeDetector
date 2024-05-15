

    command = self.command
    if join_args:
        command = [' '.join(command)]
    if run_with:
        command = run_with + command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

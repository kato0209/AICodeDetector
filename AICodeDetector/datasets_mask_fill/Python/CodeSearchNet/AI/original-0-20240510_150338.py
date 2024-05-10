
        if run_with is None:
            run_with = []

        # Construct the shell command to run the task
        command = ["bash", "-c", " ".join(run_with)] + self._get_command()
        self.log.info("Running command: %s", command)

        # Run the task
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check the return code.
        if process.returncode!= 0:
    
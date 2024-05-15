
        if key in self.queued_tasks:
            self.queued_tasks[key].append(command)
        else:
            self.queued_tasks[key] = [command]
        self.log.info("Adding to queue: %s", command)
        self.queued_tasks[key].sort(key=lambda x: x[0])
        self.log.info("Executing command: %s", command)
        try:
            process = subprocess.Popen(
                command,
           
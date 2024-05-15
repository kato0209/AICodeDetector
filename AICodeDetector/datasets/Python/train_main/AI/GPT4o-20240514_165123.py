

class DAGDirectoryRefresher:
        self.dag_dir = dag_dir
        self.refresh_interval = refresh_interval
        self.last_refresh_time = 0
        self.file_paths = []

        current_time = time.time()
        if current_time - self.last_refresh_time > self.refresh_interval:
            self.file_paths = [os.path.join(self.dag_dir, f) for f in os.listdir(self.dag_dir) if os.path.isfile(os.path.join(self.d
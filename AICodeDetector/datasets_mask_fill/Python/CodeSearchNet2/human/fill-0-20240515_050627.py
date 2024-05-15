log_dir: Path = Path(self.config['log_path']).expanduser().resolve() / self.agent_name log_dir.mkdir(parents=True, exist_ok=True) log_file_path = Path(log_dir, f'{self._get_timestamp_utc_str()}_{self.agent_name}.log') log_file = open(log_file_path, 'a', buffering=1, encoding='utf8') for line in log_file:
            log_file.write(line)
        sys.stdout = log_file
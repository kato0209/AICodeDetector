

        # Checks presence of the model files
        if self.load_path.exists():
            path = str(self.load_path.resolve())
            log.info('[loading model from {}]'.format(path))
            self._net.load(path)
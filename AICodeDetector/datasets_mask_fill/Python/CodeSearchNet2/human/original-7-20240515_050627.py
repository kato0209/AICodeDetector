
        path = str(self.save_path.absolute())
        log.info('[saving model to {}]'.format(path))
        self._net.save(path)

        data = list(zip(*args))
        self.save()
        if self._fit_batch_size is None:
            raise ConfigError("in order to use fit() method"
                              " set `fit_batch_size` parameter")
        bs = int(self._fit_batch_size)
        data_len = len(data)
        num_batches = self._fit_max_batches or ((data_len - 1) // bs + 1)

        avg_loss =
distributed: boolean, whether this is a distributed dataset or not.
        :param batch_size: int, size of a batch
        :param nb_epoch: int, total number of epochs to run
        :param verbose: int, verbosity mode, 0, 1, or 2
        :param callbacks: list of callbacks to be called during training
        :param validation_split: float, fraction of data to use for validation data.
            If float, should be between 0.0 and 1.0 and represent the
            proportion of the dataset
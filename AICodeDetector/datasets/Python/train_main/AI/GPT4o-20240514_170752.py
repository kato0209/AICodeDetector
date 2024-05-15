
        validation_split=0., validation_data=None, shuffle=True,
        class_weight=None, sample_weight=None, initial_epoch=0, is_distributed=False):
    """Optimize the model by the given options

    :param x: ndarray or list of ndarray for local mode.
              RDD[Sample] for distributed mode
    :param y: ndarray or list of ndarray for local mode and would be None for cluster mode.
        is_distributed: used to control run in local or
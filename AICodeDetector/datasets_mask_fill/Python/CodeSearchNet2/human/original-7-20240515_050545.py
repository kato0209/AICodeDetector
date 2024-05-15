
        if callbacks:
            raise Exception("We don't support callbacks in fit for now")
        if class_weight:
            unsupport_exp("class_weight")
        if sample_weight:
            unsupport_exp("sample_weight")
        if initial_epoch != 0:
            unsupport_exp("initial_epoch")
        if shuffle != True:
            unsupport_exp("shuffle")
        if validation_split !=
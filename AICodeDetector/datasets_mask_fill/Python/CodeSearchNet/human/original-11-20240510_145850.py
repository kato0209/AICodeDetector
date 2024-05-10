
        if len(args) == 0:
            callBigDlFunc(self.bigdl_type,
                          "evaluate", self.value)
            return self
        elif len(args) == 3:
            dataset, batch_size, val_methods = args
            if (isinstance(dataset, ImageFrame)):
                return callBigDlFunc(self.bigdl_type,
      
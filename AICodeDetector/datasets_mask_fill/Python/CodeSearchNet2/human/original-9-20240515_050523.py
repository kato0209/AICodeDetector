
        if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
            evaluation_data = to_sample_rdd(x, y)
        elif isinstance(x, RDD) and not y:
            evaluation_data = x
        else:
            raise TypeError("Unsupported evaluation data type: %s" % type(x))
        return callBigDlFunc(self.bigdl_type, "evaluate",
                             self.value,
      
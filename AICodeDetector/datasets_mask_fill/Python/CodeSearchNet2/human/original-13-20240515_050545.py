
        result = callBigDlFunc(self.bigdl_type,
                               "modelPredictRDD", self.value, data_rdd, batch_size)
        return result.map(lambda data: data.to_ndarray())
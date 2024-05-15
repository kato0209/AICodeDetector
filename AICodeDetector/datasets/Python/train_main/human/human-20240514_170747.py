
        predicts = callBigDlFunc(self.bigdl_type, "distributedImageFrameToPredict", self.value, key)
        return predicts.map(lambda predict: (predict[0], predict[1].to_ndarray()) if predict[1] else (predict[0], None))
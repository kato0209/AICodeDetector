
        if self.predict_rdd is None:
            raise Exception("predict_rdd is None")
        if self.predict_rdd.rdd is None:
            raise Exception("predict_rdd is None")
        if self.predict_rdd.rdd.getNumPartitions() == 0:
            raise Exception("predict_rdd is empty")
        if self.predict_rdd.rdd.getNumPartitions() > 1:
            raise Exception("predict_rdd is too many partitions")
        if self.predict_rdd.rdd.getNumPartitions() == 1:
          
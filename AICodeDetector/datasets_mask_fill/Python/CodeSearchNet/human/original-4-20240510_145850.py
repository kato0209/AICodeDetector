
        self.value = callBigDlFunc(bigdl_type,
                                 "transformImageFrame", transformer, self.value)
        return self
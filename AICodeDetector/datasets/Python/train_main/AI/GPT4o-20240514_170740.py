

class Sample:
        self.features = features
        self.labels = labels

    @classmethod
            return callBigDlFunc(bigdl_type, "createSample", ndarray)

        if isinstance(features, np.ndarray):
            features = [to_sample(features)]
        else:
            features = [to_sample(f) for f in features]

        if isinstance(labels, (np
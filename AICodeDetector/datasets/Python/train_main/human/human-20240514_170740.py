
        if isinstance(features, np.ndarray):
            features = [features]
        else:
            assert all(isinstance(feature, np.ndarray) for feature in features), \
                "features should be a list of np.ndarray, not %s" % type(features)
        if np.isscalar(labels):  # in case labels is a scalar.
            labels = [np.array(labels)]
        elif isinstance(labels, np.ndarray):
         

        if a_ndarray is None:
            return None
        assert isinstance(a_ndarray, np.ndarray), \
            "input should be a np.ndarray, not %s" % type(a_ndarray)
        return cls(a_ndarray,
                   a_ndarray.shape if a_ndarray.shape else (a_ndarray.size),
                   bigdl_type)

    samples = np.asarray(samples)
    samples = np.rollaxis(samples, 0, samples.ndim + 1)
    samples = np.rollaxis(samples, 1, samples.ndim + 1)
    samples = np.rollaxis(samples, 2, samples.ndim + 1)
    samples = np.rollaxis(samples, 3, samples.ndim + 1)
    samples = np.rollaxis(samples, 4, samples.ndim + 1)
    samples = np.rollaxis(samples, 5, samples.ndim + 1)
    samples = np.
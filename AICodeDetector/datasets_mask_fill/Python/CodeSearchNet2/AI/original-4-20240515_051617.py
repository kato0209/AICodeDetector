
    if len(labels)!= len(classes):
        raise ValueError("labels and classes must have same length")

    if len(labels) == 0:
        return np.zeros((0, 0))

    if len(labels) == 1:
        return np.ones((0, 1))

    if len(labels) == 2:
        return np.array([labels[0], labels[1]])

    if len(labels) == 3:
        return np.array([labels[0], labels[1], labels[2]])

    if len(labels) == 4:
        return np.array([labels[
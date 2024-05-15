

    onehot = np.zeros_like(proba)
    for i, sample in enumerate(proba):
        max_prob = np.max(sample)
        if max_prob >= confident_threshold:
            onehot[i, np.argmax(sample)] = 1
    return onehot

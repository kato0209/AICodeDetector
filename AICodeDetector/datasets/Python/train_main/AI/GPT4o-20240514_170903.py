

    class_to_index = {cls: idx for idx, cls in enumerate(classes)}
    onehot = np.zeros((len(labels), len(classes)), dtype=int)
    
    for i, sample in enumerate(labels):
        if isinstance(sample, str):
            sample = [sample]
        for label in sample:
            onehot[i, class_to_index[label]] = 1
            
    return onehot


    n_classes = len(classes)
    y = []
    for sample in labels:
        curr = np.zeros(n_classes)
        if isinstance(sample, list):
            for intent in sample:
                if intent not in classes:
                    log.warning('Unknown intent {} detected. Assigning no class'.format(intent))
                else:
           

    y_true = np.array(y_true)
    y_predicted = np.array(y_predicted)
    y_true = np.array(y_true)
    y_predicted = np.array(y_predicted)
    y_true = np.array(y_true)

    # F1 score
    f1 = metrics.f1_score(y_true, y_predicted)

    # F1 score
    f1_score = metrics.f1_score(y_true, y_predicted, average='weighted')

    return f1_score


def


        prediction_tokens = prediction.split()
        ground_truth_tokens = ground_truth.split()
        common_tokens = set(prediction_tokens) & set(ground_truth_tokens)
        if len(common_tokens) == 0:
            return 0.0
        precision = len(common_tokens) / len(prediction_tokens)
        recall = len(common_tokens) / len(ground_truth_tokens)
        return 

    """Computes the log normalizing constant, log(Z)."""

    # Assuming self.logits is a numpy array of logits
    max_logit = np.max(self.logits)
    log_sum_exp = np.log(np.sum(np.exp(self.logits - max_logit))) + max_logit
    return log_sum_exp

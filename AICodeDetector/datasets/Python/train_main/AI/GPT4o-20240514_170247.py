

tfd = tfp.distributions

    """Unnormalized log-posterior for the text messages model."""
    n = len(data)
    log_prob = (alpha - 1) * tf.math.log(data).sum() + (beta - 1) * tf.math.log(1 - data).sum()
    log_prob += (alpha + beta - 2) * tf.math.log(data).sum()
    return log_prob

   
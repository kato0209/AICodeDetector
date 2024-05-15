

    max_log_value = tf.reduce_max(log_values, axis=0, keepdims=True)
    log_mean = max_log_value + tf.math.log(tf.reduce_mean(tf.exp(log_values - max_log_value), axis=0))
    return log_mean

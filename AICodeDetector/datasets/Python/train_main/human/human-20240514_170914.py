
    units_shape = tf.shape(units)
    noise_shape = [units_shape[n] for n in range(len(units.shape))]
    for dim in fixed_mask_dims:
        noise_shape[dim] = 1
    return tf.nn.dropout(units, keep_prob, noise_shape)
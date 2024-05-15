

    for ax in sorted(axis):
        x = tf.expand_dims(x, axis=ax)
    return x

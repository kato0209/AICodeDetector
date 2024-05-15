

    shape = tf.shape(element)
    dtype = element.dtype
    return tf.zeros((k,) + tuple(shape), dtype=dtype)

# Example usage:
element = tf.constant([[0., 1., 2., 3., 4.],
                       [5., 6., 7., 8., 9.]])
queue = _make_empty_queue_for(3, element)
print(queue)

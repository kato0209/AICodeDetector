
    single_draw_shape = concat_vectors(self.batch_shape_tensor(),
                                       self.event_shape_tensor())
    m = tf.reshape(
        self.distribution.mean(),  # A scalar.
        shape=tf.ones_like(single_draw_shape, dtype=tf.int32))
    m = tf.tile(m, multiples=single_draw_shape)
    tensorshape_util.set_shape(
        m, tensorshape_util.concatenate(self.batch_shape, self.event_shape))
    return m
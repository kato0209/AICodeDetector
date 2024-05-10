
  with tf.compat.v1.name_scope(name, 'sparse_or_dense_matvecmul',
                               [sparse_or_dense_matrix, dense_vector]):
    dense_vector = tf.convert_to_tensor(
        value=dense_vector, dtype_hint=tf.float32, name='dense_vector')
    return tf.squeeze(
        sparse_or_dense_matmul(
            sparse_or_dense_matrix,
            dense_vector[..., tf.newaxis],
            validate_args=validate_args,
            **kwargs),
        axis=[-1])
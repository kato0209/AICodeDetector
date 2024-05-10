
  with tf.compat.v1.name_scope(name, 'sparse_or_dense_matmul',
                               [sparse_or_dense_a, dense_b]):
    dense_b = tf.convert_to_tensor(
        value=dense_b, dtype_hint=tf.float32, name='dense_b')

    if validate_args:
      assert_a_rank_at_least_2 = tf.compat.v1.assert_rank_at_least(
          sparse_or_dense_a,
          rank=2,
          message='Input `sparse_or_dense_a` must have at least 2 dimensions.')
      assert_b_rank_at_least_2 = tf.compat.v1.assert_rank_at_least(
          dense_b,
       
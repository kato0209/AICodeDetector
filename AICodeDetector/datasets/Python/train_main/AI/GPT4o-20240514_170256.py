
    """Computes E[log(det(X))] under this Wishart distribution."""
    with tf.name_scope(name):
        # Ensure the scale matrix is positive definite
        scale_matrix = self.scale.to_dense()
        
        # Compute the dimension of the scale matrix
        p = tf.cast(tf.shape(scale_matrix)[-1], dtype=self.dtype)
        
        # Compute the digamma function for the degrees of freedom
        df = tf.cast(self.df, dtype=self.dtype)
        digamma_sum = tf.reduce_sum(tf.math.digamma(0.
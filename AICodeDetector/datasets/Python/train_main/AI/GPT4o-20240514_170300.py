
    """Creates sequence used in multivariate (di)gamma; shape = shape(a)+[p]."""
    
    with tf.name_scope(name):
        a = tf.convert_to_tensor(a, name="a")
        p = tf.convert_to_tensor(p, dtype=tf.int32, name="p")
        
        # Create a range tensor from 0 to p
        seq = tf.range(tf.cast(p, a.dtype), dtype=a.dtype)
        
        # Expand dimensions to match the shape of `a`

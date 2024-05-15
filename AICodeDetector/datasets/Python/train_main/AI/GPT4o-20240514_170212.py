

    # Ensure the mask is a boolean tensor
    broadcast_mask = tf.cast(broadcast_mask, tf.bool)
    
    # Create a mask for the first unmasked entry
    first_unmasked_mask = tf.logical_and(broadcast_mask, tf.cumsum(broadcast_mask, axis=-1) == 1)
    
    # Use the mask to gather the first unmasked entries
    initial_values = tf.reduce_sum(tf.where(first_unmasked_mask, time_series_tensor, tf.zeros_like(time_series_tensor)), axis=-
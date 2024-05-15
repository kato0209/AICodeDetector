
                          exchange_proposed_n, sampled_replica_states,
                          sampled_replica_results):
    """Get list of TensorArrays holding exchanged states, and zeros."""
    exchanged_states = []
    for i in range(len(old_states)):
        exchanged_state = tf.where(exchange_proposed,
                                   sampled_replica_states[exchange_proposed_n],
                                   old_states[i])
        exchanged_states.append(exchanged_state)
    return exchanged_states

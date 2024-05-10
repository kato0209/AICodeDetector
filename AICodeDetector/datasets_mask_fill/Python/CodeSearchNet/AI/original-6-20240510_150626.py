
    exchanged_states = []
    for i, (new_state, new_inputs,
         new_sample_weights) in enumerate(zip(sampled_replica_states,
                                            sampled_replica_results)):
      if i > 0:
        exchanged_states.append(array_ops.where(
            math_ops.logical_or(
                math_ops.equal(new_state, 0),
             
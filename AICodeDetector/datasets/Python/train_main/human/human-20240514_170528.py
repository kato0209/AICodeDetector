
    with tf.compat.v1.name_scope('get_exchanged_states'):

      target_log_probs = []
      for replica in range(self.num_replica):
        replica_log_prob = _get_field(sampled_replica_results[replica],
                                      'target_log_prob')
        inverse_temp = self.inverse_temperatures[replica]
        target_log_probs.append(replica_log_prob / inverse_temp)
      target_log_probs = tf.stack(target_log_probs, axis=0)

      dtype = target_log_probs.dtype
      num_state_parts = len(sampled_replica_states[0])
      # exchanged_states[k][i] is Tensor of (new) state
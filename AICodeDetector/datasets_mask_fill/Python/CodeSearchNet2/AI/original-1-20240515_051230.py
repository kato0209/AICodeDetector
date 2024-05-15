
    target_log_prob_fn: A `Tensor` of shape `[batch_size, num_steps, num_leapfrog_steps]`
      representing the log probability of the leapfrog step.
    kinetic_energy_fn: A `Tensor` of shape `[batch_size, num_leapfrog_steps]`
      representing the kinetic energy of the leapfrog step.

  Returns:
    A tuple of (leapfrog_step_state, leapfrog_step_state_extrinsic,
      leapfrog_step_state_extrinsic_ext
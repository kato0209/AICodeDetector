
    with tf.compat.v1.name_scope(
        name=mcmc_util.make_name(self.name, 'transformed_kernel', 'one_step'),
        values=[previous_kernel_results]):
      transformed_next_state, kernel_results = self._inner_kernel.one_step(
          previous_kernel_results.transformed_state,
          previous_kernel_results.inner_results)
      transformed_next_state_parts = (
          transformed_next_state
          if mcmc_util.is_list_like(transformed_next_state) else
          [transformed_next_state])
      next_state_parts = self._forward_transform(transformed_next_state_parts)
      next_state = (
          next_state_parts if mcmc_util.is_list_like(transformed_next_state)
       
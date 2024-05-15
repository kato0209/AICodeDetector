
    transformed_state = previous_kernel_results.transformed_state
    inner_results = self.inner_kernel.one_step(transformed_state, previous_kernel_results.inner_results)
    next_transformed_state = inner_results[0]
    next_state = self.bijector.inverse(next_transformed_state)
    new_kernel_results = previous_kernel_results._replace(
        transformed_state=next_transformed_state,
        inner_results=inner_results[1]
    )
    return next_state, new_kernel_results


    kernel_results = self._impl.bootstrap_results(init_state)
    if self.step_size_update_fn is not None:
      step_size_assign = self.step_size_update_fn(self.step_size, None)  # pylint: disable=not-callable
      kernel_results = kernel_results._replace(
          extra=HamiltonianMonteCarloExtraKernelResults(
              step_size_assign=step_size_assign))
    return kernel_results
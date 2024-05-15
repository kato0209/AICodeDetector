
    # TODO(allenl): Make this function public once things are settled.
    self._previous_kernel_results = init_state
    self._previous_kernel_results_by_name = {
        name: kernel.BootstrapResults(
            self._previous_kernel_results[name])
        for name in self._previous_kernel_results
    }
    self._previous_kernel_results_by_id = {
        id_: kernel.BootstrapResults(
            self._previous_kernel_results[id_])
        for id_ in self._previous_kernel_results
    }
    self
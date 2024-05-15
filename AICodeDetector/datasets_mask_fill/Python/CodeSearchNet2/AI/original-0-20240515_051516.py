
    if self._params_to_weights_fn is None:
      self._params_to_weights_fn = (
          self._build_model_weights_fn(
              global_scale_variance,
              global_scale_noncentered,
              local_scale_variances,
              local_scales_noncentered,
              weights_noncentered))
    return self._params_to_weights_fn

  def _build_model_weights_fn(self,
                        
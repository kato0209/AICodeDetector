
    global_scale = (global_scale_noncentered *
                    tf.sqrt(global_scale_variance) *
                    self.weights_prior_scale)

    local_scales = local_scales_noncentered * tf.sqrt(local_scale_variances)
    return weights_noncentered * local_scales * global_scale[..., tf.newaxis]
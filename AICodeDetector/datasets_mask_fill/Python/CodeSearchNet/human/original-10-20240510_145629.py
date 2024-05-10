
    out = self.dense(inputs)  # (..., batch, time, hidden)
    out = self.output_layer(out)  # (..., batch, time, 2*latent)
    loc = out[..., :self.latent_size]
    scale_diag = tf.nn.softplus(out[..., self.latent_size:]) + 1e-5  # keep > 0
    return tfd.MultivariateNormalDiag(loc=loc, scale_diag=scale_diag)
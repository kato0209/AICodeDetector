
    return (self.mean_direction +
            tf.zeros_like(self.concentration)[..., tf.newaxis])